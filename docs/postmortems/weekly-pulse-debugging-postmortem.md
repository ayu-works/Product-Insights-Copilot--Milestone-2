# Weekly Pulse CI Failure — Full Debugging Story & Fix

**Date:** 2026-06-09
**Workflow affected:** `.github/workflows/weekly-pulse.yml` (the "Weekly Pulse" GitHub Action)
**Outcome:** The pipeline now runs **fully green** end-to-end on GitHub Actions.

This document explains, in plain language, what was going wrong, why it was so confusing, how each piece was fixed, and what to remember so it doesn't happen again. It's written so a non-coder can follow the story and a coder can act on the details.

---

## 1. The one-sentence summary

> The error message said **"Connection error"**, which made it look like a *networking / firewall* problem — but the real causes were completely different: we had **run out of our daily free AI usage allowance**, and two **configuration values were missing in the cloud** that were only present on the local machine. The "Connection error" was a misleading mask over the real error.

The big lesson: **the error message was lying to us.** We spent a lot of effort fighting a problem (a network "block") that never actually existed.

---

## 2. What the system does (quick context)

"Weekly Pulse" is an automated job that, once a week, builds a product-review summary:

1. **Ingest** – download app-store / play-store reviews.
2. **Cluster** – group similar reviews together (done locally, no internet AI needed).
3. **Summarize** – ask an AI model (hosted by a company called **Groq**) to write themes and pick quotes.
4. **Render** – turn the summary into a document.
5. **Publish** – append it to a **Google Doc** and create a **Gmail draft**.

It runs automatically on **GitHub Actions** — a cloud robot that runs our code on a fresh rented computer every week. The trouble was: it kept failing at **step 3 (Summarize)**.

---

## 3. The symptom we kept seeing

Every run died with this:

```
Retrying request to /openai/v1/chat/completions ...
{"provider": "groq", "error": "Connection error.", "event": "llm_retry", ...}
Run failed: Groq call 'label_theme' failed after 3 retries: Connection error.
```

"Connection error" naturally reads as: *"the computer can't reach Groq's servers."* So the earlier attempts to fix it all assumed a **network block**:

- Adding **Cloudflare WARP** (a VPN-like tunnel) to "bypass an IP block."
- **Disabling IPv6** networking.
- Swapping the software library used to talk to Groq.

**None of these worked** — because there was no network block to bypass. (More on why in the next section.)

> **Analogy:** Imagine your phone says "Call failed." You assume you have no signal and keep walking around looking for bars. But actually you have full signal — the real problem is your *prepaid balance is zero*. No amount of walking around fixes a billing problem.

---

## 4. How we found the truth (the method)

Instead of guessing, we **measured**. We added a temporary **diagnostic step** to the workflow that, from the *exact same cloud machine*, tested the connection to Groq four ways:

| Test | What it checks | Result |
|------|----------------|--------|
| DNS lookup | Can we find Groq's address? | ✅ Found it |
| Raw TCP connect | Can we open a socket to Groq? | ✅ Connected |
| `curl` (command-line web request) | Does an authenticated request work? | ✅ **HTTP 200 OK** |
| Groq's official AI library (Python) | Does a real AI call work? | ✅ Replied **"pong"** |

**Every single test passed.** From the same machine that was supposedly "blocked," we successfully made a real AI call. That **disproved the network-block theory completely.**

So why did the *real app* still fail? The app was **hiding the true error**. In the code, the error-handling looked like this (simplified):

```python
except Exception as exc:
    log.warning("llm_retry", error=str(exc))   # only logged a short string
```

For one type of error, `str(exc)` happens to be the unhelpful text `"Connection error."`. We added one temporary line to print the **full error details** instead:

```python
except Exception as exc:
    import traceback
    log.warning("llm_retry", error=str(exc),
                exc_type=type(exc).__name__,         # the REAL error class
                traceback=traceback.format_exc())    # the full stack trace
```

