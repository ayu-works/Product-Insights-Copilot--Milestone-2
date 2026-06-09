# Pulse Orchestrator Runbook

Operational guide for the weekly `pulse run` pipeline (Phase 7). Each section
below covers a specific failure scenario: how to recognise it, diagnose it,
and recover.

All commands assume you're in `phases/phase-7-orchestration/`.

---

## "Email not sent"

**Symptoms:** `runs.gmail_message_id` is empty / NULL after a run that otherwise
shows `status = 'success'` or `'published_docs'`.

**Likely causes & checks:**
1. **`PULSE_CONFIRM_SEND` is not set.** By default the agent only creates a
   Gmail *draft* (E6-3 / dry-run-by-default). Check:
   ```bash
   echo $PULSE_CONFIRM_SEND
   ```
   Set `PULSE_CONFIRM_SEND=true` in `phases/.env` to actually send.
2. **No `gmail_to` configured** for the product — check `products.yaml` and
   `PULSE_GMAIL_TO` in `.env`. The run would have failed at the publish step
   with "has no gmail_to address configured".
3. **Gmail MCP/REST auth failure** — look for `MCPAuthError` / `401`/`403` in
   the logs around `publish_gmail_complete`. Refresh `GOOGLE_CREDENTIALS_JSON`
   (see "Token revoked" below).

**Recovery:** once the cause is fixed, re-run just the Gmail leg:
```bash
uv run pulse publish --run <run_id> --target gmail
```
This is idempotent — `send_pulse_email` searches for an existing
`X-Pulse-Run-Id` header before creating a new draft (E6-2).

---

## "Duplicate section in Doc"

**Symptoms:** The weekly Google Doc has two headings for the same product/week.

**Likely causes & checks:**
1. **Anchor mismatch** — `append_pulse_section` checks for the anchor string
   `pulse-{product_key}-{iso_week}` in the existing document body before
   appending. If the anchor format changed between runs (e.g. a code change),
   the idempotency check silently misses the existing section. Diff the anchor
   construction in `agent/__main__.py` (`anchor = f"pulse-{product_key}-{iso_week}"`)
   against what's actually in the Doc.
2. **Two runs raced** — confirm only one `runs` row exists for
   `(product_key, iso_week)`: `run_id = sha1(product_key + iso_week)` is
   deterministic, so duplicates indicate either a schema problem (see
   "`runs` table has duplicate rows", EC7-8) or that the deployed REST Docs
   server was used (`PULSE_DOCS_MCP_URL`) — that thin server has **no**
   idempotency search and appends unconditionally on every call (see the
   warning in `_publish_docs_rest`).

**Recovery:** manually delete the duplicate heading/section in the Doc. If the
REST server is the cause, prefer the full `PULSE_DOCS_MCP_COMMAND` (FastMCP)
path, which performs the anchor check, for any product where duplicates matter.

**Built-in mitigation (E7-7 retry path):** because the deployed REST server has
no idempotency search, `_step_publish` in `agent/orchestrator.py` will not blindly
retry the whole `publish(target="both")` call after a connection error. If
`runs.status` has already advanced to `published_docs` (the Docs leg succeeded
before the connection dropped), the retry narrows to `target="gmail"` only —
so a flaky connection can't cause a second append to the Doc.

---

## "Ingestion empty"

**Symptoms:** `pulse ingest` / the ingest step reports `0 new reviews` for a
product that normally has reviews, or `runs.status = 'ingestion_failed'`.

**Likely causes & checks:**
1. **App Store / Play Store outage** — check `ingest_raw_count` in the logs.
   If `total = 0` for *all* products in the same run, this is EC7-2 (full
   outage): an alert `"Ingestion failed for ALL products in this week's run"`
   should have fired. No Docs/Gmail calls are made in that case (nothing to
   publish) — this is expected, not a bug.
2. **Aggressive PII/quality filtering** — check `ingest_filtered` vs
   `ingest_raw_count`. If `filtered` is unexpectedly high, review
   `agent/ingestion/filters.py` (`should_keep`, `scrub_pii`) for over-eager
   rules.
3. **Wrong `appstore_id` / `play_package`** in `products.yaml`.

**Recovery:** once the store is back online or the config is fixed, re-run
ingestion for the affected product(s) via the backfill CLI — it's safe to
re-run (dedup on `reviews.id`):
```bash
uv run pulse run --product <key> --week <iso_week>
```

---

## "LLM cost spike"

**Symptoms:** Alert `"LLM cost spike: {cost} vs avg {avg}"` (EC7-9), or the run
aborted with `runs.status = 'cost_exceeded'` (E7-5).

