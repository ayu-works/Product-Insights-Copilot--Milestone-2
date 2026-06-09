# Phase 5 — Google Docs MCP (Append Report)

> **Snapshot:** `git checkout phase-5` · **Specs:** [evaluations](../../docs/phases/phase-5-docs-mcp/evaluations.md) · [edge-cases](../../docs/phases/phase-5-docs-mcp/edge-cases.md)

## What this phase added
Append the rendered report as a new dated section to a running Google Doc, idempotently, **using only MCP**:
- A pinned Google Docs MCP server under `services/docs-mcp/` (added to `docker-compose.yml`).
- `agent/mcp_client/session.py` — connect/close MCP sessions (stdio locally, SSE in prod); validate tool schemas at handshake.
- `agent/mcp_client/docs_ops.py` — `resolve_document(product)` and `append_pulse_section(...)`: get-document → anchor check (skip if present) → `batch_update` → re-read to capture the new `headingId`. Persists `runs.gdoc_heading_id` + `gdoc_id`.
- `agent/rest_client/docs_rest.py` — REST fallback path.

## CLI introduced
```bash
uv run pulse publish --run <run_id> --target docs
```

## Exit criteria
- Against the mock MCP server: first run creates a section; second run is a no-op (anchor detected).
- Against a real test-Workspace Doc: report renders correctly; deep link works.

## Where the code lives now
`agent/mcp_client/` (`session.py`, `docs_ops.py`, `errors.py`), `agent/rest_client/docs_rest.py`, `services/docs-mcp/`.
