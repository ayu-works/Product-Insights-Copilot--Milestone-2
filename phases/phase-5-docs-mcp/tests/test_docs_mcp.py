"""Phase 5 tests — Google Docs MCP operations.

Covers evaluations E5-1 through E5-7 using a mock MCP session.
No real Google credentials required; the session.call_tool method is patched.
"""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agent.mcp_client.docs_ops import (
    _body_text,
    _find_heading_id,
    _shift_requests,
    _strip_metadata,
    append_pulse_section,
    resolve_document,
)
from agent.mcp_client.errors import MCPPermissionError, MCPResponseError, MCPToolMissing

# ── Shared constants ──────────────────────────────────────────────────────────

ISO_WEEK = "2026-W16"
ANCHOR = f"pulse-groww-{ISO_WEEK}"
DOC_ID = "doc_test_abc123"


# ── Mock helpers ──────────────────────────────────────────────────────────────

def _ok(data: dict) -> MagicMock:
    """Build a successful mock MCP tool result."""
    result = MagicMock()
    result.isError = False
    content = MagicMock()
    content.text = json.dumps(data)
    result.content = [content]
    return result


def _empty_doc() -> dict:
    """Document body with no existing content beyond the trailing newline."""
    return {
        "documentId": DOC_ID,
        "body": {
            "content": [
                {
                    "startIndex": 0,
                    "endIndex": 1,
                    "paragraph": {
                        "elements": [{"textRun": {"content": "\n"}}],
                        "paragraphStyle": {},
                    },
                }
            ]
        },
    }


def _doc_with_anchor(heading_id: str = "heading_xyz") -> dict:
    """Document that already contains the anchor in a HEADING_1."""
    text = f"{ANCHOR}: Weekly Pulse — Groww — {ISO_WEEK}\n"
    return {
        "documentId": DOC_ID,
        "body": {
            "content": [
                {
                    "startIndex": 0,
                    "endIndex": len(text),
                    "paragraph": {
                        "elements": [{"textRun": {"content": text}}],
                        "paragraphStyle": {
                            "namedStyleType": "HEADING_1",
                            "headingId": heading_id,
                        },
                    },
                }
            ]
        },
    }


# ── E5-1: First run appends section ──────────────────────────────────────────

async def test_first_run_appends_section(doc_requests: list[dict]) -> None:
    """E5-1: First run calls get_document (no anchor), then batch_update."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok(_empty_doc()),            # first get_document — no anchor
        _ok({"replies": []}),         # batch_update
        _ok(_doc_with_anchor()),      # second get_document — find heading
    ]

    result = await append_pulse_section(session, DOC_ID, doc_requests, ANCHOR)

    assert session.call_tool.call_count == 3
    assert result["heading_id"] == "heading_xyz"
    assert DOC_ID in result["deep_link"]
    assert "heading_xyz" in result["deep_link"]


async def test_first_run_calls_batch_update_exactly_once(doc_requests: list[dict]) -> None:
    """E5-1: batch_update called exactly once on first run."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok(_empty_doc()),
        _ok({"replies": []}),
        _ok(_doc_with_anchor()),
    ]

    await append_pulse_section(session, DOC_ID, doc_requests, ANCHOR)

    batch_calls = [
        c for c in session.call_tool.call_args_list
        if c.args[0] == "docs_batch_update"
    ]
    assert len(batch_calls) == 1


# ── E5-2: Second run is a no-op ───────────────────────────────────────────────

async def test_second_run_is_noop(doc_requests: list[dict]) -> None:
    """E5-2: Second run detects anchor in doc body and skips batch_update."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok(_doc_with_anchor()),  # get_document — anchor already present
    ]

    result = await append_pulse_section(session, DOC_ID, doc_requests, ANCHOR)

    called_tools = [c.args[0] for c in session.call_tool.call_args_list]
    assert "docs_batch_update" not in called_tools
    assert result["heading_id"] == "heading_xyz"


async def test_second_run_returns_existing_heading_id(doc_requests: list[dict]) -> None:
    """E5-2: No-op returns the heading_id already present in the doc."""
    session = AsyncMock()
    session.call_tool.side_effect = [_ok(_doc_with_anchor("h_existing_99"))]

    result = await append_pulse_section(session, DOC_ID, doc_requests, ANCHOR)

    assert result["heading_id"] == "h_existing_99"
    assert "h_existing_99" in result["deep_link"]


# ── E5-3: Doc creation on first run ──────────────────────────────────────────

async def test_creates_doc_when_search_empty() -> None:
    """E5-3: resolve_document creates a new doc when search returns nothing."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"documents": []}),               # search_documents: empty
        _ok({"documentId": "new_doc_456"}),   # create_document
    ]

    doc_id = await resolve_document(session, "groww", "Groww", cached_doc_id=None)

    assert doc_id == "new_doc_456"
    called = [c.args[0] for c in session.call_tool.call_args_list]
    assert "docs_search_documents" in called
    assert "docs_create_document" in called


async def test_create_document_title_format() -> None:
    """E5-3: docs_create_document called with title 'Weekly Review Pulse — Groww'."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"documents": []}),
        _ok({"documentId": "new_doc_789"}),
    ]

    await resolve_document(session, "groww", "Groww", cached_doc_id=None)

    create_call = next(
        c for c in session.call_tool.call_args_list if c.args[0] == "docs_create_document"
    )
    assert create_call.args[1]["title"] == "Weekly Review Pulse — Groww"


async def test_resolve_uses_search_result_if_found() -> None:
    """E5-3: resolve_document uses first search result without creating."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"documents": [{"documentId": "found_doc_111", "title": "Weekly Review Pulse — Groww"}]}),
    ]

    doc_id = await resolve_document(session, "groww", "Groww", cached_doc_id=None)

    assert doc_id == "found_doc_111"
    called = [c.args[0] for c in session.call_tool.call_args_list]
    assert "docs_create_document" not in called


