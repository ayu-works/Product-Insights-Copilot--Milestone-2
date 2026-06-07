# Plan A — Thin REST client for phases 5 & 6

**Goal:** Get an end-to-end `publish` run working against the deployed REST
server at `https://gmail-mcp-server-d2yv.onrender.com`, accepting its reduced
feature set (plain text only, auto-injected `[timestamp]` prefix, draft-only
email — no send, no search, no rich formatting).

## New files

- `phases/phase-5-docs-mcp/agent/rest_client/docs_rest.py`
  - `async def append_to_doc(base_url, doc_id, content) -> dict`
  - POSTs `{"doc_id": ..., "content": ...}` to `{base_url}/append_to_doc`
    via `httpx.AsyncClient`; raises on non-2xx / `{"error": ...}` bodies.
- `phases/phase-6-gmail-mcp/agent/rest_client/gmail_rest.py`
  - `async def create_email_draft(base_url, to, subject, body) -> dict`
  - POSTs `{"to": ..., "subject": ..., "body": ...}` to
    `{base_url}/create_email_draft`, same error handling.

## Config

`docs_mcp_url` / `gmail_mcp_url` already exist in `Settings` (both phases).
Populate `phases/.env`:

```
PULSE_DOCS_MCP_URL=https://gmail-mcp-server-d2yv.onrender.com
PULSE_GMAIL_MCP_URL=https://gmail-mcp-server-d2yv.onrender.com
```

## `__main__.py` changes (both phases)

In `publish`, branch on which transport is configured:

- If `docs_mcp_url` / `gmail_mcp_url` is set → use the new
  `_publish_docs_rest` / `_publish_gmail_rest` helpers (REST path).
- Else → keep the existing FastMCP session path untouched (no regression
  for users still running local servers).

**`_publish_docs_rest`**
- Collapses the rich Phase-4 `doc_requests` tree down to a flat plain-text
  string (the REST server only accepts `content: str`).
- Calls `append_to_doc(doc_id, content)`.
- No idempotency search available remotely — log that dedup is skipped.
- `doc_id` must come from `cfg.gdoc_id` / `settings.gdoc_id` (no
  search/auto-create on the deployed server) — error clearly if missing.

**`_publish_gmail_rest`**
- Calls `create_email_draft(to, subject, text_body)` — uses `text_body`
  (not `html_body`), since the server wraps it in `MIMEText` (plain only).
- No cc/bcc/custom headers/idempotency/labels — log that these are
  unavailable remotely.
- Always reports `sent: False` (server only creates drafts).

## Dependency

Add `httpx` to `pyproject.toml` for both phases (check first — may already
be present transitively via `mcp`).

## Test

Run `publish --run <id> --target both` against the deployed URL:
- Confirm a plain-text section is appended to the Google Doc.
- Confirm a Gmail draft is created.
- Confirm the existing local-FastMCP path (`docs_mcp_command` /
  `gmail_mcp_command`) still works unchanged when URLs aren't configured.
