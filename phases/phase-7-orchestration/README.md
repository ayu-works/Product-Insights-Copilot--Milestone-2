# Phase 7 — Orchestration, Scheduling & Hardening

> **Snapshot:** `git checkout phase-7` · **Specs:** [evaluations](../../docs/phases/phase-7-orchestration/evaluations.md) · [edge-cases](../../docs/phases/phase-7-orchestration/edge-cases.md)

## What this phase added
The whole pipeline runs weekly, unattended, with observability and cost controls. **This phase's tree is the one promoted to the repo root** during the restructure.
- `agent/orchestrator.py` — top-level `pulse run` chaining all phases with resumable checkpoints driven by `runs.status`.
- Scheduling: `.github/workflows/weekly-pulse.yml` (cron Mon 07:00 IST), per-product matrix.
- `agent/observability.py` — OpenTelemetry spans around every module + MCP tool call; `run_id` as a span attribute.
- Backfill: `pulse run --product groww --week 2026-W15` re-runs any past week safely.
- Runbook at [`../../docs/runbook.md`](../../docs/runbook.md).

## CLI introduced
```bash
uv run pulse run --product groww --weeks 10
uv run pulse run --product groww --week 2026-W15   # backfill
```

## Exit criteria
- Dry-run weekly workflow passes in CI with mocked MCP servers.
- One full unattended run end-to-end in < 5 minutes; LLM cost tracked and under the per-run cap.
- Kill the MCP server mid-run → orchestrator retries; second run completes and stays idempotent.

## Where the code lives now
The entire repo root — `agent/`, `services/`, `templates/`, `tests/` — is this phase's deliverable.
