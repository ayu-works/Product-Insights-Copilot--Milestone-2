# Phase 7 — Orchestration, Scheduling & Hardening: Evaluations

## How We Prove It Works

---

### E7-1: Full End-to-End Pipeline (Mocked MCP, CI)

**What to run:**
```bash
pytest tests/test_orchestrator.py::test_full_pipeline_mocked -v
```

**Setup:** All external dependencies mocked: HTTP (ingestion), embedding API, LLM API, Docs MCP, Gmail MCP.

**Pass condition:**
- `pulse run --product groww --weeks 10` completes without error.
- `runs.status = 'success'` in the database.
- All intermediate artifacts exist: `data/raw/`, `data/summaries/`, `data/artifacts/`.
- Both `runs.gdoc_heading_id` and `runs.gmail_message_id` are set.
- Total wall time < 30 seconds (mocked dependencies).

---

### E7-2: Weekly GitHub Actions Workflow

**What to verify:**
- Inspect `.github/workflows/weekly-pulse.yml`.

**Pass condition:**
- Cron schedule is `'30 1 * * 1'` (UTC 01:30 = IST 07:00 on Monday).
- Matrix includes all 5 products: `indmoney`, `groww`, `powermoney`, `wealthmonitor`, `kuvera`.
- Each matrix job sets `PRODUCT` env var and runs `pulse run --product ${{ matrix.product }}`.
- Workflow uses mocked MCP servers in CI (real servers only in a staging environment).
- CI passes on the main branch.

---

### E7-3: Resumable Checkpoints

**What to run:**
```bash
pytest tests/test_orchestrator.py::test_resume_from_checkpoint -v
```

**Setup:** Simulate a run where `runs.status = 'docs_failed'` (Docs MCP step failed, but ingestion + clustering + summarization completed).

**Pass condition:**
- Re-running `pulse run --product groww` detects the existing `run_id` and skips ingestion, clustering, and summarization.
- Only the Docs publish step is retried.
- `runs.status` transitions from `'docs_failed'` → `'success'` on successful retry.

---

### E7-4: OpenTelemetry Trace Coverage

**Pass condition:**
- Every major pipeline step produces an OTel span:
  - `pulse.ingest`, `pulse.cluster`, `pulse.summarize`, `pulse.render`, `pulse.docs_append`, `pulse.gmail_send`.
- Each span has `run_id` as an attribute.
- MCP tool calls produce child spans: `mcp.docs.batch_update`, `mcp.gmail.send_message`, etc.
- Spans are exported to the configured OTLP endpoint (verified by checking the test OTLP collector receives them).

---

### E7-5: Cost Cap Per Run (Full Pipeline)

**What to run:**
```bash
pytest tests/test_orchestrator.py::test_cost_cap_end_to_end -v
```

**Setup:** Set `PULSE_MAX_LLM_COST_USD=0.01`; real summarization on a 400-review fixture would cost ~$0.05.

**Pass condition:**
- `pulse run` raises `PulseCostExceeded` before completing summarization.
- `runs.status = 'cost_exceeded'`.
- Partial `metrics_json` records the cost at the point of the hard stop.
- No Docs or Gmail MCP calls are made.

---

### E7-6: Staging End-to-End Run (Real External Calls)

**What to run (manual, staging environment):**
```bash
PULSE_ENV=staging CONFIRM_SEND=true uv run pulse run --product groww --weeks 10
```

**Pass condition:**
- Completes in < 5 minutes wall time.
- A new dated section appears in the staging Google Doc.
- Email arrives in the staging inbox with a working deep link.
- `runs.metrics_json` contains `llm_cost_usd < $0.10` (sanity check).

---

### E7-7: MCP Server Kill and Retry

**What to test (manual):**
- Start a full run; kill the Docs MCP server subprocess after the clustering step completes.

**Pass condition:**
- Orchestrator catches `MCPConnectionError`.
- Waits 10 seconds, restarts the MCP server process.
- Retries the Docs append step.
- Run completes successfully on retry.
- `runs.gdoc_heading_id` is set exactly once (idempotency holds).

---

### E7-8: Backfill CLI

**What to run:**
```bash
uv run pulse run --product groww --week 2026-W10
```

**Pass condition:**
- Run uses `iso_week = "2026-W10"` regardless of the current date.
- `run_id = sha1("groww" + "2026-W10")` — deterministic and unique.
- Idempotency: re-running the same backfill week is a no-op.
- Backfill does not affect the current week's `run_id`.
