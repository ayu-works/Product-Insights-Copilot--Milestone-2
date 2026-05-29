# Phase 6 — Gmail MCP — Deliver Email: Evaluations

## How We Prove It Works

---

### E6-1: First Run Sends Email (Mock MCP)

**What to run:**
```bash
pytest tests/test_gmail_mcp.py::test_first_run_sends_email -v
```

**Setup:** Mock MCP server; `gmail.search_messages` returns empty results; `CONFIRM_SEND=true`.

**Pass condition:**
- `gmail.create_draft` is called once with:
  - Correct `To`, `Subject`, and HTML/text body.
  - Custom header `X-Pulse-Run-Id: {run_id}`.
  - Label `Pulse/groww`.
- `gmail.send_message` is called once with the `draftId` from `create_draft`.
- `runs.gmail_message_id` is set to the `messageId` returned by the mock.
- CLI exits 0.

---

### E6-2: Second Run Is a No-Op (Idempotency)

**What to run:**
```bash
pytest tests/test_gmail_mcp.py::test_second_run_is_noop -v
```

**Setup:** Mock `gmail.search_messages` returns a result matching `X-Pulse-Run-Id:{run_id}`.

**Pass condition:**
- `gmail.create_draft` is **not** called.
- `gmail.send_message` is **not** called.
- Log entry: `"Email already sent for run {run_id}, skipping"`.
- `runs.gmail_message_id` is **not** overwritten.
- CLI exits 0.

---

### E6-3: Dry-Run Default (No `CONFIRM_SEND`)

**What to run:**
```bash
CONFIRM_SEND=false uv run pulse publish --run <id> --target gmail
```

**Pass condition:**
- `gmail.create_draft` is called — draft is created.
- `gmail.send_message` is **not** called.
- Log entry: `"Draft created (id: {draftId}). Set CONFIRM_SEND=true to send."`.
- `runs.gmail_message_id` is **not** set (no send occurred).
- Draft is visible in the Gmail UI under the configured account.

---

### E6-4: Deep Link Substitution

**Pass condition:**
- The email body sent to `gmail.create_draft` contains the real Google Docs deep link from Phase 5.
- The placeholder `{DOC_DEEP_LINK}` does **not** appear in the final draft.
- The "Read full report →" anchor in the HTML body points to `https://docs.google.com/document/d/{docId}/edit#heading={headingId}`.

---

### E6-5: Email Label Applied

**Pass condition:**
- After `gmail.send_message`, `gmail.modify_labels` is called to apply the `Pulse/groww` label.
- The label is visible in Gmail's label list for the sent message.
- If the label does not exist, `gmail.create_label` is called first (once), then the label is applied.

---

### E6-6: `gmail_message_id` Persistence

**Pass condition:**
- After a successful send, `runs.gmail_message_id` contains the Gmail `messageId` (a non-empty string like `"18e1a2b3c4d5e6f7"`).
- `runs.gmail_thread_id` (if tracked) contains the `threadId`.
- These values are only written after `gmail.send_message` succeeds — not after `create_draft`.

---

### E6-7: Real Workspace Smoke Test (Staging)

**What to run (manual):**
```bash
CONFIRM_SEND=true PULSE_GMAIL_MCP=real uv run pulse publish --run <id> --target gmail
```

**Pass condition (manual):**
- Email arrives in the configured test inbox within 2 minutes.
- Subject line: `[Weekly Pulse] Groww — 2026-W16 — {Top theme}`.
- Email body contains 3–5 bullet teaser themes.
- "Read full report →" link opens the Google Doc and scrolls to the correct section.
- Email has the `Pulse/groww` label in Gmail.

---

### E6-8: Combined `--target both`

**What to run:**
```bash
uv run pulse publish --run <id> --target both
```

**Pass condition:**
- Docs append completes first (Phase 5 logic).
- Deep link from Docs is injected into email before `create_draft`.
- Email send completes second.
- Both `runs.gdoc_heading_id` and `runs.gmail_message_id` are set in the same run record.
