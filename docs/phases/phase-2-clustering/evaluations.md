# Phase 2 — Embeddings & Clustering: Evaluations

## How We Prove It Works

---

### E2-1: Cluster Count Within Bounds

**What to run:**
```bash
pytest tests/test_clustering.py::test_cluster_count_on_golden_fixture -v
```

**Setup:** Uses `tests/fixtures/reviews_snapshot.jsonl` (~400 reviews from Phase 1 golden fixture).

**Pass condition:**
- HDBSCAN produces between **4 and 12** named clusters.
- Noise ratio (reviews assigned to cluster `-1`) is **< 35%**.
- At least one cluster has `sentiment = 'negative'` (typical for app reviews).

---

### E2-2: Determinism With Fixed Seeds

**What to run:**
```bash
pytest tests/test_clustering.py::test_determinism -v
```

**Pass condition:**
- Running `pulse cluster --run <id>` twice on the same input with `RANDOM_SEED=42` produces byte-identical cluster assignment rows in the `clusters` table.
- UMAP and HDBSCAN both accept the seed; results are reproducible across Python restarts.

---

### E2-3: Embedding Cache Hit Rate

**What to run:**
```bash
uv run pulse cluster --run <id>   # first run (cold cache)
uv run pulse cluster --run <id>   # second run (warm cache)
```

**Pass condition:**
- On the second run, the log shows `embedding_cache_hits = N`, `embedding_cache_misses = 0` where `N` equals the number of reviews.
- No calls to the embedding API are made on the second run (verified by checking API call count mock or network log).
- Total wall time of second run is significantly less than first run.

---

### E2-4: Medoid Selection

**Pass condition:**
- Every cluster has exactly one `medoid_review_id` pointing to a review that actually belongs to that cluster.
- The medoid is the review whose embedding is closest (cosine distance) to the cluster centroid.
- Each cluster also has 2 additional representative reviews selected for rating variance (one high-rating, one low-rating review if available).

---

### E2-5: Language and Length Filtering

**What to run:**
```bash
pytest tests/test_clustering.py::test_language_and_length_filter -v
```

**Test input:** A set of 100 reviews: 80 English (body ≥ 20 chars), 10 Hindi, 5 English with body < 20 chars, 5 empty bodies.

**Pass condition:**
- Only the 80 English reviews with body ≥ 20 chars are passed to the embedding model.
- Filtered reviews are logged with reason: `"filtered: language={lang}"` or `"filtered: body_too_short"`.
- Filtered reviews are NOT added to `review_embeddings`.

---

### E2-6: KeyBERT Keyphrases

**Pass condition:**
- Each cluster row in the `clusters` table has `keyphrases_json` containing 1–8 keyphrases.
- Keyphrases are relevant to the cluster's review content (manual spot-check on golden fixture).
- Empty or single-review clusters fall back to the review title / first 10 words if KeyBERT returns nothing.

---

### E2-7: Embedding Provider Swap

**Pass condition:**
- Setting `EMBEDDING_PROVIDER=local` uses `bge-small-en-v1.5` via sentence-transformers (no API call).
- Setting `EMBEDDING_PROVIDER=openai` uses `text-embedding-3-small`.
- Both produce the same number of clusters on the golden fixture (within ±2 clusters).
- Cache keys are provider-agnostic: `sha1(text)` (so switching providers correctly misses the cache).
