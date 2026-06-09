from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, field_validator


class RawReview(BaseModel):
    id: str                              # sha1(source + external_id)
    product_key: str
    source: Literal["appstore", "playstore"]
    rating: int
    title: str | None = None
    body: str
    posted_at: datetime
    version: str | None = None
    language: str
    country: str


class Window(BaseModel):
    start: date
    end: date
    weeks: int


class PulseStats(BaseModel):
    total_reviews: int
    avg_rating: float
    rating_delta_vs_prev: float | None = None


class Theme(BaseModel):
    id: str
    rank: int
    label: str
    description: str
    sentiment: Literal["negative", "mixed", "positive"]
    review_count: int
    representative_review_ids: list[str]


class Quote(BaseModel):
    id: str
    theme_id: str
    body: str
    review_id: str
    rating: int


class ActionIdea(BaseModel):
    id: str
    title: str
    description: str
    theme_ids: list[str]


class AudienceValue(BaseModel):
    audience: str
    value: str


class PulseSummary(BaseModel):
    product: str
    window: Window
    stats: PulseStats
    top_themes: list[Theme]
    quotes: list[Quote]
    action_ideas: list[ActionIdea]
    what_this_solves: list[AudienceValue]

    @field_validator("top_themes")
    @classmethod
    def at_least_one_theme(cls, v: list[Theme]) -> list[Theme]:
        if len(v) < 1:
            raise ValueError("PulseSummary must have at least one theme")
        return v
