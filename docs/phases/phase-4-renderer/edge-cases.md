# Phase 4 — Report & Email Rendering: Edge Cases

## What We Must Survive

---

### EC4-1: PulseSummary with Only One Theme

**Scenario:** Phase 3 only produced 1 theme (too few clusters).

**Expected behaviour:**
- `docs_tree.py` renders a report with a single theme section — valid output.
- Email teaser shows 1 bullet instead of 3.
- No `IndexError` when iterating `top_themes`.
- Schema validator does NOT require exactly 3 themes; minimum is 1.

---

### EC4-2: Theme with No Associated Quotes

**Scenario:** The verbatim quote validator dropped all quotes for a theme (all LLM-proposed quotes were hallucinated).

**Expected behaviour:**
- The theme section in the Doc omits the "User Quotes" subsection entirely.
- No empty `insertText` requests with blank content are included in the batch.
- Email teaser shows the theme name without a quote — valid output.

---

### EC4-3: Special Characters in Review Text (XSS Risk in Email HTML)

**Scenario:** A review body contains `<script>alert('xss')</script>` or `"` or `&`.

**Expected behaviour:**
- Jinja2's autoescaping is enabled for HTML templates (`autoescape=True`).
- The email HTML contains `&lt;script&gt;` not `<script>`.
- Plain-text email is not affected (no HTML escaping needed).
- Doc batchUpdate requests use `insertText` which treats content as literal text, not HTML — no escaping needed there.

---

### EC4-4: Very Long Theme Description

**Scenario:** A theme description is 2,000 characters long.

**Expected behaviour:**
- No truncation in the Doc renderer (Google Docs can handle long paragraphs).
- Email HTML teaser truncates to 200 characters with `"..."` for readability.
- Truncation is applied only to the email template, not to `PulseSummary.themes[i].description`.

---

### EC4-5: Product Name Contains Special Characters

**Scenario:** A product display name is `"INDMoney — Invest & Save"` (em dash and ampersand).

**Expected behaviour:**
- Doc anchor string uses only the `product_key` (e.g. `indmoney`), which is ASCII-safe.
- Email subject line HTML-encodes the ampersand: `INDMoney &amp; Invest &amp; Save`.
- Google Docs `insertText` receives the raw Unicode string — em dash and ampersand are valid in Docs content.

---

### EC4-6: Artifact Directory Already Exists

**Scenario:** `data/artifacts/{run_id}/` already exists from a previous partial render.

**Expected behaviour:**
- Existing files are overwritten (re-render is idempotent).
- `mkdir(parents=True, exist_ok=True)` does not raise `FileExistsError`.

---

### EC4-7: Empty `action_ideas` List

**Scenario:** Phase 3 LLM produced themes but failed to generate action ideas.

**Expected behaviour:**
- The "Action Ideas" section is omitted from the Doc entirely (not rendered as an empty section).
- Email teaser omits the action ideas bullet list.
- No `KeyError` or `AttributeError` when accessing `pulse_summary.action_ideas`.

---

### EC4-8: `what_this_solves` Table Has a Single Row

**Scenario:** Only one `AudienceValue` entry (e.g. only "Product" audience is relevant).

**Expected behaviour:**
- `insertTable` creates a 2-column, 2-row table (1 header row + 1 data row).
- No crash from a single-row table (Google Docs API accepts this).
