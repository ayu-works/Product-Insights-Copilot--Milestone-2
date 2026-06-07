from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any, Optional

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
            cached_gdoc_id: str | None = cfg.gdoc_id
            gmail_to = cfg.gmail_to
        except KeyError:
            display_name = product_key.title()
            cached_gdoc_id = None
            gmail_to = ""

        doc_requests = build_doc_requests(summary, iso_week, display_name)
        anchor = f"pulse-{product_key}-{iso_week}"
        subject, html_body, text_body = render_email(summary, iso_week, display_name)

        deep_link = "{DOC_DEEP_LINK}"

        # ── Docs step ────────────────────────────────────────────────────────
        if target in ("docs", "both"):
            if settings.docs_mcp_url:
                gdoc_id = cached_gdoc_id or settings.gdoc_id
                if not gdoc_id:
                    typer.echo(
                        "No Google Doc ID configured. Set 'gdoc_id' in products.yaml "
                        "or PULSE_GDOC_ID in .env (the deployed REST server cannot "
                        "search/create documents).",
                        err=True,
                    )
                    raise typer.Exit(code=1)

                docs_result = asyncio.run(
                    _publish_docs_rest(
                        run_id=run,
                        display_name=display_name,
                        iso_week=iso_week,
                        doc_requests=doc_requests,
                        anchor=anchor,
                        gdoc_id=gdoc_id,
                        db_path=settings.db_path,
                        base_url=settings.docs_mcp_url,
                    )
                )
                deep_link = docs_result["deep_link"]
                typer.echo(f"Docs: section appended via REST to {gdoc_id}")
                typer.echo(f"Deep link: {deep_link}")

            elif settings.docs_mcp_command:
                docs_result = asyncio.run(
                    _publish_docs(
                        run_id=run,
                        product_key=product_key,
                        display_name=display_name,
                        doc_requests=doc_requests,
                        anchor=anchor,
                        cached_gdoc_id=cached_gdoc_id,
                        db_path=settings.db_path,
                        mcp_command=settings.docs_mcp_command,
                    )
                )
                deep_link = docs_result["deep_link"]
                typer.echo(f"Docs: section appended (heading_id={docs_result['heading_id']})")
                typer.echo(f"Deep link: {deep_link}")

            else:
                typer.echo(
                    "Neither PULSE_DOCS_MCP_URL nor PULSE_DOCS_MCP_COMMAND is set. "
                    "Configure one in .env (URL for the deployed REST server, "
                    "command to launch services/docs-mcp/server.py locally).",
                    err=True,
                )
                raise typer.Exit(code=1)

        elif target == "gmail":
            # Reconstruct deep link from DB for gmail-only re-runs (EC6-2)
            gdoc_heading_id = run_row["gdoc_heading_id"] or ""
            prod_row = conn.execute(
                "SELECT gdoc_id FROM products WHERE key = ?", (product_key,)
            ).fetchone()
            if prod_row and prod_row["gdoc_id"] and gdoc_heading_id:
                deep_link = (
                    f"https://docs.google.com/document/d/{prod_row['gdoc_id']}"
                    f"/edit#heading={gdoc_heading_id}"
                )

        # ── Gmail step ───────────────────────────────────────────────────────
        if target in ("gmail", "both"):
            if not gmail_to:
                typer.echo(
                    f"Product '{product_key}' has no gmail_to address configured.", err=True
                )
                raise typer.Exit(code=1)

            if settings.gmail_mcp_url:
                gmail_result = asyncio.run(
                    _publish_gmail_rest(
                        run_id=run,
                        to=gmail_to,
                        subject=subject,
                        text_body=text_body,
                        deep_link=deep_link,
                        base_url=settings.gmail_mcp_url,
                    )
                )
                typer.echo(
                    f"Gmail: draft created via REST (draft_id={gmail_result['draft_id']}). "
                    "The deployed server only creates drafts — no send/labels available."
                )

            elif settings.gmail_mcp_command:
                gmail_result = asyncio.run(
                    _publish_gmail(
                        run_id=run,
                        product_key=product_key,
                        to=gmail_to,
                        subject=subject,
                        html_body=html_body,
                        text_body=text_body,
                        deep_link=deep_link,
                        confirm_send=settings.confirm_send,
                        db_path=settings.db_path,
                        mcp_command=settings.gmail_mcp_command,
                    )
                )

                if gmail_result["sent"]:
                    typer.echo(f"Gmail: email sent (message_id={gmail_result['message_id']})")
                else:
                    typer.echo(
                        f"Gmail: draft created (draft_id={gmail_result['draft_id']}). "
                        "Set PULSE_CONFIRM_SEND=true to send."
                    )

            else:
                typer.echo(
                    "Neither PULSE_GMAIL_MCP_URL nor PULSE_GMAIL_MCP_COMMAND is set. "
                    "Configure one in .env (URL for the deployed REST server, "
                    "command to launch services/gmail-mcp/server.py locally).",
                    err=True,
                )
                raise typer.Exit(code=1)

    finally:
        conn.close()


