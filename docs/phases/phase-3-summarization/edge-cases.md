# Phase 3 — LLM Summarization: Edge Cases

## What We Must Survive

---

### EC3-1: LLM Returns Malformed JSON

**Scenario:** The LLM returns a response that starts with text before the JSON (`"Sure! Here is the JSON: {...}"`), breaking JSON parsing.

**Expected behaviour:**
- The LLM client wrapper strips leading/trailing prose using a regex (`re.search(r'\{.*\}', response, re.DOTALL)`).
- If stripping yields valid JSON, parsing proceeds normally.
- If JSON is still invalid after stripping, the call is counted as a failure and retried.
- After 3 retries, `LLMSchemaError` is raised with the raw response saved to the log for debugging.

---

### EC3-2: All Clusters Are Negative Sentiment

**Scenario:** All 5 clusters from Phase 2 are labelled `negative` by the LLM.

**Expected behaviour:**
- `PulseSummary.top_themes` contains 3 negative themes — this is a valid outcome, not an error.
- No artificial "positive" theme is fabricated.
- The report's narrative will reflect the uniformly negative signal.

---

### EC3-3: Review Body Exceeds LLM Context Window

**Scenario:** A single review body is 8,000 tokens long (e.g. a user pasted a legal complaint).

**Expected behaviour:**
- Reviews are truncated to `max_body_tokens` (configurable, default 512 tokens) before being included in LLM prompts.
- Truncation is logged: `"Review {id} truncated from {n} to 512 tokens"`.
- Verbatim quote validator uses the original (un-truncated) body to check validity.

---

### EC3-4: LLM API Rate Limit (HTTP 429)

**Scenario:** OpenAI or Anthropic API returns 429 after the 3rd call in a batch of 5 cluster-labelling calls.

**Expected behaviour:**
- Exponential backoff: wait 5s, 10s, 20s before retrying.
- If all retries fail for a single cluster, that cluster is skipped and logged: `"Cluster {id} skipped: rate limited after 3 retries"`.
- Run continues with remaining clusters; `PulseSummary` is assembled from successful clusters.
- `runs.status = 'partial'` if any cluster was skipped.

---

### EC3-5: LLM Returns Fewer Than 3 Themes

**Scenario:** Only 2 clusters passed from Phase 2; LLM labels both → only 2 themes.

**Expected behaviour:**
- `PulseSummary.top_themes` contains 2 themes.
- This is acceptable; the report simply has 2 theme sections instead of 3.
- No padding or fabrication of a third theme.

---

### EC3-6: LLM Proposes Quotes for a Zero-Review Cluster

**Scenario:** A cluster ends up with 0 reviews after filtering (e.g. all reviews were too short).

**Expected behaviour:**
- `select_quotes` is not called for empty clusters.
- The cluster is skipped with a log: `"Skipping quote selection for empty cluster {id}"`.

---

### EC3-7: Cost Cap Hit Mid-Summarization (Partial State)

**Scenario:** Cost cap is hit after 2 of 4 cluster-labelling calls complete.

**Expected behaviour:**
- The 2 completed themes are saved to `data/summaries/{run_id}_partial.json`.
- `PulseCostExceeded` is raised with `partial_themes` in the exception payload.
- On re-run with a higher cap, the run starts from scratch (no resumption from partial — simpler and avoids stale state).

---

### EC3-8: Verbatim Quote Contains Regex Special Characters

**Scenario:** A review says `"5+5 = 10? Really??"` and the LLM returns this as a verbatim quote.

**Expected behaviour:**
- The validator uses `re.escape()` or a plain substring check (`quote in review.body`), not a raw regex match.
- The quote passes validation correctly.

---

### EC3-9: Network Disconnect During Long Summarization Call

**Scenario:** The LLM call for a large cluster times out after 30 seconds.

**Expected behaviour:**
- `httpx.ReadTimeout` is caught by the LLM client wrapper.
- Logged as a timeout with the cluster ID.
- Retried using the same backoff as rate-limit handling.
- After max retries, cluster is skipped (see EC3-4).
