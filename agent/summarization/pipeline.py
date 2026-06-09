"""Phase 3 pipeline: label_theme → select_quotes → action_ideas → PulseSummary."""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from pathlib import Path
from typing import Any, Optional

import structlog

from agent.ingestion.filters import scrub_pii
from agent.models import (
    ActionIdea,
    AudienceValue,
    PulseSummary,
    PulseStats,
    Quote,
    Theme,
    Window,
)
from agent.summarization.client import (
    LLMClient,
    PulseCostExceeded,
    RunMetrics,
)
from agent.summarization.prompts import (
    SYSTEM_ANALYST,
    generate_action_ideas_prompt,
    generate_what_this_solves_prompt,
    label_theme_prompt,
    select_quotes_prompt,
    select_quotes_retry_prompt,
)

log = structlog.get_logger()

# Ranking weights per sentiment (evaluations E3-1)
_SENTIMENT_WEIGHT: dict[str, float] = {
    "negative": 1.5,
    "mixed":    1.0,
    "positive": 0.8,
}

# Max characters sent to LLM per review body  (~512 tokens ≈ 2048 chars)
_MAX_BODY_CHARS = 2048


# ---------------------------------------------------------------------------
# JSON schemas for tool-use / structured output
# ---------------------------------------------------------------------------

_THEME_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "label":       {"type": "string"},
        "description": {"type": "string"},
        "sentiment":   {"type": "string", "enum": ["negative", "mixed", "positive"]},
    },
    "required": ["label", "description", "sentiment"],
}

_QUOTES_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "quotes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "body":         {"type": "string"},
                    "review_index": {"type": "integer"},
                },
                "required": ["body", "review_index"],
            },
        }
    },
    "required": ["quotes"],
}

_ACTION_IDEAS_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "action_ideas": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title":       {"type": "string"},
                    "description": {"type": "string"},
                    "theme_ids":   {"type": "array", "items": {"type": "string"}},
                },
                "required": ["title", "description", "theme_ids"],
            },
        }
    },
    "required": ["action_ideas"],
}

_WHAT_SOLVES_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "what_this_solves": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "audience": {"type": "string"},
                    "value":    {"type": "string"},
                },
                "required": ["audience", "value"],
            },
        }
    },
    "required": ["what_this_solves"],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def _is_verbatim(quote: str, bodies: list[str]) -> bool:
    """EC3-8: plain substring check — no regex, handles special characters."""
    norm_q = _normalize_ws(quote)
    if not norm_q:
        return False
    return any(norm_q in _normalize_ws(b) for b in bodies)


def _truncate_body(body: str, max_chars: int = _MAX_BODY_CHARS) -> str:
    """EC3-3: truncate long bodies before including in LLM prompts."""
    if len(body) <= max_chars:
        return body
    log.debug("review_body_truncated", original_len=len(body), max_chars=max_chars)
    return body[:max_chars] + "…"


def _scrub_and_truncate(reviews: list[dict[str, Any]], max_chars: int = _MAX_BODY_CHARS) -> list[dict[str, Any]]:
    """PII-scrub and truncate review bodies before any LLM call."""
    out = []
    for r in reviews:
        body = scrub_pii(r.get("body", "") or "")
        body = _truncate_body(body, max_chars)
        out.append({**r, "body": body})
    return out


# ---------------------------------------------------------------------------
# Step 1: label_theme
# ---------------------------------------------------------------------------

def _normalize_theme_response(raw: dict[str, Any]) -> dict[str, Any]:
    """Tolerate key/value variants that open-source models sometimes return."""
    # Key aliases: theme/name/title → label
    label = raw.get("label") or raw.get("theme") or raw.get("name") or raw.get("title") or ""
    description = raw.get("description") or raw.get("summary") or raw.get("details") or ""
    # Sentiment: normalise "Generally Positive" → "positive" etc.
    raw_sentiment = str(raw.get("sentiment", "mixed")).lower()
    if "negative" in raw_sentiment:
        sentiment = "negative"
    elif "positive" in raw_sentiment:
        sentiment = "positive"
    else:
        sentiment = "mixed"
    return {"label": str(label), "description": str(description), "sentiment": sentiment}


def label_theme(
    keyphrases: list[str],
    medoid_reviews: list[dict[str, Any]],
    client: LLMClient,
) -> dict[str, Any]:
    clean = _scrub_and_truncate(medoid_reviews)
    user = label_theme_prompt(keyphrases, clean)
    result = client.call_structured(SYSTEM_ANALYST, user, "label_theme", _THEME_SCHEMA)
    return _normalize_theme_response(result)


# ---------------------------------------------------------------------------
# Step 2: select_quotes  (with verbatim validator + one retry)
# ---------------------------------------------------------------------------

