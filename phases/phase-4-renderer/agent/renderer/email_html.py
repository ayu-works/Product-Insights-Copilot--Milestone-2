"""Phase 4: PulseSummary → HTML + plain-text email using Jinja2.

The rendered email always contains the literal placeholder ``{DOC_DEEP_LINK}``.
Phase 5 substitutes the real Google Doc deep-link URL before sending.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from agent.models import PulseSummary

_TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"
_MAX_DESC_CHARS = 200


def _jinja_env() -> Environment:
    # Enable autoescape for .html only; plain-text .txt template must NOT escape.
    return Environment(
        loader=FileSystemLoader(str(_TEMPLATES_DIR)),
        autoescape=select_autoescape(enabled_extensions=("html",), default=False),
        keep_trailing_newline=True,
    )


def _truncate(text: str, max_chars: int = _MAX_DESC_CHARS) -> str:
    """Truncate *text* to *max_chars* with ellipsis. EC4-4."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "..."


def render_email(
    summary: PulseSummary,
    iso_week: str,
    display_name: str,
    doc_deep_link: str = "{DOC_DEEP_LINK}",
) -> tuple[str, str, str]:
    """Render the stakeholder email for *summary*.

    Returns ``(subject, html_body, plain_text_body)``.

    The *doc_deep_link* defaults to the literal Phase-4 placeholder.
    Phase 5 passes the real ``https://docs.google.com/...#heading=...`` URL.
    """
    top_theme = summary.top_themes[0].label if summary.top_themes else "Review Insights"
    subject = f"[Weekly Pulse] {display_name} — {iso_week} — {top_theme}"

    ctx: dict[str, Any] = {
        "summary": summary,
        "iso_week": iso_week,
        "display_name": display_name,
        "doc_deep_link": doc_deep_link,
        "subject": subject,
        "top_theme": top_theme,
        "truncate": _truncate,
    }

    env = _jinja_env()
    html = env.get_template("email.html").render(**ctx)
    text = env.get_template("email.txt").render(**ctx)
    return subject, html, text
