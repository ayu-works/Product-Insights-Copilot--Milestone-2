"""Phase 7 — top-level orchestrator: ``pulse run --product <key> [--weeks N | --week ISO]``.

Chains ingest -> cluster -> summarize -> render -> publish for one product,
driven by ``runs.status`` checkpoints so a re-run resumes from the last
completed step rather than starting over (E7-3 / EC7-3).

Run identity is deterministic: ``run_id = sha1(product_key + iso_week)``
(see :func:`agent.helpers.make_run_id`), which makes both the weekly cron and
manual backfills (``--week 2026-W15``) idempotent (E7-8).
"""

from __future__ import annotations

import time
from typing import Callable, Optional

import structlog
import typer

from agent.config import get_product, settings
from agent.helpers import current_iso_week, make_run_id
from agent.logging_setup import bind_run_context, configure_logging
from agent.mcp_client.errors import MCPConnectionError
from agent.observability import span
from agent.storage import get_connection, init_db
from agent.summarization.client import PulseCostExceeded

log = structlog.get_logger()

__all__ = ["run_pulse", "PulseCostExceeded"]

STEP_ORDER = ["ingest", "cluster", "summarize", "render", "publish"]

# Map a `runs.status` checkpoint to the index of the *next* step to run.
# Anything not listed (None, 'created', 'ingesting', 'ingestion_failed', ...)
# means "start from the top" (index 0).
_RESUME_INDEX: dict[str, int] = {
    "ingested": 1,
    "cluster_failed": 1,
    "clustered": 2,
    "summarize_failed": 2,
    "cost_exceeded": 2,
    "summarized": 3,
    "render_failed": 3,
    "rendered": 4,
    "docs_failed": 4,
    "gmail_failed": 4,
    "published_docs": 4,
    "published_gmail": 4,
    "success": len(STEP_ORDER),
}


def _resume_index(status: Optional[str]) -> int:
    return _RESUME_INDEX.get(status or "", 0)


def _alert(message: str, **fields: object) -> None:
    """Fire an operational alert. Routed through structured logging at WARNING+
    so it can be picked up by whatever log-based alerting the deployment uses."""
    log.warning("pulse_alert", alert=message, **fields)


def _set_status(run_id: str, status: str) -> None:
    conn = get_connection(settings.db_path)
    try:
        with conn:
            conn.execute("UPDATE runs SET status = ? WHERE id = ?", (status, run_id))
    finally:
        conn.close()


def _get_run_row(run_id: str):
    conn = get_connection(settings.db_path)
    try:
        return conn.execute("SELECT * FROM runs WHERE id = ?", (run_id,)).fetchone()
    finally:
        conn.close()


def _record_metrics(run_id: str, **fields: object) -> None:
    """Merge ``fields`` into ``runs.metrics_json`` without clobbering existing keys
    (e.g. the LLM cost/token metrics written by the summarize step)."""
    import json

    conn = get_connection(settings.db_path)
    try:
        row = conn.execute(
            "SELECT metrics_json FROM runs WHERE id = ?", (run_id,)
        ).fetchone()
        existing: dict[str, object] = {}
        if row and row["metrics_json"]:
            try:
                existing = json.loads(row["metrics_json"])
            except (TypeError, ValueError):
                existing = {}
        existing.update(fields)
        with conn:
            conn.execute(
                "UPDATE runs SET metrics_json = ? WHERE id = ?",
                (json.dumps(existing), run_id),
            )
    finally:
        conn.close()


# ── Pipeline steps ────────────────────────────────────────────────────────────
#
# Each step delegates to the existing CLI command functions in agent.__main__ —
# they already own DB transactions, status transitions, and logging for their
# stage. Importing lazily avoids a module-load-time cycle with __main__.

