from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Optional

import structlog
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


# ── init-db ──────────────────────────────────────────────────────────────────

@app.command("init-db")
def init_db_cmd() -> None:
    """Initialise the SQLite database with all tables."""
    _setup()
    init_db(settings.db_path)
    typer.echo(f"Database initialised at {settings.db_path}")


# ── render ───────────────────────────────────────────────────────────────────

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
            typer.echo(f"Run {run!r} not found.", err=True)
            raise typer.Exit(code=1)

        product_key = run_row["product_key"]
        iso_week = run_row["iso_week"]

        summaries_dir = settings.db_path.parent / "summaries"
        summary_path = summaries_dir / f"{run}.json"
        if not summary_path.exists():
            typer.echo(f"Summary file not found: {summary_path}", err=True)
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
            conn.execute("UPDATE runs SET status = 'rendered' WHERE id = ?", (run,))

        log.info("render_complete", run_id=run, doc_requests=len(doc_requests))
        typer.echo(f"Rendered run {run}: {len(doc_requests)} doc requests → {artifact_dir}")
        typer.echo(f"Subject: {subject}")
    finally:
        conn.close()


# ── publish ───────────────────────────────────────────────────────────────────

@app.command()
def publish(
    run: str = typer.Option(..., "--run", "-r", help="Run ID"),
    target: str = typer.Option(
        "both", "--target", "-t", help="Target: docs, gmail, or both"
    ),
) -> None:
    """Publish rendered report to Google Docs and/or Gmail via FastMCP servers."""
    _setup()
    bind_run_context(run)

    if target not in ("docs", "gmail", "both"):
        typer.echo(f"Error: --target must be one of: docs, gmail, both (got {target!r})", err=True)
        raise typer.Exit(code=1)

    init_db(settings.db_path)
    conn = get_connection(settings.db_path)
    try:
        run_row = conn.execute("SELECT * FROM runs WHERE id = ?", (run,)).fetchone()
        if not run_row:
            typer.echo(f"Run {run!r} not found in database.", err=True)
            raise typer.Exit(code=1)

        product_key = run_row["product_key"]
        iso_week = run_row["iso_week"]

        # Load summary
        summary_path = settings.db_path.parent / "summaries" / f"{run}.json"
        if not summary_path.exists():
            typer.echo(f"Summary not found: {summary_path}", err=True)
            raise typer.Exit(code=1)

        from agent.models import PulseSummary
        from agent.renderer.docs_tree import build_doc_requests
        from agent.renderer.email_html import render_email

        summary = PulseSummary.model_validate(
            json.loads(summary_path.read_text(encoding="utf-8"))
        )

        try:
            cfg = get_product(product_key, settings.products_file)
            display_name = cfg.display
            cached_gdoc_id = cfg.gdoc_id
            gmail_to = cfg.gmail_to
        except KeyError:
            display_name = product_key.title()
            cached_gdoc_id = None
            gmail_to = ""

        doc_requests = build_doc_requests(summary, iso_week, display_name)
        anchor = f"pulse-{product_key}-{iso_week}"

        if target in ("docs", "both"):
            if not settings.docs_mcp_command:
                typer.echo(
                    "PULSE_DOCS_MCP_COMMAND is not set. "
                    "Configure it in .env to point at services/docs-mcp/server.py",
                    err=True,
                )
                raise typer.Exit(code=1)

            result = asyncio.run(
                _publish_docs(
                    run_id=run,
                    product_key=product_key,
                    display_name=display_name,
                    iso_week=iso_week,
                    doc_requests=doc_requests,
                    anchor=anchor,
                    cached_gdoc_id=cached_gdoc_id,
                    db_path=settings.db_path,
                    products_file=settings.products_file,
                    mcp_command=settings.docs_mcp_command,
                )
            )
            deep_link = result["deep_link"]
            typer.echo(f"Docs: section appended (heading_id={result['heading_id']})")
            typer.echo(f"Deep link: {deep_link}")
        else:
            # When --target gmail only, try to reconstruct deep link from DB
            gdoc_heading_id = run_row["gdoc_heading_id"] or ""
            # Retrieve cached doc_id from products table
            prod_row = conn.execute(
                "SELECT gdoc_id FROM products WHERE key = ?", (product_key,)
            ).fetchone()
            if prod_row and prod_row["gdoc_id"] and gdoc_heading_id:
                deep_link = (
                    f"https://docs.google.com/document/d/{prod_row['gdoc_id']}"
                    f"/edit#heading={gdoc_heading_id}"
                )
            else:
                deep_link = "{DOC_DEEP_LINK}"

        if target in ("gmail", "both"):
            typer.echo("[Phase 6] gmail publish not yet implemented in phase-5.")

    finally:
        conn.close()


async def _publish_docs(
    *,
    run_id: str,
    product_key: str,
    display_name: str,
    iso_week: str,
    doc_requests: list[dict],
    anchor: str,
    cached_gdoc_id: str | None,
    db_path: Path,
    products_file: Path,
    mcp_command: str,
) -> dict[str, str]:
    """Async core of the docs publish step."""
    from agent.mcp_client.session import open_docs_session
    from agent.mcp_client.docs_ops import resolve_document, append_pulse_section

    log = structlog.get_logger()

    async with open_docs_session(mcp_command) as session:
        doc_id = await resolve_document(
            session, product_key, display_name, cached_gdoc_id
        )

        # Persist doc_id to products table if new
        conn = get_connection(db_path)
        try:
            with conn:
                conn.execute(
                    "UPDATE products SET gdoc_id = ? WHERE key = ?",
                    (doc_id, product_key),
                )
        finally:
            conn.close()

        result = await append_pulse_section(session, doc_id, doc_requests, anchor)

        # Persist heading_id
        conn = get_connection(db_path)
        try:
            with conn:
                conn.execute(
                    "UPDATE runs SET gdoc_heading_id = ?, status = 'published_docs' WHERE id = ?",
                    (result["heading_id"], run_id),
                )
        finally:
            conn.close()

        log.info(
            "publish_docs_complete",
            run_id=run_id,
            doc_id=doc_id,
            heading_id=result["heading_id"],
        )
        return result


# ── run (Phase 7 placeholder) ────────────────────────────────────────────────

@app.command("run")
def run_pipeline(
    product: str = typer.Option(..., "--product", "-p", help="Product key"),
    weeks: int = typer.Option(10, "--weeks", "-w", help="Number of weeks to ingest"),
    week: Optional[str] = typer.Option(None, "--week", help="Specific ISO week"),
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
