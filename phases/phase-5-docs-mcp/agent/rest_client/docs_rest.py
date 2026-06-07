"""Thin REST client for the deployed Gmail-MCP-server's Docs endpoint.

The deployed server (https://github.com/ayu-works/Gmail-mcp-server-101) is a
plain FastAPI REST API, not an MCP server. It exposes a single Docs operation:

    POST /append_to_doc {"doc_id": str, "content": str}

It always wraps *content* in a "[timestamp]\\n{content}\\n" envelope and does
a single plain-text insertText — no rich formatting, search, or creation.
"""

from __future__ import annotations

from typing import Any

import httpx
import structlog

from agent.mcp_client.errors import MCPResponseError

log = structlog.get_logger()


async def append_to_doc(base_url: str, doc_id: str, content: str) -> dict[str, Any]:
    """POST {doc_id, content} to {base_url}/append_to_doc and return the JSON body."""
    url = f"{base_url.rstrip('/')}/append_to_doc"

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, json={"doc_id": doc_id, "content": content})

    try:
        data: dict[str, Any] = response.json()
    except ValueError as exc:
        raise MCPResponseError(
            f"append_to_doc: non-JSON response (HTTP {response.status_code}): {response.text!r}"
        ) from exc

    if response.status_code >= 400 or data.get("status") == "error":
        raise MCPResponseError(
            f"append_to_doc failed (HTTP {response.status_code}): {data}"
        )

    log.info("rest_doc_appended", doc_id=doc_id, status=response.status_code)
    return data
