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
    provider: Optional[str] = typer.Option(None, "--provider", help="Override embedding provider (openai|local)"),
    min_cluster_size: int = typer.Option(8, "--min-cluster-size", help="HDBSCAN min_cluster_size"),
) -> None:
    """Embed reviews and produce HDBSCAN clusters for a run."""
    import structlog as _slog

    _setup()
    bind_run_context(run)
    log = _slog.get_logger()

    init_db(settings.db_path)
    conn = get_connection(settings.db_path)

    try:
        run_row = conn.execute("SELECT * FROM runs WHERE id = ?", (run,)).fetchone()
        if not run_row:
            typer.echo(f"Run {run!r} not found in DB. Run `pulse ingest` first.", err=True)
            raise typer.Exit(code=1)

        product_key = run_row["product_key"]
        window_start = run_row["window_start"]
        window_end = run_row["window_end"]

        rows = conn.execute(
            """SELECT id, product_key, source, rating, title, body, posted_at,
                      version, language, country
               FROM reviews
               WHERE product_key = ?
                 AND posted_at BETWEEN ? AND ?""",
            (product_key, window_start, window_end),
        ).fetchall()

        from datetime import timezone as _tz
        reviews = [
            RawReview(
                id=r["id"],
                product_key=r["product_key"],
                source=r["source"],
                rating=r["rating"],
                title=r["title"],
                body=r["body"] or "",
                posted_at=datetime.fromisoformat(r["posted_at"]).replace(tzinfo=_tz.utc),
                version=r["version"],
                language=r["language"] or "en",
                country=r["country"] or "IN",
            )
            for r in rows
        ]
        log.info("cluster_reviews_loaded", count=len(reviews), run_id=run)

        from pathlib import Path as _Path
        from agent.clustering.embeddings import EmbeddingCache, get_provider
        from agent.clustering.pipeline import run_clustering_pipeline

        provider_name = provider or settings.embedding_provider
        embed_provider = get_provider(provider_name)

        cache_path = settings.db_path.parent / "cache" / "embeddings.json"
        cache = EmbeddingCache(cache_path)

        clusters = run_clustering_pipeline(
            conn=conn,
            run_id=run,
            reviews=reviews,
            provider=embed_provider,
            cache=cache,
            seed=settings.random_seed,
            min_cluster_size=min_cluster_size,
        )

        typer.echo(
            f"Clustered {len(reviews)} reviews into {len(clusters)} clusters "
            f"for run {run} (provider={provider_name})"
        )
    finally:
        conn.close()


@app.command()
def summarize(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
    provider: Optional[str] = typer.Option(None, "--provider", help="LLM provider override (anthropic|openai)"),
    model: Optional[str] = typer.Option(None, "--model", help="LLM model override"),
    max_themes: int = typer.Option(3, "--max-themes", help="Max themes in PulseSummary"),
) -> None:
    """Summarize clusters into themes, quotes, and action ideas via LLM."""
    import structlog as _slog

    _setup()
    bind_run_context(run)
    log = _slog.get_logger()

    init_db(settings.db_path)
    conn = get_connection(settings.db_path)

    try:
        run_row = conn.execute("SELECT * FROM runs WHERE id = ?", (run,)).fetchone()
        if not run_row:
            typer.echo(f"Run {run!r} not found. Run `pulse cluster` first.", err=True)
            raise typer.Exit(code=1)

        from datetime import date
        from agent.models import Window
        from agent.summarization.client import (
            AnthropicLLMClient, GroqLLMClient, OpenAILLMClient, PulseCostExceeded,
        )
        from agent.summarization.pipeline import summarize_pulse

        _start = date.fromisoformat(run_row["window_start"])
        _end   = date.fromisoformat(run_row["window_end"])
        window = Window(
            start=_start,
            end=_end,
            weeks=round((_end - _start).days / 7),
        )

        llm_provider = provider or settings.llm_provider
        llm_model = model or settings.llm_model

        if llm_provider == "groq":
            llm_client = GroqLLMClient(
                model=llm_model,
                api_key=settings.groq_api_key,
                max_cost_usd=settings.max_llm_cost_usd,
                max_tokens_per_run=settings.max_tokens_per_run,
            )
        elif llm_provider == "anthropic":
            llm_client = AnthropicLLMClient(
                model=llm_model,
                api_key=settings.anthropic_api_key,
                max_cost_usd=settings.max_llm_cost_usd,
                max_tokens_per_run=settings.max_tokens_per_run,
            )
        else:
            llm_client = OpenAILLMClient(
                model=llm_model,
                api_key=settings.openai_api_key,
                max_cost_usd=settings.max_llm_cost_usd,
                max_tokens_per_run=settings.max_tokens_per_run,
            )

        summaries_dir = settings.db_path.parent / "summaries"

        try:
            summary = summarize_pulse(
                conn=conn,
                run_id=run,
                product_key=run_row["product_key"],
                window=window,
                client=llm_client,
                max_themes=max_themes,
                summaries_dir=summaries_dir,
            )
        except PulseCostExceeded as exc:
            typer.echo(f"Cost cap exceeded: {exc}", err=True)
            raise typer.Exit(code=2)

        m = llm_client.metrics
        typer.echo(
            f"Summarized run {run}: {len(summary.top_themes)} themes, "
            f"{len(summary.quotes)} quotes, {len(summary.action_ideas)} actions | "
            f"LLM calls={m.call_count}  tokens={m.total_input_tokens + m.total_output_tokens}  "
            f"cost=${m.total_cost_usd:.4f}"
        )
    finally:
        conn.close()


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
