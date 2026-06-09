# Weekly Product Review Pulse

An AI agent that ingests **App Store / Play Store reviews** for a fintech product (Groww, INDMoney, PowerUp Money, Wealth Monitor, Kuvera), uses an LLM to detect recurring **themes** and produce a one-page **weekly insight report**, then delivers it through **MCP (Model Context Protocol)** to Google Workspace:

- **Google Docs MCP** — appends the report as a new dated section to a single running Google Doc per product (the system of record).
- **Gmail MCP** — emails stakeholders a short teaser with a deep link to the new Doc section.

The pipeline is **idempotent** (re-running the same ISO week never duplicates a Doc section or an email) and **auditable** (every run records the Google resource IDs it produced).

> **MCP boundary is sacred:** the agent talks to Google *only* through MCP servers — no direct Google API calls from agent code. Everything else (ingestion, clustering, summarization, rendering) is local code.

## Pipeline

```
ingest → cluster → summarize → render → publish (Docs MCP + Gmail MCP)
```

| Stage | Module | What it does |
|-------|--------|--------------|
| ingest | `agent/ingestion/` | Pull 8–12 weeks of reviews; dedupe by stable id; PII-scrub |
| cluster | `agent/clustering/` | Embed → UMAP → HDBSCAN → medoids → KeyBERT keyphrases |
| summarize | `agent/summarization/` | LLM themes, **verbatim** quotes, action ideas (strict JSON) |
| render | `agent/renderer/` | Docs `batchUpdate` request tree + HTML/text email |
| publish | `agent/mcp_client/`, `services/` | Append to Google Doc + send Gmail, idempotently |
| orchestrate | `agent/orchestrator.py` | `pulse run` chains it all with resumable checkpoints |

The MCP servers themselves live under [`services/docs-mcp/`](services/docs-mcp) and [`services/gmail-mcp/`](services/gmail-mcp) (separate `pyproject.toml`, run as subprocesses).

## Quickstart

Requires [uv](https://docs.astral.sh/uv/) and Python 3.11.

```bash
uv sync                          # install deps from uv.lock
cp .env.example .env             # then fill in your values (see below)
uv run pulse init-db             # create the SQLite database

# run the full pipeline for one product, last 10 weeks
uv run pulse run --product groww --weeks 10
```

Individual stages (each writes to `data/` and can be run on a prior run's id):

```bash
uv run pulse ingest    --product groww --weeks 10
uv run pulse cluster   --run <run_id>
uv run pulse summarize --run <run_id>
uv run pulse render    --run <run_id>
uv run pulse publish   --run <run_id> --target both   # docs | gmail | both
```

Backfill any past week safely (same idempotency logic):

```bash
uv run pulse run --product groww --week 2026-W15
```

## Configuration

Copy `.env.example` → `.env`. Key variables (full list + Google OAuth setup notes are in `.env.example`):

| Variable | Purpose |
|----------|---------|
| `PULSE_DB_PATH` | SQLite path (default `data/pulse.db`) |
| `PULSE_EMBEDDING_PROVIDER` | `local` (bge-small, no key) or `openai` |
| `PULSE_LLM_PROVIDER` / `PULSE_LLM_MODEL` | `groq` / `anthropic` and the model id |
| `PULSE_GROQ_API_KEY` / `PULSE_ANTHROPIC_API_KEY` | LLM credentials |
| `PULSE_MAX_LLM_COST_USD` / `PULSE_MAX_TOKENS_PER_RUN` | per-run hard caps |
| `PULSE_DOCS_MCP_COMMAND` / `PULSE_GMAIL_MCP_COMMAND` | how to launch the MCP servers (stdio) |
| `PULSE_CONFIRM_SEND` | `false` (draft only) until you want real sends |

Products are defined in [`products.yaml`](products.yaml).

## Development

```bash
uv run pytest -m "not slow and not integration"   # fast suite
uv run pytest                                       # full (slow = model/LLM; integration = real Google creds)
uv run ruff check
uv run mypy agent
```

See [`CLAUDE.md`](CLAUDE.md) for conventions and guardrails.

## Scheduling

`.github/workflows/weekly-pulse.yml` runs the pipeline weekly (cron Mon 07:00 IST) in a per-product matrix, and supports manual backfill via `workflow_dispatch`. Operational playbook: [`docs/runbook.md`](docs/runbook.md).

## Documentation

- [`docs/Architecture.md`](docs/Architecture.md) — full design (MCP surface, data model, guardrails, idempotency).
- [`docs/Implementation-Plan.md`](docs/Implementation-Plan.md) — the 8-phase build plan.
- [`docs/Problem-Statement.md`](docs/Problem-Statement.md) — the original brief.
- [`docs/runbook.md`](docs/runbook.md) — operational runbook.
- [`phases/`](phases/) — the phase-by-phase build journey (docs-only; full code at the root, snapshots as git tags `phase-0`…`phase-7`).
- [`docs/phases/`](docs/phases/) — per-phase `evaluations.md` + `edge-cases.md`.
- [`docs/postmortems/`](docs/postmortems/) — debugging write-ups.

## Project layout

```
agent/        the pulse package (ingestion, clustering, summarization, renderer,
              mcp_client, rest_client, orchestrator, observability, storage, config)
services/     the Google Docs and Gmail MCP servers (run as subprocesses)
templates/    Jinja2 email templates + Docs section JSON schema
tests/        pytest suite (fixtures + mock MCP servers)
docs/         architecture, plan, runbook, per-phase specs, postmortems
phases/       docs-only narrative of the 8-phase build journey
```
