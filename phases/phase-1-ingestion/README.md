# Phase 1 — Review Ingestion

> **Snapshot:** `git checkout phase-1` · **Specs:** [evaluations](../../docs/phases/phase-1-ingestion/evaluations.md) · [edge-cases](../../docs/phases/phase-1-ingestion/edge-cases.md)

## What this phase added
Reliable pull + store of 8–12 weeks of reviews for any supported product:
- `agent/ingestion/appstore.py` — iTunes RSS `customerreviews` feed, paginated (1..10), country-configurable.
- `agent/ingestion/playstore.py` — `google-play-scraper` wrapper with time-bounded pagination.
- Unified `RawReview` model; stable `id = sha1(source + external_id)`; dedup-upsert into `reviews`.
- Regex PII scrubber (emails, phone numbers, Aadhaar-like) applied before persistence.
- Raw JSON snapshot to `data/raw/{product}/{run_id}.jsonl` for audit.

## CLI introduced
```bash
uv run pulse ingest --product groww --weeks 10
```

## Exit criteria
- Fixture-replay test: canned App Store + Play Store responses → deterministic reviews snapshot.
- Real `groww` run returns ≥ 200 reviews (gated behind a live-network flag).
- Re-running within a minute is a no-op (0 inserts, some updates).

## Where the code lives now
`agent/ingestion/` (`appstore.py`, `playstore.py`, `filters.py`).
