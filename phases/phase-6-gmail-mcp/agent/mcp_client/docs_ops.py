"""Phase 5: Google Docs operations via MCP.

Key operations:
  resolve_document   — get or create the running Google Doc for a product
  append_pulse_section — idempotently append a weekly report section
"""

from __future__ import annotations

import copy
import json
from typing import Any

import structlog
from mcp import ClientSession

from agent.mcp_client.errors import MCPAuthError, MCPPermissionError, MCPResponseError

log = structlog.get_logger()


# ── Low-level MCP call helper ─────────────────────────────────────────────────

async def _call(session: ClientSession, tool: str, **kwargs: Any) -> Any:
    """Call *tool* on the MCP session and return the parsed JSON result.

    Raises MCPPermissionError, MCPAuthError, or MCPResponseError on failure.
    """
    result = await session.call_tool(tool, kwargs)

    if result.isError:
        err_text = result.content[0].text if result.content else "unknown error"
        raise MCPResponseError(f"{tool} returned MCP error: {err_text}")

    raw = result.content[0].text if result.content else "{}"
    data: dict[str, Any] = json.loads(raw)

    # The FastMCP server returns {"error": ..., "status": ...} for API failures.
    if "error" in data:
        msg = str(data["error"])
        status = data.get("status", 0)
        if status == 401 or "token" in msg.lower() or "auth" in msg.lower():
            raise MCPAuthError(f"{tool}: {msg}")
        if status == 403 or "permission" in msg.lower() or "forbidden" in msg.lower():
            raise MCPPermissionError(
                f"Docs MCP: insufficient permission for {tool} — {msg}. "
                "Ensure the service account has Editor access to the document."
            )
        raise MCPResponseError(f"{tool} API error (HTTP {status}): {msg}")

    return data


# ── Index shifting ────────────────────────────────────────────────────────────

def _shift_requests(
    requests: list[dict[str, Any]], shift: int
) -> list[dict[str, Any]]:
    """Deep-copy *requests* and shift every Docs API index by *shift*.

    This converts Phase-4 requests (indices from 1) into append-at-end requests
    by adding (doc_end_index - 1) to every index/range value.
    """
    shifted = copy.deepcopy(requests)
    for req in shifted:
        for op in req.values():
            if not isinstance(op, dict):
                continue
            if "location" in op and "index" in op["location"]:
                op["location"]["index"] += shift
            for range_key in ("range", "cellLocation"):
                rng = op.get(range_key)
                if isinstance(rng, dict):
                    if "startIndex" in rng:
                        rng["startIndex"] += shift
                    if "endIndex" in rng:
                        rng["endIndex"] += shift
    return shifted


