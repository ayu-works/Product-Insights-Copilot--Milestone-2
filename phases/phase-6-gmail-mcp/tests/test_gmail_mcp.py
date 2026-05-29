"""Phase 6 tests — Gmail MCP operations.

Covers evaluations E6-1 through E6-8 using a mock MCP session.
No real Google credentials required; session.call_tool is patched.
"""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from agent.mcp_client.errors import MCPAuthError, MCPResponseError
from agent.mcp_client.gmail_ops import _guard_body_size, send_pulse_email

# ── Shared constants ──────────────────────────────────────────────────────────

RUN_ID = "run_test_abc123"
PRODUCT_KEY = "groww"
DEEP_LINK = "https://docs.google.com/document/d/doc123/edit#heading=h_abc"
SUBJECT = "[Weekly Pulse] Groww — 2026-W16 — App Crashes"
HTML_BODY = "<html><body><p>Top theme</p><a href='{DOC_DEEP_LINK}'>Report</a></body></html>"
TEXT_BODY = "Top theme\n\nRead full report: {DOC_DEEP_LINK}\n"


# ── Mock helpers ──────────────────────────────────────────────────────────────

def _ok(data: dict) -> MagicMock:
    result = MagicMock()
    result.isError = False
    content = MagicMock()
    content.text = json.dumps(data)
    result.content = [content]
    return result


# ── E6-1: First run sends email ───────────────────────────────────────────────

async def test_first_run_creates_draft_and_sends() -> None:
    """E6-1: First run creates draft and sends when CONFIRM_SEND=true."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),                              # search: no prior send
        _ok({"draftId": "draft_001", "messageId": "msg_tmp"}),  # create_draft
        _ok({"messageId": "msg_sent_001", "threadId": "thread_1"}),  # send_message
        _ok({"labelId": "label_001", "name": "Pulse/groww"}),  # create_label
        _ok({"messageId": "msg_sent_001"}),                  # modify_labels
    ]

    result = await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=True,
    )

    assert result["sent"] is True
    assert result["message_id"] == "msg_sent_001"
    assert result["draft_id"] == "draft_001"


async def test_first_run_includes_run_id_header() -> None:
    """E6-1: X-Pulse-Run-Id header is passed to gmail_create_draft."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"draftId": "d1", "messageId": "m1"}),
        _ok({"messageId": "msg_sent", "threadId": "t1"}),
        _ok({"labelId": "lbl1", "name": "Pulse/groww"}),
        _ok({"messageId": "msg_sent"}),
    ]

    await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=True,
    )

    create_draft_call = next(
        c for c in session.call_tool.call_args_list if c.args[0] == "gmail_create_draft"
    )
    extra_headers = create_draft_call.args[1].get("extra_headers", {})
    assert extra_headers.get("X-Pulse-Run-Id") == RUN_ID


# ── E6-2: Second run is a no-op ───────────────────────────────────────────────

async def test_second_run_is_noop() -> None:
    """E6-2: Second run finds existing message via search and skips send."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": [{"id": "existing_msg", "threadId": "t1"}]}),
    ]

    result = await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=True,
    )

    called_tools = [c.args[0] for c in session.call_tool.call_args_list]
    assert "gmail_create_draft" not in called_tools
    assert "gmail_send_message" not in called_tools
    assert result["message_id"] == "existing_msg"
    assert result["sent"] is True


# ── E6-3: Dry-run default (no CONFIRM_SEND) ───────────────────────────────────

async def test_dry_run_creates_draft_but_does_not_send() -> None:
    """E6-3: Without confirm_send, draft is created but send_message never called."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"draftId": "draft_dry", "messageId": "msg_dry"}),
    ]

    result = await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=False,  # dry-run
    )

    called_tools = [c.args[0] for c in session.call_tool.call_args_list]
    assert "gmail_send_message" not in called_tools
    assert result["sent"] is False
    assert result["draft_id"] == "draft_dry"
    assert result["message_id"] == ""


# ── E6-4: Deep link substitution ─────────────────────────────────────────────

