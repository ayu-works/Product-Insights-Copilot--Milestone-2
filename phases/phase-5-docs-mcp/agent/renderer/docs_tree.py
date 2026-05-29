"""Phase 4: PulseSummary → Google Docs batchUpdate request tree.

All insertText requests use sequential indices starting at 1 (beginning of
body). Phase 5 shifts every index by (doc_end_index - 1) to append rather
than prepend.

The first request always embeds the anchor string
    pulse-{product}-{iso_week}
as a substring of the Heading 1 text, enabling the idempotency check in
Phase 5 (docs_get_document body substring search).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema

from agent.models import PulseSummary

_SCHEMA_PATH = (
    Path(__file__).parent.parent.parent / "templates" / "doc_section.schema.json"
)


def _load_schema() -> dict[str, Any]:
    return json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))


def build_doc_requests(
    summary: PulseSummary,
    iso_week: str,
    display_name: str,
) -> list[dict[str, Any]]:
    """Convert a PulseSummary into ordered Google Docs batchUpdate requests.

    Indices are deterministic: each character of inserted text advances the
    position counter by 1, matching Google Docs' index model. The table
    request carries a ``_tableContent`` metadata field (underscore-prefixed,
    not a real Docs API field) so Phase 5 can fill cell content after
    inserting the table structure.
    """
    requests: list[dict[str, Any]] = []
    pos = 1  # Google Docs body starts at index 1

    def _insert(text: str) -> tuple[int, int]:
        nonlocal pos
        start = pos
        requests.append({
            "insertText": {
                "location": {"index": start},
                "text": text,
            }
        })
        pos += len(text)
        return start, pos

    def _para_style(start: int, end: int, named_style: str) -> None:
        requests.append({
            "updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "paragraphStyle": {"namedStyleType": named_style},
                "fields": "namedStyleType",
            }
        })

    def _bullet(start: int, end: int) -> None:
        requests.append({
            "createParagraphBullets": {
                "range": {"startIndex": start, "endIndex": end},
                "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
            }
        })

    def _italic(start: int, end: int) -> None:
        requests.append({
            "updateTextStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "textStyle": {"italic": True},
                "fields": "italic",
            }
        })

    def _indent(start: int, end: int) -> None:
        requests.append({
            "updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "paragraphStyle": {
                    "indentFirstLine": {"magnitude": 36.0, "unit": "PT"},
                    "indentStart": {"magnitude": 36.0, "unit": "PT"},
                },
                "fields": "indentFirstLine,indentStart",
            }
        })

    # ── Section title (HEADING_1) with embedded anchor ─────────────────────
    anchor = f"pulse-{summary.product}-{iso_week}"
    date_start = f"{summary.window.start.strftime('%b')} {summary.window.start.day}"
    date_end = f"{summary.window.end.strftime('%b')} {summary.window.end.day}"
    heading_text = (
        f"{anchor}: Weekly Pulse — {display_name} — "
        f"{iso_week} ({date_start} → {date_end})\n"
    )
    s, e = _insert(heading_text)
    _para_style(s, e, "HEADING_1")

    # ── Stats line ──────────────────────────────────────────────────────────
    delta_str = ""
    if summary.stats.rating_delta_vs_prev is not None:
        delta = summary.stats.rating_delta_vs_prev
        sign = "+" if delta >= 0 else ""
        delta_str = f" ({sign}{delta:.1f} vs prev)"
    stats_text = (
        f"Reviews: {summary.stats.total_reviews} | "
        f"Avg Rating: {summary.stats.avg_rating:.1f}/5.0{delta_str}\n"
    )
    _insert(stats_text)

    # ── Themes ──────────────────────────────────────────────────────────────
    for theme in summary.top_themes:
        s, e = _insert(f"{theme.rank}. {theme.label}\n")
        _para_style(s, e, "HEADING_2")

        if theme.description:
            s, e = _insert(f"{theme.description}\n")
            _bullet(s, e)

        theme_quotes = [q for q in summary.quotes if q.theme_id == theme.id]
        for quote in theme_quotes:
            quote_text = f"“{quote.body}”\n"
            s, e = _insert(quote_text)
            _italic(s, e - 1)
            _indent(s, e)

    # ── Action Ideas ────────────────────────────────────────────────────────
    if summary.action_ideas:
        s, e = _insert("Action Ideas\n")
        _para_style(s, e, "HEADING_2")

        for idea in summary.action_ideas:
            s, e = _insert(f"{idea.title}: {idea.description}\n")
            _bullet(s, e)

    # ── What This Solves (table) ─────────────────────────────────────────────
    if summary.what_this_solves:
        s, e = _insert("What This Solves\n")
        _para_style(s, e, "HEADING_2")

        num_rows = len(summary.what_this_solves) + 1  # +1 for header row
        requests.append({
            "insertTable": {
                "location": {"index": pos},
                "rows": num_rows,
                "columns": 2,
            },
            # Phase 5 reads _tableContent to fill cell text after inserting the table.
            "_tableContent": {
                "headers": ["Audience", "Value"],
                "rows": [
                    [av.audience, av.value]
                    for av in summary.what_this_solves
                ],
            },
        })

    return requests


def validate_doc_requests(requests: list[dict[str, Any]]) -> None:
    """Validate *requests* against the JSON schema."""
    schema = _load_schema()
    jsonschema.validate(instance=requests, schema=schema)
