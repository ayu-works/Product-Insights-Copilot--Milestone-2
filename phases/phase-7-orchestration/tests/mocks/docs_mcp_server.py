"""Mock Google Docs MCP server for CI dry-runs (E7-1, E7-2).

Implements the same four tools as ``services/docs-mcp/server.py`` against an
in-memory document store, so ``pulse run`` can exercise the full
resolve -> append -> locate-heading flow without real Google credentials.

Run (stdio, launched as a subprocess by the agent):
    python tests/mocks/docs_mcp_server.py
"""

from __future__ import annotations

import itertools
from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mock Google Docs MCP")

_id_seq = itertools.count(1)
_docs: dict[str, dict[str, Any]] = {}


def _new_doc(title: str) -> dict[str, Any]:
    doc_id = f"mock-doc-{next(_id_seq)}"
    doc = {
        "documentId": doc_id,
        "title": title,
        "body": {"content": [{"endIndex": 1, "paragraph": {"elements": []}}]},
    }
    _docs[doc_id] = doc
    return doc


@mcp.tool()
def docs_get_document(doc_id: str) -> dict[str, Any]:
    doc = _docs.get(doc_id)
    if doc is None:
        return {"error": f"Document {doc_id} not found", "status": 404}
    return doc


@mcp.tool()
def docs_batch_update(doc_id: str, requests: list[dict[str, Any]]) -> dict[str, Any]:
    doc = _docs.get(doc_id)
    if doc is None:
        return {"error": f"Document {doc_id} not found", "status": 404}

    content = doc["body"]["content"]
    base_index = max((el.get("endIndex", 1) for el in content), default=1)

    for req in requests:
        insert = req.get("insertText")
        if not insert:
            continue
        text = insert.get("text", "")
        style = (req.get("updateParagraphStyle") or {}).get("paragraphStyle", {})
        named_style = style.get("namedStyleType", "NORMAL_TEXT")
        heading_id = f"heading-{next(_id_seq)}" if named_style == "HEADING_1" else None

        end_index = base_index + len(text)
        paragraph: dict[str, Any] = {
            "elements": [{"textRun": {"content": text}}],
            "paragraphStyle": {"namedStyleType": named_style},
        }
        if heading_id:
            paragraph["paragraphStyle"]["headingId"] = heading_id

        content.append({"startIndex": base_index, "endIndex": end_index, "paragraph": paragraph})
        base_index = end_index

    return {"documentId": doc_id, "replies": [{} for _ in requests]}


@mcp.tool()
def docs_create_document(title: str) -> dict[str, Any]:
    return _new_doc(title)


@mcp.tool()
def docs_search_documents(query: str) -> dict[str, Any]:
    matches = [
        {"documentId": doc_id, "title": doc["title"]}
        for doc_id, doc in _docs.items()
        if query.lower() in doc["title"].lower()
    ]
    return {"documents": matches}


if __name__ == "__main__":
    mcp.run()
