from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import typer

from agent.config import get_product, settings
from agent.helpers import current_iso_week, iso_week_to_dates, make_run_id
from agent.logging_setup import bind_run_context, configure_logging
from agent.models import RawReview
from agent.storage import get_connection, init_db

app = typer.Typer(
    name="pulse",
    help="Weekly Product Review Pulse Agent",
    no_args_is_help=True,
)


def _setup() -> None:
    configure_logging(settings.log_level)


# ---------------------------------------------------------------------------
# Ingestion helpers
# ---------------------------------------------------------------------------

def _upsert_reviews(conn: sqlite3.Connection, reviews: list[RawReview]) -> int:
    """Upsert reviews into the DB. Returns the number of new inserts."""
    now = datetime.now(timezone.utc).isoformat()
    inserts = 0
    for r in reviews:
        raw_json = r.model_dump_json()
        cursor = conn.execute(
            """
            INSERT INTO reviews
                (id, product_key, source, rating, title, body, posted_at,
                 version, language, country, ingested_at, raw_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                body        = excluded.body,
                rating      = excluded.rating,
                version     = excluded.version,
                ingested_at = excluded.ingested_at,
                raw_json    = excluded.raw_json
            """,
            (
                r.id,
                r.product_key,
                r.source,
                r.rating,
                r.title,
                r.body,
                r.posted_at.isoformat(),
                r.version,
                r.language,
                r.country,
                now,
                raw_json,
            ),
        )
        if cursor.rowcount == 1 and conn.execute(
            "SELECT changes()"
        ).fetchone()[0] == 1:
            inserts += 1
    return inserts


def _upsert_reviews_counted(conn: sqlite3.Connection, reviews: list[RawReview]) -> tuple[int, int]:
    """Return (new_inserts, updates) counts."""
    now = datetime.now(timezone.utc).isoformat()
    new_inserts = 0
    updates = 0
    for r in reviews:
        raw_json = r.model_dump_json()
        existing = conn.execute(
            "SELECT id FROM reviews WHERE id = ?", (r.id,)
        ).fetchone()
        conn.execute(
            """
            INSERT INTO reviews
                (id, product_key, source, rating, title, body, posted_at,
                 version, language, country, ingested_at, raw_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                body        = excluded.body,
                rating      = excluded.rating,
                version     = excluded.version,
                ingested_at = excluded.ingested_at,
                raw_json    = excluded.raw_json
            """,
            (
                r.id,
                r.product_key,
                r.source,
                r.rating,
                r.title,
                r.body,
                r.posted_at.isoformat(),
                r.version,
                r.language,
                r.country,
                now,
                raw_json,
            ),
        )
        if existing:
            updates += 1
        else:
            new_inserts += 1
    return new_inserts, updates


def _write_jsonl_audit(reviews: list[RawReview], product_key: str, run_id: str) -> Path:
    """Write JSONL audit file. Skipped (idempotent) if the file already exists."""
    out_dir = settings.db_path.parent / "raw" / product_key
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{run_id}.jsonl"
    if out_path.exists():
        return out_path
    with out_path.open("w", encoding="utf-8") as fh:
        for r in reviews:
            fh.write(r.model_dump_json() + "\n")
    return out_path


def _ensure_run(
    conn: sqlite3.Connection,
    run_id: str,
    product_key: str,
    iso_week: str,
    weeks: int,
) -> None:
    today = datetime.now(timezone.utc).date()
    window_start = (today - timedelta(weeks=weeks)).isoformat()
    window_end = today.isoformat()
    conn.execute(
        """
        INSERT INTO runs (id, product_key, iso_week, window_start, window_end, status)
        VALUES (?, ?, ?, ?, ?, 'ingesting')
        ON CONFLICT(id) DO UPDATE SET status = 'ingesting'
        """,
        (run_id, product_key, iso_week, window_start, window_end),
    )


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

@app.command("init-db")
def init_db_cmd() -> None:
    """Initialise the SQLite database with all tables."""
    _setup()
    init_db(settings.db_path)
    typer.echo(f"Database initialised at {settings.db_path}")


