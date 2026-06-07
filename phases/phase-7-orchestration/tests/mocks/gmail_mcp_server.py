"""Mock Gmail MCP server for CI dry-runs (E7-1, E7-2).

Implements the same five tools as ``services/gmail-mcp/server.py`` against an
in-memory mailbox, so ``pulse run`` can exercise the full
search -> draft -> (send -> label) flow without real Google credentials.

Run (stdio, launched as a subprocess by the agent):
    python tests/mocks/gmail_mcp_server.py
"""

from __future__ import annotations

import itertools
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mock Gmail MCP")

_id_seq = itertools.count(1)
_drafts: dict[str, dict[str, Any]] = {}
_messages: dict[str, dict[str, Any]] = {}
_labels: dict[str, str] = {}


@mcp.tool()
def gmail_search_messages(query: str, max_results: int = 10) -> dict[str, Any]:
    run_id = ""
    if "X-Pulse-Run-Id:" in query:
        run_id = query.split("X-Pulse-Run-Id:", 1)[1].strip()

    matches = [
        {"id": msg_id}
        for msg_id, msg in _messages.items()
        if not run_id or msg.get("run_id") == run_id
    ][:max_results]
    return {"messages": matches}


@mcp.tool()
def gmail_create_draft(
    to: str,
    subject: str,
    html_body: str,
    text_body: str,
    cc: str = "",
    bcc: str = "",
    extra_headers: Optional[dict[str, str]] = None,
) -> dict[str, Any]:
    draft_id = f"mock-draft-{next(_id_seq)}"
    message_id = f"mock-msg-{next(_id_seq)}"
    _drafts[draft_id] = {
        "message_id": message_id,
        "to": to,
        "subject": subject,
        "run_id": (extra_headers or {}).get("X-Pulse-Run-Id", ""),
    }
    return {"draftId": draft_id, "messageId": message_id}


@mcp.tool()
def gmail_send_message(draft_id: str) -> dict[str, Any]:
    draft = _drafts.get(draft_id)
    if draft is None:
        return {"error": f"Draft {draft_id} not found", "status": 404}

    message_id = draft["message_id"]
    _messages[message_id] = {"run_id": draft["run_id"], "labels": []}
    return {"messageId": message_id, "threadId": f"mock-thread-{message_id}"}


@mcp.tool()
def gmail_create_label(name: str) -> dict[str, Any]:
    label_id = _labels.setdefault(name, f"mock-label-{next(_id_seq)}")
    return {"labelId": label_id, "name": name}


@mcp.tool()
def gmail_modify_labels(
    message_id: str,
    add_label_ids: Optional[list[str]] = None,
    remove_label_ids: Optional[list[str]] = None,
) -> dict[str, Any]:
    msg = _messages.get(message_id)
    if msg is None:
        return {"error": f"Message {message_id} not found", "status": 404}

    labels = set(msg.get("labels", []))
    labels.update(add_label_ids or [])
    labels.difference_update(remove_label_ids or [])
    msg["labels"] = sorted(labels)
    return {"messageId": message_id, "labelIds": msg["labels"]}


if __name__ == "__main__":
    mcp.run()