def _step_ingest(*, run_id: str, product_key: str, weeks: int) -> None:
    from agent.__main__ import ingest

    ingest(product=product_key, weeks=weeks)

    conn = get_connection(settings.db_path)
    try:
        run_row = conn.execute(
            "SELECT window_start, window_end FROM runs WHERE id = ?", (run_id,)
        ).fetchone()
        count = conn.execute(
            "SELECT COUNT(*) AS n FROM reviews WHERE product_key = ? AND posted_at BETWEEN ? AND ?",
            (product_key, run_row["window_start"], run_row["window_end"]),
        ).fetchone()["n"]
    finally:
        conn.close()
    _record_metrics(run_id, reviews_ingested=count)


def _step_cluster(*, run_id: str, product_key: str, weeks: int) -> None:
    from agent.__main__ import cluster

    cluster(run=run_id, provider=None, min_cluster_size=8)

    conn = get_connection(settings.db_path)
    try:
        count = conn.execute(
            "SELECT COUNT(*) AS n FROM clusters WHERE run_id = ?", (run_id,)
        ).fetchone()["n"]
    finally:
        conn.close()
    _record_metrics(run_id, clusters_formed=count)


def _step_summarize(*, run_id: str, product_key: str, weeks: int) -> None:
    from agent.__main__ import summarize

    summarize(run=run_id, provider=None, model=None, max_themes=3)
    _check_cost_spike(run_id, product_key)


def _step_render(*, run_id: str, product_key: str, weeks: int) -> None:
    from agent.__main__ import render

    render(run=run_id)


def _step_publish(*, run_id: str, product_key: str, weeks: int) -> None:
    from agent.__main__ import publish

    max_attempts = max(1, settings.mcp_max_retries + 1)
    last_exc: Optional[BaseException] = None

    for attempt in range(1, max_attempts + 1):
        # The deployed REST Docs server has no idempotency search — it appends
        # unconditionally on every call. If the docs leg already completed on a
        # prior attempt (status advanced to 'published_docs'), retry only the
        # Gmail leg so we don't duplicate the Doc section (runbook: "Duplicate
        # section in Doc").
        row = _get_run_row(run_id)
        already_published_docs = bool(row and row["status"] == "published_docs")
        target = "gmail" if (attempt > 1 and already_published_docs) else "both"

        try:
            with span(f"mcp.docs.publish", run_id=run_id):
                publish(run=run_id, target=target)
            break
        except MCPConnectionError as exc:
            last_exc = exc
            log.warning(
                "mcp_connection_lost_retrying",
                run_id=run_id,
                attempt=attempt,
                max_attempts=max_attempts,
                wait_seconds=settings.mcp_retry_wait_seconds,
                error=str(exc),
            )
            if attempt < max_attempts:
                time.sleep(settings.mcp_retry_wait_seconds)
    else:
        assert last_exc is not None
        raise last_exc

    row = _get_run_row(run_id)
    docs_ok = bool(row and row["gdoc_heading_id"])
    gmail_ok = bool(row and row["gmail_message_id"])
    if docs_ok and gmail_ok:
        publish_status = "success"
    elif docs_ok:
        publish_status = "docs_only"
    elif gmail_ok:
        publish_status = "gmail_only"
    else:
        publish_status = "drafted"
    _record_metrics(run_id, publish_status=publish_status)


_STEPS: dict[str, Callable[..., None]] = {
    "ingest": _step_ingest,
    "cluster": _step_cluster,
    "summarize": _step_summarize,
    "render": _step_render,
    "publish": _step_publish,
}

# Status the orchestrator sets if a step raises without setting its own
# terminal "<step>_failed" status (defensive fallback; most steps already
# record a precise failure status themselves).
_FALLBACK_FAILURE_STATUS = {
    "ingest": "ingestion_failed",
    "cluster": "cluster_failed",
    "summarize": "summarize_failed",
    "render": "render_failed",
    "publish": "docs_failed",
}


# ── Cost-spike check (EC7-9) ──────────────────────────────────────────────────