async def test_deep_link_substituted_in_body() -> None:
    """E6-4: {DOC_DEEP_LINK} placeholder is replaced before create_draft."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"draftId": "d1", "messageId": "m1"}),
    ]

    await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=False,
    )

    create_call = next(
        c for c in session.call_tool.call_args_list if c.args[0] == "gmail_create_draft"
    )
    sent_html: str = create_call.args[1]["html_body"]
    sent_text: str = create_call.args[1]["text_body"]

    assert "{DOC_DEEP_LINK}" not in sent_html
    assert "{DOC_DEEP_LINK}" not in sent_text
    assert DEEP_LINK in sent_html
    assert DEEP_LINK in sent_text


# ── E6-5: Label applied after send ───────────────────────────────────────────

async def test_label_applied_after_send() -> None:
    """E6-5: gmail_modify_labels called with the Pulse/{product} label after send."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"draftId": "d1", "messageId": "m_tmp"}),
        _ok({"messageId": "msg_sent", "threadId": "t1"}),
        _ok({"labelId": "lbl_groww", "name": "Pulse/groww"}),
        _ok({"messageId": "msg_sent"}),
    ]

    await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=True,
    )

    modify_call = next(
        c for c in session.call_tool.call_args_list if c.args[0] == "gmail_modify_labels"
    )
    assert "lbl_groww" in modify_call.args[1].get("add_label_ids", [])


async def test_label_created_before_apply() -> None:
    """E6-5: gmail_create_label called before gmail_modify_labels."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"draftId": "d1", "messageId": "m_tmp"}),
        _ok({"messageId": "msg_sent", "threadId": "t1"}),
        _ok({"labelId": "lbl_new", "name": "Pulse/groww"}),
        _ok({"messageId": "msg_sent"}),
    ]

    await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=True,
    )

    tool_order = [c.args[0] for c in session.call_tool.call_args_list]
    create_label_pos = tool_order.index("gmail_create_label")
    modify_labels_pos = tool_order.index("gmail_modify_labels")
    assert create_label_pos < modify_labels_pos


# ── E6-6: gmail_message_id only written after send ───────────────────────────

async def test_message_id_empty_when_draft_only() -> None:
    """E6-6: message_id is empty string when confirm_send=False."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"draftId": "d1", "messageId": "m1"}),
    ]

    result = await send_pulse_email(
        session,
        run_id=RUN_ID,
        product_key=PRODUCT_KEY,
        to="team@example.com",
        subject=SUBJECT,
        html_body=HTML_BODY,
        text_body=TEXT_BODY,
        deep_link=DEEP_LINK,
        confirm_send=False,
    )

    assert result["message_id"] == ""
    assert result["sent"] is False


# ── EC6-1: Auth token expired ─────────────────────────────────────────────────

async def test_auth_error_on_create_draft() -> None:
    """EC6-1: MCPAuthError raised when create_draft returns 401."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"error": "Token has been expired or revoked", "status": 401}),
    ]

    with pytest.raises(MCPAuthError):
        await send_pulse_email(
            session,
            run_id=RUN_ID,
            product_key=PRODUCT_KEY,
            to="team@example.com",
            subject=SUBJECT,
            html_body=HTML_BODY,
            text_body=TEXT_BODY,
            deep_link=DEEP_LINK,
            confirm_send=True,
        )


# ── EC6-8: Missing draftId in response ───────────────────────────────────────

async def test_missing_draft_id_raises() -> None:
    """EC6-8: MCPResponseError raised when create_draft response lacks draftId."""
    session = AsyncMock()
    session.call_tool.side_effect = [
        _ok({"messages": []}),
        _ok({"messageId": "m1"}),  # draftId intentionally missing
    ]

    with pytest.raises(MCPResponseError, match="draftId"):
        await send_pulse_email(
            session,
            run_id=RUN_ID,
            product_key=PRODUCT_KEY,
            to="team@example.com",
            subject=SUBJECT,
            html_body=HTML_BODY,
            text_body=TEXT_BODY,
            deep_link=DEEP_LINK,
            confirm_send=True,
        )


# ── EC6-6: Body size guard ────────────────────────────────────────────────────

def test_guard_body_size_passthrough_for_small_body() -> None:
    html = "<p>Short email</p>"
    text = "Short email"
    out_html, out_text = _guard_body_size(html, text)
    assert out_html == html
    assert out_text == text


def test_guard_body_size_trims_oversized_html() -> None:
    # Build a body larger than 50 KB
    big_html = "x" * 60_000
    big_text = "y" * 60_000
    out_html, out_text = _guard_body_size(big_html, big_text)
    assert len(out_html.encode("utf-8")) <= 50_000
    assert len(out_text) <= 50_000
