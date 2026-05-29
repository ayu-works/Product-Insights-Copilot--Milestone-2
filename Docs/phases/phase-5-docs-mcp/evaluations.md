# Phase 5 — Google Docs MCP — Append Report: Evaluations

## How We Prove It Works

---

### E5-1: First Run Creates a New Doc Section (Mock MCP)

**What to run:**
```bash
pytest tests/test_docs_mcp.py::test_first_run_appends_section -v
```

**Setup:** Mock MCP server speaks real JSON-RPC; `docs.get_document` returns a body with no existing anchor; `docs.batch_update` records the request.

**Pass condition:**
- `append_pulse_section` calls `docs.get_document` exactly once to check for the anchor.
- `docs.batch_update` is called exactly once with the Phase-4 request tree.
- The batch includes, in order: page break → Heading 1 (with anchor) → body content → horizontal rule.
- `runs.gdoc_heading_id` is set to the `headingId` returned by the mock.

---

### E5-2: Second Run Is a No-Op (Idempotency)

**What to run:**
```bash
pytest tests/test_docs_mcp.py::test_second_run_is_noop -v
```

**Setup:** Mock MCP server's `docs.get_document` returns a body that already contains the anchor string `pulse-groww-2026-W16`.

**Pass condition:**
- `docs.batch_update` is **not** called.
- `append_pulse_section` returns early with a log: `"Section already present, skipping append"`.
- `runs.gdoc_heading_id` is **not** overwritten if already set.
- CLI exits 0 (not an error).

---

### E5-3: First-Run Doc Creation

**What to run:**
```bash
pytest tests/test_docs_mcp.py::test_creates_doc_on_first_run -v
```

**Setup:** Mock `docs.search_documents` returns empty results; `docs.create_document` returns a new `docId`.

**Pass condition:**
- `docs.create_document` is called with title `"Weekly Review Pulse — Groww"`.
- The new `docId` is cached in the `products` table (`gdoc_id` column).
- Subsequent calls use the cached `docId` and skip `docs.search_documents`.

---

### E5-4: Real Google Doc Rendering (Staging Workspace)

**What to run (manual):**
```bash
PULSE_DOCS_MCP=real uv run pulse publish --run <id> --target docs
```

**Pass condition (manual spot-check):**
- The target Google Doc has a new section with:
  - A Heading 1 styled title containing the week label.
  - Theme names as Heading 2.
  - Theme details as bullet lists.
  - Verbatim quotes as indented italic paragraphs.
  - A "What This Solves" table with 2 columns.
  - A horizontal rule separating it from the previous section.
- The anchor string is visible in the Heading 1 text.

---

### E5-5: Deep Link Construction

**Pass condition:**
- After a successful append, `runs.gdoc_heading_id` is set to a non-empty string (the `headingId` from the Docs API).
- The computed deep link follows the format: `https://docs.google.com/document/d/{docId}/edit#heading={headingId}`.
- The link is stored in `runs` table and returned to the orchestrator for use in the email (Phase 6).

---

### E5-6: MCP Session Lifecycle

**Pass condition:**
- `session.py` connects to the Docs MCP server at the start of the `publish` command.
- The session is closed cleanly (no dangling processes) when the command completes or fails.
- Reconnect logic works: if the session drops mid-run, it reconnects and retries the failed tool call.

---

### E5-7: Tool Schema Validation at Handshake

**Pass condition:**
- On session connect, the agent calls `tools/list` and validates that the expected tools (`docs.get_document`, `docs.batch_update`, `docs.create_document`, `docs.search_documents`) are present.
- If any required tool is missing, the agent raises `MCPToolMissing("{tool_name}")` and exits before attempting any work.
