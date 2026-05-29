from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from agent.config import get_product, settings
from agent.helpers import make_run_id, current_iso_week
from agent.logging_setup import bind_run_context, configure_logging
from agent.storage import get_connection, init_db

app = typer.Typer(
    name="pulse",
    help="Weekly Product Review Pulse Agent",
    no_args_is_help=True,
)


def _setup() -> None:
    configure_logging(settings.log_level)


@app.command("init-db")
def init_db_cmd() -> None:
    """Initialise the SQLite database with all tables."""
    _setup()
    init_db(settings.db_path)
    typer.echo(f"Database initialised at {settings.db_path}")


@app.command()
def render(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
) -> None:
    """Render PulseSummary to Doc request tree and email HTML/text artifacts."""
    import structlog as _slog

    _setup()
    bind_run_context(run)
    log = _slog.get_logger()

    init_db(settings.db_path)
    conn = get_connection(settings.db_path)

    try:
        run_row = conn.execute("SELECT * FROM runs WHERE id = ?", (run,)).fetchone()
        if not run_row:
            typer.echo(f"Run {run!r} not found. Copy Phase 3 data/pulse.db into data/ first.", err=True)
            raise typer.Exit(code=1)

        product_key = run_row["product_key"]
        iso_week = run_row["iso_week"]

        summaries_dir = settings.db_path.parent / "summaries"
        summary_path = summaries_dir / f"{run}.json"
        if not summary_path.exists():
            typer.echo(
                f"Summary file not found: {summary_path}  "
                f"(copy Phase 3 data/summaries/ into data/summaries/)",
                err=True,
            )
            raise typer.Exit(code=1)

        from agent.models import PulseSummary
        from agent.renderer.docs_tree import build_doc_requests, validate_doc_requests
        from agent.renderer.email_html import render_email

        summary = PulseSummary.model_validate(
            json.loads(summary_path.read_text(encoding="utf-8"))
        )

        try:
            cfg = get_product(product_key, settings.products_file)
            display_name = cfg.display
        except KeyError:
            display_name = product_key.title()

        doc_requests = build_doc_requests(summary, iso_week, display_name)
        validate_doc_requests(doc_requests)

        subject, html_body, text_body = render_email(summary, iso_week, display_name)

        artifact_dir = settings.db_path.parent / "artifacts" / run
        artifact_dir.mkdir(parents=True, exist_ok=True)

        (artifact_dir / "doc_requests.json").write_text(
            json.dumps(doc_requests, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        (artifact_dir / "email.html").write_text(html_body, encoding="utf-8")
        (artifact_dir / "email.txt").write_text(text_body, encoding="utf-8")

        with conn:
            conn.execute(
                "UPDATE runs SET status = 'rendered' WHERE id = ?", (run,)
            )

        log.info(
            "render_complete",
            run_id=run,
            doc_requests=len(doc_requests),
            artifact_dir=str(artifact_dir),
        )
        typer.echo(
            f"Rendered run {run}: {len(doc_requests)} doc requests | "
            f"artifacts -> {artifact_dir}"
        )
        typer.echo(f"Subject: {subject}")
    finally:
        conn.close()


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
    typer.echo(f"[Phase 5/6] publish: run={run}, target={target} -- not yet implemented")
    raise typer.Exit(code=0)


@app.command("run")
def run_pipeline(
    product: str = typer.Option(..., "--product", "-p", help="Product key"),
    weeks: int = typer.Option(10, "--weeks", "-w", help="Number of weeks to ingest"),
    week: Optional[str] = typer.Option(None, "--week", help="Specific ISO week (e.g. 2026-W16)"),
) -> None:
    """[Phase 7] Run the full pipeline end-to-end."""
    _setup()
    typer.echo(
        f"[Phase 7] run: product={product}, weeks={weeks}"
        + (f", week={week}" if week else "")
        + " -- not yet implemented"
    )
    raise typer.Exit(code=0)


if __name__ == "__main__":
    app()
