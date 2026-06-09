# Phase 4 — Report & Email Rendering

> **Snapshot:** `git checkout phase-4` · **Specs:** [evaluations](../../docs/phases/phase-4-renderer/evaluations.md) · [edge-cases](../../docs/phases/phase-4-renderer/edge-cases.md)

## What this phase added
Deterministic conversion of `PulseSummary` into delivery artifacts — pure local rendering, no MCP:
- `agent/renderer/docs_tree.py` — `PulseSummary` → list of Google Docs `batchUpdate` requests (mapping per Architecture §3.1). Anchor `pulse-{product}-{iso_week}` embedded in the Heading 1. Validates against `templates/doc_section.schema.json`.
- `agent/renderer/email_html.py` — Jinja2 → HTML + plain text; `{DOC_DEEP_LINK}` placeholder filled after Phase 5. Subject: `[Weekly Pulse] {Product} — {ISO week} — {Top theme}`.

## CLI introduced
```bash
uv run pulse render --run <run_id>   # writes data/artifacts/{run_id}/{doc_requests.json,email.html,email.txt}
```

## Exit criteria
- Golden-image test: `doc_requests.json` and `email.html` byte-stable on fixture input.
- Schema validator rejects malformed summaries (missing themes, wrong sentiment enum).

## Where the code lives now
`agent/renderer/` (`docs_tree.py`, `email_html.py`); `templates/`.
