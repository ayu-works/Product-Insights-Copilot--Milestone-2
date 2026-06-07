# Plan B — Extending the deployed MCP-server repo

This is a prompt to hand to another chat session that has access to
`https://github.com/ayu-works/Gmail-mcp-server-101` (the source behind the
deployed server at `https://gmail-mcp-server-d2yv.onrender.com`). It closes
the gap between what the server does today (verified by reading
`docs_tool.py` / `gmail_tool.py` directly) and what the Pulse agent actually
needs: idempotency search, rich text/HTML, cc/bcc, configurable timestamp
behavior.

## Prompt to paste into the other session

> I maintain `ayu-works/Gmail-mcp-server-101`, a FastAPI "MCP-inspired" REST
> server deployed at `https://gmail-mcp-server-d2yv.onrender.com`, used by a
> downstream agent (Product Insights Copilot). Please make these changes to
> `docs_tool.py`, `gmail_tool.py`, and `server.py`:
>
> 1. **Remove the hardcoded `[timestamp]` prefix** from `append_to_doc` and
>    `create_email_draft` (or make it opt-in via a boolean field, default
>    off) — the caller wants to control exact content.
> 2. **`append_to_doc`**: accept an optional `requests: list[dict] | None`
>    field (raw Google Docs `batchUpdate` request objects). If provided,
>    pass them through directly to `service.documents().batchUpdate(...)`
>    instead of building a single `insertText`; if omitted, fall back to
>    the current plain-text behavior. This unlocks headings, bold/italic
>    text styles, and named-range/heading anchors.
> 3. **`append_to_doc`**: add a `GET /search_documents?query=` endpoint
>    wrapping Drive's `files().list` (so the caller can resolve an existing
>    doc by title instead of always needing a fixed `doc_id`), and a
>    `POST /create_document {title}` endpoint.
> 4. **`create_email_draft`**: switch `MIMEText(body)` to
>    `MIMEMultipart("alternative")` with both a plain-text part and an
>    `html_body` part (accept an optional `html_body: str | None` field; if
>    present, attach as `text/html`).
> 5. **`create_email_draft`**: accept optional `cc: str`, `bcc: str`, and
>    `extra_headers: dict[str, str]` fields and set them on the message
>    before encoding.
> 6. Add `GET /search_messages?query=` (Gmail `users().messages().list`) so
>    the caller can do idempotency checks (e.g.
>    `header:X-Pulse-Run-Id:{run_id}`).
> 7. Keep the existing `approve()` human-in-the-loop gate and the lack of a
>    `/send_message` endpoint exactly as-is — that's intentional.
>
> Keep changes additive/backwards-compatible (new fields optional, old
> behavior as fallback) so existing callers don't break. After changes,
> redeploy to Render and confirm `/openapi.json` reflects the new schema.

## Why these specific items

- **Timestamp prefix removal**: currently un-suppressible — pollutes both
  doc sections and email bodies with content the caller didn't write.
- **Raw `batchUpdate` passthrough**: only way to get headings/anchors/rich
  styling without rewriting the server's Docs logic from scratch.
- **HTML + cc/bcc**: `MIMEText(body)` is plain-text-only and the Pydantic
  schema has no cc/bcc fields — confirmed at the implementation level.
- **Search endpoints**: needed for the idempotency checks the local FastMCP
  servers already perform (`docs_search_documents`,
  `gmail_search_messages`) — without them, every run risks duplicating
  sections/drafts.
