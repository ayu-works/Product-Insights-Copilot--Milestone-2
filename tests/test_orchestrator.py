"""Phase 7 — Orchestrator tests.

Covers E7-1 (full pipeline), E7-3 (resumable checkpoints), E7-5 (cost cap),
and EC7-1 (in-progress double-run guard) using monkeypatched pipeline steps —
the orchestrator's job is to sequence/checkpoint those steps correctly, not to
re-test ingestion/clustering/summarization themselves (covered elsewhere).
"""

from __future__ import annotations

from pathlib import Path

import pytest

import agent.orchestrator as orch
from agent.config import settings
from agent.helpers import current_iso_week, make_run_id
from agent.storage import get_connection, init_db
from agent.summarization.client import PulseCostExceeded

PRODUCT_KEY = "groww"
ISO_WEEK = current_iso_week()
RUN_ID = make_run_id(PRODUCT_KEY, ISO_WEEK)


@pytest.fixture()
def orchestrator_env(tmp_db: Path, products_yaml: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(settings, "db_path", tmp_db)
    monkeypatch.setattr(settings, "products_file", products_yaml)
    init_db(tmp_db)
    return tmp_db


def _seed_run(db_path: Path, status: str, **extra) -> None:
    conn = get_connection(db_path)
    try:
        with conn:
            conn.execute(
                """
                INSERT INTO runs (id, product_key, iso_week, window_start, window_end, status,
                                  metrics_json, gdoc_heading_id, gmail_message_id)
                VALUES (?, ?, ?, '2026-01-01', '2026-01-08', ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET status = excluded.status
                """,
                (
                    RUN_ID,
                    PRODUCT_KEY,
                    ISO_WEEK,
                    status,
                    extra.get("metrics_json"),
                    extra.get("gdoc_heading_id"),
                    extra.get("gmail_message_id"),
                ),
            )
    finally:
        conn.close()


def _run_status(db_path: Path) -> str | None:
    conn = get_connection(db_path)
    try:
        row = conn.execute("SELECT status FROM runs WHERE id = ?", (RUN_ID,)).fetchone()
        return row["status"] if row else None
    finally:
        conn.close()


def _patch_steps(monkeypatch: pytest.MonkeyPatch, calls: list[str], *, fail_on: str | None = None,
                 raise_exc: BaseException | None = None) -> None:
    """Replace each pipeline step with a recorder that appends its name to *calls*.

    Steps are responsible for their own status transitions in production; here
    we emulate that minimally so the orchestrator's resume/terminal logic can
    be exercised end-to-end.
    """
    terminal_status = {
        "ingest": "ingested",
        "cluster": "clustered",
        "summarize": "summarized",
        "render": "rendered",
        "publish": "published_gmail",
    }

    def _make(name: str):
        def _step(*, run_id: str, product_key: str, weeks: int) -> None:
            calls.append(name)
            if name == "ingest":
                # Mirrors _ensure_run(): the real ingest step creates the row.
                _seed_run(settings.db_path, "ingesting")
            if raise_exc is not None and name == fail_on:
                raise raise_exc
            orch._set_status(run_id, terminal_status[name])

        return _step

    for name in orch.STEP_ORDER:
        monkeypatch.setitem(orch._STEPS, name, _make(name))


# ── E7-1: full pipeline runs all steps in order, ends in success ─────────────

def test_full_pipeline_mocked(orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []
    _patch_steps(monkeypatch, calls)

    orch.run_pulse(product=PRODUCT_KEY, weeks=10)

    assert calls == ["ingest", "cluster", "summarize", "render", "publish"]
    assert _run_status(orchestrator_env) == "success"


# ── E7-3: resumable checkpoints — only the failed step (and beyond) reruns ──

def test_resume_from_checkpoint_skips_completed_steps(
    orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Simulate: ingestion + clustering + summarization + render done, docs publish failed.
    _seed_run(orchestrator_env, "rendered")

    calls: list[str] = []
    _patch_steps(monkeypatch, calls)

    orch.run_pulse(product=PRODUCT_KEY, weeks=10)

    assert calls == ["publish"]
    assert _run_status(orchestrator_env) == "success"


def test_resume_from_docs_failed_only_retries_publish(
    orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _seed_run(orchestrator_env, "docs_failed")

    calls: list[str] = []
    _patch_steps(monkeypatch, calls)

    orch.run_pulse(product=PRODUCT_KEY, weeks=10)

    assert calls == ["publish"]
    assert _run_status(orchestrator_env) == "success"


def test_already_successful_run_is_a_noop(
    orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _seed_run(orchestrator_env, "success")

    calls: list[str] = []
    _patch_steps(monkeypatch, calls)

    orch.run_pulse(product=PRODUCT_KEY, weeks=10)

    assert calls == []
    assert _run_status(orchestrator_env) == "success"


# ── EC7-1: previous run still in progress -> exit without double-running ────

def test_in_progress_run_exits_without_rerunning(
    orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _seed_run(orchestrator_env, "in_progress")

    calls: list[str] = []
    _patch_steps(monkeypatch, calls)

    orch.run_pulse(product=PRODUCT_KEY, weeks=10)

    assert calls == []
    # Status must be left untouched — a second trigger must not clobber the
    # in-flight run's checkpoint.
    assert _run_status(orchestrator_env) == "in_progress"


# ── E7-5: cost cap aborts before render/publish, status = cost_exceeded ─────

def test_cost_cap_exceeded_stops_pipeline(
    orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _seed_run(orchestrator_env, "clustered")

    calls: list[str] = []
    _patch_steps(monkeypatch, calls, fail_on="summarize", raise_exc=PulseCostExceeded("cap hit"))

    with pytest.raises(PulseCostExceeded):
        orch.run_pulse(product=PRODUCT_KEY, weeks=10)

    assert calls == ["summarize"]
    assert _run_status(orchestrator_env) == "cost_exceeded"


# ── E7-8: backfill run_id is deterministic and isolated from current week ───

def test_backfill_uses_deterministic_run_id_for_specified_week(
    orchestrator_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    backfill_week = "2026-W10"
    backfill_run_id = make_run_id(PRODUCT_KEY, backfill_week)

    calls: list[str] = []

    def _make(name: str):
        def _step(*, run_id: str, product_key: str, weeks: int) -> None:
            calls.append((name, run_id))
            orch._set_status(run_id, {"ingest": "ingested", "cluster": "clustered",
                                      "summarize": "summarized", "render": "rendered",
                                      "publish": "published_gmail"}[name])

        return _step

    for name in orch.STEP_ORDER:
        monkeypatch.setitem(orch._STEPS, name, _make(name))

    orch.run_pulse(product=PRODUCT_KEY, week=backfill_week)

    assert all(run_id == backfill_run_id for _, run_id in calls)
    assert backfill_run_id != RUN_ID
