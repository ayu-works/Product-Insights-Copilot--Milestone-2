from __future__ import annotations

from typing import Any

import httpx
import structlog

from agent.mcp_client.errors import MCPResponseError

log = structlog.get_logger()


async def append_to_doc(base_url: str, gdoc_id: str, content: str) -> dict[str, Any]:
    """POST {document_id, content} to {base_url}/append_to_doc and return the JSON body."""
    # The endpoint might be /append_to_doc or similar. We will try /append_to_doc.
    url = f"{base_url.rstrip('/')}/append_to_doc"

    async with httpx.AsyncClient(timeout=60.0) as client:
        # Assuming the payload keys match the generic names. 
        # If it's different (e.g. doc_id), the user will let us know or we'll see a 422 error.
        response = await client.post(url, json={"doc_id": gdoc_id, "content": content})

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

    log.info("rest_doc_appended", doc_id=gdoc_id, status=response.status_code)
    return data
