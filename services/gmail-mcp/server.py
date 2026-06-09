"""FastMCP server — Gmail API wrapper.

Tools exposed:
  gmail_search_messages  — search Gmail with a query string
  gmail_create_draft     — create a MIME draft (HTML + plain text, custom headers)
  gmail_send_message     — send an existing draft
  gmail_create_label     — create a Gmail label (idempotent)
  gmail_modify_labels    — add/remove labels on a message

Authentication:
  Set GOOGLE_CREDENTIALS_JSON to a user OAuth credentials JSON
  (from google-auth-oauthlib flow, saved to a file, then pasted in as one line).
  For service accounts with domain-wide delegation, also set:
    GMAIL_DELEGATED_EMAIL=user@yourdomain.com

Run locally (stdio):
  python server.py

Run as SSE server (Docker):
  python server.py --transport sse --port 8002
"""

from __future__ import annotations

import base64
import email.mime.multipart
import email.mime.text
import json
import os
from typing import Any

from fastmcp import FastMCP

mcp = FastMCP("Gmail MCP")

_GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/gmail.readonly",
]


def _creds() -> Any:
    raw = os.environ.get("GOOGLE_CREDENTIALS_JSON", "")
    if not raw:
        raise RuntimeError(
            "GOOGLE_CREDENTIALS_JSON env var is not set. "
            "See services/gmail-mcp/README.md for setup instructions."
        )
    info = json.loads(raw)

    if info.get("type") == "service_account":
        from google.oauth2 import service_account  # type: ignore[import-untyped]

        delegated = os.environ.get("GMAIL_DELEGATED_EMAIL", "")
        creds = service_account.Credentials.from_service_account_info(
            info, scopes=_GMAIL_SCOPES
        )
        if delegated:
            creds = creds.with_subject(delegated)
        return creds

    from google.oauth2.credentials import Credentials  # type: ignore[import-untyped]
    return Credentials.from_authorized_user_info(info, _GMAIL_SCOPES)


def _gmail_svc() -> Any:
    from googleapiclient.discovery import build  # type: ignore[import-untyped]
    return build("gmail", "v1", credentials=_creds(), cache_discovery=False)


# ── Tools ────────────────────────────────────────────────────────────────────

@mcp.tool()
def gmail_search_messages(query: str, max_results: int = 10) -> dict[str, Any]:
    """Search Gmail messages matching *query*.

    Returns {"messages": [{"id": ..., "threadId": ...}, ...]}.
    The *query* supports Gmail search operators (from:, subject:, header:, etc.).
    """
    try:
        resp = (
            _gmail_svc()
            .users()
            .messages()
            .list(userId="me", q=query, maxResults=max_results)
            .execute()
        )
        return {"messages": resp.get("messages", [])}
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status, "messages": []}


@mcp.tool()
def gmail_create_draft(
    to: str,
    subject: str,
    html_body: str,
    text_body: str,
    cc: str = "",
    bcc: str = "",
    extra_headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Create a Gmail draft with HTML and plain-text parts.

    Pass custom headers (e.g. ``X-Pulse-Run-Id``) via *extra_headers*.
    Returns {"draftId": ..., "messageId": ...}.
    """
    try:
        msg = email.mime.multipart.MIMEMultipart("alternative")
        msg["To"] = to
        msg["Subject"] = subject
        # From header — Gmail always sends from the authenticated account, but
        # setting it explicitly keeps email clients happy and matches display name.
        sender = os.environ.get("PULSE_GMAIL_FROM", "")
        if sender:
            msg["From"] = sender
        if cc:
            msg["Cc"] = cc
        if bcc:
            msg["Bcc"] = bcc
        for k, v in (extra_headers or {}).items():
            msg[k] = v

        msg.attach(email.mime.text.MIMEText(text_body, "plain", "utf-8"))
        msg.attach(email.mime.text.MIMEText(html_body, "html", "utf-8"))

        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        draft = (
            _gmail_svc()
            .users()
            .drafts()
            .create(userId="me", body={"message": {"raw": raw}})
            .execute()
        )
        return {
            "draftId": draft["id"],
            "messageId": draft["message"]["id"],
        }
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status}


@mcp.tool()
def gmail_send_message(draft_id: str) -> dict[str, Any]:
    """Send an existing draft by its *draft_id*.

    Returns {"messageId": ..., "threadId": ...}.
    """
    try:
        sent = (
            _gmail_svc()
            .users()
            .drafts()
            .send(userId="me", body={"id": draft_id})
            .execute()
        )
        return {"messageId": sent["id"], "threadId": sent.get("threadId", "")}
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status}


@mcp.tool()
def gmail_create_label(name: str) -> dict[str, Any]:
    """Create a Gmail label named *name* (idempotent — returns existing if found).

    Returns {"labelId": ..., "name": ...}.
    """
    try:
        svc = _gmail_svc()
        label = (
            svc.users()
            .labels()
            .create(
                userId="me",
                body={
                    "name": name,
                    "labelListVisibility": "labelShow",
                    "messageListVisibility": "show",
                },
            )
            .execute()
        )
        return {"labelId": label["id"], "name": label["name"]}
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        if status == 409:
            # Label already exists — find and return it
            try:
                all_labels = _gmail_svc().users().labels().list(userId="me").execute()
                for lbl in all_labels.get("labels", []):
                    if lbl["name"] == name:
                        return {"labelId": lbl["id"], "name": lbl["name"]}
            except Exception:
                pass
        return {"error": str(exc), "status": status}


@mcp.tool()
def gmail_modify_labels(
    message_id: str,
    add_label_ids: list[str] | None = None,
    remove_label_ids: list[str] | None = None,
) -> dict[str, Any]:
    """Add or remove labels on a sent message.

    Returns {"messageId": ...}.
    """
    try:
        body: dict[str, Any] = {}
        if add_label_ids:
            body["addLabelIds"] = add_label_ids
        if remove_label_ids:
            body["removeLabelIds"] = remove_label_ids
        result = (
            _gmail_svc()
            .users()
            .messages()
            .modify(userId="me", id=message_id, body=body)
            .execute()
        )
        return {"messageId": result["id"]}
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status}


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Gmail FastMCP server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8002)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    if args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run()
