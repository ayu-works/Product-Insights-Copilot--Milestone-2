"""Prompt templates for each LLM call in Phase 3."""

from __future__ import annotations

SYSTEM_ANALYST = (
    "You are a senior product analyst reviewing mobile app user feedback. "
    "Your job is to identify patterns, themes, and actionable insights from app reviews. "
    "Be concise, factual, and grounded only in the provided review text. "
    "Never fabricate information not present in the reviews."
)


def label_theme_prompt(keyphrases: list[str], medoid_reviews: list[dict]) -> str:
    kp_text = ", ".join(keyphrases) if keyphrases else "(none)"
    reviews_text = "\n".join(
        f"  [{r.get('rating', '?')} stars] {r.get('body', '')[:400]}"
        for r in medoid_reviews[:5]
    )
    return (
        f"Analyse the following representative app reviews and keyphrases.\n\n"
        f"Keyphrases: {kp_text}\n\n"
        f"Representative reviews:\n{reviews_text}\n\n"
        f"Return ONLY a JSON object with EXACTLY these three keys:\n"
        f'  "label"       - a concise 2-5 word theme name (string)\n'
        f'  "description" - 1-2 sentence description of what users are experiencing (string)\n'
        f'  "sentiment"   - MUST be exactly one of: "negative", "mixed", "positive" (string)\n\n'
        f"Example: {{\"label\": \"App Crashes on Login\", "
        f"\"description\": \"Users report the app crashes immediately after login.\", "
        f"\"sentiment\": \"negative\"}}"
    )


def select_quotes_prompt(theme_label: str, reviews: list[dict]) -> str:
    numbered = "\n".join(
        f"[{i}] [{r.get('rating', '?')} stars] {r.get('body', '')[:350]}"
        for i, r in enumerate(reviews)
    )
    return (
        f'Select 2-3 quotes from the reviews below that best illustrate: "{theme_label}".\n\n'
        f"CRITICAL: Copy text CHARACTER-FOR-CHARACTER from a review. No changes at all.\n\n"
        f"Reviews:\n{numbered}\n\n"
        f"Return ONLY a JSON object with EXACTLY this structure:\n"
        f'{{"quotes": [{{"body": "exact copied text", "review_index": 0}}]}}'
    )


def select_quotes_retry_prompt(theme_label: str, reviews: list[dict], bad_quotes: list[str]) -> str:
    bad_text = "\n".join(f'  - "{q[:80]}"' for q in bad_quotes)
    return (
        f"{select_quotes_prompt(theme_label, reviews)}\n\n"
        f"NOTE: The following quotes from your previous attempt were NOT found verbatim "
        f"in any review — do not return them again:\n{bad_text}\n"
        f"Copy text character-for-character from the review list above."
    )


def generate_action_ideas_prompt(product: str, themes: list[dict]) -> str:
    themes_text = "\n".join(
        f"  - id={t['id']}  label={t['label']}  sentiment={t['sentiment']}  "
        f"reviews={t['review_count']}  desc={t['description']}"
        for t in themes
    )
    return (
        f"Based on these user-reported themes from {product} app reviews:\n\n"
        f"{themes_text}\n\n"
        f"Generate 2-3 concrete product improvement actions.\n\n"
        f"Return ONLY a JSON object with EXACTLY this structure:\n"
        f'{{"action_ideas": [{{"title": "short title", "description": "what to do and why", '
        f'"theme_ids": ["id_from_above"]}}]}}\n\n'
        f"Use the exact id values from above for theme_ids."
    )


def generate_what_this_solves_prompt(product: str, themes: list[dict]) -> str:
    themes_text = "\n".join(
        f"  - {t['label']}: {t['description']}" for t in themes
    )
    return (
        f"Given the top themes from {product} app reviews:\n\n"
        f"{themes_text}\n\n"
        f"For 2-3 distinct user segments (e.g. 'New investors', 'Active traders'), "
        f"explain the value that fixing these issues delivers.\n\n"
        f"Return ONLY a JSON object with EXACTLY this structure:\n"
        f'{{"what_this_solves": [{{"audience": "segment name", "value": "benefit to them"}}]}}'
    )