def _check_cost_spike(run_id: str, product_key: str) -> None:
    """Compare this run's LLM cost to the 4-week rolling average and warn (not abort)
    if it's > cost_spike_multiplier times higher."""
    import json

    conn = get_connection(settings.db_path)
    try:
        row = conn.execute(
            "SELECT metrics_json FROM runs WHERE id = ?", (run_id,)
        ).fetchone()
        if not row or not row["metrics_json"]:
            return
        current = json.loads(row["metrics_json"]).get("llm_cost_usd")
        if current is None:
            return

        history = conn.execute(
            """
            SELECT metrics_json FROM runs
            WHERE product_key = ? AND id != ? AND metrics_json IS NOT NULL
            ORDER BY iso_week DESC LIMIT 4
            """,
            (product_key, run_id),
        ).fetchall()
    finally:
        conn.close()

    past_costs = []
    for h in history:
        try:
            cost = json.loads(h["metrics_json"]).get("llm_cost_usd")
        except (TypeError, ValueError):
            continue
        if isinstance(cost, (int, float)):
            past_costs.append(float(cost))

    if not past_costs:
        return

    avg = sum(past_costs) / len(past_costs)
    if avg > 0 and current > settings.cost_spike_multiplier * avg:
        _alert(
            f"LLM cost spike: {current:.4f} vs avg {avg:.4f}",
            run_id=run_id,
            product=product_key,
            cost_usd=current,
            avg_cost_usd=avg,
        )


# ── Entry point ───────────────────────────────────────────────────────────────

def run_pulse(*, product: str, weeks: int = 10, week: Optional[str] = None) -> None:
    """Run the full pipeline for one product, resuming from the last checkpoint.

    Raises:
        PulseCostExceeded: if the LLM cost cap is hit during summarization
            (``runs.status`` is set to ``cost_exceeded``; no Docs/Gmail calls follow).
        typer.Exit: propagated from a failed step (non-zero exit code).
        Exception: any other step failure, after the run's status has been
            recorded as ``<step>_failed``.
    """
    configure_logging(settings.log_level)
    cfg = get_product(product, settings.products_file)
    product_key = cfg.key

    iso_week = week or current_iso_week()
    run_id = make_run_id(product_key, iso_week)
    bind_run_context(run_id, product_key)

    row = _get_run_row(run_id)
    previous_status: Optional[str] = row["status"] if row else None

    # EC7-1 — a previous trigger (e.g. last week's slow run) is still going: bail out.
    if previous_status == "in_progress":
        _alert(
            f"Weekly cron: run {run_id} still in progress from previous trigger",
            run_id=run_id,
            product=product_key,
            iso_week=iso_week,
        )
        log.info(
            "run_already_in_progress",
            run_id=run_id,
            product=product_key,
            iso_week=iso_week,
            msg=f"Run {run_id} already in progress, exiting to avoid double-run",
        )
        return

    start_index = _resume_index(previous_status)
    if start_index >= len(STEP_ORDER):
        log.info("run_already_complete", run_id=run_id, status=previous_status)
        return

    if row is not None:
        _set_status(run_id, "in_progress")
    # else: the ingest step's _ensure_run() INSERTs the row with status='ingesting'

    log.info(
        "pulse_run_start",
        run_id=run_id,
        product=product_key,
        iso_week=iso_week,
        resume_from=STEP_ORDER[start_index],
        previous_status=previous_status,
    )

    init_db(settings.db_path)

    step_name = STEP_ORDER[start_index]
    try:
        for step_name in STEP_ORDER[start_index:]:
            with span(f"pulse.{step_name}", run_id=run_id, product=product_key):
                _STEPS[step_name](run_id=run_id, product_key=product_key, weeks=weeks)
    except PulseCostExceeded:
        _set_status(run_id, "cost_exceeded")
        log.error("pulse_cost_exceeded", run_id=run_id, step=step_name)
        raise
    except Exception as exc:
        row = _get_run_row(run_id)
        if row is not None and not (row["status"] or "").endswith("_failed") and row["status"] != "cost_exceeded":
            _set_status(run_id, _FALLBACK_FAILURE_STATUS[step_name])
        log.error("pulse_run_step_failed", run_id=run_id, step=step_name, error=str(exc))
        raise

    _set_status(run_id, "success")
    log.info("pulse_run_complete", run_id=run_id, product=product_key, iso_week=iso_week)
