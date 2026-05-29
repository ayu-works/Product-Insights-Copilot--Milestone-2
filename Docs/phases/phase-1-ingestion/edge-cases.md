# Phase 1 — Review Ingestion: Edge Cases

## What We Must Survive

---

### EC1-1: App Store Returns Zero Reviews for a Country

**Scenario:** iTunes RSS returns an empty feed for `country=IN` for a product that has no Indian App Store presence.

**Expected behaviour:**
- Ingestion logs a warning: `"App Store returned 0 reviews for {product} in {country}"`.
- Play Store ingestion continues normally.
- Run is not marked as failed; `reviews` table has Play Store rows only.
- No exception is raised.

---

### EC1-2: Play Store Rate Limiting (HTTP 429)

**Scenario:** `google-play-scraper` receives a 429 response mid-pagination.

**Expected behaviour:**
- Exponential backoff: retries after 2s, 4s, 8s (max 3 retries).
- If all retries fail, logs `"Play Store rate limited, partial ingestion for {product}"` and saves what was fetched so far.
- `runs` table records `status = 'partial'`; does not mark as success.

---

### EC1-3: Network Timeout Mid-Pagination

**Scenario:** App Store RSS fetch times out on page 5 of 10 (5 pages already fetched).

**Expected behaviour:**
- Reviews from pages 1–4 (already fetched and parsed) are upserted to the database.
- Error is logged with the page number that failed.
- CLI exits with a non-zero code and a clear message: `"Ingestion incomplete: timed out at page 5"`.
- Re-running the command safely processes all pages (the previously fetched reviews are deduped out).

---

### EC1-4: Review with Null or Empty Body

**Scenario:** An App Store review has `body = null` or `body = ""`.

**Expected behaviour:**
- Review is stored with `body = ""` (normalized to empty string, never `null`).
- PII scrubber is a no-op on an empty string without crashing.
- Review is included in the `reviews` table but will be filtered out in Phase 2 (length < 20 chars filter).

---

### EC1-5: UTF-8 / Non-ASCII Review Text

**Scenario:** Reviews contain Devanagari script (Hindi), emoji, or right-to-left characters.

**Expected behaviour:**
- SQLite stores the text as UTF-8 without truncation or encoding errors.
- PII scrubber regex operates on Unicode strings (`re.UNICODE` flag set).
- JSONL audit file is written in UTF-8 without BOM.

---

### EC1-6: Extremely Long Review Body

**Scenario:** A review body is 10,000+ characters (e.g. a user pasted a long complaint).

**Expected behaviour:**
- Review is stored as-is (no truncation at ingestion time).
- If a downstream LLM context limit is a concern, truncation happens at Phase 3, not Phase 1.

---

### EC1-7: Product Not Found on One Store

**Scenario:** `powermoney` is not available on the Apple App Store (no `appstore_id` configured).

**Expected behaviour:**
- `config.py` marks `appstore_id = null` for this product.
- App Store ingestion is skipped entirely with a log: `"No App Store ID configured for {product}, skipping"`.
- Play Store ingestion runs normally.

---

### EC1-8: Duplicate External IDs Across Sources

**Scenario:** App Store and Play Store happen to produce the same `external_id` string for different reviews.

**Expected behaviour:**
- `id = sha1(source + external_id)` ensures uniqueness because `source` is part of the hash.
- No collision occurs; both reviews are stored separately.

---

### EC1-9: Clock Skew / Future-Dated Reviews

**Scenario:** A review has `posted_at` set to a date in the future (data quality issue on the store side).

**Expected behaviour:**
- Review is ingested without error.
- It falls outside the 8–12 week window filter applied at ingestion time and is excluded.
- A warning is logged: `"Review {id} has future posted_at {date}, excluding from window"`.