async def test_resolve_uses_cached_doc_id_when_valid() -> None:
    """E5-3: Cached gdoc_id is used if the doc still exists."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"documentId": "cached_doc_999", "title": "Weekly Review Pulse — Groww"}),
    ]

    doc_id = await resolve_document(session, "groww", "Groww", cached_doc_id="cached_doc_999")

    assert doc_id == "cached_doc_999"
    called = [c.args[0] for c in session.call_tool.call_args_list]
    assert "docs_search_documents" not in called


async def test_cached_doc_id_stale_falls_back_to_search() -> None:
    """EC5-1: Stale cached gdoc_id triggers fallback to search."""
    session = AsyncMock()
    # First call: get_document returns 404-style error
    session.call_tool.side_effect = [
        _ok({"error": "Document not found", "status": 404}),  # cached doc gone
        _ok({"documents": [{"documentId": "found_doc_222", "title": "Weekly Review Pulse — Groww"}]}),
    ]

    doc_id = await resolve_document(session, "groww", "Groww", cached_doc_id="stale_doc_000")

    assert doc_id == "found_doc_222"


# ── E5-5: Deep link construction ─────────────────────────────────────────────

async def test_deep_link_format(doc_requests: list[dict]) -> None:
    """E5-5: Deep link follows docs.google.com/document/d/{docId}/edit#heading=."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok(_empty_doc()),
        _ok({"replies": []}),
        _ok(_doc_with_anchor("h_abc")),
    ]

    result = await append_pulse_section(session, DOC_ID, doc_requests, ANCHOR)

    expected = f"https://docs.google.com/document/d/{DOC_ID}/edit#heading=h_abc"
    assert result["deep_link"] == expected


# ── E5-7: MCPToolMissing error ────────────────────────────────────────────────

def test_mcp_tool_missing_carries_tool_name() -> None:
    """E5-7: MCPToolMissing exception message includes the missing tool name."""
    exc = MCPToolMissing("docs_batch_update")
    assert "docs_batch_update" in str(exc)


def test_mcp_tool_missing_is_distinct_from_mcp_response_error() -> None:
    assert not isinstance(MCPToolMissing("x"), MCPResponseError)


# ── Index shifting unit tests ─────────────────────────────────────────────────

def test_shift_requests_moves_insert_text_index() -> None:
    reqs = [{"insertText": {"location": {"index": 1}, "text": "Hello\n"}}]
    shifted = _shift_requests(reqs, shift=50)
    assert shifted[0]["insertText"]["location"]["index"] == 51


def test_shift_requests_moves_range_indices() -> None:
    reqs = [{
        "updateParagraphStyle": {
            "range": {"startIndex": 1, "endIndex": 7},
            "paragraphStyle": {"namedStyleType": "HEADING_1"},
            "fields": "namedStyleType",
        }
    }]
    shifted = _shift_requests(reqs, shift=10)
    rng = shifted[0]["updateParagraphStyle"]["range"]
    assert rng["startIndex"] == 11
    assert rng["endIndex"] == 17


def test_shift_requests_does_not_mutate_original() -> None:
    reqs = [{"insertText": {"location": {"index": 1}, "text": "x\n"}}]
    _shift_requests(reqs, shift=99)
    assert reqs[0]["insertText"]["location"]["index"] == 1


# ── _strip_metadata unit tests ────────────────────────────────────────────────

def test_strip_metadata_removes_table_content_key() -> None:
    reqs = [
        {"insertTable": {"location": {"index": 1}, "rows": 2, "columns": 2},
         "_tableContent": {"headers": ["A", "B"], "rows": [["x", "y"]]}},
    ]
    clean, metas = _strip_metadata(reqs)
    assert "_tableContent" not in clean[0]
    assert len(metas) == 1
    assert metas[0]["headers"] == ["A", "B"]


def test_strip_metadata_passthrough_for_clean_requests() -> None:
    reqs = [{"insertText": {"location": {"index": 1}, "text": "hi\n"}}]
    clean, metas = _strip_metadata(reqs)
    assert clean == reqs
    assert metas == []


# ── Permission error propagation ─────────────────────────────────────────────

async def test_permission_error_propagates(doc_requests: list[dict]) -> None:
    """EC5-4: MCPPermissionError raised when batch_update returns 403."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok(_empty_doc()),
        # batch_update returns a 403
        _ok({"error": "The caller does not have permission", "status": 403}),
    ]

    with pytest.raises(MCPPermissionError, match="permission"):
        await append_pulse_section(session, DOC_ID, doc_requests, ANCHOR)


# ── Body text / heading helpers ───────────────────────────────────────────────

def test_body_text_extracts_all_runs() -> None:
    doc = {
        "body": {
            "content": [
                {"paragraph": {"elements": [{"textRun": {"content": "Hello "}}]}},
                {"paragraph": {"elements": [{"textRun": {"content": "world\n"}}]}},
            ]
        }
    }
    assert _body_text(doc) == "Hello world\n"


def test_find_heading_id_locates_anchor() -> None:
    doc = _doc_with_anchor("my_heading_id")
    hid = _find_heading_id(doc, ANCHOR)
    assert hid == "my_heading_id"


def test_find_heading_id_returns_none_when_absent() -> None:
    doc = _empty_doc()
    assert _find_heading_id(doc, ANCHOR) is None
