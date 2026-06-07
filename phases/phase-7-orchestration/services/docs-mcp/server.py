"""FastMCP server — Google Docs API wrapper.

Tools exposed:
  docs_get_document      — retrieve a document by ID
  docs_batch_update      — apply batchUpdate requests
  docs_create_document   — create a new document
  docs_search_documents  — search Drive for Docs by title substring

Authentication:
  Set GOOGLE_CREDENTIALS_JSON to the contents of a service-account JSON key
  (or a user OAuth credentials JSON from the Google OAuth flow).
  For service accounts, ensure the service account has Editor access to the
  target document and, if using docs_search_documents, Drive read access.

Run locally (stdio, for agent subprocess):
  python server.py

Run as SSE server (Docker / production):
  python server.py --transport sse --port 8001
"""

from __future__ import annotations

import json
import os
from typing import Any

from fastmcp import FastMCP

mcp = FastMCP("Google Docs MCP")

_DOCS_SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.readonly",
]


def _creds() -> Any:
    raw = os.environ.get("GOOGLE_CREDENTIALS_JSON", "")
    if not raw:
        raise RuntimeError(
            "GOOGLE_CREDENTIALS_JSON env var is not set. "
            "See services/docs-mcp/README.md for setup instructions."
        )
    info = json.loads(raw)

    if info.get("type") == "service_account":
        from google.oauth2 import service_account  # type: ignore[import-untyped]
        return service_account.Credentials.from_service_account_info(
            info, scopes=_DOCS_SCOPES
        )

    from google.oauth2.credentials import Credentials  # type: ignore[import-untyped]
    return Credentials.from_authorized_user_info(info, _DOCS_SCOPES)


def _docs_svc() -> Any:
    from googleapiclient.discovery import build  # type: ignore[import-untyped]
    return build("docs", "v1", credentials=_creds(), cache_discovery=False)


def _drive_svc() -> Any:
    from googleapiclient.discovery import build  # type: ignore[import-untyped]
    from google.oauth2 import service_account  # type: ignore[import-untyped]
    from google.oauth2.credentials import Credentials  # type: ignore[import-untyped]

    raw = os.environ.get("GOOGLE_CREDENTIALS_JSON", "")
    info = json.loads(raw)
    drive_scopes = ["https://www.googleapis.com/auth/drive.readonly"]

    if info.get("type") == "service_account":
        creds = service_account.Credentials.from_service_account_info(
            info, scopes=drive_scopes
        )
    else:
        creds = Credentials.from_authorized_user_info(info, drive_scopes)

    return build("drive", "v3", credentials=creds, cache_discovery=False)


# ── Tools ────────────────────────────────────────────────────────────────────

@mcp.tool()
def docs_get_document(doc_id: str) -> dict[str, Any]:
    """Retrieve a Google Document by its ID.

    Returns the full document resource as returned by the Docs API.
    On error returns {"error": "<message>", "status": <http_code>}.
    """
    try:
        return _docs_svc().documents().get(documentId=doc_id).execute()
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status}


@mcp.tool()
def docs_batch_update(doc_id: str, requests: list[dict[str, Any]]) -> dict[str, Any]:
    """Apply a list of batchUpdate requests to a Google Document.

    *requests* must follow the Google Docs batchUpdate request schema.
    Returns the batchUpdate response on success, or {"error": ..., "status": ...}.
    """
    try:
        return (
            _docs_svc()
            .documents()
            .batchUpdate(documentId=doc_id, body={"requests": requests})
            .execute()
        )
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status}


@mcp.tool()
def docs_create_document(title: str) -> dict[str, Any]:
    """Create a new Google Document with *title*.

    Returns the created document resource (includes *documentId*).
    """
    try:
        return _docs_svc().documents().create(body={"title": title}).execute()
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status}


@mcp.tool()
def docs_search_documents(query: str) -> dict[str, Any]:
    """Search Google Drive for Docs whose title contains *query*.

    Returns {"documents": [{"documentId": ..., "title": ...}, ...]}.
    """
    try:
        safe_q = query.replace("'", "\\'")
        resp = (
            _drive_svc()
            .files()
            .list(
                q=(
                    f"mimeType='application/vnd.google-apps.document'"
                    f" and name contains '{safe_q}'"
                    f" and trashed=false"
                ),
                fields="files(id,name)",
                pageSize=5,
            )
            .execute()
        )
        return {
            "documents": [
                {"documentId": f["id"], "title": f["name"]}
                for f in resp.get("files", [])
            ]
        }
    except Exception as exc:
        status = getattr(getattr(exc, "resp", None), "status", 500)
        return {"error": str(exc), "status": status, "documents": []}


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Google Docs FastMCP server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8001)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    if args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run()
