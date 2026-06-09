# Phase 0 — Foundations & Scaffolding

> **Snapshot:** `git checkout phase-0` · **Specs:** [evaluations](../../docs/phases/phase-0-foundations/evaluations.md) · [edge-cases](../../docs/phases/phase-0-foundations/edge-cases.md)

## What this phase added
Everything except business logic — the skeleton every later phase builds on:
- `pyproject.toml` (uv) with pinned core deps; `agent/config.py` loading `products.yaml` via pydantic-settings.
- `agent/storage.py` creating all SQLite tables (`products`, `reviews`, `review_embeddings`, `runs`, `themes`).
- `agent/__main__.py` — Typer CLI skeleton with subcommands: `ingest`, `cluster`, `summarize`, `render`, `publish`, `run`.
- `run_id = sha1(product_key + iso_week)` helper + IST-aware ISO-week `Window` helper.
- Structured logging (structlog) with a `run_id` context var; `Dockerfile`, `docker-compose.yml`, GitHub Actions CI.

## CLI introduced
```bash
uv run pulse --help        # lists all subcommands
uv run pulse init-db       # creates a fresh SQLite file with all tables
```

## Exit criteria
- `pulse --help` prints all subcommands.
- `pulse init-db` creates a fresh SQLite file with all tables.
- CI green with two smoke tests.

## Where the code lives now
`agent/config.py`, `agent/storage.py`, `agent/__main__.py`, `agent/helpers.py`, `agent/logging_setup.py`, `agent/models.py`.
