import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture()
def tmp_db(tmp_path: Path) -> Path:
    return tmp_path / "pulse_test.db"


@pytest.fixture()
def products_yaml(tmp_path: Path) -> Path:
    content = """
products:
  - key: groww
    display: "Groww"
    appstore_id: "1404871982"
    play_package: "com.nextbillion.groww"
    gmail_to: "test@example.com"
  - key: indmoney
    display: "INDMoney"
    play_package: "com.indwealth"
    gmail_to: "test@example.com"
"""
    path = tmp_path / "products.yaml"
    path.write_text(content, encoding="utf-8")
    return path


@pytest.fixture()
def appstore_fixture() -> dict:
    return json.loads((FIXTURES / "appstore_groww_page1.json").read_text(encoding="utf-8"))


@pytest.fixture()
def playstore_fixture() -> list:
    raw = json.loads((FIXTURES / "playstore_groww.json").read_text(encoding="utf-8"))
    for item in raw:
        if isinstance(item.get("at"), str):
            item["at"] = datetime.fromisoformat(item["at"]).replace(tzinfo=timezone.utc)
    return raw
