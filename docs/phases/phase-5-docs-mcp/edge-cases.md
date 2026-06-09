# Phase 5 — Google Docs MCP — Append Report: Edge Cases

## What We Must Survive

---

### EC5-1: Cached Doc ID No Longer Exists

**Scenario:** `products.gdoc_id` points to a Doc that was deleted from Google Drive.

**Expected behaviour:**
- `docs.get_document` returns a 404-equivalent error.
- Agent detects the 404 and clears the cached `gdoc_id` in `products` table.
- Falls back to `docs.search_documents` to find the Doc by title.
- If not found by title, calls `docs.create_document` to create a fresh one.
- Entire recovery path is logged with the old and new `docId`.

---

### EC5-2: MCP Server Unreachable at Startup

**Scenario:** The Google Docs MCP server process is not running (stdio transport: subprocess fails to start).

**Expected behaviour:**
- `session.py` raises `MCPConnectionError("Could not start Docs MCP server: {stderr}")`.
- CLI exits with code 1 and a clear message: `"Docs MCP server unavailable. Check docs_mcp_command in config."`.
- No partial state is written to the database.

---

### EC5-3: `docs.batch_update` Fails Mid-Write

**Scenario:** The MCP server returns an error response after the `batch_update` call (e.g. quota exceeded, or the Doc is owned by a different user).

**Expected behaviour:**
- The Google Docs API rolls back partial updates (the API processes the entire batch atomically).
- `runs.gdoc_heading_id` is **not** set.
- Error is logged with the full MCP error payload.
- `runs.status = 'docs_failed'` so the orchestrator (Phase 7) can retry the Docs step specifically.

---

### EC5-4: Doc is Read-Only (Shared Without Edit Permission)

**Scenario:** The service account / OAuth token has only viewer access to the target Doc.

**Expected behaviour:**
- `docs.batch_update` returns a permission error.
- Agent raises `MCPPermissionError("Docs MCP: insufficient permission to write to {docId}")`.
- Runbook entry: "Check that the MCP server's Google account has Editor access to the Doc."

---

### EC5-5: Network Timeout Between `get_document` and `batch_update`

**Scenario:** The agent checks for the anchor (not found), then loses connectivity before `batch_update` completes.

**Expected behaviour:**
- `batch_update` raises a timeout error.
- `runs.gdoc_heading_id` is not set (no false positive).
- On re-run, `get_document` is called again; if the partial batch actually completed server-side, the anchor will be found and the run is a no-op.
- If the anchor is not found (batch did not complete), the full append is retried.

---

### EC5-6: `docs.get_document` Returns a Very Large Document

**Scenario:** The running pulse Doc has 52 weeks of history, making `get_document` return a very large body (> 1 MB JSON).

**Expected behaviour:**
- Anchor check uses a simple substring search on the returned body text — O(n) but correct.
- No timeout on the anchor search (it's a local string operation after the HTTP fetch).
- MCP server may paginate large docs; the client reads all pages before searching.

---

### EC5-7: Anchor String Appears in Review Content (False Positive)

**Scenario:** A user review happens to contain the text `pulse-groww-2026-W16` (extremely unlikely but theoretically possible).

**Expected behaviour:**
- The anchor is embedded inside a Heading 1 text element, not as body paragraph text.
- The idempotency check searches the Doc body broadly; a false positive would cause the run to skip the append.
- Mitigation: the anchor format includes a UUID suffix in a future version if collisions are ever observed. For now, log a warning if the anchor is found but `runs.gdoc_heading_id` is not yet set.

---

### EC5-8: SSE Transport Drops Connection Mid-Stream

**Scenario:** In production (SSE transport), the connection drops while receiving the `batch_update` response.

**Expected behaviour:**
- The MCP client library detects the stream interruption.
- The call is retried from the beginning (not from mid-response, as the response is atomic).
- After 3 retries, `MCPConnectionError` is raised and `runs.status = 'docs_failed'`.
