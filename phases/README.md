# The Build Journey — Phase by Phase

The Weekly Product Review Pulse agent was built in **8 incremental phases**. The runnable code for *all* phases now lives once at the repo root (`agent/`, `services/`, `tests/`, …). This folder is **documentation only** — it preserves the milestone narrative without duplicating code.

Each phase added a vertical slice that ended in a runnable CLI command. The full source snapshot of every phase is preserved as a **git tag**:

```bash
git checkout phase-2     # full working tree exactly as it was at the end of Phase 2
git checkout chore/repo-restructure   # back to the cleaned, current layout
```

You can also browse a phase's files without switching branches, e.g.:

```bash
git show phase-3:agent/summarization/pipeline.py
```

| Phase | Name | CLI introduced | Notes |
|-------|------|----------------|-------|
| [0](phase-0-foundations/README.md) | Foundations & Scaffolding | `pulse --help`, `pulse init-db` | config, SQLite schema, CLI skeleton, CI |
| [1](phase-1-ingestion/README.md) | Review Ingestion | `pulse ingest` | App Store + Play Store scrapers, PII scrub |
| [2](phase-2-clustering/README.md) | Embeddings & Clustering | `pulse cluster` | embed → UMAP → HDBSCAN → keyphrases |
| [3](phase-3-summarization/README.md) | LLM Summarization | `pulse summarize` | themes, verbatim quotes, action ideas |
| [4](phase-4-renderer/README.md) | Report & Email Rendering | `pulse render` | Docs request tree + HTML/text email |
| [5](phase-5-docs-mcp/README.md) | Google Docs MCP | `pulse publish --target docs` | append dated section, idempotent |
| [6](phase-6-gmail-mcp/README.md) | Gmail MCP | `pulse publish --target gmail` | deliver email with deep link |
| [7](phase-7-orchestration/README.md) | Orchestration & Hardening | `pulse run` | weekly cron, OTel, cost caps, runbook |

**Specs per phase** (kept verbatim from the build) live under [`../docs/phases/<phase>/`](../docs/phases/): each has an `evaluations.md` (how we prove it works) and `edge-cases.md` (what it must survive).

The authoritative design is in [`../docs/Architecture.md`](../docs/Architecture.md) and [`../docs/Implementation-Plan.md`](../docs/Implementation-Plan.md).
