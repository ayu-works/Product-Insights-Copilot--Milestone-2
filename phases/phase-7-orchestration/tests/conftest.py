import json
from pathlib import Path

import pytest

from agent.models import PulseSummary
from agent.renderer.docs_tree import build_doc_requests

FIXTURES = Path(__file__).parent / "fixtures"

ISO_WEEK = "2026-W16"
ANCHOR = f"pulse-groww-{ISO_WEEK}"
DOC_ID = "doc_test_abc123"


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


@pytest.fixture()
def pulse_summary() -> PulseSummary:
    data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
    return PulseSummary.model_validate(data)


@pytest.fixture()
def doc_requests(pulse_summary: PulseSummary) -> list[dict]:
    return build_doc_requests(pulse_summary, ISO_WEEK, "Groww")
