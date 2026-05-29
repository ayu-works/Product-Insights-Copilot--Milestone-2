"""Phase 1 ingestion tests — evaluations E1-1 through E1-6."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from agent.config import ProductConfig
from agent.ingestion.filters import has_emoji, is_english, scrub_pii, should_keep, word_count
from agent.ingestion.appstore import fetch_appstore_reviews
from agent.ingestion.playstore import fetch_playstore_reviews
from agent.models import RawReview
from agent.storage import get_connection, init_db


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _review_id(source: str, external_id: str) -> str:
    return hashlib.sha1(f"{source}{external_id}".encode()).hexdigest()


def _make_product(key: str = "groww", appstore_id: str = "1404871982",
                  play_package: str = "com.nextbillion.groww") -> ProductConfig:
    return ProductConfig(
        key=key,
        display="Groww",
        appstore_id=appstore_id,
        play_package=play_package,
        gmail_to="test@example.com",
    )


def _upsert(conn, reviews: list[RawReview]) -> None:
    now = datetime.now(timezone.utc).isoformat()
    for r in reviews:
        conn.execute(
            """
            INSERT INTO reviews
                (id, product_key, source, rating, title, body, posted_at,
                 version, language, country, ingested_at, raw_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                body        = excluded.body,
                rating      = excluded.rating,
                version     = excluded.version,
                ingested_at = excluded.ingested_at,
                raw_json    = excluded.raw_json
            """,
            (r.id, r.product_key, r.source, r.rating, r.title, r.body,
             r.posted_at.isoformat(), r.version, r.language, r.country,
             now, r.model_dump_json()),
        )


# ---------------------------------------------------------------------------
# E1-1: Fixture replay — deterministic snapshot
# ---------------------------------------------------------------------------

class TestFixtureReplay:
    def test_appstore_fixture_produces_correct_ids(self, appstore_fixture: dict) -> None:
        product = _make_product()
        mock_resp = MagicMock()
        mock_resp.json.return_value = appstore_fixture
        mock_resp.raise_for_status = MagicMock()

        # Page 1 returns fixture; page 2 returns empty feed
        empty_resp = MagicMock()
        empty_resp.json.return_value = {"feed": {}}
        empty_resp.raise_for_status = MagicMock()

        import httpx
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = [mock_resp, empty_resp]

        reviews = fetch_appstore_reviews(product, client=mock_client)
        ids = {r.id for r in reviews}

        assert _review_id("appstore", "1111") in ids
        assert _review_id("appstore", "3333") in ids

    def test_appstore_id_is_sha1_of_source_plus_external_id(self, appstore_fixture: dict) -> None:
        product = _make_product()
        empty_resp = MagicMock()
        empty_resp.json.return_value = {"feed": {}}
        empty_resp.raise_for_status = MagicMock()

        page1_resp = MagicMock()
        page1_resp.json.return_value = appstore_fixture
        page1_resp.raise_for_status = MagicMock()

        import httpx
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = [page1_resp, empty_resp]

        reviews = fetch_appstore_reviews(product, client=mock_client)
        for r in reviews:
            assert len(r.id) == 40
            assert all(c in "0123456789abcdef" for c in r.id)

    def test_playstore_fixture_produces_correct_ids(self, playstore_fixture: list) -> None:
        product = _make_product()

        def mock_reviews_fn(**kwargs):
            return playstore_fixture, None

        reviews = fetch_playstore_reviews(product, _reviews_fn=mock_reviews_fn)
        ids = {r.id for r in reviews}

        assert _review_id("playstore", "p1111") in ids
        assert _review_id("playstore", "p2222") in ids
        assert _review_id("playstore", "p5555") in ids

    def test_end_to_end_fixture_kept_count(
        self, tmp_db: Path, appstore_fixture: dict, playstore_fixture: list
    ) -> None:
        """After filters: emoji(2222,p3333), non-en(4444), short(5555,p4444) removed → 5 kept."""
        init_db(tmp_db)

        import httpx
        page1_resp = MagicMock()
        page1_resp.json.return_value = appstore_fixture
        page1_resp.raise_for_status = MagicMock()
        empty_resp = MagicMock()
        empty_resp.json.return_value = {"feed": {}}
        empty_resp.raise_for_status = MagicMock()
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = [page1_resp, empty_resp]

        def mock_reviews_fn(**kwargs):
            return playstore_fixture, None

        product = _make_product()
        from agent.ingestion.filters import scrub_pii, should_keep

        appstore = fetch_appstore_reviews(product, client=mock_client)
        playstore = fetch_playstore_reviews(product, _reviews_fn=mock_reviews_fn)
        kept = [
            r.model_copy(update={"body": scrub_pii(r.body)})
            for r in appstore + playstore
            if should_keep(r.body)
        ]

        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, kept)
        rows = conn.execute(
            "SELECT id FROM reviews WHERE product_key = 'groww'"
        ).fetchall()
        conn.close()

        assert len(rows) == 5


# ---------------------------------------------------------------------------
# E1-2: PII scrubbing
# ---------------------------------------------------------------------------

class TestPiiScrubbing:
    def test_email_replaced(self) -> None:
        body = "My email is john@example.com and I use this app daily"
        result = scrub_pii(body)
        assert "john@example.com" not in result
        assert "[EMAIL]" in result

    def test_aadhaar_replaced(self) -> None:
        body = "My Aadhaar is 1234 5678 9012 and I need a refund from this app"
        result = scrub_pii(body)
        assert "1234 5678 9012" not in result
        assert "[AADHAAR]" in result

    def test_phone_replaced(self) -> None:
        body = "Call me on +91-9876543210 for a refund on my investment"
        result = scrub_pii(body)
        assert "9876543210" not in result
        assert "[PHONE]" in result

    def test_empty_body_is_noop(self) -> None:
        assert scrub_pii("") == ""

    def test_clean_body_unchanged(self) -> None:
        body = "This is a great investment app with no issues whatsoever"
        assert scrub_pii(body) == body

    def test_pii_scrubbed_before_db(self, tmp_db: Path, appstore_fixture: dict) -> None:
        init_db(tmp_db)
        product = _make_product()

        import httpx
        page1_resp = MagicMock()
        page1_resp.json.return_value = appstore_fixture
        page1_resp.raise_for_status = MagicMock()
        empty_resp = MagicMock()
        empty_resp.json.return_value = {"feed": {}}
        empty_resp.raise_for_status = MagicMock()
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = [page1_resp, empty_resp]

        from agent.ingestion.filters import scrub_pii, should_keep

        reviews = fetch_appstore_reviews(product, client=mock_client)
        kept = [
            r.model_copy(update={"body": scrub_pii(r.body)})
            for r in reviews
            if should_keep(r.body)
        ]
        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, kept)
        pii_review_id = _review_id("appstore", "3333")
        row = conn.execute(
            "SELECT body FROM reviews WHERE id = ?", (pii_review_id,)
        ).fetchone()
        conn.close()

        assert row is not None
        assert "test@example.com" not in row["body"]
        assert "[EMAIL]" in row["body"]


# ---------------------------------------------------------------------------
# E1-3: Dedup / upsert behaviour
# ---------------------------------------------------------------------------

class TestDedupUpsert:
    def _make_review(self, body: str = "This is a great app worth using daily") -> RawReview:
        return RawReview(
            id=_review_id("playstore", "dup_test_001"),
            product_key="groww",
            source="playstore",
            rating=4,
            body=body,
            posted_at=datetime(2026, 4, 15, tzinfo=timezone.utc),
            language="en",
            country="IN",
        )

    def test_same_id_inserted_once(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        review = self._make_review()
        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, [review])
            _upsert(conn, [review])
        count = conn.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
        conn.close()
        assert count == 1

    def test_upsert_updates_body(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        original = self._make_review("Original body text with enough words here")
        updated = self._make_review("Updated body text with different content now")
        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, [original])
        with conn:
            _upsert(conn, [updated])
        row = conn.execute("SELECT body FROM reviews WHERE id = ?", (original.id,)).fetchone()
        conn.close()
        assert row["body"] == "Updated body text with different content now"

    def test_no_duplicate_rows(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = [self._make_review() for _ in range(5)]
        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, reviews)
        count = conn.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
        conn.close()
        assert count == 1


# ---------------------------------------------------------------------------
# E1-5: Re-run is a no-op (unit-level)
# ---------------------------------------------------------------------------

class TestRerunIsNoOp:
    def test_second_upsert_same_data(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        reviews = [
            RawReview(
                id=_review_id("playstore", f"noop_{i}"),
                product_key="groww",
                source="playstore",
                rating=4,
                body="App is quite good and reliable for investments",
                posted_at=datetime(2026, 4, 15, tzinfo=timezone.utc),
                language="en",
                country="IN",
            )
            for i in range(3)
        ]
        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, reviews)
        count_before = conn.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
        with conn:
            _upsert(conn, reviews)
        count_after = conn.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
        conn.close()
        assert count_before == count_after == 3


# ---------------------------------------------------------------------------
# Filter unit tests (emoji, language, word count)
# ---------------------------------------------------------------------------

class TestFilters:
    def test_has_emoji_true(self) -> None:
        assert has_emoji("Great app 🚀🔥 highly recommend") is True

    def test_has_emoji_false(self) -> None:
        assert has_emoji("Great app highly recommended for all") is False

    def test_has_emoji_empty(self) -> None:
        assert has_emoji("") is False

    def test_word_count_under_four_filtered(self) -> None:
        assert should_keep("Great") is False
        assert should_keep("Too slow bro") is False

    def test_word_count_four_or_more_passes(self) -> None:
        assert word_count("This is four words") == 4

    def test_english_passes(self) -> None:
        assert is_english("This app is great for investing money every month") is True

    def test_non_english_filtered(self) -> None:
        assert should_keep("बहुत अच्छा एप है निवेश के लिए सभी के लिए") is False

    def test_emoji_review_filtered(self) -> None:
        assert should_keep("Best investment app ever 🚀🔥 highly recommend") is False

    def test_short_review_filtered(self) -> None:
        assert should_keep("Too slow") is False

    def test_good_review_kept(self) -> None:
        assert should_keep("This is a great investment app for long term") is True


# ---------------------------------------------------------------------------
# EC1-7: No App Store ID configured
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_no_appstore_id_returns_empty(self) -> None:
        product = ProductConfig(
            key="powermoney",
            display="PowerUp Money",
            appstore_id=None,
            play_package="com.powermoney",
            gmail_to="test@example.com",
        )
        result = fetch_appstore_reviews(product)
        assert result == []

    def test_no_play_package_returns_empty(self) -> None:
        product = ProductConfig(
            key="someapp",
            display="Some App",
            appstore_id=None,
            play_package=None,
            gmail_to="test@example.com",
        )
        result = fetch_playstore_reviews(product)
        assert result == []

    def test_empty_review_body_stored_empty(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        review = RawReview(
            id=_review_id("playstore", "empty_body_001"),
            product_key="groww",
            source="playstore",
            rating=3,
            body="",
            posted_at=datetime(2026, 4, 15, tzinfo=timezone.utc),
            language="en",
            country="IN",
        )
        conn = get_connection(tmp_db)
        with conn:
            _upsert(conn, [review])
        row = conn.execute("SELECT body FROM reviews WHERE id = ?", (review.id,)).fetchone()
        conn.close()
        assert row["body"] == ""

    def test_duplicate_external_ids_across_sources_no_collision(self) -> None:
        id_appstore = _review_id("appstore", "SAME_ID")
        id_playstore = _review_id("playstore", "SAME_ID")
        assert id_appstore != id_playstore

    def test_appstore_page_empty_stops_pagination(self) -> None:
        product = _make_product()
        empty_resp = MagicMock()
        empty_resp.json.return_value = {"feed": {}}
        empty_resp.raise_for_status = MagicMock()

        import httpx
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = empty_resp

        result = fetch_appstore_reviews(product, client=mock_client)
        assert result == []
        assert mock_client.get.call_count == 1
