# Phase 7 — Orchestration, Scheduling & Hardening: Edge Cases

## What We Must Survive

---

### EC7-1: Previous Run Still In Progress When New One Starts

**Scenario:** The weekly cron fires at 07:00 IST, but last week's run is still executing (e.g. due to LLM rate limiting delays).

**Expected behaviour:**
- A `runs` row with `status = 'in_progress'` and the current `iso_week` already exists.
- The new run detects the in-progress run by checking `SELECT * FROM runs WHERE product_key=? AND iso_week=? AND status='in_progress'`.
- The new run exits immediately with a log: `"Run {run_id} already in progress, exiting to avoid double-run"`.
- An alert is fired: `"Weekly cron: run {run_id} still in progress from previous trigger"`.

---

### EC7-2: All Products Fail Ingestion

**Scenario:** The App Store and Play Store are both unreachable for a full hour (rare outage).

**Expected behaviour:**
- Each product's run is marked `status = 'ingestion_failed'`.
- An alert fires: `"Ingestion failed for ALL products in this week's run"`.
- No Docs or Gmail calls are made (nothing to publish).
- Backfill CLI can re-run each product individually once the stores are back online.

---

### EC7-3: Partial Pipeline Failure (Ingested but Not Clustered)

**Scenario:** `pulse ingest` succeeds, but `pulse cluster` crashes due to an HDBSCAN OOM error.

**Expected behaviour:**
- `runs.status = 'cluster_failed'`.
- Reviews are already in the database (ingestion was committed).
- On re-run, ingestion is skipped (reviews already present, dedup catches them).
- Clustering is retried from scratch with the already-ingested reviews.
- No duplicate ingestion or duplicated API calls.

---

### EC7-4: GitHub Actions Runner Out of Memory

**Scenario:** Embedding 400+ reviews with sentence-transformers exhausts the 7 GB GitHub-hosted runner.

**Expected behaviour:**
- CI uses `EMBEDDING_PROVIDER=openai` (API-based, no local model) by default.
- Local model is only used if `EMBEDDING_PROVIDER=local` is explicitly set.
- If OOM still occurs (e.g. UMAP on large fixture), the workflow fails with a clear error and a runbook note to increase the runner size.

---

### EC7-5: Timezone Edge Case — Monday 00:00 IST

**Scenario:** The cron fires exactly at Monday 00:00 IST (23:30 UTC Sunday), which is the boundary between ISO week N and ISO week N+1.

**Expected behaviour:**
- `Window.from_iso_week` uses IST-aware `date` objects.
- Monday 00:00 IST is the start of the new ISO week (ISO 8601: weeks start on Monday).
- `run_id = sha1(product_key + "2026-W17")` for week starting Monday Apr 20, not `W16`.
- No off-by-one: the report covers the just-completed week (W16), not the week that just started (W17).
- Cron is scheduled for Mon 07:00 IST to provide a safe buffer from the midnight boundary.

---

### EC7-6: Backfill of Many Weeks at Once

**Scenario:** Developer runs backfill for 12 consecutive weeks:
```bash
for week in $(seq 1 12); do pulse run --product groww --week 2026-W$week; done
```

**Expected behaviour:**
- Each week has a distinct `run_id`; no collisions.
- Runs execute sequentially (not concurrently from the CLI); each completes before the next starts.
- LLM and MCP rate limits may be hit; backoff handles them per-run.
- All 12 Doc sections are appended in chronological order (ordering is based on run time, not week number — acceptable).

---

### EC7-7: OTel Collector Unreachable

**Scenario:** The OTLP endpoint is not running (e.g. local dev without a collector).

**Expected behaviour:**
- OTel export failure is caught and logged as a warning: `"OTel export failed: {error}. Traces lost but run continues."`.
- The pipeline does NOT fail because of an observability export error.
- Traces are not buffered indefinitely (avoid memory leak); they are dropped after 3 failed export attempts.

---

### EC7-8: `runs` Table Has Duplicate Rows for Same `run_id`

**Scenario:** A race condition or bug creates two rows with the same `run_id` (should be prevented by `PRIMARY KEY`, but edge cases can arise with SQLite WAL mode).

**Expected behaviour:**
- `run_id TEXT PRIMARY KEY` constraint prevents duplicates at the DB level — an `IntegrityError` is raised.
- Orchestrator catches `IntegrityError` on `INSERT` and switches to `UPDATE` (upsert logic).
- An alert fires: `"Duplicate run_id detected: {run_id} — investigate immediately"`.

---

### EC7-9: Cost Spike Alert

**Scenario:** LLM tokens for a single run exceed 5× the historical average (e.g. a product suddenly has 2,000 reviews instead of 200).

**Expected behaviour:**
- After `pulse summarize` completes, the orchestrator compares `llm_cost_usd` against the 4-week rolling average from `runs.metrics_json`.
- If cost is > 3× the average, a warning alert fires: `"LLM cost spike: {cost_usd:.4f} vs avg {avg:.4f}"`.
- The run is not aborted by this check alone (it's a warning, not a hard stop).
- The hard stop from Phase 3 (`PULSE_MAX_LLM_COST_USD`) is the circuit breaker.