@app.command()
def ingest(
    product: str = typer.Option(..., "--product", "-p", help="Product key (e.g. groww)"),
    weeks: int = typer.Option(10, "--weeks", "-w", help="Number of weeks to look back"),
) -> None:
    """Ingest App Store and Play Store reviews for a product."""
    import structlog

    _setup()
    cfg = get_product(product, settings.products_file)

    iso_week = current_iso_week()
    run_id = make_run_id(product, iso_week)
    bind_run_context(run_id, product)

    log = structlog.get_logger()
    log.info("ingest_start", product=product, weeks=weeks, run_id=run_id)

    init_db(settings.db_path)
    conn = get_connection(settings.db_path)

    try:
        with conn:
            _ensure_run(conn, run_id, product, iso_week, weeks)

        from agent.ingestion.appstore import fetch_appstore_reviews
        from agent.ingestion.filters import scrub_pii, should_keep
        from agent.ingestion.playstore import fetch_playstore_reviews

        appstore_reviews = fetch_appstore_reviews(cfg)
        playstore_reviews = fetch_playstore_reviews(cfg, weeks=weeks)

        raw_total = len(appstore_reviews) + len(playstore_reviews)
        log.info("ingest_raw_count", total=raw_total)

        kept: list[RawReview] = []
        filtered = 0
        for r in appstore_reviews + playstore_reviews:
            if not should_keep(r.body):
                filtered += 1
                continue
            kept.append(r.model_copy(update={"body": scrub_pii(r.body)}))

        log.info("ingest_filtered", filtered=filtered, kept=len(kept))

        with conn:
            new_inserts, updates = _upsert_reviews_counted(conn, kept)

        audit_path = _write_jsonl_audit(kept, product, run_id)

        with conn:
            conn.execute(
                "UPDATE runs SET status = 'ingested' WHERE id = ?", (run_id,)
            )

        log.info(
            "ingest_complete",
            run_id=run_id,
            inserts=new_inserts,
            updates=updates,
            audit=str(audit_path),
        )
        typer.echo(
            f"Ingested {new_inserts} new reviews ({updates} updated) "
            f"for {product} — run {run_id}"
        )
    finally:
        conn.close()


@app.command()
def cluster(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
) -> None:
    """[Phase 2] Embed reviews and produce HDBSCAN clusters."""
    _setup()
    typer.echo(f"[Phase 2] cluster: run={run} — not yet implemented")
    raise typer.Exit(code=0)


@app.command()
def summarize(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
) -> None:
    """[Phase 3] LLM summarization: themes, verbatim quotes, action ideas."""
    _setup()
    bind_run_context(run)
    typer.echo(f"[Phase 3] summarize: run={run} — not yet implemented")
    raise typer.Exit(code=0)


@app.command()
def render(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
) -> None:
    """[Phase 4] Render PulseSummary to Doc request tree and email HTML."""
    _setup()
    bind_run_context(run)
    typer.echo(f"[Phase 4] render: run={run} — not yet implemented")
    raise typer.Exit(code=0)


@app.command()
def publish(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
    target: str = typer.Option("both", "--target", "-t", help="Target: docs, gmail, or both"),
) -> None:
    """[Phase 5/6] Publish to Google Docs and/or Gmail via MCP."""
    _setup()
    bind_run_context(run)
    if target not in ("docs", "gmail", "both"):
        typer.echo(f"Error: --target must be one of: docs, gmail, both (got '{target}')", err=True)
        raise typer.Exit(code=1)
    typer.echo(f"[Phase 5/6] publish: run={run}, target={target} — not yet implemented")
    raise typer.Exit(code=0)


@app.command("run")
def run_pipeline(
    product: str = typer.Option(..., "--product", "-p", help="Product key"),
    weeks: int = typer.Option(10, "--weeks", "-w", help="Number of weeks to ingest"),
    week: Optional[str] = typer.Option(None, "--week", help="Specific ISO week (e.g. 2026-W16)"),
) -> None:
    """[Phase 7] Run the full ingestion → clustering → summarization → publish pipeline."""
    _setup()
    get_product(product, settings.products_file)
    typer.echo(
        f"[Phase 7] run: product={product}, weeks={weeks}"
        + (f", week={week}" if week else "")
        + " — not yet implemented"
    )
    raise typer.Exit(code=0)


if __name__ == "__main__":
    app()