# ── Async helpers ─────────────────────────────────────────────────────────────

async def _publish_docs(
    *,
    run_id: str,
    product_key: str,
    display_name: str,
    doc_requests: list[dict],
    anchor: str,
    cached_gdoc_id: str | None,
    db_path: Path,
    mcp_command: str,
) -> dict[str, str]:
    from agent.mcp_client.session import open_docs_session
    from agent.mcp_client.docs_ops import resolve_document, append_pulse_section

    log = structlog.get_logger()

    async with open_docs_session(mcp_command) as session:
        doc_id = await resolve_document(
            session, product_key, display_name, cached_gdoc_id
        )

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


async def _publish_gmail(
    *,
    run_id: str,
    product_key: str,
    to: str,
    subject: str,
    html_body: str,
    text_body: str,
    deep_link: str,
    confirm_send: bool,
    db_path: Path,
    mcp_command: str,
) -> dict[str, Any]:
    from agent.mcp_client.session import open_gmail_session
    from agent.mcp_client.gmail_ops import send_pulse_email

    log = structlog.get_logger()

    async with open_gmail_session(mcp_command) as session:
        result = await send_pulse_email(
            session,
            run_id=run_id,
            product_key=product_key,
            to=to,
            subject=subject,
            html_body=html_body,
            text_body=text_body,
            deep_link=deep_link,
            confirm_send=confirm_send,
        )

        if result["sent"] and result["message_id"]:
            conn = get_connection(db_path)
            try:
                with conn:
                    conn.execute(
                        "UPDATE runs SET gmail_message_id = ?, status = 'published_gmail' WHERE id = ?",
                        (result["message_id"], run_id),
                    )
            finally:
                conn.close()

        log.info(
            "publish_gmail_complete",
            run_id=run_id,
            sent=result["sent"],
            message_id=result.get("message_id", ""),
        )
        return result


def _flatten_doc_requests(doc_requests: list[dict[str, Any]]) -> str:
    """Collapse a Phase-4 insertText request tree into a flat plain-text string.

    The deployed REST server only accepts a single ``content: str`` field, so
    rich structure (headings, tables, styling) is lost — this concatenates the
    inserted text runs in order.
    """
    return "".join(
        req["insertText"]["text"]
        for req in doc_requests
        if "insertText" in req
    )


async def _publish_docs_rest(
    *,
    run_id: str,
    display_name: str,
    iso_week: str,
    doc_requests: list[dict],
    anchor: str,
    gdoc_id: str,
    db_path: Path,
    base_url: str,
) -> dict[str, str]:
    """Append the pulse section to a Google Doc via the deployed REST server.

    The server has no idempotency search and no rich formatting — it appends
    plain text (with its own auto-injected timestamp banner) every call.
    """
    from agent.rest_client.docs_rest import append_to_doc

    log = structlog.get_logger()

    content = f"{anchor}\n{display_name} — Weekly Pulse ({iso_week})\n\n"
    content += _flatten_doc_requests(doc_requests)

    await append_to_doc(base_url, gdoc_id, content)

    deep_link = f"https://docs.google.com/document/d/{gdoc_id}/edit"

    conn = get_connection(db_path)
    try:
        with conn:
            conn.execute(
                "UPDATE runs SET status = 'published_docs' WHERE id = ?",
                (run_id,),
            )
    finally:
        conn.close()

    log.info("publish_docs_rest_complete", run_id=run_id, doc_id=gdoc_id)
    return {"heading_id": "", "deep_link": deep_link}


async def _publish_gmail_rest(
    *,
    run_id: str,
    to: str,
    subject: str,
    text_body: str,
    deep_link: str,
    base_url: str,
) -> dict[str, Any]:
    """Create a Gmail draft via the deployed REST server.

    The server has no idempotency search, no cc/bcc/custom headers, no HTML
    body, and never sends — it only ever creates a plain-text draft (with its
    own auto-injected timestamp banner).
    """
    from agent.rest_client.gmail_rest import create_email_draft

    log = structlog.get_logger()

    body = text_body.replace("{DOC_DEEP_LINK}", deep_link)

    result = await create_email_draft(base_url, to, subject, body)
    draft_id = result.get("draft_id", "")

    log.info("publish_gmail_rest_complete", run_id=run_id, draft_id=draft_id)
    return {"message_id": "", "draft_id": draft_id, "sent": False}


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
