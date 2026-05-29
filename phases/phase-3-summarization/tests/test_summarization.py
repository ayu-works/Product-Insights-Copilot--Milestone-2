"""Phase 3 summarization tests — E3-1 through E3-8 and edge cases."""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import pytest

from agent.models import Window
from agent.storage import get_connection, init_db
from agent.summarization.client import (
    LLMSchemaError,
    MockLLMClient,
    PulseCostExceeded,
    RunMetrics,
)
from agent.summarization.pipeline import (
    _is_verbatim,
    _normalize_ws,
    _scrub_and_truncate,
    generate_action_ideas,
    generate_what_this_solves,
    label_theme,
    select_quotes,
    summarize_pulse,
)


# ---------------------------------------------------------------------------
# Fixtures & helpers
# ---------------------------------------------------------------------------

WINDOW = Window(start=date(2026, 4, 1), end=date(2026, 4, 30), weeks=4)

_CRASH_REVIEWS = [
    {
        "id": hashlib.sha1(b"r1").hexdigest(),
        "body": "The app crashes every time I try to open my portfolio showing a black screen",
        "rating": 1,
        "title": None,
    },
    {
        "id": hashlib.sha1(b"r2").hexdigest(),
        "body": "App keeps crashing when I navigate to the mutual funds section constantly",
        "rating": 1,
        "title": None,
    },
    {
        "id": hashlib.sha1(b"r3").hexdigest(),
        "body": "Keeps force closing in the middle of transactions which is very frustrating",
        "rating": 2,
        "title": None,
    },
]

_UI_REVIEWS = [
    {
        "id": hashlib.sha1(b"r4").hexdigest(),
        "body": "Clean and intuitive interface makes investing very simple for complete beginners",
        "rating": 5,
        "title": None,
    },
    {
        "id": hashlib.sha1(b"r5").hexdigest(),
        "body": "Beautiful design and smooth navigation makes the app really pleasant to use",
        "rating": 5,
        "title": None,
    },
]

_CANNED_LABEL_CRASH = {
    "label": "App Crashes Frequently",
    "description": "Users report the app crashes when opening portfolio or placing orders.",
    "sentiment": "negative",
}
_CANNED_LABEL_UI = {
    "label": "Excellent UI Design",
    "description": "Users praise the clean, intuitive interface and smooth navigation.",
    "sentiment": "positive",
}
_CANNED_QUOTES_CRASH = {
    "quotes": [
        {
            "body": "The app crashes every time I try to open my portfolio showing a black screen",
            "review_index": 0,
        },
        {
            "body": "Keeps force closing in the middle of transactions which is very frustrating",
            "review_index": 2,
        },
    ]
}
_CANNED_QUOTES_UI = {
    "quotes": [
        {
            "body": "Clean and intuitive interface makes investing very simple for complete beginners",
            "review_index": 0,
        },
    ]
}
_CANNED_ACTIONS = {
    "action_ideas": [
        {
            "title": "Fix Portfolio Crash",
            "description": "Investigate and fix crash on portfolio screen load.",
            "theme_ids": ["cluster_a"],
        },
        {
            "title": "Maintain UI Quality",
            "description": "Continue design system investment and gather UI feedback regularly.",
            "theme_ids": ["cluster_b"],
        },
    ]
}
_CANNED_WHAT_SOLVES = {
    "what_this_solves": [
        {"audience": "New investors", "value": "Reliable portfolio access without crashes"},
        {"audience": "Active traders", "value": "Confidence in app stability during trades"},
    ]
}


