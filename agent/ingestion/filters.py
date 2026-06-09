"""Review filtering and PII scrubbing applied before DB persistence."""

from __future__ import annotations

import re

import structlog

log = structlog.get_logger()

# ---------------------------------------------------------------------------
# PII patterns
# ---------------------------------------------------------------------------

_EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
    re.UNICODE,
)
_AADHAAR_RE = re.compile(
    r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b",
    re.UNICODE,
)
_PHONE_RE = re.compile(
    r"(\+91[-\s]?)?[6-9]\d{9}",
    re.UNICODE,
)

# ---------------------------------------------------------------------------
# Emoji pattern — covers all major Unicode emoji blocks
# ---------------------------------------------------------------------------

_EMOJI_RE = re.compile(
    "["
    "\U00002600-\U000027BF"   # Misc Symbols + Dingbats
    "\U0001F300-\U0001F5FF"   # Symbols & Pictographs
    "\U0001F600-\U0001F64F"   # Emoticons
    "\U0001F680-\U0001F6FF"   # Transport & Map
    "\U0001F700-\U0001FAFF"   # Extended symbols
    "\U00002702-\U000027B0"   # Dingbats subset
    "\U0000FE00-\U0000FE0F"   # Variation Selectors
    "\U00020000-\U0002A6DF"   # CJK Extension B
    "\U0002A700-\U0002CEAF"   # CJK Extension C/D/E
    "\U0002CEB0-\U0002EBEF"   # CJK Extension F
    "\U00030000-\U0003134F"   # CJK Extension G
    "]+",
    flags=re.UNICODE,
)


def scrub_pii(text: str) -> str:
    """Replace PII tokens with placeholder labels. Order: Aadhaar before phone."""
    text = _EMAIL_RE.sub("[EMAIL]", text)
    text = _AADHAAR_RE.sub("[AADHAAR]", text)
    text = _PHONE_RE.sub("[PHONE]", text)
    return text


def has_emoji(text: str) -> bool:
    return bool(_EMOJI_RE.search(text))


def is_english(text: str) -> bool:
    """Return True if the text is detected as English, False otherwise.

    Falls back to True (keep) on detection failure to avoid false positives.
    """
    stripped = text.strip()
    if not stripped:
        return True
    try:
        from langdetect import detect, LangDetectException  # type: ignore[import-untyped]

        return detect(stripped) == "en"
    except Exception:
        return True


def word_count(text: str) -> int:
    return len(text.split())


def should_keep(body: str) -> bool:
    """Return True if a review body passes all ingestion-time quality filters."""
    if has_emoji(body):
        log.debug("review_filtered_emoji")
        return False
    if word_count(body) < 4:
        log.debug("review_filtered_short", words=word_count(body))
        return False
    if not is_english(body):
        log.debug("review_filtered_language")
        return False
    return True
