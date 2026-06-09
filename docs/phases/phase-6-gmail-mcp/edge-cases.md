# Phase 6 — Gmail MCP — Deliver Email: Edge Cases

## What We Must Survive

---

### EC6-1: Gmail MCP Server Auth Token Expired

**Scenario:** The OAuth refresh token stored in the Gmail MCP server has expired or been revoked.

**Expected behaviour:**
- `gmail.create_draft` returns an authentication error.
- Agent raises `MCPAuthError("Gmail MCP: auth token expired. Re-authenticate the MCP server.")`.
- `runs.status = 'gmail_auth_failed'`.
- Runbook entry: "Run `pulse-gmail-mcp auth` to re-authenticate, then retry."

---

### EC6-2: Docs Append Succeeded but Gmail Send Fails

**Scenario:** Phase 5 completed (Doc section exists, `runs.gdoc_heading_id` set), but Phase 6 fails with a Gmail API error.

**Expected behaviour:**
- On re-run, the orchestrator detects `runs.gdoc_heading_id` is set and `runs.gmail_message_id` is not.
- The Docs append step is **skipped** (anchor found in doc = idempotency).
- Only the Gmail step is retried.
- Deep link is reconstructed from the persisted `runs.gdoc_heading_id` and `gdoc_id` — no need to re-read the Doc.

---

### EC6-3: Gmail Quota Exceeded (HTTP 429 / Quota Limit)

**Scenario:** Gmail MCP server returns a quota error (e.g. daily sending limit reached).

**Expected behaviour:**
- Exponential backoff: wait 60s, 120s, 240s before retrying `send_message`.
- If all retries fail, the draft is left unsent and `runs.status = 'gmail_quota'`.
- Alert fired: "Gmail send failed: quota exceeded for run {run_id}".
- Runbook entry: "Check Gmail sending limits; retry after 24 hours using `pulse publish --run <id> --target gmail`."

---

### EC6-4: Invalid Recipient Email Address

**Scenario:** `products.gmail_to` contains a malformed address like `"stakeholder@"` (no domain).

**Expected behaviour:**
- Validated at config load time by `pydantic` email validator before any MCP calls are made.
- Agent exits with `ValidationError` naming the product and the invalid address.
- Does NOT attempt to call `gmail.create_draft` with an invalid address.

---

### EC6-5: `gmail.search_messages` Returns Stale Results

**Scenario:** The idempotency search query returns a message, but it belongs to a different run (different `run_id` in header) due to a Gmail search index delay.

**Expected behaviour:**
- The search query is exact: `from:me subject:[Weekly Pulse] header:X-Pulse-Run-Id:{run_id}` — narrow enough to avoid false positives.
- If the search returns 0 results but `runs.gmail_message_id` is already set in the local DB, trust the local DB and skip the send.
- The DB is the source of truth; Gmail search is a secondary guard.

---

### EC6-6: Email Body Too Large

**Scenario:** The HTML email body exceeds Gmail's size limit (typically 25 MB, in practice much less for text emails).

**Expected behaviour:**
- Email renderer enforces a maximum of 50 KB for the email body.
- If the rendered body exceeds 50 KB (e.g. 20 verbatim quotes all included), the renderer trims quotes to the top 3.
- Warning logged: `"Email body trimmed from {n} quotes to 3 to stay under size limit"`.

---

### EC6-7: Recipient Inbox Full

**Scenario:** `gmail.send_message` succeeds (Gmail accepts the message) but the recipient's inbox bounces it.

**Expected behaviour:**
- This is outside the agent's control. The send is recorded as successful (`runs.gmail_message_id` set).
- Bounce handling is the responsibility of the Gmail account owner, not the agent.
- No retry on bounce — would cause duplicate sends.

---

### EC6-8: Draft Created but `draftId` Not Returned

**Scenario:** `gmail.create_draft` MCP response is missing the `draftId` field (MCP server bug or version mismatch).

**Expected behaviour:**
- The agent raises `MCPResponseError("gmail.create_draft response missing 'draftId'")`.
- `runs.status = 'gmail_draft_failed'`.
- The MCP server's tool schema is re-validated at session startup (Phase 5 §E5-7 approach) to catch version mismatches early.

---

### EC6-9: `CONFIRM_SEND` Accidentally Set in Production

**Scenario:** A developer sets `CONFIRM_SEND=true` in a production environment and triggers a backfill for 10 past weeks, causing 10 emails to be sent at once.

**Expected behaviour:**
- Each run's idempotency check prevents duplicate sends within the same week.
- Backfill sends are legitimate (one email per past week) — this is working as intended.
- The `--dry-run` flag overrides `CONFIRM_SEND=true` for safe testing: `pulse publish --run <id> --target gmail --dry-run` always creates a draft only.
