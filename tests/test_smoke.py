"""Phase 0 smoke tests — carried forward from foundations."""

from pathlib import Path

import pytest

from agent.config import ProductConfig, get_product, load_products
from agent.helpers import iso_week_to_dates, make_run_id
from agent.storage import init_db, table_names


def test_init_db_creates_all_tables(tmp_db: Path) -> None:
    init_db(tmp_db)
    expected = {"products", "reviews", "review_embeddings", "runs", "themes", "clusters"}
    assert table_names(tmp_db) == expected


def test_init_db_is_idempotent(tmp_db: Path) -> None:
    init_db(tmp_db)
    init_db(tmp_db)
    assert table_names(tmp_db) == {"products", "reviews", "review_embeddings", "runs", "themes", "clusters"}


def test_run_id_is_deterministic() -> None:
    assert make_run_id("groww", "2026-W16") == make_run_id("groww", "2026-W16")


def test_run_id_is_40_chars() -> None:
    rid = make_run_id("groww", "2026-W16")
    assert len(rid) == 40
    assert all(c in "0123456789abcdef" for c in rid)


def test_iso_week_to_dates_boundaries() -> None:
    from datetime import date
    monday, sunday = iso_week_to_dates("2026-W16")
    assert monday == date(2026, 4, 13)
    assert sunday == date(2026, 4, 19)


def test_load_products_from_yaml(products_yaml: Path) -> None:
    products = load_products(products_yaml)
    assert len(products) == 1
    assert products[0].key == "groww"


def test_get_product_found(products_yaml: Path) -> None:
    p = get_product("groww", products_yaml)
    assert isinstance(p, ProductConfig)
    assert p.display == "Groww"


def test_get_product_not_found_raises(products_yaml: Path) -> None:
    with pytest.raises(KeyError, match="kuvera"):
        get_product("kuvera", products_yaml)
