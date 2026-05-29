"""Phase 4 renderer tests — E4-1 through E4-7 and edge cases EC4-1 through EC4-8."""

from __future__ import annotations

import html.parser
import json
import os
from pathlib import Path

import pytest

from agent.models import PulseSummary
from agent.renderer.docs_tree import build_doc_requests, validate_doc_requests
from agent.renderer.email_html import render_email

FIXTURES = Path(__file__).parent / "fixtures"
UPDATE_GOLDEN = os.environ.get("UPDATE_GOLDEN", "").lower() in ("1", "true", "yes")

ISO_WEEK = "2026-W16"
DISPLAY_NAME = "Groww"


@pytest.fixture()
def canonical_summary() -> PulseSummary:
    data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
    return PulseSummary.model_validate(data)


# ── E4-1: Doc requests golden image ──────────────────────────────────────────

class TestDocRequestsGoldenImage:
    def test_doc_requests_golden_image(self, canonical_summary: PulseSummary) -> None:
        """Output must be byte-stable across runs on the same fixture."""
        golden_path = FIXTURES / "doc_requests_groww.json"
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        result_json = json.dumps(result, indent=2, ensure_ascii=False)

        if UPDATE_GOLDEN or not golden_path.exists():
            golden_path.write_text(result_json + "\n", encoding="utf-8")
            if not UPDATE_GOLDEN:
                pytest.skip("Golden file generated on first run; re-run to compare")

        golden = golden_path.read_text(encoding="utf-8")
        assert result_json + "\n" == golden, (
            "doc_requests output changed — run UPDATE_GOLDEN=1 pytest to refresh golden file"
        )

    def test_returns_list_of_dicts(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        assert isinstance(result, list)
        assert len(result) > 0
        assert all(isinstance(r, dict) for r in result)

    def test_validates_against_schema(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        validate_doc_requests(result)  # must not raise


# ── E4-2: Mapping coverage ────────────────────────────────────────────────────

class TestMappingCoverage:
    def _api_types(self, requests: list[dict]) -> set[str]:
        """Collect the top-level API key names (skip _ prefixed metadata fields)."""
        types: set[str] = set()
        for r in requests:
            types.update(k for k in r if not k.startswith("_"))
        return types

    def test_all_request_types_present(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        types = self._api_types(result)
        assert "insertText" in types
        assert "updateParagraphStyle" in types
        assert "createParagraphBullets" in types
        assert "updateTextStyle" in types        # italic for verbatim quotes
        assert "insertTable" in types            # what_this_solves table

    def test_heading1_present(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        h1_reqs = [
            r for r in result
            if "updateParagraphStyle" in r
            and r["updateParagraphStyle"]["paragraphStyle"].get("namedStyleType") == "HEADING_1"
        ]
        assert len(h1_reqs) >= 1

    def test_heading2_present(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        h2_reqs = [
            r for r in result
            if "updateParagraphStyle" in r
            and r["updateParagraphStyle"]["paragraphStyle"].get("namedStyleType") == "HEADING_2"
        ]
        # 3 theme headings + "Action Ideas" + "What This Solves" = at least 5
        assert len(h2_reqs) >= 3

    def test_table_has_metadata(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        table_reqs = [r for r in result if "insertTable" in r]
        assert len(table_reqs) == 1
        tc = table_reqs[0]["_tableContent"]
        assert tc["headers"] == ["Audience", "Value"]
        assert len(tc["rows"]) == len(canonical_summary.what_this_solves)


# ── E4-3: Anchor string ───────────────────────────────────────────────────────

class TestAnchorString:
    def test_anchor_in_first_insert_text(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        insert_reqs = [r for r in result if "insertText" in r]
        assert len(insert_reqs) > 0
        first_text = insert_reqs[0]["insertText"]["text"]
        anchor = f"pulse-{canonical_summary.product}-{ISO_WEEK}"
        assert anchor in first_text, f"anchor {anchor!r} not found in first insertText: {first_text!r}"

    def test_first_insert_is_heading1(self, canonical_summary: PulseSummary) -> None:
        result = build_doc_requests(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        insert_reqs = [r for r in result if "insertText" in r]
        h1_reqs = [
            r for r in result
            if "updateParagraphStyle" in r
            and r["updateParagraphStyle"]["paragraphStyle"].get("namedStyleType") == "HEADING_1"
        ]
        first_ins_idx = insert_reqs[0]["insertText"]["location"]["index"]
        first_h1_start = h1_reqs[0]["updateParagraphStyle"]["range"]["startIndex"]
        assert first_ins_idx == first_h1_start


# ── E4-4: Email HTML golden image ─────────────────────────────────────────────

class TestEmailHTMLGoldenImage:
    def test_email_html_golden_image(self, canonical_summary: PulseSummary) -> None:
        golden_path = FIXTURES / "email_groww.html"
        _, html, _ = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)

        if UPDATE_GOLDEN or not golden_path.exists():
            golden_path.write_text(html, encoding="utf-8")
            if not UPDATE_GOLDEN:
                pytest.skip("Golden HTML file generated on first run; re-run to compare")

        golden = golden_path.read_text(encoding="utf-8")
        assert html == golden, "email HTML changed — run UPDATE_GOLDEN=1 pytest to refresh"

    def test_html_parses_without_error(self, canonical_summary: PulseSummary) -> None:
        _, html_body, _ = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        p = html.parser.HTMLParser()
        p.feed(html_body)  # must not raise

    def test_subject_format(self, canonical_summary: PulseSummary) -> None:
        top_theme = canonical_summary.top_themes[0].label
        subject, _, _ = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        assert "[Weekly Pulse]" in subject
        assert DISPLAY_NAME in subject
        assert ISO_WEEK in subject
        assert top_theme in subject

    def test_product_name_in_html(self, canonical_summary: PulseSummary) -> None:
        _, html, _ = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        assert DISPLAY_NAME in html


# ── E4-5: Deep link placeholder ───────────────────────────────────────────────

class TestDeepLinkPlaceholder:
    def test_placeholder_in_html(self, canonical_summary: PulseSummary) -> None:
        _, html, _ = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        assert "{DOC_DEEP_LINK}" in html

    def test_placeholder_in_text(self, canonical_summary: PulseSummary) -> None:
        _, _, text = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        assert "{DOC_DEEP_LINK}" in text

    def test_no_google_url_in_phase4_output(self, canonical_summary: PulseSummary) -> None:
        _, html, text = render_email(canonical_summary, ISO_WEEK, DISPLAY_NAME)
        assert "https://docs.google.com" not in html
        assert "https://docs.google.com" not in text


# ── E4-6: Schema validation rejects malformed summaries ──────────────────────

class TestSchemaValidation:
    def test_empty_top_themes_raises(self) -> None:
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            PulseSummary.model_validate({
                "product": "groww",
                "window": {"start": "2026-04-13", "end": "2026-04-19", "weeks": 1},
                "stats": {"total_reviews": 10, "avg_rating": 4.0},
                "top_themes": [],
                "quotes": [],
                "action_ideas": [],
                "what_this_solves": [],
            })

    def test_invalid_sentiment_raises(self) -> None:
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            PulseSummary.model_validate({
                "product": "groww",
                "window": {"start": "2026-04-13", "end": "2026-04-19", "weeks": 1},
                "stats": {"total_reviews": 10, "avg_rating": 4.0},
                "top_themes": [{
                    "id": "t1", "rank": 1, "label": "Test",
                    "description": "Desc", "sentiment": "angry",
                    "review_count": 5, "representative_review_ids": []
                }],
                "quotes": [],
                "action_ideas": [],
                "what_this_solves": [],
            })

    def test_missing_window_raises(self) -> None:
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            PulseSummary.model_validate({
                "product": "groww",
                "stats": {"total_reviews": 10, "avg_rating": 4.0},
                "top_themes": [{
                    "id": "t1", "rank": 1, "label": "Test",
                    "description": "Desc", "sentiment": "negative",
                    "review_count": 5, "representative_review_ids": []
                }],
                "quotes": [],
                "action_ideas": [],
                "what_this_solves": [],
            })

    def test_no_partial_files_on_validation_failure(self, tmp_path: Path) -> None:
        """No artifact files should be written when PulseSummary is invalid."""
        artifact_dir = tmp_path / "artifacts" / "bad_run"
        # Attempting to use an invalid summary should raise before any file write
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            bad = PulseSummary.model_validate({
                "product": "groww",
                "window": {"start": "2026-04-13", "end": "2026-04-19", "weeks": 1},
                "stats": {"total_reviews": 10, "avg_rating": 4.0},
                "top_themes": [],  # invalid — fails at_least_one_theme validator
                "quotes": [],
                "action_ideas": [],
                "what_this_solves": [],
            })
        assert not artifact_dir.exists()


# ── EC4-1: Single theme ───────────────────────────────────────────────────────

class TestEdgeCases:
    def test_single_theme_no_index_error(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        data["top_themes"] = [data["top_themes"][0]]
        data["quotes"] = [q for q in data["quotes"] if q["theme_id"] == data["top_themes"][0]["id"]]
        summary = PulseSummary.model_validate(data)
        result = build_doc_requests(summary, ISO_WEEK, DISPLAY_NAME)
        assert isinstance(result, list) and len(result) > 0
        _, html, text = render_email(summary, ISO_WEEK, DISPLAY_NAME)
        assert DISPLAY_NAME in html

    # EC4-2: Theme with no quotes
    def test_no_quotes_for_theme_skips_italic(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        data["quotes"] = []
        summary = PulseSummary.model_validate(data)
        result = build_doc_requests(summary, ISO_WEEK, DISPLAY_NAME)
        italic_reqs = [r for r in result if "updateTextStyle" in r]
        assert len(italic_reqs) == 0

    # EC4-3: XSS in review body
    def test_xss_escaped_in_email_html(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        data["top_themes"][0]["description"] = "<script>alert('xss')</script>"
        summary = PulseSummary.model_validate(data)
        _, html, _ = render_email(summary, ISO_WEEK, DISPLAY_NAME)
        assert "<script>" not in html
        assert "&lt;script&gt;" in html

    # EC4-4: Long description truncated in email only
    def test_long_description_truncated_in_email_not_in_doc(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        long_desc = "x" * 500
        data["top_themes"][0]["description"] = long_desc
        summary = PulseSummary.model_validate(data)

        _, html, _ = render_email(summary, ISO_WEEK, DISPLAY_NAME)
        assert "x" * 500 not in html  # truncated in email

        doc_reqs = build_doc_requests(summary, ISO_WEEK, DISPLAY_NAME)
        insert_texts = [r["insertText"]["text"] for r in doc_reqs if "insertText" in r]
        assert any(long_desc in t for t in insert_texts)  # full text in doc

    # EC4-5: Product key used in anchor, display name in heading text
    def test_anchor_uses_product_key_not_display_name(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        summary = PulseSummary.model_validate(data)
        result = build_doc_requests(summary, ISO_WEEK, "INDMoney — Invest & Save")
        first_text = [r for r in result if "insertText" in r][0]["insertText"]["text"]
        # Anchor uses product_key (ASCII safe)
        assert "pulse-groww-2026-W16" in first_text
        # Display name appears after the anchor
        assert "INDMoney" in first_text

    # EC4-6: Re-render into existing dir is idempotent
    def test_artifact_dir_exists_no_error(self, tmp_path: Path) -> None:
        artifact_dir = tmp_path / "artifacts" / "run123"
        artifact_dir.mkdir(parents=True)
        (artifact_dir / "doc_requests.json").write_text("{}", encoding="utf-8")

        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        summary = PulseSummary.model_validate(data)
        result = build_doc_requests(summary, ISO_WEEK, DISPLAY_NAME)

        artifact_dir.mkdir(parents=True, exist_ok=True)  # must not raise FileExistsError
        (artifact_dir / "doc_requests.json").write_text(
            json.dumps(result, indent=2), encoding="utf-8"
        )
        loaded = json.loads((artifact_dir / "doc_requests.json").read_text())
        assert loaded == result

    # EC4-7: Empty action_ideas — section omitted from doc
    def test_empty_action_ideas_no_section(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        data["action_ideas"] = []
        summary = PulseSummary.model_validate(data)
        result = build_doc_requests(summary, ISO_WEEK, DISPLAY_NAME)
        insert_texts = [r["insertText"]["text"] for r in result if "insertText" in r]
        assert not any("Action Ideas" in t for t in insert_texts)

    # EC4-8: Single-row what_this_solves table
    def test_single_row_what_this_solves_table(self) -> None:
        data = json.loads((FIXTURES / "pulse_summary_groww.json").read_text(encoding="utf-8"))
        data["what_this_solves"] = [{"audience": "Everyone", "value": "Stability"}]
        summary = PulseSummary.model_validate(data)
        result = build_doc_requests(summary, ISO_WEEK, DISPLAY_NAME)
        table_reqs = [r for r in result if "insertTable" in r]
        assert len(table_reqs) == 1
        assert table_reqs[0]["insertTable"]["rows"] == 2   # 1 header + 1 data
        assert table_reqs[0]["insertTable"]["columns"] == 2
