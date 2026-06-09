# Phase 4 — Report & Email Rendering: Evaluations

## How We Prove It Works

---

### E4-1: Doc Request Tree — Golden Image Test

**What to run:**
```bash
pytest tests/test_renderer.py::test_doc_requests_golden_image -v
```

**Setup:** Uses the canonical `PulseSummary` from `tests/fixtures/pulse_summary_groww.json`.

**Pass condition:**
- `docs_tree.py` produces a `list[dict]` of Google Docs `batchUpdate` requests.
- The output is JSON-serialised and compared byte-for-byte to `tests/fixtures/doc_requests_groww.json`.
- Any change to the renderer that alters output must explicitly update the golden file (making diffs visible in code review).

---

### E4-2: Mapping Coverage

**Pass condition:**
- Every `PulseSummary` element type has a corresponding Docs request type:

| Element               | Docs Request Type                                         |
|-----------------------|-----------------------------------------------------------|
| Section title         | `insertText` + `updateParagraphStyle: HEADING_1`          |
| Theme title           | `insertText` + `updateParagraphStyle: HEADING_2`          |
| Bullet point          | `insertText` + `createParagraphBullets: BULLET_DISC_CIRCLE_SQUARE` |
| Verbatim quote        | `insertText` + `updateParagraphStyle: indentFirstLine` + italic |
| "What This Solves" table | `insertTable` with 2 columns (Audience, Value)         |

- Unit test verifies each mapping type is present in the output for a fixture with all element types.

---

### E4-3: Anchor String Embedding

**Pass condition:**
- The very first `insertText` request in the batch contains the anchor string `pulse-{product}-{iso_week}` (e.g. `pulse-groww-2026-W16`).
- This string is inside the `HEADING_1` paragraph, not as a hidden comment.
- Running the idempotency check from Phase 5 (`anchor in doc_body`) on the rendered doc would return `True`.

---

### E4-4: Email HTML — Golden Image Test

**What to run:**
```bash
pytest tests/test_renderer.py::test_email_html_golden_image -v
```

**Pass condition:**
- `email_html.py` produces HTML byte-identical to `tests/fixtures/email_groww.html` for the canonical fixture.
- The HTML is valid (no unclosed tags) — validated using `html.parser`.
- The subject line matches `[Weekly Pulse] Groww — 2026-W16 — {Top theme}`.

---

### E4-5: Deep Link Placeholder

**Pass condition:**
- `email.html` contains the literal string `{DOC_DEEP_LINK}` (unfilled placeholder).
- `email.txt` also contains `{DOC_DEEP_LINK}`.
- No `https://docs.google.com/...` URL appears in the rendered output at this phase (URL is only filled in Phase 5).

---

### E4-6: Schema Validation Rejects Malformed Input

**What to run:**
```bash
pytest tests/test_renderer.py::test_schema_validation -v
```

**Test cases:**
1. `PulseSummary` with `top_themes = []` (empty list) → `ValidationError`.
2. `PulseSummary` with a `Theme` whose `sentiment = "angry"` (invalid enum) → `ValidationError`.
3. `PulseSummary` with missing `window` field → `ValidationError`.

**Pass condition:**
- All three raise `pydantic.ValidationError` with a message naming the failing field.
- No partial output is written to disk when validation fails.

---

### E4-7: CLI Artifact Output

**What to run:**
```bash
uv run pulse render --run <id>
```

**Pass condition:**
- `data/artifacts/{run_id}/doc_requests.json` exists and is valid JSON.
- `data/artifacts/{run_id}/email.html` exists and contains the product name.
- `data/artifacts/{run_id}/email.txt` exists as a plain-text fallback.
- All three files are created atomically (no partial files left on failure).
