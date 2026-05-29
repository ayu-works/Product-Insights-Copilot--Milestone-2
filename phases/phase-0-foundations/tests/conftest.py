import pytest
from pathlib import Path


@pytest.fixture()
def tmp_db(tmp_path: Path) -> Path:
    """Return a path to a fresh, empty SQLite database in a temp directory."""
    return tmp_path / "pulse_test.db"


@pytest.fixture()
def products_yaml(tmp_path: Path) -> Path:
    """Write a minimal products.yaml to a temp directory and return its path."""
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
