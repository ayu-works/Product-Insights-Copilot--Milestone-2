"""Phase 6: Gmail operations via MCP.

Key operation:
  send_pulse_email — idempotently create a draft and optionally send it,
                     applying a product-specific label after send.
"""

from __future__ import annotations

import json
from typing import Any

import structlog
from mcp import ClientSession

from agent.mcp_client.errors import MCPAuthError, MCPPermissionError, MCPResponseError

log = structlog.get_logger()

_MAX_EMAIL_BYTES = 50_000  # EC6-6: trim body if over this limit


# ── Low-level helper (shared pattern with docs_ops) ───────────────────────────

async def _call(session: ClientSession, tool: str, **kwargs: Any) -> Any:
    """Call *tool* on the MCP session and return the parsed JSON result."""
    result = await session.call_tool(tool, kwargs)

    if result.isError:
        err_text = result.content[0].text if result.content else "unknown error"
        raise MCPResponseError(f"{tool} returned MCP error: {err_text}")

    raw = result.content[0].text if result.content else "{}"
    data: dict[str, Any] = json.loads(raw)

    if "error" in data:
        msg = str(data["error"])
        status = data.get("status", 0)
        if status == 401 or "token" in msg.lower() or "expired" in msg.lower():
            raise MCPAuthError(
                f"Gmail MCP: auth token expired or revoked. "
                f"Re-authenticate the MCP server. Details: {msg}"
            )
        if status == 403 or "permission" in msg.lower():
            raise MCPPermissionError(f"Gmail MCP: insufficient permission — {msg}")
        raise MCPResponseError(f"{tool} API error (HTTP {status}): {msg}")

    return data


# ── Label management ──────────────────────────────────────────────────────────

async def _ensure_label(session: ClientSession, label_name: str) -> str:
    """Return the label ID for *label_name*, creating it if necessary. E6-5"""
    result = await _call(session, "gmail_create_label", name=label_name)
    label_id: str = result["labelId"]
    log.info("label_ready", name=label_name, label_id=label_id)
    return label_id


# ── Body size guard ───────────────────────────────────────────────────────────

def _guard_body_size(
    html_body: str,
    text_body: str,
) -> tuple[str, str]:
    """EC6-6: Trim bodies that exceed _MAX_EMAIL_BYTES to avoid Gmail rejection."""
    html_bytes = html_body.encode("utf-8")
    if len(html_bytes) <= _MAX_EMAIL_BYTES:
        return html_body, text_body

    log.warning(
        "email_body_trimmed",
        original_bytes=len(html_bytes),
        limit=_MAX_EMAIL_BYTES,
    )
    trimmed_html = html_bytes[:_MAX_EMAIL_BYTES].decode("utf-8", errors="ignore")
    trimmed_text = text_body[:_MAX_EMAIL_BYTES]
    return trimmed_html, trimmed_text


# ── Main operation ────────────────────────────────────────────────────────────

async def send_pulse_email(
    session: ClientSession,
    *,
    run_id: str,
    product_key: str,
    to: str,
    subject: str,
    html_body: str,
    text_body: str,
    deep_link: str,
    confirm_send: bool = False,
    cc: str = "",
    bcc: str = "",
) -> dict[str, str]:
    """Idempotently create and optionally send a pulse email.

    Steps:
      1. Search Gmail for header X-Pulse-Run-Id:{run_id}.
         If found, skip everything and return persisted message_id. E6-2
      2. Substitute *deep_link* into email bodies. E6-4
      3. Trim bodies to _MAX_EMAIL_BYTES if needed. EC6-6
      4. gmail_create_draft with custom header. E6-1
      5. If *confirm_send* is True, gmail_send_message → gmail_modify_labels. E6-1, E6-5
         Otherwise stop at draft and log. E6-3

    Returns {"message_id": str, "draft_id": str, "sent": bool}.
    """
    # ── Step 1: idempotency check ─────────────────────────────────────────────
    search_q = f"header:X-Pulse-Run-Id:{run_id}"
    search_result = await _call(session, "gmail_search_messages", query=search_q)
    if search_result.get("messages"):
        msg_id: str = search_result["messages"][0]["id"]
        log.info("email_already_sent_skipping", run_id=run_id, message_id=msg_id)
        return {"message_id": msg_id, "draft_id": "", "sent": True}

    # ── Step 2: substitute deep link ─────────────────────────────────────────
    html_body = html_body.replace("{DOC_DEEP_LINK}", deep_link)
    text_body = text_body.replace("{DOC_DEEP_LINK}", deep_link)

    # ── Step 3: size guard ────────────────────────────────────────────────────
    html_body, text_body = _guard_body_size(html_body, text_body)

    # ── Step 4: create draft ──────────────────────────────────────────────────
    draft_result = await _call(
        session,
        "gmail_create_draft",
        to=to,
        subject=subject,
        html_body=html_body,
        text_body=text_body,
        cc=cc,
        bcc=bcc,
        extra_headers={"X-Pulse-Run-Id": run_id},
    )

    if "draftId" not in draft_result:
        raise MCPResponseError(
            f"gmail.create_draft response missing 'draftId'. Got: {draft_result}"
        )

    draft_id: str = draft_result["draftId"]
    log.info("draft_created", run_id=run_id, draft_id=draft_id)

    # ── Step 5: send or stop at draft ────────────────────────────────────────
    if not confirm_send:
        log.info(
            "draft_only_confirm_send_not_set",
            draft_id=draft_id,
            hint="Set PULSE_CONFIRM_SEND=true to send.",
        )
        return {"message_id": "", "draft_id": draft_id, "sent": False}

    send_result = await _call(session, "gmail_send_message", draft_id=draft_id)
    message_id: str = send_result["messageId"]
    log.info("email_sent", run_id=run_id, message_id=message_id)

    # Apply product label after send
    label_name = f"Pulse/{product_key}"
    try:
        label_id = await _ensure_label(session, label_name)
        await _call(
            session,
            "gmail_modify_labels",
            message_id=message_id,
            add_label_ids=[label_id],
        )
        log.info("label_applied", message_id=message_id, label=label_name)
    except Exception as label_exc:
        # Label failure is non-fatal — email was already sent
        log.warning("label_apply_failed", error=str(label_exc), label=label_name)

    return {"message_id": message_id, "draft_id": draft_id, "sent": True}
