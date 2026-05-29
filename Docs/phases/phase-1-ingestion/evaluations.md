# Phase 1 — Review Ingestion: Evaluations

## How We Prove It Works

---

### E1-1: Fixture Replay — Deterministic Snapshot

**What to run:**
```bash
pytest tests/test_ingestion.py::test_fixture_replay -v
```

**Setup:** `tests/fixtures/appstore_groww_page1.json` and `tests/fixtures/playstore_groww.json` contain canned HTTP responses.

**Pass condition:**
- The ingestion modules, when HTTP is mocked to return these fixtures, produce a deterministic set of `RawReview` objects.
- The resulting `reviews` rows in a fresh SQLite DB are byte-identical to `tests/fixtures/reviews_snapshot.jsonl` (the golden snapshot).
- `id` for each review is stable: `sha1(source + external_id)` produces the same hex on every run.

---

### E1-2: PII Scrubbing

**What to run:**
```bash
pytest tests/test_ingestion.py::test_pii_scrubbing -v
```

**Test inputs:**
- Body: `"My email is john@example.com and my Aadhaar is 1234 5678 9012"`
- Body: `"Call me on +91-9876543210 for a refund"`

**Pass condition:**
- Stored `body` field contains `[EMAIL]` instead of the email address.
- Stored `body` field contains `[PHONE]` instead of the phone number.
- Stored `body` field contains `[AADHAAR]` instead of the Aadhaar number.
- Original text never reaches the database or log output.

---

### E1-3: Dedup / Upsert Behaviour

**What to run:**
```bash
pytest tests/test_ingestion.py::test_dedup_upsert -v
```

**Pass condition:**
- Inserting the same review twice (same `id`) results in exactly 1 row in the `reviews` table.
- Updating a review (same `id`, different `body`) updates the existing row rather than inserting a duplicate.
- `ingested_at` is updated on upsert; `id` and `posted_at` are not changed.

---

### E1-4: CLI Smoke Test (Live Network, Gated)

**What to run:**
```bash
PULSE_LIVE_NETWORK=true uv run pulse ingest --product groww --weeks 10
```

**Pass condition:**
- Command exits 0.
- `reviews` table contains ≥ 200 rows for `product_key = 'groww'`.
- Both `source = 'appstore'` and `source = 'playstore'` rows are present.
- `data/raw/groww/{run_id}.jsonl` file exists and is valid JSONL.

---

### E1-5: Re-run Is a No-Op

**What to run:**
```bash
uv run pulse ingest --product groww --weeks 10  # first run
uv run pulse ingest --product groww --weeks 10  # second run, same minute
```

**Pass condition:**
- Second run logs `inserts=0` (or a very small number for reviews added in the interim).
- Row count in `reviews` table is the same before and after the second run.
- No duplicate rows with the same `id`.

---

### E1-6: Raw JSONL Audit File

**Pass condition:**
- `data/raw/{product}/{run_id}.jsonl` is created after every ingest run.
- Each line is valid JSON parseable as a `RawReview`.
- The file is not overwritten on a re-run of the same `run_id` — it is appended or left as-is (idempotent).

---

### E1-7: Multi-Product Ingestion

**What to run:**
```bash
for product in indmoney groww kuvera; do
  uv run pulse ingest --product $product --weeks 8
done
```

**Pass condition:**
- `reviews` table contains rows for all three `product_key` values.
- No cross-contamination: `WHERE product_key = 'kuvera'` returns only Kuvera reviews.