def select_quotes(
    theme_label: str,
    cluster_reviews: list[dict[str, Any]],
    client: LLMClient,
    cluster_id: str,
) -> list[Quote]:
    if not cluster_reviews:
        log.warning("quote_selection_empty_cluster", cluster_id=cluster_id)
        return []

    # Cap to 30 reviews for the LLM prompt — sort by rating variance for diversity
    _sample = sorted(cluster_reviews, key=lambda r: abs(r.get("rating", 3) - 3), reverse=True)
    sample_reviews = _sample[:30]

    original_bodies = [r.get("body", "") for r in cluster_reviews]  # validate against ALL
    clean_reviews = _scrub_and_truncate(sample_reviews)
    bad_quotes: list[str] = []

    for attempt in range(2):
        if attempt == 0:
            user = select_quotes_prompt(theme_label, clean_reviews)
        else:
            user = select_quotes_retry_prompt(theme_label, clean_reviews, bad_quotes)

        result = client.call_structured(SYSTEM_ANALYST, user, "select_quotes", _QUOTES_SCHEMA)
        raw_quotes = result.get("quotes", [])
        valid: list[Quote] = []

        for q in raw_quotes:
            body = (q.get("body") or "").strip()
            if not body:
                continue

            # Validate against ORIGINAL (un-truncated) bodies — EC3-3
            if not _is_verbatim(body, original_bodies):
                log.warning(
                    "dropping_hallucinated_quote",
                    quote_preview=body[:50],
                    cluster_id=cluster_id,
                )
                bad_quotes.append(body)
                continue

            # Find the source review
            rev_idx = q.get("review_index", -1)
            source: Optional[dict[str, Any]] = None
            if 0 <= rev_idx < len(cluster_reviews):
                source = cluster_reviews[rev_idx]
            else:
                for r in cluster_reviews:
                    if _normalize_ws(body) in _normalize_ws(r.get("body", "")):
                        source = r
                        break

            if source is None:
                bad_quotes.append(body)
                continue

            valid.append(
                Quote(
                    id=hashlib.sha1(f"{cluster_id}{body}".encode()).hexdigest(),
                    theme_id=cluster_id,
                    body=scrub_pii(body),
                    review_id=source["id"],
                    rating=source.get("rating", 3),
                )
            )

        if valid:
            return valid

        if attempt == 0:
            log.warning("quote_selection_retry", cluster_id=cluster_id, bad_count=len(bad_quotes))

    log.warning("quote_selection_no_valid_quotes", cluster_id=cluster_id)
    return []


# ---------------------------------------------------------------------------
# Step 3: generate_action_ideas
# ---------------------------------------------------------------------------

def generate_action_ideas(
    product: str,
    themes: list[Theme],
    client: LLMClient,
) -> list[ActionIdea]:
    theme_dicts = [
        {
            "label":        t.label,
            "sentiment":    t.sentiment,
            "review_count": t.review_count,
            "description":  t.description,
            "id":           t.id,
        }
        for t in themes
    ]
    user = generate_action_ideas_prompt(product, theme_dicts)
    result = client.call_structured(SYSTEM_ANALYST, user, "generate_action_ideas", _ACTION_IDEAS_SCHEMA)

    ideas: list[ActionIdea] = []
    for i, item in enumerate(result.get("action_ideas", [])[:5]):
        ideas.append(
            ActionIdea(
                id=hashlib.sha1(f"{product}action{i}{item.get('title','')}".encode()).hexdigest(),
                title=item.get("title", ""),
                description=item.get("description", ""),
                theme_ids=item.get("theme_ids", []),
            )
        )
    return ideas


# ---------------------------------------------------------------------------
# Step 4: generate_what_this_solves
# ---------------------------------------------------------------------------

def generate_what_this_solves(
    product: str,
    themes: list[Theme],
    client: LLMClient,
) -> list[AudienceValue]:
    theme_dicts = [{"label": t.label, "description": t.description} for t in themes]
    user = generate_what_this_solves_prompt(product, theme_dicts)
    result = client.call_structured(SYSTEM_ANALYST, user, "generate_what_this_solves", _WHAT_SOLVES_SCHEMA)

    return [
        AudienceValue(
            audience=item.get("audience", ""),
            value=item.get("value", ""),
        )
        for item in result.get("what_this_solves", [])
        if item.get("audience") and item.get("value")
    ]


# ---------------------------------------------------------------------------
# Top-level orchestration
# ---------------------------------------------------------------------------