**Likely causes & checks:**
1. **Review volume jumped** (e.g. 2,000 reviews instead of 200) — check
   `runs.metrics_json -> reviews_ingested` and `clusters_formed` for this run
   vs the last 4 weeks (`SELECT iso_week, metrics_json FROM runs WHERE
   product_key = ? ORDER BY iso_week DESC LIMIT 5`).
2. **Model/provider changed** — check `PULSE_LLM_PROVIDER` / `PULSE_LLM_MODEL`
   and per-token pricing in `agent/summarization/client.py`.

**Distinguishing warning vs hard-stop:**
- The **cost-spike alert** (>3x rolling average, `cost_spike_multiplier` in
  config) is a *warning* — the run continues (EC7-9).
- The **cost cap** `PULSE_MAX_LLM_COST_USD` is a *hard stop* — `summarize`
  raises `PulseCostExceeded`, the orchestrator sets `runs.status =
  'cost_exceeded'`, and **no Docs/Gmail calls are made**.

**Recovery:**
- For a one-off spike (real review surge): raise `PULSE_MAX_LLM_COST_USD`
  temporarily and re-run — resumes from `summarize` (status `cost_exceeded`
  resumes at the summarize step):
  ```bash
  PULSE_MAX_LLM_COST_USD=0.50 uv run pulse run --product <key>
  ```
- For a runaway/looping bug: investigate `agent/summarization/pipeline.py`
  before re-running — don't just raise the cap.

---

## "MCP server crash"

**Symptoms:** `MCPConnectionError` in the logs during the publish step;
`runs.status` stuck at `docs_failed` / `gmail_failed`.

**Expected automatic behaviour (E7-7):** the orchestrator catches
`MCPConnectionError`, waits `PULSE_MCP_RETRY_WAIT_SECONDS` (default 10s),
and retries the publish step up to `PULSE_MCP_MAX_RETRIES` times (default 1
retry). If it still fails, the run stops with a `<step>_failed` status and the
error is logged via `pulse_run_step_failed`.

**Manual checks:**
1. Is the MCP server subprocess command (`PULSE_DOCS_MCP_COMMAND` /
   `PULSE_GMAIL_MCP_COMMAND`) still valid (correct path, Python env, deps
   installed)?
2. Check for OOM / crash logs from the subprocess itself
   (`services/docs-mcp/server.py`, `services/gmail-mcp/server.py`).
3. Verify `GOOGLE_CREDENTIALS_JSON` is present in the subprocess environment —
   missing credentials cause an immediate crash on startup, which looks like a
   connection error from the agent's side.

**Recovery:** once the server is healthy again, re-run — it picks up exactly
where it left off (idempotent: `gdoc_heading_id` / `gmail_message_id` are set
exactly once):
```bash
uv run pulse run --product <key>
```

---

## "Token revoked"

**Symptoms:** `MCPAuthError`, or tool responses containing
`{"error": ..., "status": 401}` / `403` from the Docs or Gmail MCP server.

**Likely causes & checks:**
1. **OAuth refresh token expired or was revoked** (e.g. user changed their
   Google Account password, revoked third-party access, or the token simply
   aged out).
2. **Service account key rotated/deleted** without updating
   `GOOGLE_CREDENTIALS_JSON`.
3. **Scopes insufficient** — Docs needs `documents` + `drive.readonly`; Gmail
   needs `gmail.send`, `gmail.compose`, `gmail.modify`, `gmail.labels`.

**Recovery:**
1. Re-run the OAuth flow (or regenerate the service-account key) for the
   affected Google Workspace account.
2. Update `GOOGLE_CREDENTIALS_JSON` (and `GMAIL_DELEGATED_EMAIL` if using
   domain-wide delegation) in the deployment's secret store / `phases/.env`.
3. Restart the MCP server subprocess (or just re-run `pulse run` — the agent
   launches it fresh each time for the `*_MCP_COMMAND` path).
4. Re-run the failed step:
   ```bash
   uv run pulse run --product <key>
   ```

---

## General diagnostics

```bash
# Inspect a run's checkpoint history
sqlite3 data/pulse.db "SELECT id, product_key, iso_week, status, gdoc_heading_id, gmail_message_id, metrics_json FROM runs WHERE id = '<run_id>';"

# Re-run from scratch for the current week (safe — dedup/idempotency hold throughout)
uv run pulse run --product <key>

# Backfill a specific past week (deterministic run_id, no effect on current week)
uv run pulse run --product <key> --week 2026-W15
```

Every pipeline stage emits an OTel span (`pulse.ingest`, `pulse.cluster`,
`pulse.summarize`, `pulse.render`, `pulse.publish`, plus `mcp.*` child spans),
each tagged with `run_id` — use these to correlate logs with traces in your
OTLP backend. If the OTLP collector is unreachable, export failures are logged
as warnings and traces are dropped after 3 attempts — the pipeline itself is
unaffected (EC7-7).