The moment we did that, the real error appeared.

---

## 5. The real problems (there were several, stacked)

Debugging peeled back **five layers**. Each fix revealed the next problem underneath.

### Problem #1 — "Connection error" was a red herring
**Detail:** The genuine network was fine. The early intermittent connection errors were almost certainly caused by the **WARP tunnel we ourselves added** — a VPN-like layer that can drop connections. We were adding instability to "fix" a problem that didn't exist.
**Fix:** Recognize it's not a network issue. (Recommended cleanup: remove WARP and the IPv6-disable step entirely.)

### Problem #2 — We ran out of our daily AI allowance (the 429 error)
Once we exposed the real error, it was:
```
groq.RateLimitError: Error code: 429 -
  Rate limit reached ... tokens per day (TPD): Limit 100000, Used 99227.
  Please try again in 23m. ... Upgrade to Dev Tier
```
**Detail (plain):** Groq's **free plan allows 100,000 "tokens" of AI usage per day** (a token ≈ ¾ of a word). We had used 99,227 — essentially all of it. So new requests were politely refused with error code **429 ("too many requests")**. The app turned that refusal into the vague "Connection error."
**Fix:** Use a fresh API key with an unused daily allowance. (See Problem #5 — this is also a deeper capacity issue.)

### Problem #3 — Publishing to Google Docs failed with a *blank* error
With a fresh key, the AI steps succeeded — but the run then failed at **Publish**, logging an empty error (`"error": ""`).
**Detail:** A blank error is the fingerprint of a program exiting on purpose (`raise typer.Exit(1)`) after printing the real reason to a different output channel. The real reason was:
```
No Google Doc ID configured. Set 'gdoc_id' in products.yaml or PULSE_GDOC_ID.
```
The cloud robot needs to know **which** Google Doc to write into. That ID was saved on the **local computer** (in `phases/.env`) but was **never given to the cloud**. The cloud has no access to your local files — secrets must be supplied separately.
**Fix:** Added `PULSE_GDOC_ID` as a **GitHub repository secret**, and passed it into the workflow's run step.

### Problem #4 — Gmail step failed: "URL is missing a protocol"
Next, the **Gmail** part failed:
```
Request URL is missing an 'http://' or 'https://' protocol.
```
**Detail:** The address of the email service was stored in a cloud secret **without the `https://` at the front**, so the software didn't know it was a web address. (Locally it was correct; the cloud copy was malformed.)
**Fix:** Re-saved the `PULSE_GMAIL_MCP_URL` secret using the correct full value (with `https://`, no stray spaces).

### Problem #5 — The real ceiling: one run uses an entire day's free budget
After fixing everything, a *second* run the same day failed again at the AI step — out of tokens.
**Detail:** A full run over ~1,300 reviews and ~30 clusters consumes **roughly 100,000 tokens — essentially the entire free daily allowance in a single run.** So the free plan realistically allows only **about one run per day**, with no margin for retries or testing.
**Fix options (a decision, not a bug):**
- **Shrink the workload** (fewer weeks, fewer clusters, shorter text) to fit comfortably under the limit, **or**
- **Switch to a different AI provider** (e.g. Anthropic) with higher limits and a built-in spend cap, **or**
- **Upgrade Groq to a paid tier.**

---

## 6. The final, confirmed result

A clean run on a fresh key completed **fully green**, with every stage confirmed:

```
ingest_complete ✅   clustering_complete ✅   summarize_complete ✅
render_complete ✅   publish_docs_rest_complete ✅   (Google Doc updated)
publish_gmail_rest_complete ✅  (Gmail draft created)
pulse_run_complete ✅  (week 2026-W23)
```

There is **no remaining code or network bug.** The pipeline works.

---

## 7. Summary table — what was wrong vs. what fixed it

| # | What it *looked* like | What it *actually* was | The fix |
|---|------------------------|------------------------|---------|
| 1 | Network / Cloudflare IP block | Nothing — network was fine | Stop fighting it (remove WARP/IPv6 hacks) |
| 2 | "Connection error" | Out of daily AI tokens (429) | Fresh key; exposed real error with full traceback logging |
| 3 | Publish failed, blank error | Missing `PULSE_GDOC_ID` in the cloud | Add it as a GitHub secret + pass to workflow |
| 4 | "URL missing protocol" | Gmail URL secret had no `https://` | Re-save the secret correctly |
| 5 | Random re-failures | One run ≈ entire free daily budget | Shrink workload / switch provider / upgrade plan |

---

## 8. Lessons — how to avoid this next time

1. **Don't trust the error message's surface meaning.** "Connection error" was a wrapper over a billing/rate-limit error. **Always reveal the real error first** (full exception type + traceback) before theorizing.
2. **Measure, don't guess.** One small diagnostic test (curl + a real API call from the same machine) instantly disproved hours of assumptions. Reproduce the failure in isolation before "fixing."
3. **The cloud cannot see your local `.env`.** Every secret/config the app needs locally (`PULSE_GDOC_ID`, `PULSE_GMAIL_MCP_URL`, API keys) must be **added separately as GitHub secrets** and **passed into the workflow's `env:` block.** Check these match your local `.env` exactly — including the `https://` prefix and no trailing spaces.
4. **Know your free-tier limits as a capacity number, not just a vague "free."** Free = **100,000 Groq tokens/day**, and **one run ≈ one day's budget.** Plan testing around that, or you'll exhaust it and see confusing failures.
5. **A blank/empty error usually means "the program chose to quit"** after printing the reason elsewhere — go read the standard-error output, not just the structured logs.
6. **Make error logs honest.** The app swallowing the true exception as a short string cost hours. Logging the exception *type* and *traceback* should be the default for any external call.

---

## 9. For coders — exact changes made

**Kept in the final `main` version:**
- **`.github/workflows/weekly-pulse.yml`** — added `PULSE_GDOC_ID: ${{ secrets.PULSE_GDOC_ID }}` to the `Run weekly pulse` step's `env`.
- **`agent/summarization/client.py`** — `GroqLLMClient` retry log now also records `exc_type=type(exc).__name__`. This one cheap field is what makes the *real* error class (`RateLimitError` vs `APIConnectionError`) visible in logs instead of the misleading `"Connection error."` string.
- **GitHub repository secrets**
  - `PULSE_GDOC_ID` — created from the local `.env` value.
  - `PULSE_GMAIL_MCP_URL` — re-set with the correct `https://…` value (the old one lacked a scheme).

**Removed during cleanup (were temporary scaffolding or disproven hacks):**
- The two diagnostic steps (shell connectivity probe + Python SDK probe).
- The heavy `traceback.format_exc()` / `cause` debug fields in the retry log.
- The `Bypass IP Block via Cloudflare WARP` and `Disable IPv6` steps — proven unnecessary (Groq was never IP-blocked) and a likely source of the original intermittent connection drops.

**Known follow-up bug (not yet fixed):** `GroqLLMClient` retries a daily-cap `429` three times (5/10/20s backoff) even though the API says "try again in ~23m." It should fail fast (or honor `Retry-After`) since retrying within a run cannot succeed.

### Quick triage checklist for the next CI failure
1. Look at the **exception type**, not the message string. `RateLimitError` (429) ≠ `APIConnectionError`.
2. If it's a 429 → check the **daily token usage** in the Groq console; you may just be out of budget.
3. If a step exits with a **blank error** → read the step's **stderr** for the real reason.
4. If it's a "missing protocol" / connection-shaped error to an internal service → **inspect the secret value** for a missing `https://` or stray whitespace.
5. Confirm every value in local `phases/.env` has a matching, correctly-formatted **GitHub secret**.
