# Phase 6 — Gmail MCP (Deliver Email)

> **Snapshot:** `git checkout phase-6` · **Specs:** [evaluations](../../docs/phases/phase-6-gmail-mcp/evaluations.md) · [edge-cases](../../docs/phases/phase-6-gmail-mcp/edge-cases.md)

## What this phase added
Send the stakeholder email with the Doc deep link, once per run, via the Gmail MCP server:
- A pinned Gmail MCP server under `services/gmail-mcp/`.
- `agent/mcp_client/gmail_ops.py` — `send_pulse_email(...)`: `search_messages` for `X-Pulse-Run-Id:{run_id}` (skip if found) → `create_draft` with that custom header + `Pulse/{product}` label → if `PULSE_CONFIRM_SEND=true`, `send_message`; else stop at draft. Persists `runs.gmail_message_id`.
- Email body gets the real `{DOC_DEEP_LINK}` from Phase 5.

## CLI introduced
```bash
uv run pulse publish --run <run_id> --target gmail
uv run pulse publish --run <run_id> --target both
```

## Exit criteria
- Mock MCP test: first run sends (draft→send); second run detects header and skips; `runs.gmail_message_id` set exactly once.
- Dry-run default: without `PULSE_CONFIRM_SEND`, a draft exists but no send occurs.

## Where the code lives now
`agent/mcp_client/gmail_ops.py`, `agent/rest_client/gmail_rest.py`, `services/gmail-mcp/`.
