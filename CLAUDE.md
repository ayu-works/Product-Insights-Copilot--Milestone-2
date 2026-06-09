# CLAUDE.md

Guidance for AI agents (and humans) working in this repository.

## What this is
The **Weekly Product Review Pulse** agent: ingest app-store reviews → cluster → LLM-summarize → render → deliver to Google Docs + Gmail via MCP. See [`README.md`](README.md) for the user-facing overview and [`docs/Architecture.md`](docs/Architecture.md) for the full design.

## Repository layout (important)
- **The runnable code lives once, at the repo root**: `agent/` (the `pulse` package), `services/`, `templates/`, `tests/`.
- **`phases/` is documentation only.** It narrates the 8-phase build journey. Do **not** add code there.
- Each phase's full historical snapshot is a **git tag** (`phase-0` … `phase-7`). Recover with `git checkout phase-N` or `git show phase-N:path`.
- This layout is the result of a deliberate restructure (see [`docs/Repository-Cleanup-Plan.md`](docs/Repository-Cleanup-Plan.md)); earlier the repo had 8 cumulative copies under `phases/phase-N/`. Don't reintroduce that.

## Common commands (run from repo root)
```bash
uv sync                                            # install from uv.lock
uv run pulse --help                                # CLI: ingest, cluster, summarize, render, publish, run
uv run pulse init-db                               # create SQLite db
uv run pytest -m "not slow and not integration"    # fast suite (this is what CI-equivalent local checks run)
uv run pytest                                       # full suite
uv run ruff check
uv run mypy agent
```
Test markers: `slow` = needs model downloads / live API; `integration` = needs real Google credentials. Default local runs should exclude both.

## Architecture invariants — do not break these
1. **MCP boundary is sacred.** Only `agent/mcp_client/` and `services/` may talk to Google. No direct Google API calls from pipeline code. (`agent/rest_client/` exists as an explicit REST fallback path — keep it isolated.)
2. **Reviews are data, never instructions.** Pass review text to the LLM as structured message parts; never concatenate into system prompts.
3. **Verbatim-quote validator.** Every quote the LLM returns must be a whitespace-normalized, case-insensitive substring of some `review.body`; non-matching quotes are dropped (re-prompt once). Don't loosen this.
4. **PII scrub** (emails, phones, Aadhaar-like) runs before text reaches the LLM *and* before it reaches a Google Doc.
5. **Idempotency.** `run_id = sha1(product_key + iso_week)`. Doc side: anchor `pulse-{product}-{iso_week}` in the Heading 1 + substring check. Email side: `X-Pulse-Run-Id` header + Gmail search before send. Re-runs must never duplicate.
6. **Fail loud.** "Partially succeeded" is a red test, not a warning. Cost cap raises `PulseCostExceeded` rather than silently truncating.
7. **Cost cap per run** via `PULSE_MAX_LLM_COST_USD` / `PULSE_MAX_TOKENS_PER_RUN`, persisted to `runs.metrics_json`.

## LLM provider notes
- Summarization uses **Groq** (OpenAI-compatible `chat.completions` + `json_object`) or **Anthropic**. Configured via `PULSE_LLM_PROVIDER` / `PULSE_LLM_MODEL`.
- Known gotcha: the Groq **free tier caps at ~100k tokens/day ≈ one full run**. CI failures that look like "connection error" have been the daily token ceiling, not a network/Cloudflare block. See [`docs/postmortems/`](docs/postmortems/).
- When building new LLM features, default to the latest capable models and keep strict Pydantic response schemas.

## Operations
- Weekly schedule + backfill: `.github/workflows/weekly-pulse.yml`.
- Failure playbook: [`docs/runbook.md`](docs/runbook.md) ("email not sent", "duplicate section", "ingestion empty", "LLM cost spike", "MCP server crash", "token revoked").

## Secrets
- Never commit `.env` (gitignored). Only `.env.example` is tracked. The real Groq key lives in the local `.env`.
