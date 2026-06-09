"""App Store review ingestion via the iTunes RSS customer-reviews feed."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Optional

import httpx
import structlog

from agent.config import ProductConfig
from agent.models import RawReview

log = structlog.get_logger()

_RSS_URL = (
    "https://itunes.apple.com/{country}/rss/customerreviews"
    "/page={page}/id={appstore_id}/sortby=mostrecent/json"
)


def _review_id(external_id: str) -> str:
    return hashlib.sha1(f"appstore{external_id}".encode()).hexdigest()


def _parse_entry(entry: dict, product_key: str, country: str) -> Optional[RawReview]:
    """Parse one iTunes RSS entry dict into a RawReview.

    Entries without `im:rating` are app-info rows, not reviews — skip them.
    """
    if "im:rating" not in entry:
        return None
    try:
        external_id = entry["id"]["label"]
        body = (entry.get("content") or {}).get("label") or ""
        title_label = (entry.get("title") or {}).get("label")
        rating_str = entry["im:rating"]["label"]
        version = (entry.get("im:version") or {}).get("label")
        updated_str = (entry.get("updated") or {}).get("label", "")

        try:
            posted_at = datetime.fromisoformat(updated_str.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            posted_at = datetime.now(timezone.utc)

        return RawReview(
            id=_review_id(external_id),
            product_key=product_key,
            source="appstore",
            rating=max(1, min(5, int(rating_str))),
            title=title_label,
            body=body,
            posted_at=posted_at,
            version=version,
            language="en",
            country=country.upper(),
        )
    except Exception as exc:
        log.warning("appstore_parse_error", error=str(exc))
        return None


def fetch_appstore_reviews(
    product: ProductConfig,
    country: str = "in",
    client: Optional[httpx.Client] = None,
) -> list[RawReview]:
    """Fetch up to 10 pages of App Store reviews for *product*.

    Returns an empty list (no exception) if the product has no appstore_id.
    Raises httpx.TimeoutException on network timeout so the caller can log
    and surface the partial result.
    """
    if not product.appstore_id:
        log.info("appstore_skipped_no_id", product=product.key)
        return []

    own_client = client is None
    if own_client:
        client = httpx.Client(timeout=30.0)

    reviews: list[RawReview] = []
    try:
        for page in range(1, 11):
            url = _RSS_URL.format(
                country=country,
                page=page,
                appstore_id=product.appstore_id,
            )
            try:
                resp = client.get(url)
                resp.raise_for_status()
                data = resp.json()
            except httpx.TimeoutException:
                log.error("appstore_timeout", product=product.key, page=page)
                raise
            except Exception as exc:
                log.error("appstore_fetch_error", product=product.key, page=page, error=str(exc))
                break

            entries = data.get("feed", {}).get("entry", [])
            if not entries:
                log.debug("appstore_no_more_entries", product=product.key, page=page)
                break

            for entry in entries:
                review = _parse_entry(entry, product.key, country)
                if review:
                    reviews.append(review)
    finally:
        if own_client:
            client.close()

    if not reviews:
        log.warning(
            "appstore_zero_reviews",
            product=product.key,
            country=country,
        )

    log.info("appstore_fetched", product=product.key, count=len(reviews))
    return reviews
