"""Phase 0 smoke tests — exit criteria for Foundations & Scaffolding."""

from pathlib import Path

import pytest

from agent.helpers import make_run_id, iso_week_to_dates, current_iso_week
from agent.storage import init_db, table_names
from agent.config import load_products, get_product, ProductConfig


# ---------------------------------------------------------------------------
# E0-2: Database initialisation
# ---------------------------------------------------------------------------

def test_init_db_creates_all_tables(tmp_db: Path) -> None:
    init_db(tmp_db)
    expected = {"products", "reviews", "review_embeddings", "runs", "themes"}
    assert table_names(tmp_db) == expected


def test_init_db_is_idempotent(tmp_db: Path) -> None:
    init_db(tmp_db)
    init_db(tmp_db)  # second call must not raise or destroy data
    assert table_names(tmp_db) == {"products", "reviews", "review_embeddings", "runs", "themes"}


# ---------------------------------------------------------------------------
# E0-4: run_id determinism
# ---------------------------------------------------------------------------

def test_run_id_is_deterministic() -> None:
    assert make_run_id("groww", "2026-W16") == make_run_id("groww", "2026-W16")


def test_run_id_is_40_chars() -> None:
    rid = make_run_id("groww", "2026-W16")
    assert len(rid) == 40
    assert all(c in "0123456789abcdef" for c in rid)


def test_run_id_differs_by_week() -> None:
    assert make_run_id("groww", "2026-W16") != make_run_id("groww", "2026-W17")


def test_run_id_differs_by_product() -> None:
    assert make_run_id("groww", "2026-W16") != make_run_id("indmoney", "2026-W16")


# ---------------------------------------------------------------------------
# E0-5: ISO-week window helper
# ---------------------------------------------------------------------------

def test_iso_week_to_dates_boundaries() -> None:
    from datetime import date
    monday, sunday = iso_week_to_dates("2026-W16")
    assert monday == date(2026, 4, 13)
    assert sunday == date(2026, 4, 19)
    assert (sunday - monday).days == 6


def test_current_iso_week_returns_previous_week() -> None:
    from datetime import date, timedelta
    today = date(2026, 4, 20)  # a Monday in week W17
    result = current_iso_week(today=today)
    # last complete week is W16
    assert result == "2026-W16"


# ---------------------------------------------------------------------------
# E0-3: Config loading
# ---------------------------------------------------------------------------

def test_load_products_from_yaml(products_yaml: Path) -> None:
    products = load_products(products_yaml)
    assert len(products) == 2
    keys = {p.key for p in products}
    assert keys == {"groww", "indmoney"}


def test_load_products_returns_empty_for_missing_file(tmp_path: Path) -> None:
    result = load_products(tmp_path / "nonexistent.yaml")
    assert result == []


def test_get_product_found(products_yaml: Path) -> None:
    p = get_product("groww", products_yaml)
    assert isinstance(p, ProductConfig)
    assert p.display == "Groww"


def test_get_product_not_found_raises(products_yaml: Path) -> None:
    with pytest.raises(KeyError, match="kuvera"):
        get_product("kuvera", products_yaml)


def test_product_key_is_lowercased(products_yaml: Path) -> None:
    products = load_products(products_yaml)
    for p in products:
        assert p.key == p.key.lower()


# ---------------------------------------------------------------------------
# Models smoke test
# ---------------------------------------------------------------------------

def test_raw_review_model() -> None:
    from datetime import datetime, timezone
    from agent.models import RawReview

    review = RawReview(
        id="abc123",
        product_key="groww",
        source="playstore",
        rating=4,
        body="Great app, fast execution",
        posted_at=datetime(2026, 4, 15, tzinfo=timezone.utc),
        language="en",
        country="IN",
    )
    assert review.source == "playstore"
    assert review.title is None


def test_pulse_summary_requires_top_themes() -> None:
    from datetime import date
    from agent.models import PulseSummary, Window, PulseStats
    import pydantic

    with pytest.raises(pydantic.ValidationError):
        # top_themes is required
        PulseSummary(  # type: ignore[call-arg]
            product="groww",
            window=Window(start=date(2026, 4, 13), end=date(2026, 4, 19), weeks=1),
            stats=PulseStats(total_reviews=100, avg_rating=4.2),
            # missing top_themes, quotes, action_ideas, what_this_solves
        )
