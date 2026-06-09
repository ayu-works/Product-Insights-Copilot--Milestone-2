"""Clustering pipeline: filter → UMAP → HDBSCAN → medoid → keyphrases → persist."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import dataclass

import numpy as np
import structlog
from sklearn.metrics.pairwise import cosine_distances

from agent.clustering.embeddings import EmbeddingCache, EmbeddingProvider, embed_reviews
from agent.models import RawReview

log = structlog.get_logger()

_MIN_BODY_LEN = 20          # EC2-6: inclusive lower bound
_DEFAULT_MIN_CLUSTER = 8


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class ClusterResult:
    cluster_label: int
    review_ids: list[str]
    medoid_review_id: str
    representative_review_ids: list[str]
    keyphrases: list[str]


# ---------------------------------------------------------------------------
# Step 1: Language + length filter
# ---------------------------------------------------------------------------

def filter_reviews(reviews: list[RawReview]) -> tuple[list[RawReview], int]:
    """Keep only English reviews with body >= 20 chars. Returns (kept, filtered_count)."""
    kept: list[RawReview] = []
    filtered = 0
    for r in reviews:
        if len(r.body) < _MIN_BODY_LEN:
            log.debug("filtered_body_too_short", review_id=r.id, length=len(r.body))
            filtered += 1
            continue
        if r.language != "en":
            log.debug("filtered_language", review_id=r.id, lang=r.language)
            filtered += 1
            continue
        kept.append(r)
    return kept, filtered


# ---------------------------------------------------------------------------
# Step 2: UMAP dimensionality reduction
# ---------------------------------------------------------------------------

def reduce_umap(
    embeddings: np.ndarray,
    n_components: int = 15,
    seed: int = 42,
) -> np.ndarray:
    """Reduce embeddings to n_components dims with UMAP.

    Falls back to raw embeddings if UMAP fails (EC2-7).
    """
    try:
        import umap  # type: ignore[import-untyped]

        reducer = umap.UMAP(
            n_components=min(n_components, embeddings.shape[1] - 1, embeddings.shape[0] - 2),
            metric="cosine",
            random_state=seed,
            low_memory=True,
        )
        return reducer.fit_transform(embeddings).astype(np.float32)
    except Exception as exc:
        log.warning("umap_failed_fallback", error=str(exc))
        return embeddings


# ---------------------------------------------------------------------------
# Step 3: HDBSCAN clustering
# ---------------------------------------------------------------------------

def run_hdbscan(
    reduced: np.ndarray,
    min_cluster_size: int = _DEFAULT_MIN_CLUSTER,
    seed: int = 42,
) -> np.ndarray:
    """Cluster with HDBSCAN. Falls back to KMeans(k=3) if all noise (EC2-2)."""
    n = len(reduced)
    # EC2-1: clamp min_cluster_size for small review sets
    clamped = max(3, min(min_cluster_size, n // 5))
    if clamped != min_cluster_size:
        log.warning(
            "min_cluster_size_clamped",
            original=min_cluster_size,
            clamped=clamped,
            n_reviews=n,
        )

    from sklearn.cluster import HDBSCAN

    clusterer = HDBSCAN(min_cluster_size=clamped, store_centers="centroid")
    labels: np.ndarray = clusterer.fit_predict(reduced)

    if np.all(labels == -1):
        log.warning("hdbscan_all_noise_fallback_kmeans")
        from sklearn.cluster import KMeans

        km = KMeans(n_clusters=3, random_state=seed, n_init="auto")
        labels = km.fit_predict(reduced)

    unique = set(labels) - {-1}
    noise = int(np.sum(labels == -1))
    log.info("hdbscan_result", clusters=len(unique), noise=noise, total=n)
    return labels


# ---------------------------------------------------------------------------
# Step 4: Medoid + representative selection
# ---------------------------------------------------------------------------

def select_representatives(
    indices: list[int],
    embeddings: np.ndarray,
    review_ids: list[str],
    ratings: list[int],
) -> tuple[str, list[str]]:
    """Return (medoid_id, [medoid_id, high_rating_id, low_rating_id])."""
    cluster_embs = embeddings[indices]
    centroid = cluster_embs.mean(axis=0, keepdims=True)
    dists = cosine_distances(centroid, cluster_embs)[0]
    medoid_local = int(np.argmin(dists))
    medoid_id = review_ids[indices[medoid_local]]

    # Sort cluster by rating for variance picks
    rated = sorted(
        [(review_ids[i], ratings[i]) for i in indices],
        key=lambda x: x[1],
    )
    reps: list[str] = [medoid_id]

    # Add highest-rated (if different from medoid)
    if rated[-1][0] != medoid_id:
        reps.append(rated[-1][0])
    # Add lowest-rated (if different from above)
    if rated[0][0] != medoid_id and rated[0][0] not in reps:
        reps.append(rated[0][0])

    return medoid_id, reps


# ---------------------------------------------------------------------------
# Step 5: KeyBERT keyphrases
# ---------------------------------------------------------------------------

def extract_keyphrases(texts: list[str], top_n: int = 8) -> list[str]:
    """Extract top keyphrases from combined cluster text using KeyBERT."""
    combined = " ".join(texts)[:4000]  # cap to avoid slow processing
    if not combined.strip():
        return []
    try:
        from keybert import KeyBERT  # type: ignore[import-untyped]

        kw_model = KeyBERT()
        kws = kw_model.extract_keywords(
            combined,
            keyphrase_ngram_range=(1, 2),
            stop_words="english",
            top_n=top_n,
        )
        return [str(item[0]) for item in kws if item]
    except Exception as exc:
        log.warning("keybert_failed", error=str(exc))
        # Fallback: first 10 words of combined text
        words = combined.split()
        return words[:min(10, len(words))]


# ---------------------------------------------------------------------------
# Step 6: Persist to DB
# ---------------------------------------------------------------------------

def _cluster_id(run_id: str, label: int) -> str:
    return hashlib.sha1(f"{run_id}{label}".encode()).hexdigest()


def persist_clusters(
    conn: sqlite3.Connection,
    run_id: str,
    clusters: list[ClusterResult],
) -> None:
    # Clear any existing clusters for this run (idempotent re-run)
    conn.execute("DELETE FROM clusters WHERE run_id = ?", (run_id,))
    for c in clusters:
        conn.execute(
            """
            INSERT INTO clusters
                (id, run_id, cluster_label, review_ids_json,
                 keyphrases_json, medoid_review_id, representative_review_ids_json)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                _cluster_id(run_id, c.cluster_label),
                run_id,
                c.cluster_label,
                json.dumps(c.review_ids),
                json.dumps(c.keyphrases),
                c.medoid_review_id,
                json.dumps(c.representative_review_ids),
            ),
        )


