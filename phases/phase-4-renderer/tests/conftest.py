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
"""
    path = tmp_path / "products.yaml"
    path.write_text(content, encoding="utf-8")
    return path
