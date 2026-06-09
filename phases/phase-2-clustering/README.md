# Phase 2 — Embeddings & Clustering

> **Snapshot:** `git checkout phase-2` · **Specs:** [evaluations](../../docs/phases/phase-2-clustering/evaluations.md) · [edge-cases](../../docs/phases/phase-2-clustering/edge-cases.md)

## What this phase added
Turn a pile of reviews into a small set of coherent clusters with representative members:
- Language filter (keep `en`), length filter (≥ 20 chars).
- Embedding provider interface: OpenAI `text-embedding-3-small` **or** local `bge-small-en-v1.5` (sentence-transformers); on-disk cache keyed by `sha1(text)`.
- UMAP (`n_components=15`, `metric=cosine`) → HDBSCAN (`min_cluster_size=8`).
- Medoid selection per cluster + 2 extra picks with rating variance; KeyBERT top-8 keyphrases.
- Persists `review_embeddings` + a `clusters` table.

## CLI introduced
```bash
uv run pulse cluster --run <run_id>
```

## Exit criteria
- On the ~400-review golden fixture, HDBSCAN returns 4–12 clusters; noise ratio < 35%.
- Fixed seeds → byte-identical cluster assignments across runs.
- Embedding cache hit rate on a re-run is 100%.

## Where the code lives now
`agent/clustering/` (`embeddings.py`, `pipeline.py`).