def persist_embeddings(
    conn: sqlite3.Connection,
    review_ids: list[str],
    embeddings: np.ndarray,
) -> None:
    for rid, vec in zip(review_ids, embeddings):
        blob = vec.astype(np.float32).tobytes()
        conn.execute(
            """
            INSERT INTO review_embeddings (review_id, embedding)
            VALUES (?, ?)
            ON CONFLICT(review_id) DO UPDATE SET embedding = excluded.embedding
            """,
            (rid, blob),
        )


# ---------------------------------------------------------------------------
# Top-level orchestration
# ---------------------------------------------------------------------------

def run_clustering_pipeline(
    conn: sqlite3.Connection,
    run_id: str,
    reviews: list[RawReview],
    provider: EmbeddingProvider,
    cache: EmbeddingCache,
    seed: int = 42,
    min_cluster_size: int = _DEFAULT_MIN_CLUSTER,
) -> list[ClusterResult]:
    """Full pipeline: filter → embed → UMAP → HDBSCAN → medoid → keyphrases → persist."""

    # 1. Filter
    filtered_reviews, n_filtered = filter_reviews(reviews)
    if n_filtered:
        log.info("clustering_filter", removed=n_filtered, kept=len(filtered_reviews))

    if len(filtered_reviews) < 5:
        log.error("clustering_too_few_reviews", count=len(filtered_reviews))
        raise ValueError(f"Only {len(filtered_reviews)} reviews after filtering — cannot cluster")

    if len(filtered_reviews) < 20:
        log.warning(
            "clustering_unreliable_few_reviews",
            count=len(filtered_reviews),
        )

    texts = [r.body for r in filtered_reviews]
    review_ids = [r.id for r in filtered_reviews]
    ratings = [r.rating for r in filtered_reviews]

    # 2. Embed
    embeddings, hits, misses = embed_reviews(texts, provider, cache)

    # 3. UMAP
    reduced = reduce_umap(embeddings, seed=seed)

    # 4. HDBSCAN
    labels = run_hdbscan(reduced, min_cluster_size=min_cluster_size, seed=seed)

    # 5. Build cluster results
    label_set = sorted(set(labels) - {-1})
    clusters: list[ClusterResult] = []

    for label in label_set:
        indices = [i for i, lbl in enumerate(labels) if lbl == label]
        medoid_id, reps = select_representatives(indices, embeddings, review_ids, ratings)
        cluster_texts = [texts[i] for i in indices]
        keyphrases = extract_keyphrases(cluster_texts)
        clusters.append(
            ClusterResult(
                cluster_label=int(label),
                review_ids=[review_ids[i] for i in indices],
                medoid_review_id=medoid_id,
                representative_review_ids=reps,
                keyphrases=keyphrases,
            )
        )

    # Handle noise reviews as a single cluster if any exist
    noise_indices = [i for i, lbl in enumerate(labels) if lbl == -1]
    if noise_indices:
        log.info("clustering_noise_reviews", count=len(noise_indices))

    # 6. Persist
    with conn:
        persist_embeddings(conn, review_ids, embeddings)
        persist_clusters(conn, run_id, clusters)
        conn.execute(
            "UPDATE runs SET status = 'clustered' WHERE id = ?", (run_id,)
        )

    log.info(
        "clustering_complete",
        run_id=run_id,
        clusters=len(clusters),
        noise=len(noise_indices),
        total_reviews=len(filtered_reviews),
    )
    return clusters
