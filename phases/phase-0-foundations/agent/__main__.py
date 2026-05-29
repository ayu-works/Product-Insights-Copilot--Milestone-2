from __future__ import annotations

from typing import Optional

import typer

from agent.config import get_product, settings
from agent.logging_setup import bind_run_context, configure_logging
from agent.storage import init_db

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
def ingest(
    product: str = typer.Option(..., "--product", "-p", help="Product key (e.g. groww)"),
    weeks: int = typer.Option(10, "--weeks", "-w", help="Number of weeks to ingest"),
) -> None:
    """[Phase 1] Ingest App Store and Play Store reviews for a product."""
    _setup()
    get_product(product, settings.products_file)  # validates product key early
    typer.echo(f"[Phase 1] ingest: product={product}, weeks={weeks} — not yet implemented")
    raise typer.Exit(code=0)


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
