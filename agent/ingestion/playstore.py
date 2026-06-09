"""Play Store review ingestion via google-play-scraper."""

from __future__ import annotations

import hashlib
import time
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from typing import Any

import structlog

from agent.config import ProductConfig
from agent.models import RawReview

log = structlog.get_logger()

_MAX_RETRIES = 3
_BACKOFF_BASE = 2.0
_BATCH_SIZE = 200
_MAX_REVIEWS = 5000  # hard cap to avoid runaway pagination


def _review_id(external_id: str) -> str:
    return hashlib.sha1(f"playstore{external_id}".encode()).hexdigest()


def _parse_item(item: dict[str, Any], product_key: str) -> RawReview | None:
    try:
        external_id = item["reviewId"]
        body = item.get("content", "") or ""
        score = item.get("score", 3)
        at = item.get("at")

        if isinstance(at, datetime):
            posted_at = at if at.tzinfo else at.replace(tzinfo=UTC)
        else:
            posted_at = datetime.now(UTC)

        return RawReview(
            id=_review_id(external_id),
            product_key=product_key,
            source="playstore",
            rating=max(1, min(5, int(score))),
            body=body,
            posted_at=posted_at,
            version=item.get("appVersion"),
            language="en",
            country="IN",
        )
    except Exception as exc:
        log.warning("playstore_parse_error", error=str(exc))
        return None


def _fetch_batch(
    reviews_fn: Callable[..., Any],
    kwargs: dict[str, Any],
    product_key: str,
) -> tuple[list[Any], Any]:
    """Fetch one batch with exponential-backoff retry. Returns (items, next_token)."""
    for attempt in range(_MAX_RETRIES):
        try:
            result, token = reviews_fn(**kwargs)
            return result, token
        except Exception as exc:
            err_str = str(exc).lower()
            is_rate_limit = "429" in err_str or "rate" in err_str
            if is_rate_limit and attempt < _MAX_RETRIES - 1:
                wait = _BACKOFF_BASE ** (attempt + 1)
                log.warning("playstore_rate_limited", product=product_key, retry_in=wait)
                time.sleep(wait)
                continue
            if is_rate_limit:
                log.error("playstore_rate_limit_exceeded", product=product_key)
            else:
                log.error("playstore_fetch_error", product=product_key, error=str(exc))
            raise
    return [], None  # unreachable but satisfies type checker


def fetch_playstore_reviews(
    product: ProductConfig,
    weeks: int = 10,
    _reviews_fn: Callable[..., Any] | None = None,
) -> list[RawReview]:
    """Paginate through Play Store reviews until *weeks* weeks back or _MAX_REVIEWS hit.

    Uses continuation_token to walk backwards in time, stopping as soon as a
    review's posted_at falls before the cutoff. This means for active apps like
    Groww (200 reviews/day) we may fetch 10-20+ pages to cover 10 weeks.

    *_reviews_fn* is injectable for unit tests.
    """
    if not product.play_package:
        log.info("playstore_skipped_no_package", product=product.key)
        return []

    if _reviews_fn is None:
        try:
            from google_play_scraper import Sort  # type: ignore[import-untyped]
            from google_play_scraper import reviews as gps_reviews

            reviews_fn: Callable[..., Any] = gps_reviews
            sort_arg: Any = Sort.NEWEST
        except ImportError:
            log.error("google_play_scraper_not_installed")
            return []
    else:
        reviews_fn = _reviews_fn
        sort_arg = None

    cutoff = datetime.now(UTC) - timedelta(weeks=weeks)
    all_reviews: list[RawReview] = []
    continuation_token: Any = None
    page = 0

    while len(all_reviews) < _MAX_REVIEWS:
        page += 1
        kwargs: dict[str, Any] = {
            "app_id": product.play_package,
            "lang": "en",
            "country": "in",
            "count": _BATCH_SIZE,
        }
        if sort_arg is not None:
            kwargs["sort"] = sort_arg
        if continuation_token is not None:
            kwargs["continuation_token"] = continuation_token

        log.debug("playstore_fetching_page", product=product.key, page=page, fetched_so_far=len(all_reviews))

        try:
            batch, continuation_token = _fetch_batch(reviews_fn, kwargs, product.key)
        except Exception:
            log.warning("playstore_partial_ingestion", product=product.key, fetched=len(all_reviews))
            break

        if not batch:
            log.debug("playstore_no_more_results", product=product.key, page=page)
            break

        reached_cutoff = False
        for item in batch:
            at = item.get("at")
            if isinstance(at, datetime):
                item_dt = at if at.tzinfo else at.replace(tzinfo=UTC)
                if item_dt < cutoff:
                    reached_cutoff = True
                    continue  # skip but keep scanning batch (not all are sorted perfectly)
            review = _parse_item(item, product.key)
            if review:
                all_reviews.append(review)

        # Stop paginating once the batch contained reviews older than our cutoff
        if reached_cutoff:
            log.debug("playstore_reached_cutoff", product=product.key, page=page)
            break

        # No more pages available
        if continuation_token is None:
            break

    log.info(
        "playstore_fetched",
        product=product.key,
        pages=page,
        count=len(all_reviews),
        cutoff=cutoff.date().isoformat(),
    )
    return all_reviews
