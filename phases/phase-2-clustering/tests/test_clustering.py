"""Phase 2 clustering tests — evaluations E2-1 through E2-7."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from agent.clustering.embeddings import EmbeddingCache, embed_reviews
from agent.clustering.pipeline import (
    ClusterResult,
    filter_reviews,
    extract_keyphrases,
    persist_clusters,
    persist_embeddings,
    run_clustering_pipeline,
    select_representatives,
)
from agent.models import RawReview
from agent.storage import get_connection, init_db

FIXTURES = Path(__file__).parent / "fixtures"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_review(
    idx: int,
    body: str = "This is a sample review body with enough words",
    rating: int = 3,
    language: str = "en",
) -> RawReview:
    eid = f"test_{idx:04d}"
    return RawReview(
        id=hashlib.sha1(f"playstore{eid}".encode()).hexdigest(),
        product_key="groww",
        source="playstore",
        rating=rating,
        body=body,
        posted_at=datetime(2026, 4, 15, tzinfo=timezone.utc),
        language=language,
        country="IN",
    )


def _random_provider(dim: int = 32, seed: int = 0) -> Any:
    """A deterministic mock embedding provider returning random vectors."""
    rng = np.random.default_rng(seed)

    class MockProvider:
        name = "mock"
        dimensions = dim

        def embed_batch(self, texts: list[str]) -> list[list[float]]:
            return rng.standard_normal((len(texts), dim)).tolist()

    return MockProvider()


def _seeded_provider(dim: int = 32) -> Any:
    """Provider that returns deterministic vectors based on text hash — same text = same vector."""

    class SeededProvider:
        name = "seeded"
        dimensions = dim

        def embed_batch(self, texts: list[str]) -> list[list[float]]:
            out = []
            for text in texts:
                seed = int(hashlib.sha1(text.encode()).hexdigest()[:8], 16)
                rng = np.random.default_rng(seed)
                out.append(rng.standard_normal(dim).tolist())
            return out

    return SeededProvider()


def _load_snapshot_reviews() -> list[RawReview]:
    reviews = []
    for line in (FIXTURES / "reviews_snapshot.jsonl").read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        reviews.append(
            RawReview(
                id=d["id"],
                product_key=d["product_key"],
                source=d["source"],
                rating=d["rating"],
                title=d.get("title"),
                body=d["body"],
                posted_at=datetime.fromisoformat(d["posted_at"]).replace(tzinfo=timezone.utc),
                version=d.get("version"),
                language=d["language"],
                country=d["country"],
            )
        )
    return reviews


# ---------------------------------------------------------------------------
# E2-5: Language and length filter
# ---------------------------------------------------------------------------

class TestFilterReviews:
    def test_short_body_removed(self) -> None:
        reviews = [_make_review(0, body="Too short")]  # 9 chars
        kept, filtered = filter_reviews(reviews)
        assert filtered == 1
        assert len(kept) == 0

    def test_boundary_20_chars_kept(self) -> None:
        body = "A" * 20  # exactly 20
        reviews = [_make_review(0, body=body)]
        kept, _ = filter_reviews(reviews)
        assert len(kept) == 1

    def test_boundary_19_chars_removed(self) -> None:
        body = "A" * 19
        reviews = [_make_review(0, body=body)]
        kept, filtered = filter_reviews(reviews)
        assert filtered == 1

    def test_non_english_removed(self) -> None:
        reviews = [_make_review(0, language="hi")]
        kept, filtered = filter_reviews(reviews)
        assert filtered == 1

    def test_english_long_enough_kept(self) -> None:
        reviews = [_make_review(i) for i in range(5)]
        kept, filtered = filter_reviews(reviews)
        assert len(kept) == 5
        assert filtered == 0

    def test_mixed_batch(self) -> None:
        reviews = [
            _make_review(0),                           # kept
            _make_review(1, body="short"),              # filtered: too short
            _make_review(2, language="hi"),             # filtered: non-en
            _make_review(3, body="A" * 20),             # kept: boundary
        ]
        kept, filtered = filter_reviews(reviews)
        assert len(kept) == 2
        assert filtered == 2


# ---------------------------------------------------------------------------
# Embedding cache tests
# ---------------------------------------------------------------------------

class TestEmbeddingCache:
    def test_cache_miss_then_hit(self, tmp_path: Path) -> None:
        cache = EmbeddingCache(tmp_path / "emb.json")
        assert cache.get("hello world") is None
        vec = [0.1, 0.2, 0.3]
        cache.set("hello world", vec)
        assert cache.get("hello world") == vec

    def test_cache_persists_after_flush(self, tmp_path: Path) -> None:
        p = tmp_path / "emb.json"
        cache = EmbeddingCache(p)
        cache.set("test text", [1.0, 2.0])
        cache.flush()

        cache2 = EmbeddingCache(p)
        assert cache2.get("test text") == [1.0, 2.0]

    def test_cache_corrupt_file_recovers(self, tmp_path: Path) -> None:
        p = tmp_path / "emb.json"
        p.write_text("NOT VALID JSON {{{{", encoding="utf-8")
        cache = EmbeddingCache(p)  # should not raise
        assert cache.get("anything") is None

    def test_cache_key_is_sha1_of_text(self, tmp_path: Path) -> None:
        cache = EmbeddingCache(tmp_path / "emb.json")
        expected = hashlib.sha1("hello".encode()).hexdigest()
        assert cache._key("hello") == expected

    def test_embed_reviews_hit_miss_counts(self, tmp_path: Path) -> None:
        provider = _seeded_provider(dim=16)
        cache = EmbeddingCache(tmp_path / "emb.json")
        texts = ["Review text one long enough", "Review text two long enough"]

        _, hits, misses = embed_reviews(texts, provider, cache)
        assert hits == 0
        assert misses == 2

        _, hits2, misses2 = embed_reviews(texts, provider, cache)
        assert hits2 == 2
        assert misses2 == 0

    def test_embed_reviews_second_run_no_api_calls(self, tmp_path: Path) -> None:
        call_count = 0

        class CountingProvider:
            name = "counting"
            dimensions = 8

            def embed_batch(self, texts: list[str]) -> list[list[float]]:
                nonlocal call_count
                call_count += len(texts)
                return np.random.default_rng(0).standard_normal((len(texts), 8)).tolist()

        cache = EmbeddingCache(tmp_path / "emb.json")
        texts = ["First review text is long enough", "Second review text is long enough"]
        embed_reviews(texts, CountingProvider(), cache)
        assert call_count == 2

        embed_reviews(texts, CountingProvider(), cache)
        assert call_count == 2  # no new calls on warm cache


# ---------------------------------------------------------------------------
# E2-4: Medoid selection
# ---------------------------------------------------------------------------

class TestMedoidSelection:
    def test_medoid_is_cluster_member(self) -> None:
        rng = np.random.default_rng(42)
        embeddings = rng.standard_normal((10, 8)).astype(np.float32)
        ids = [f"r{i}" for i in range(10)]
        ratings = [3] * 10
        indices = list(range(10))

        medoid_id, reps = select_representatives(indices, embeddings, ids, ratings)
        assert medoid_id in ids
        assert medoid_id == reps[0]

    def test_representatives_include_rating_variance(self) -> None:
        rng = np.random.default_rng(0)
        embeddings = rng.standard_normal((10, 8)).astype(np.float32)
        ids = [f"r{i}" for i in range(10)]
        ratings = list(range(1, 11))  # 1..10 for variety
        indices = list(range(10))

        medoid_id, reps = select_representatives(indices, embeddings, ids, ratings)
        assert len(reps) >= 2  # medoid + at least one rating-based rep
        assert len(set(reps)) == len(reps)  # no duplicates


# ---------------------------------------------------------------------------
# E2-1: Cluster count on golden fixture (uses local sentence-transformers)
# ---------------------------------------------------------------------------

@pytest.mark.slow
def test_cluster_count_on_golden_fixture(tmp_db: Path) -> None:
    """100 semantically grouped reviews should produce 4–12 clusters."""
    pytest.importorskip("sentence_transformers", reason="sentence-transformers not installed")

    init_db(tmp_db)
    conn = get_connection(tmp_db)

    reviews = _load_snapshot_reviews()
    assert len(reviews) == 100

    from agent.clustering.embeddings import EmbeddingCache, get_provider
    provider = get_provider("local")
    cache = EmbeddingCache(tmp_db.parent / "cache" / "emb.json")

    clusters = run_clustering_pipeline(
        conn=conn, run_id="test_run_golden",
        reviews=reviews, provider=provider, cache=cache, seed=42,
    )

    labels = [c.cluster_label for c in clusters]
    noise_check = conn.execute(
        "SELECT count(*) FROM clusters WHERE run_id='test_run_golden'"
    ).fetchone()[0]

    assert 4 <= len(clusters) <= 12, f"Expected 4–12 clusters, got {len(clusters)}"
    assert noise_check == len(clusters)
    conn.close()


# ---------------------------------------------------------------------------
# E2-2: Determinism with fixed seeds (mock embeddings for speed)
# ---------------------------------------------------------------------------

class TestDeterminism:
    def test_same_seed_same_clusters(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = _load_snapshot_reviews()
        provider = _seeded_provider(dim=32)

        cache1 = EmbeddingCache(tmp_db.parent / "cache1.json")
        conn1 = get_connection(tmp_db)
        clusters1 = run_clustering_pipeline(
            conn=conn1, run_id="run_a", reviews=reviews,
            provider=provider, cache=cache1, seed=42,
        )
        conn1.close()

        cache2 = EmbeddingCache(tmp_db.parent / "cache2.json")
        conn2 = get_connection(tmp_db)
        clusters2 = run_clustering_pipeline(
            conn=conn2, run_id="run_b", reviews=reviews,
            provider=provider, cache=cache2, seed=42,
        )
        conn2.close()

        # Same number of clusters
        assert len(clusters1) == len(clusters2)
        # Same review sets per cluster (sorted for comparison)
        ids1 = sorted(sorted(c.review_ids) for c in clusters1)
        ids2 = sorted(sorted(c.review_ids) for c in clusters2)
        assert ids1 == ids2


# ---------------------------------------------------------------------------
# E2-3: Embedding cache hit rate on re-run
# ---------------------------------------------------------------------------

class TestCacheHitRate:
    def test_full_cache_hit_on_rerun(self, tmp_db: Path) -> None:
        reviews = [_make_review(i) for i in range(10)]
        provider = _seeded_provider(dim=16)
        cache_path = tmp_db.parent / "emb.json"
        cache = EmbeddingCache(cache_path)

        texts = [r.body for r in reviews]
        _, hits1, misses1 = embed_reviews(texts, provider, cache)
        assert hits1 == 0
        assert misses1 == 10

        cache2 = EmbeddingCache(cache_path)
        _, hits2, misses2 = embed_reviews(texts, provider, cache2)
        assert hits2 == 10
        assert misses2 == 0


# ---------------------------------------------------------------------------
# EC2-1: Fewer than 20 reviews after filtering
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_small_review_set_clusters_without_error(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = [_make_review(i) for i in range(15)]
        provider = _seeded_provider(dim=16)
        cache = EmbeddingCache(tmp_db.parent / "emb.json")
        conn = get_connection(tmp_db)

        # Should not raise — min_cluster_size is auto-clamped
        clusters = run_clustering_pipeline(
            conn=conn, run_id="small_run", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        conn.close()
        assert isinstance(clusters, list)

    def test_duplicate_texts_handled(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        body = "App keeps crashing and this is a very frustrating experience for users"
        reviews = [_make_review(i, body=body) for i in range(20)]
        provider = _seeded_provider(dim=16)
        cache = EmbeddingCache(tmp_db.parent / "emb.json")
        conn = get_connection(tmp_db)

        clusters = run_clustering_pipeline(
            conn=conn, run_id="dup_run", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        conn.close()
        assert isinstance(clusters, list)

    def test_idempotent_recluster_deletes_old_clusters(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = _load_snapshot_reviews()
        provider = _seeded_provider(dim=32)
        cache = EmbeddingCache(tmp_db.parent / "emb.json")

        conn = get_connection(tmp_db)
        run_clustering_pipeline(
            conn=conn, run_id="idem_run", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        count1 = conn.execute(
            "SELECT count(*) FROM clusters WHERE run_id='idem_run'"
        ).fetchone()[0]

        run_clustering_pipeline(
            conn=conn, run_id="idem_run", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        count2 = conn.execute(
            "SELECT count(*) FROM clusters WHERE run_id='idem_run'"
        ).fetchone()[0]
        conn.close()

        assert count1 == count2  # idempotent: same count on re-run

    def test_clusters_table_populated(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = _load_snapshot_reviews()
        provider = _seeded_provider(dim=32)
        cache = EmbeddingCache(tmp_db.parent / "emb.json")

        conn = get_connection(tmp_db)
        clusters = run_clustering_pipeline(
            conn=conn, run_id="persist_run", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        rows = conn.execute(
            "SELECT * FROM clusters WHERE run_id='persist_run'"
        ).fetchall()
        conn.close()

        assert len(rows) == len(clusters)
        for row in rows:
            ids = json.loads(row["review_ids_json"])
            kps = json.loads(row["keyphrases_json"])
            assert len(ids) > 0
            assert row["medoid_review_id"] in ids

    def test_review_embeddings_persisted(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = _load_snapshot_reviews()[:20]
        provider = _seeded_provider(dim=32)
        cache = EmbeddingCache(tmp_db.parent / "emb.json")

        conn = get_connection(tmp_db)
        run_clustering_pipeline(
            conn=conn, run_id="emb_run", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        count = conn.execute("SELECT count(*) FROM review_embeddings").fetchone()[0]
        conn.close()

        assert count == len(reviews)

    def test_run_status_updated_to_clustered(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        conn = get_connection(tmp_db)
        with conn:
            conn.execute(
                """INSERT INTO runs (id, product_key, iso_week, window_start, window_end, status)
                   VALUES ('r1', 'groww', '2026-W16', '2026-04-01', '2026-04-30', 'ingested')"""
            )

        reviews = _load_snapshot_reviews()
        provider = _seeded_provider(dim=32)
        cache = EmbeddingCache(tmp_db.parent / "emb.json")

        run_clustering_pipeline(
            conn=conn, run_id="r1", reviews=reviews,
            provider=provider, cache=cache, seed=42,
        )
        status = conn.execute("SELECT status FROM runs WHERE id='r1'").fetchone()["status"]
        conn.close()
        assert status == "clustered"
