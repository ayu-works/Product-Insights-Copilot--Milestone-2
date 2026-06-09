"""Thin REST client for the deployed Gmail-MCP-server's email endpoint.

The deployed server (https://github.com/ayu-works/Gmail-mcp-server-101) is a
plain FastAPI REST API, not an MCP server. It exposes a single Gmail operation:

    POST /create_email_draft {"to": str, "subject": str, "body": str}

It builds a plain-text MIMEText message (no HTML, cc, bcc, or custom headers),
always wraps *body* in a "[timestamp]\\n\\n{body}\\n" envelope, and only ever
creates a draft — it never sends.
"""

from __future__ import annotations

from typing import Any

import httpx
import structlog

from agent.mcp_client.errors import MCPResponseError

log = structlog.get_logger()


async def create_email_draft(base_url: str, to: str, subject: str, body: str) -> dict[str, Any]:
    """POST {to, subject, body} to {base_url}/create_email_draft and return the JSON body."""
    url = f"{base_url.rstrip('/')}/create_email_draft"

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, json={"to": to, "subject": subject, "body": body})

    try:
        data: dict[str, Any] = response.json()
    except ValueError as exc:
        raise MCPResponseError(
            f"create_email_draft: non-JSON response (HTTP {response.status_code}): {response.text!r}"
        ) from exc

    if response.status_code >= 400 or data.get("status") == "error":
        raise MCPResponseError(
            f"create_email_draft failed (HTTP {response.status_code}): {data}"
        )

    log.info("rest_draft_created", to=to, status=response.status_code)
    return data
