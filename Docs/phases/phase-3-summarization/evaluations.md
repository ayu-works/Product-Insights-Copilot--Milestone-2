# Phase 3 — LLM Summarization: Evaluations

## How We Prove It Works

---

### E3-1: Theme Generation on Golden Fixture

**What to run:**
```bash
pytest tests/test_summarization.py::test_theme_generation_golden -v
```

**Setup:** Uses the golden fixture clusters from Phase 2 with a mocked LLM (vcr.py cassette).

**Pass condition:**
- Exactly 3 `Theme` objects are produced.
- Each `Theme` has: non-empty `label`, non-empty `description`, valid `sentiment` (`negative`/`mixed`/`positive`), `review_count > 0`.
- Themes are ranked by `review_count × |sentiment_weight|` (negative = 1.5, mixed = 1.0, positive = 0.8).

---

### E3-2: Verbatim Quote Validator

**What to run:**
```bash
pytest tests/test_summarization.py::test_verbatim_quote_validator -v
```

**Test cases:**
1. LLM returns a quote that is an exact substring of a review body → **kept**.
2. LLM returns a quote that differs by whitespace normalisation only → **kept** (normalise both sides before comparison).
3. LLM returns a hallucinated quote not found in any review → **dropped**, re-prompted once.
4. After re-prompt, LLM returns another hallucinated quote → **dropped**, zero quotes for this cluster (not an error).

**Pass condition:**
- No hallucinated quotes survive to `PulseSummary.quotes`.
- Re-prompt is attempted exactly once per failed cluster (no infinite loops).
- Log entry for each dropped quote: `"Dropping hallucinated quote: '{quote[:50]}...'"`.

---

### E3-3: Deterministic Snapshot with Mocked LLM

**What to run:**
```bash
pytest tests/test_summarization.py::test_deterministic_snapshot -v
```

**Pass condition:**
- With a vcr.py cassette replaying fixed LLM responses, `summarize_pulse()` produces a `PulseSummary` whose JSON serialisation is byte-identical across runs.
- No randomness introduced outside the LLM (which is mocked).

---

### E3-4: Cost Cap Enforcement

**What to run:**
```bash
pytest tests/test_summarization.py::test_cost_cap_triggers -v
```

**Setup:** Set `PULSE_MAX_TOKENS_PER_RUN=100`; golden fixture requires ~2000 tokens.

**Pass condition:**
- `summarize_pulse()` raises `PulseCostExceeded` (custom exception) before completing.
- `runs.metrics_json` records `llm_tokens_used` and `llm_cost_usd` at the point of the hard stop.
- Exception message includes: `"Token limit 100 exceeded at {n} tokens"`.
- Does NOT silently truncate to partial results and call it success.

---

### E3-5: PII Re-Scrub Before LLM

**What to run:**
```bash
pytest tests/test_summarization.py::test_pii_rescrub_before_llm -v
```

**Setup:** Inject a review with a phone number that slipped through Phase 1 scrubbing (to simulate a scrubber regression).

**Pass condition:**
- PII scrubber runs again on all review bodies before they are included in LLM prompts.
- The LLM prompt captured by the mock does not contain the raw phone number.

---

### E3-6: Structured JSON Response Validation

**Pass condition:**
- All LLM calls use function calling / `json_object` mode.
- If the LLM returns invalid JSON or a schema mismatch, the call is retried up to 3 times.
- After 3 failures, the run raises `LLMSchemaError` — not a Python `KeyError` or `AttributeError`.

---

### E3-7: Action Ideas Generation

**Pass condition:**
- `generate_action_ideas(themes)` produces at least 1 and at most 5 `ActionIdea` objects.
- Each `ActionIdea` has a non-empty `title` and `description`.
- Action ideas are grounded in the theme descriptions (manual spot-check: action ideas reference the same topics as the themes).

---

### E3-8: Token and Cost Accounting

**Pass condition:**
- After `pulse summarize --run <id>`, `runs.metrics_json` contains:
  - `llm_tokens_prompt`: total prompt tokens across all LLM calls.
  - `llm_tokens_completion`: total completion tokens.
  - `llm_cost_usd`: computed cost (model pricing × tokens).
  - `llm_calls`: number of API calls made.
- Values are non-zero and plausible for the number of clusters processed.