def summarize_pulse(
    conn: sqlite3.Connection,
    run_id: str,
    product_key: str,
    window: Window,
    client: LLMClient,
    max_themes: int = 3,
    summaries_dir: Optional[Path] = None,
) -> PulseSummary:
    """Full Phase 3 pipeline for one run.

    Persists PulseSummary JSON and updates runs.status / runs.metrics_json.
    Raises PulseCostExceeded (with partial_themes) if the cost cap is hit.
    """
    # --- Load clusters ---
    cluster_rows = conn.execute(
        "SELECT * FROM clusters WHERE run_id = ? ORDER BY cluster_label",
        (run_id,),
    ).fetchall()

    if not cluster_rows:
        raise ValueError(f"No clusters found for run {run_id!r}. Run `pulse cluster` first.")

    # --- Load reviews for window ---
    review_rows = conn.execute(
        """SELECT id, body, rating, title
           FROM reviews
           WHERE product_key = ?
             AND DATE(posted_at) BETWEEN ? AND ?""",
        (product_key, window.start.isoformat(), window.end.isoformat()),
    ).fetchall()
    review_map: dict[str, dict[str, Any]] = {r["id"]: dict(r) for r in review_rows}

    # --- Stats ---
    all_ratings = [r["rating"] for r in review_rows]
    avg_rating = sum(all_ratings) / len(all_ratings) if all_ratings else 0.0
    stats = PulseStats(total_reviews=len(review_rows), avg_rating=round(avg_rating, 2))

    # --- Per-cluster LLM calls ---
    themes: list[Theme] = []
    all_quotes: list[Quote] = []

    for cluster_row in cluster_rows:
        cluster_id   = cluster_row["id"]
        review_ids   = json.loads(cluster_row["review_ids_json"])
        keyphrases   = json.loads(cluster_row["keyphrases_json"])
        rep_ids      = json.loads(cluster_row["representative_review_ids_json"])

        cluster_reviews = [review_map[rid] for rid in review_ids if rid in review_map]
        if not cluster_reviews:
            log.warning("cluster_no_reviews", cluster_id=cluster_id)
            continue

        medoid_reviews = [review_map[rid] for rid in rep_ids if rid in review_map][:3]

        # label_theme — PulseCostExceeded propagates with partial_themes accumulated so far
        try:
            theme_data = label_theme(keyphrases, medoid_reviews, client)
        except PulseCostExceeded as exc:
            exc.partial_themes = themes
            _persist_partial(conn, run_id, themes, client.metrics, summaries_dir)
            raise

        theme = Theme(
            id=cluster_id,
            rank=0,
            label=theme_data["label"],
            description=theme_data["description"],
            sentiment=theme_data["sentiment"],
            review_count=len(review_ids),
            representative_review_ids=rep_ids,
        )
        themes.append(theme)

        # select_quotes
        try:
            quotes = select_quotes(theme.label, cluster_reviews, client, cluster_id)
        except PulseCostExceeded as exc:
            exc.partial_themes = themes
            _persist_partial(conn, run_id, themes, client.metrics, summaries_dir)
            raise
        all_quotes.extend(quotes)

    # --- Rank and cap themes ---
    themes.sort(key=lambda t: t.review_count * _SENTIMENT_WEIGHT.get(t.sentiment, 1.0), reverse=True)
    top_themes = themes[:max_themes]
    for rank, t in enumerate(top_themes, 1):
        t.rank = rank

    top_ids = {t.id for t in top_themes}
    top_quotes = [q for q in all_quotes if q.theme_id in top_ids]

    # --- Cross-cluster calls ---
    action_ideas = generate_action_ideas(product_key, top_themes, client)
    what_this_solves = generate_what_this_solves(product_key, top_themes, client)

    summary = PulseSummary(
        product=product_key,
        window=window,
        stats=stats,
        top_themes=top_themes,
        quotes=top_quotes,
        action_ideas=action_ideas,
        what_this_solves=what_this_solves,
    )

    # --- Persist ---
    _persist_summary(conn, run_id, summary, client.metrics, summaries_dir)
    log.info(
        "summarize_complete",
        run_id=run_id,
        themes=len(top_themes),
        quotes=len(top_quotes),
        llm_calls=client.metrics.call_count,
        cost_usd=round(client.metrics.total_cost_usd, 6),
    )
    return summary


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def _persist_summary(
    conn: sqlite3.Connection,
    run_id: str,
    summary: PulseSummary,
    metrics: RunMetrics,
    summaries_dir: Optional[Path],
) -> None:
    if summaries_dir:
        summaries_dir.mkdir(parents=True, exist_ok=True)
        out = summaries_dir / f"{run_id}.json"
        out.write_text(summary.model_dump_json(indent=2), encoding="utf-8")
        log.info("summary_written", path=str(out))

    with conn:
        conn.execute(
            "UPDATE runs SET status = 'summarized', metrics_json = ? WHERE id = ?",
            (json.dumps(metrics.as_dict()), run_id),
        )


def _persist_partial(
    conn: sqlite3.Connection,
    run_id: str,
    partial_themes: list[Theme],
    metrics: RunMetrics,
    summaries_dir: Optional[Path],
) -> None:
    if summaries_dir and partial_themes:
        summaries_dir.mkdir(parents=True, exist_ok=True)
        out = summaries_dir / f"{run_id}_partial.json"
        data = {"partial_themes": [t.model_dump() for t in partial_themes]}
        out.write_text(json.dumps(data, indent=2), encoding="utf-8")
        log.warning("partial_summary_written", path=str(out))

    with conn:
        conn.execute(
            "UPDATE runs SET status = 'summarize_failed', metrics_json = ? WHERE id = ?",
            (json.dumps(metrics.as_dict()), run_id),
        )