def _strip_metadata(
    requests: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Separate _tableContent metadata from real Docs API requests.

    Returns (clean_requests, table_metas).
    The Docs API rejects keys it doesn't recognise, so underscore-prefixed
    metadata keys must be removed before the batchUpdate call.
    """
    clean: list[dict[str, Any]] = []
    table_metas: list[dict[str, Any]] = []
    for req in requests:
        if "_tableContent" in req:
            table_metas.append(req["_tableContent"])
            clean.append({k: v for k, v in req.items() if not k.startswith("_")})
        else:
            clean.append(req)
    return clean, table_metas


# ── Table cell filling ────────────────────────────────────────────────────────

async def _fill_table_cells(
    session: ClientSession,
    doc_id: str,
    table_metas: list[dict[str, Any]],
    inserted_after_index: int,
) -> None:
    """Fill table cells that were just inserted by batch_update.

    Fetches the updated doc, locates tables that start at or after
    *inserted_after_index*, then inserts text into each cell using a second
    batch_update call. Cell indices are filled in reverse order to avoid
    shifting subsequent indices.
    """
    if not table_metas:
        return

    doc = await _call(session, "docs_get_document", doc_id=doc_id)
    body_content = doc.get("body", {}).get("content", [])

    new_tables = [
        el["table"]
        for el in body_content
        if "table" in el and el.get("startIndex", 0) >= inserted_after_index
    ]

    cell_requests: list[dict[str, Any]] = []

    for meta, table in zip(table_metas, new_tables):
        headers = meta.get("headers", [])
        data_rows = meta.get("rows", [])
        all_rows = [headers] + data_rows
        table_rows = table.get("tableRows", [])

        # Collect (cell_start_index, text) in forward order, then reverse to
        # avoid invalidating earlier indices when inserting backwards.
        insertions: list[tuple[int, str]] = []
        for row_data, table_row in zip(all_rows, table_rows):
            cells = table_row.get("tableCells", [])
            for cell_text, cell in zip(row_data, cells):
                # +1 to move past the cell's opening paragraph element
                cell_start = cell.get("startIndex", 0) + 1
                insertions.append((cell_start, str(cell_text)))

        for cell_start, text in reversed(insertions):
            cell_requests.append({
                "insertText": {
                    "location": {"index": cell_start},
                    "text": text,
                }
            })

    if cell_requests:
        await _call(session, "docs_batch_update", doc_id=doc_id, requests=cell_requests)
        log.info("table_cells_filled", doc_id=doc_id, cells=len(cell_requests))


# ── Body text / heading helpers ───────────────────────────────────────────────

def _body_text(doc: dict[str, Any]) -> str:
    """Concatenate all text runs from the document body."""
    parts: list[str] = []
    for el in doc.get("body", {}).get("content", []):
        for pe in el.get("paragraph", {}).get("elements", []):
            parts.append(pe.get("textRun", {}).get("content", ""))
    return "".join(parts)


def _find_heading_id(doc: dict[str, Any], anchor: str) -> str | None:
    """Return the headingId of the HEADING_1 paragraph containing *anchor*."""
    for el in doc.get("body", {}).get("content", []):
        para = el.get("paragraph", {})
        style = para.get("paragraphStyle", {})
        if style.get("namedStyleType") != "HEADING_1":
            continue
        text = "".join(
            pe.get("textRun", {}).get("content", "")
            for pe in para.get("elements", [])
        )
        if anchor in text:
            return style.get("headingId")
    return None


def _doc_end_index(doc: dict[str, Any]) -> int:
    """Return the end index of the last element in the document body."""
    content = doc.get("body", {}).get("content", [])
    return max((el.get("endIndex", 1) for el in content), default=1)


# ── Public operations ─────────────────────────────────────────────────────────

async def resolve_document(
    session: ClientSession,
    product_key: str,
    display_name: str,
    cached_doc_id: str | None,
) -> str:
    """Return the Google Doc ID for *product_key*.

    Resolution order:
      1. If *cached_doc_id* is set, verify it still exists and return it.
         On 404 / not-found, clear the cache and fall through.
      2. Search Drive for a Doc whose title contains *display_name*.
      3. Create a fresh Doc titled "Weekly Review Pulse — {display_name}".

    E5-3 / EC5-1
    """
    title = f"Weekly Review Pulse — {display_name}"

    if cached_doc_id:
        try:
            await _call(session, "docs_get_document", doc_id=cached_doc_id)
            log.info("doc_resolved_from_cache", doc_id=cached_doc_id)
            return cached_doc_id
        except MCPResponseError as exc:
            if "404" in str(exc) or "not found" in str(exc).lower():
                log.warning("cached_doc_id_stale", old_id=cached_doc_id)
            else:
                raise

    results = await _call(session, "docs_search_documents", query=title)
    docs_list = results.get("documents", [])
    if docs_list:
        doc_id: str = docs_list[0]["documentId"]
        log.info("doc_found_by_search", doc_id=doc_id, title=title)
        return doc_id

    created = await _call(session, "docs_create_document", title=title)
    doc_id = created["documentId"]
    log.info("doc_created", doc_id=doc_id, title=title)
    return doc_id


async def append_pulse_section(
    session: ClientSession,
    doc_id: str,
    doc_requests: list[dict[str, Any]],
    anchor: str,
) -> dict[str, str]:
    """Idempotently append a pulse report section to *doc_id*.

    Steps:
      1. docs_get_document → search body text for *anchor* substring.
         If found, return existing heading ID immediately (no-op). E5-2
      2. Compute shift = doc_end_index - 1, strip _tableContent metadata.
      3. docs_batch_update with shifted requests.
      4. Fill any table cells (_tableContent). E5-4
      5. docs_get_document again → locate heading by anchor, return headingId.
         E5-5 (deep link construction)

    Returns {"heading_id": str, "deep_link": str}.
    """
    # ── Step 1: idempotency check ─────────────────────────────────────────────
    doc = await _call(session, "docs_get_document", doc_id=doc_id)
    existing_text = _body_text(doc)

    if anchor in existing_text:
        log.info("section_already_present_skipping_append", anchor=anchor, doc_id=doc_id)
        heading_id = _find_heading_id(doc, anchor) or ""
        deep_link = (
            f"https://docs.google.com/document/d/{doc_id}/edit#heading={heading_id}"
            if heading_id else ""
        )
        return {"heading_id": heading_id, "deep_link": deep_link}

    # ── Step 2: prepare requests ─────────────────────────────────────────────
    end_index = _doc_end_index(doc)
    shift = end_index - 1
    clean_requests, table_metas = _strip_metadata(doc_requests)
    shifted = _shift_requests(clean_requests, shift)

    log.info(
        "appending_section",
        doc_id=doc_id,
        anchor=anchor,
        shift=shift,
        requests=len(shifted),
    )

    # ── Step 3: batch update ─────────────────────────────────────────────────
    await _call(session, "docs_batch_update", doc_id=doc_id, requests=shifted)

    # ── Step 4: fill table cells ─────────────────────────────────────────────
    await _fill_table_cells(session, doc_id, table_metas, inserted_after_index=end_index)

    # ── Step 5: locate heading ID ─────────────────────────────────────────────
    updated_doc = await _call(session, "docs_get_document", doc_id=doc_id)
    heading_id = _find_heading_id(updated_doc, anchor) or ""
    if not heading_id:
        log.warning("heading_id_not_found_after_append", anchor=anchor, doc_id=doc_id)

    deep_link = f"https://docs.google.com/document/d/{doc_id}/edit#heading={heading_id}"
    log.info("section_appended", doc_id=doc_id, heading_id=heading_id)
    return {"heading_id": heading_id, "deep_link": deep_link}
