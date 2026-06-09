# Phase 2 — Embeddings & Clustering: Edge Cases

## What We Must Survive

---

### EC2-1: Fewer Than 20 Reviews After Filtering

**Scenario:** After language + length filtering, only 15 reviews remain (e.g. niche product with few English reviews).

**Expected behaviour:**
- HDBSCAN `min_cluster_size` is automatically clamped to `max(3, len(reviews) // 5)` to avoid producing 0 clusters.
- A warning is logged: `"Only {n} reviews after filtering; clustering may be unreliable"`.
- A single "catch-all" cluster is formed; the run continues to Phase 3.
- Does NOT raise an exception or mark the run as failed.

---

### EC2-2: All Reviews Assigned to Noise Cluster

**Scenario:** HDBSCAN assigns every review to cluster `-1` (all noise, no clusters found).

**Expected behaviour:**
- Detected by checking: `all(label == -1 for label in labels)`.
- Fallback: run k-means with `k=3` as a backstop.
- Log warning: `"HDBSCAN produced no clusters, falling back to k-means with k=3"`.
- Phase 3 receives at least 1 cluster (the k-means result).

---

### EC2-3: Single Dominant Cluster (90%+ of Reviews)

**Scenario:** 380 of 400 reviews end up in one cluster; 2 small clusters of 10 reviews each.

**Expected behaviour:**
- No error; all clusters are passed to Phase 3.
- The dominant cluster's theme will likely be ranked #1 in `PulseSummary`.
- Representative picks from the dominant cluster prioritise rating diversity.

---

### EC2-4: Embedding API Failure Mid-Batch

**Scenario:** OpenAI embedding API returns a 500 error after processing 200 of 400 reviews.

**Expected behaviour:**
- The 200 successfully embedded reviews are persisted to `review_embeddings` (partial progress saved).
- The run is retried from the first un-embedded batch (cache hits skip re-embedding already-done reviews).
- After max retries, CLI exits with a clear error: `"Embedding failed at batch 3/8: {error}"`.
- `runs.status` is set to `'embedding_failed'`, not `'success'`.

---

### EC2-5: Embedding Cache Corruption

**Scenario:** The on-disk embedding cache file is truncated or contains invalid bytes.

**Expected behaviour:**
- Cache read fails gracefully; the embedding is re-computed from the API.
- A warning is logged: `"Cache miss (corrupt entry) for review {id}, re-embedding"`.
- Does NOT propagate a `struct.error` or `pickle.UnpicklingError` to the user.

---

### EC2-6: Very Short Reviews Slipping Through Filter

**Scenario:** A review body of exactly 20 characters (boundary condition).

**Expected behaviour:**
- The length filter is `>= 20` (inclusive), so 20-char reviews are kept.
- A 19-char review is filtered out.
- Unit test explicitly covers both boundary values.

---

### EC2-7: UMAP Fails to Converge

**Scenario:** UMAP raises a `numba` JIT compilation error or convergence warning on an unusual review set.

**Expected behaviour:**
- UMAP is wrapped in a try/except; on failure, skip dimensionality reduction and run HDBSCAN directly on the raw embeddings (higher dimensional, slower but correct).
- Warning logged: `"UMAP failed ({error}), running HDBSCAN on raw embeddings"`.

---

### EC2-8: Duplicate Review Text (Near-Identical Reviews)

**Scenario:** 50 reviews have nearly identical text (copy-pasted reviews, bot reviews, or template complaints).

**Expected behaviour:**
- They are embedded and will naturally cluster together.
- The cluster is valid; the medoid will be one of these near-duplicate reviews.
- Phase 3 LLM will label this as a theme (e.g. "Templated/Bot Complaints") without error.
- No dedup at embedding stage — dedup already happened at ingestion (same `id`); these are genuinely different reviews with similar text.
