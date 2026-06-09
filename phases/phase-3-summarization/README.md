# Phase 3 — LLM Summarization

> **Snapshot:** `git checkout phase-3` · **Specs:** [evaluations](../../docs/phases/phase-3-summarization/evaluations.md) · [edge-cases](../../docs/phases/phase-3-summarization/edge-cases.md)

## What this phase added
Convert numeric clusters into named themes, verbatim quotes, and action ideas — with grounding guarantees:
- Pydantic response models for every LLM call; Groq (OpenAI-compatible `chat.completions` + `json_object`) or Anthropic structured JSON.
- `label_theme`, `select_quotes` (with a **verbatim validator** — every quote must be a whitespace-normalized substring of some `review.body`, else dropped/re-prompted once), `generate_action_ideas`, `summarize_pulse`.
- LLM client wrapper: retries, timeout, token/cost accounting persisted to `runs.metrics_json`, per-run hard cap.
- PII re-scrub before any LLM call.

## CLI introduced
```bash
uv run pulse summarize --run <run_id>   # writes data/summaries/{run_id}.json
```

## Exit criteria
- On the golden fixture, 3 themes produced; every quote passes the verbatim validator.
- Deterministic snapshot test with a mocked LLM — `PulseSummary` JSON is byte-stable.
- Cost cap triggers a controlled `PulseCostExceeded`, not a silent truncation.

## Where the code lives now
`agent/summarization/` (`client.py`, `pipeline.py`, `prompts.py`).