def _seed_db(conn, run_id: str, clusters: list[dict], reviews: list[dict]) -> None:
    """Seed DB with run, clusters, and reviews for a summarization test."""
    with conn:
        conn.execute(
            """INSERT INTO runs (id, product_key, iso_week, window_start, window_end, status)
               VALUES (?, 'groww', '2026-W16', ?, ?, 'clustered')""",
            (run_id, WINDOW.start.isoformat(), WINDOW.end.isoformat()),
        )
        for r in reviews:
            conn.execute(
                """INSERT OR IGNORE INTO reviews
                   (id, product_key, source, rating, title, body, posted_at,
                    language, country, ingested_at)
                   VALUES (?, 'groww', 'playstore', ?, ?, ?, '2026-04-15T10:00:00+00:00',
                           'en', 'IN', '2026-04-15T10:00:00+00:00')""",
                (r["id"], r["rating"], r.get("title"), r["body"]),
            )
        for c in clusters:
            conn.execute(
                """INSERT INTO clusters
                   (id, run_id, cluster_label, review_ids_json,
                    keyphrases_json, medoid_review_id, representative_review_ids_json)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    c["id"], run_id, c["label"],
                    json.dumps(c["review_ids"]),
                    json.dumps(c.get("keyphrases", [])),
                    c["medoid_id"],
                    json.dumps(c.get("rep_ids", [c["medoid_id"]])),
                ),
            )


# ---------------------------------------------------------------------------
# Verbatim validator unit tests  (E3-2)
# ---------------------------------------------------------------------------

class TestVerbatimValidator:
    def test_exact_substring_passes(self) -> None:
        bodies = ["The app crashes every time I try to open my portfolio"]
        assert _is_verbatim("app crashes every time", bodies) is True

    def test_whitespace_normalised_passes(self) -> None:
        bodies = ["The  app  crashes  every   time"]
        assert _is_verbatim("app crashes every time", bodies) is True

    def test_hallucinated_quote_fails(self) -> None:
        bodies = ["App is great and works well"]
        assert _is_verbatim("app crashes constantly", bodies) is False

    def test_empty_quote_fails(self) -> None:
        assert _is_verbatim("", ["any body text here"]) is False

    def test_regex_special_chars_handled(self) -> None:
        """EC3-8: quotes with regex special chars should not break validator."""
        bodies = ["5+5 = 10? Really?? This is weird (but true)."]
        assert _is_verbatim("5+5 = 10? Really??", bodies) is True


# ---------------------------------------------------------------------------
# select_quotes: retry on hallucination  (E3-2)
# ---------------------------------------------------------------------------

class TestSelectQuotesRetry:
    def test_good_quotes_returned(self) -> None:
        client = MockLLMClient([_CANNED_QUOTES_CRASH])
        quotes = select_quotes("App Crashes", _CRASH_REVIEWS, client, "c1")
        assert len(quotes) >= 1
        assert all(
            _is_verbatim(q.body, [r["body"] for r in _CRASH_REVIEWS])
            for q in quotes
        )

    def test_hallucinated_quote_dropped_and_retried(self) -> None:
        hallucinated = {
            "quotes": [{"body": "This quote was invented by the LLM", "review_index": 0}]
        }
        # First call: hallucinated; second call (retry): valid
        client = MockLLMClient([hallucinated, _CANNED_QUOTES_CRASH])
        quotes = select_quotes("App Crashes", _CRASH_REVIEWS, client, "c1")
        assert client.metrics.call_count == 2
        assert all(
            _is_verbatim(q.body, [r["body"] for r in _CRASH_REVIEWS])
            for q in quotes
        )

    def test_double_hallucination_returns_empty(self) -> None:
        hallucinated = {
            "quotes": [{"body": "Completely made up text not in any review", "review_index": 0}]
        }
        client = MockLLMClient([hallucinated, hallucinated])
        quotes = select_quotes("App Crashes", _CRASH_REVIEWS, client, "c1")
        assert quotes == []
        assert client.metrics.call_count == 2  # tried twice, no more

    def test_empty_cluster_returns_empty(self) -> None:
        client = MockLLMClient([])
        quotes = select_quotes("App Crashes", [], client, "c1")
        assert quotes == []
        assert client.metrics.call_count == 0


# ---------------------------------------------------------------------------
# E3-1: Theme generation
# ---------------------------------------------------------------------------

class TestThemeGeneration:
    def test_label_theme_structure(self) -> None:
        client = MockLLMClient([_CANNED_LABEL_CRASH])
        result = label_theme(["crashes", "freeze", "black screen"], _CRASH_REVIEWS, client)
        assert result["label"] == "App Crashes Frequently"
        assert result["sentiment"] == "negative"
        assert len(result["description"]) > 0

    def test_sentiment_values_valid(self) -> None:
        for sentiment in ("negative", "mixed", "positive"):
            canned = {"label": "Test Theme", "description": "Desc.", "sentiment": sentiment}
            client = MockLLMClient([canned])
            result = label_theme([], _CRASH_REVIEWS, client)
            assert result["sentiment"] == sentiment


# ---------------------------------------------------------------------------
# E3-7: Action ideas
# ---------------------------------------------------------------------------

class TestActionIdeas:
    def test_action_ideas_count(self, tmp_db: Path) -> None:
        from agent.models import Theme
        themes = [
            Theme(
                id="c1", rank=1, label="App Crashes",
                description="Crashes on portfolio", sentiment="negative",
                review_count=50, representative_review_ids=[],
            ),
        ]
        client = MockLLMClient([_CANNED_ACTIONS])
        ideas = generate_action_ideas("groww", themes, client)
        assert 1 <= len(ideas) <= 5
        for idea in ideas:
            assert idea.title
            assert idea.description


# ---------------------------------------------------------------------------
# E3-3: Deterministic snapshot with mocked LLM
# ---------------------------------------------------------------------------

class TestDeterministicSnapshot:
    def _run(self, tmp_db: Path) -> dict:
        init_db(tmp_db)
        conn = get_connection(tmp_db)

        cluster_a_id = hashlib.sha1(b"cluster_a").hexdigest()
        cluster_b_id = hashlib.sha1(b"cluster_b").hexdigest()

        clusters = [
            {
                "id": cluster_a_id, "label": 0,
                "review_ids": [r["id"] for r in _CRASH_REVIEWS],
                "medoid_id": _CRASH_REVIEWS[0]["id"],
                "keyphrases": ["crashes", "freeze"],
            },
            {
                "id": cluster_b_id, "label": 1,
                "review_ids": [r["id"] for r in _UI_REVIEWS],
                "medoid_id": _UI_REVIEWS[0]["id"],
                "keyphrases": ["clean", "intuitive"],
            },
        ]
        _seed_db(conn, "run_snap", clusters, _CRASH_REVIEWS + _UI_REVIEWS)

        responses = [
            _CANNED_LABEL_CRASH, _CANNED_QUOTES_CRASH,
            _CANNED_LABEL_UI, _CANNED_QUOTES_UI,
            _CANNED_ACTIONS, _CANNED_WHAT_SOLVES,
        ]
        client = MockLLMClient(responses)
        summary = summarize_pulse(
            conn=conn, run_id="run_snap", product_key="groww",
            window=WINDOW, client=client,
        )
        conn.close()
        return json.loads(summary.model_dump_json())

    def test_same_output_across_two_runs(self, tmp_db: Path, tmp_path: Path) -> None:
        result1 = self._run(tmp_db)
        result2 = self._run(tmp_path / "pulse2.db")
        assert result1 == result2

    def test_summary_has_three_fields(self, tmp_db: Path) -> None:
        result = self._run(tmp_db)
        assert "top_themes" in result
        assert "quotes" in result
        assert "action_ideas" in result
        assert "what_this_solves" in result


# ---------------------------------------------------------------------------
# E3-4: Cost cap
# ---------------------------------------------------------------------------

class TestCostCap:
    def test_cost_cap_raises_pulse_cost_exceeded(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        conn = get_connection(tmp_db)

        cluster_id = hashlib.sha1(b"cap_cluster").hexdigest()
        clusters = [{
            "id": cluster_id, "label": 0,
            "review_ids": [r["id"] for r in _CRASH_REVIEWS],
            "medoid_id": _CRASH_REVIEWS[0]["id"],
        }]
        _seed_db(conn, "run_cap", clusters, _CRASH_REVIEWS)

        # fail_after_calls=1 means PulseCostExceeded on the 2nd call
        client = MockLLMClient(
            responses=[_CANNED_LABEL_CRASH] * 10,
            fail_after_calls=1,
        )
        with pytest.raises(PulseCostExceeded) as exc_info:
            summarize_pulse(
                conn=conn, run_id="run_cap", product_key="groww",
                window=WINDOW, client=client,
            )
        assert "Token limit" in str(exc_info.value) or "exceeded" in str(exc_info.value).lower()
        conn.close()

    def test_run_status_set_to_failed_on_cap(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        conn = get_connection(tmp_db)

        cluster_id = hashlib.sha1(b"cap2").hexdigest()
        clusters = [{
            "id": cluster_id, "label": 0,
            "review_ids": [r["id"] for r in _CRASH_REVIEWS],
            "medoid_id": _CRASH_REVIEWS[0]["id"],
        }]
        _seed_db(conn, "run_cap2", clusters, _CRASH_REVIEWS)

        client = MockLLMClient(responses=[_CANNED_LABEL_CRASH] * 10, fail_after_calls=1)
        with pytest.raises(PulseCostExceeded):
            summarize_pulse(conn=conn, run_id="run_cap2", product_key="groww", window=WINDOW, client=client)

        status = conn.execute("SELECT status FROM runs WHERE id='run_cap2'").fetchone()["status"]
        conn.close()
        assert status == "summarize_failed"


# ---------------------------------------------------------------------------
# E3-5: PII re-scrub before LLM
# ---------------------------------------------------------------------------

class TestPiiRescrub:
    def test_phone_scrubbed_from_llm_prompt(self) -> None:
        reviews_with_pii = [
            {
                "id": "pii1",
                "body": "Call me on +91-9876543210 for a refund on my failed transaction",
                "rating": 1,
                "title": None,
            }
        ]
        client = MockLLMClient([_CANNED_LABEL_CRASH])
        label_theme(["refund", "call"], reviews_with_pii, client)
        assert "9876543210" not in client._last_user
        assert "[PHONE]" in client._last_user

    def test_email_scrubbed_from_llm_prompt(self) -> None:
        reviews_with_pii = [
            {
                "id": "pii2",
                "body": "My email is test@example.com and I cannot login to the app",
                "rating": 2,
                "title": None,
            }
        ]
        client = MockLLMClient([_CANNED_LABEL_CRASH])
        label_theme([], reviews_with_pii, client)
        assert "test@example.com" not in client._last_user
        assert "[EMAIL]" in client._last_user


# ---------------------------------------------------------------------------
# E3-8: Token and cost accounting
# ---------------------------------------------------------------------------

class TestCostAccounting:
    def test_metrics_accumulated_across_calls(self) -> None:
        client = MockLLMClient(
            [_CANNED_LABEL_CRASH, _CANNED_LABEL_UI],
            tokens_per_call=200,
        )
        label_theme([], _CRASH_REVIEWS, client)
        label_theme([], _UI_REVIEWS, client)

        assert client.metrics.call_count == 2
        assert client.metrics.total_input_tokens == 400
        assert client.metrics.total_cost_usd > 0

    def test_metrics_as_dict_keys(self) -> None:
        client = MockLLMClient([_CANNED_LABEL_CRASH])
        label_theme([], _CRASH_REVIEWS, client)
        d = client.metrics.as_dict()
        assert "llm_tokens_prompt" in d
        assert "llm_tokens_completion" in d
        assert "llm_cost_usd" in d
        assert "llm_calls" in d

    def test_run_metrics_json_persisted(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        conn = get_connection(tmp_db)

        cluster_id = hashlib.sha1(b"metrics_cluster").hexdigest()
        clusters = [{
            "id": cluster_id, "label": 0,
            "review_ids": [r["id"] for r in _UI_REVIEWS],
            "medoid_id": _UI_REVIEWS[0]["id"],
        }]
        _seed_db(conn, "run_metrics", clusters, _UI_REVIEWS)

        responses = [_CANNED_LABEL_UI, _CANNED_QUOTES_UI, _CANNED_ACTIONS, _CANNED_WHAT_SOLVES]
        client = MockLLMClient(responses, tokens_per_call=150)
        summarize_pulse(conn=conn, run_id="run_metrics", product_key="groww", window=WINDOW, client=client)

        row = conn.execute("SELECT metrics_json, status FROM runs WHERE id='run_metrics'").fetchone()
        conn.close()

        assert row["status"] == "summarized"
        metrics = json.loads(row["metrics_json"])
        assert metrics["llm_calls"] > 0
        assert metrics["llm_tokens_prompt"] > 0
        assert metrics["llm_cost_usd"] > 0


# ---------------------------------------------------------------------------
# EC3-5: Fewer than 3 themes is acceptable
# ---------------------------------------------------------------------------

class TestFewThemes:
    def test_two_clusters_produces_two_themes(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        conn = get_connection(tmp_db)

        ca = hashlib.sha1(b"few_a").hexdigest()
        cb = hashlib.sha1(b"few_b").hexdigest()
        clusters = [
            {"id": ca, "label": 0, "review_ids": [r["id"] for r in _CRASH_REVIEWS],
             "medoid_id": _CRASH_REVIEWS[0]["id"]},
            {"id": cb, "label": 1, "review_ids": [r["id"] for r in _UI_REVIEWS],
             "medoid_id": _UI_REVIEWS[0]["id"]},
        ]
        _seed_db(conn, "run_few", clusters, _CRASH_REVIEWS + _UI_REVIEWS)

        responses = [
            _CANNED_LABEL_CRASH, _CANNED_QUOTES_CRASH,
            _CANNED_LABEL_UI, _CANNED_QUOTES_UI,
            _CANNED_ACTIONS, _CANNED_WHAT_SOLVES,
        ]
        client = MockLLMClient(responses)
        summary = summarize_pulse(
            conn=conn, run_id="run_few", product_key="groww",
            window=WINDOW, client=client, max_themes=3,
        )
        conn.close()
        assert len(summary.top_themes) == 2  # only 2 clusters, no padding


# ---------------------------------------------------------------------------
# Theme ranking
# ---------------------------------------------------------------------------

class TestThemeRanking:
    def test_negative_outranks_positive_with_same_count(self, tmp_db: Path) -> None:
        init_db(tmp_db)
        conn = get_connection(tmp_db)

        ca = hashlib.sha1(b"rank_neg").hexdigest()
        cb = hashlib.sha1(b"rank_pos").hexdigest()
        # Same number of reviews (3 each), but one negative one positive
        clusters = [
            {"id": ca, "label": 0, "review_ids": [r["id"] for r in _UI_REVIEWS] + [_UI_REVIEWS[0]["id"]],
             "medoid_id": _UI_REVIEWS[0]["id"]},  # positive, 3 reviews
            {"id": cb, "label": 1, "review_ids": [r["id"] for r in _CRASH_REVIEWS],
             "medoid_id": _CRASH_REVIEWS[0]["id"]},  # negative, 3 reviews
        ]
        _seed_db(conn, "run_rank", clusters, _CRASH_REVIEWS + _UI_REVIEWS)

        responses = [
            _CANNED_LABEL_UI, _CANNED_QUOTES_UI,      # positive cluster processed first
            _CANNED_LABEL_CRASH, _CANNED_QUOTES_CRASH, # negative cluster second
            _CANNED_ACTIONS, _CANNED_WHAT_SOLVES,
        ]
        client = MockLLMClient(responses)
        summary = summarize_pulse(
            conn=conn, run_id="run_rank", product_key="groww",
            window=WINDOW, client=client,
        )
        conn.close()

        # Negative theme (weight=1.5) should rank above positive (weight=0.8) with same count
        assert summary.top_themes[0].sentiment == "negative"
