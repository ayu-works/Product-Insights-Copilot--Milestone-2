**## Architecture

Weekly Product Review Pulse — Detailed Architecture

An AI Agent that ingests App Store / Play Store reviews for a selected fintech product (INDMoney, Groww, PowerUp Money, Wealth Monitor, Kuvera), uses LLMs to detect themes and produce a one-page weekly insight report, and then delivers that report to stakeholders using MCP (Model Context Protocol) for Google Workspace — specifically the Google Docs MCP server (to append the report to a running Google Doc) and the Gmail MCP server (to send the stakeholder email).

---

1. Goals & Non-Goals

Goals

* Automated weekly pulse: zero-touch generation of a 1-page product review report every week.
* MCP-based delivery: the agent talks to Google Docs and Gmailonly through MCP servers. No direct Google API calls from the agent code.
* Google Doc as the system of record: every weekly report is appended as a dated section to a single running Google Doc per product (e.g., "Weekly Review Pulse — Groww"), so history is preserved and linkable.
* Email with a link to the doc: the Gmail MCP is used to send a short email that links directly to the newly added section in the Google Doc.
* Re-runnable & idempotent: re-running the same ISO week does not create duplicate Doc sections or duplicate emails.
* Auditable: every run records which MCP tool calls were made, with what arguments, and what Google resource IDs (docId, messageId) resulted.

Non-Goals

* Building a generic Google Workspace integration — we use only the MCP tools we need (append to Doc, send Gmail).
* Real-time streaming analytics (this is a weekly batch).
* A BI dashboard — the Google Doc is the dashboard.
* Social media ingestion (Twitter/Reddit) — out of scope.

3. MCP Integration (the Google Workspace surface)

The agent acts as an MCP Host and Client. It connects to two MCP servers, each wrapping a Google Workspace product.

3.1 Google Docs MCP Server

Purpose: append the rendered weekly pulse as a new dated section to a running Google Doc (one doc per product).

Transport: stdio (local dev) or SSE (containerised).

Tools used by the agent (typical surface exposed by a Google Docs MCP server; exact tool names will match the chosen server implementation):

| MCP tool                  | Agent usage                                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docs.search_documents     | Look up the per-product Doc by title if the docId isn't cached                                                                                                      |
| docs.get_document         | Read the current structure to find the end-of-body index for appending                                                                                              |
| docs.create_document      | First-run only — create"Weekly Review Pulse — {Product}"if it doesn't exist                                                                                       |
| docs.batch_update         | Primary tool. Append a new H1 section (YYYY-WW —`<window>`), the report body, and a horizontal rule. Also used to insert a bookmark/heading we can deep-link to. |
| docs.get_document (again) | Retrieve the new heading's headingId so we can build a deep-link URL for the email                                                                                  |

Appending strategy (idempotent):

1. Compute section_anchor = "pulse-{product}-{iso_week}" (e.g., pulse-groww-2026-W16).
2. Call docs.get_document and search its body for that anchor string.
3. If found → skip (run already appended; re-render email only if requested).
4. If not found → docs.batch_update with a single batched request that:
   * Inserts a page break at endIndex - 1.
   * Inserts a Heading 1 containing the anchor text (e.g., "Weekly Pulse — Groww — 2026-W16 (Apr 13 → Apr 19)").
   * Inserts the rendered report content (converted from Markdown to Docs batchUpdate requests: headings, bullets, bold/italic, quotes as indented text).
   * Inserts an insertSectionBreak / horizontal rule at the end.
5. Re-read the doc and capture the new heading's headingId; persist {run_id → { docId, headingId }} in local state.
6. Build the shareable link: https://docs.google.com/document/d/{docId}/edit#heading={headingId}.

Markdown → Google Docs conversion: the agent renders the pulse to a structured in-memory tree (not raw Markdown), then maps that tree to the batchUpdate request shape. This avoids Markdown-to-Docs ambiguity. The mapping is:

| Pulse element                       | Docs request                                                   |
| ----------------------------------- | -------------------------------------------------------------- |
| Section title                       | insertText + updateParagraphStyle: HEADING_1                   |
| Theme title                         | HEADING_2                                                      |
| Bullet (theme detail / action idea) | insertText + createParagraphBullets: BULLET_DISC_CIRCLE_SQUARE |
| Verbatim quote                      | insertText + updateParagraphStyle: indentFirstLine + italic    |
| "What this solves" table            | insertTable (2 columns: Audience, Value)                       |

3.2 Gmail MCP Server

Purpose: draft and send the stakeholder email with a deep link to the Google Doc section just created.

Tools used by the agent:

| MCP tool                                | Agent usage                                                                                 |
| --------------------------------------- | ------------------------------------------------------------------------------------------- |
| gmail.create_draft                      | Build the email from the templated body + deep link; always called first (dry-run friendly) |
| gmail.send_message                      | Send the draft. Gated behind CONFIRM_SEND=true to avoid accidental sends in dev             |
| gmail.list_labels / gmail.modify_labels | Tag outgoing message with a Pulse/`<product>` label for auditability                      |
| gmail.get_message                       | Post-send, fetch messageId and threadId to persist in run metadata                          |

Email content (HTML + plain-text multipart):

* Subject: [Weekly Pulse] {Product} — {ISO week} — {Top theme}
* Body (short): 3–5 bullet "top themes" teaser + a prominent "Read full report →" link pointing at the Google Doc #heading= deep link from §3.1.
* Footer: run_id, ingestion window, "Generated by Pulse Agent", unsubscribe/opt-out note.

Idempotency: the agent includes a custom header X-Pulse-Run-Id: {run_id} in gmail.create_draft. Before sending, it uses gmail.search_messages (query: from:me X-Pulse-Run-Id:{run_id}) to confirm no prior send exists; if one does, the new draft is discarded.

3.3 Authentication

Authentication is handled inside each MCP server, not in the agent. The agent only needs to know how to reach the server (stdio command or SSE URL). Typical setups:

* OAuth user flow: the MCP server stores refreshable OAuth tokens locally (scopes: https://www.googleapis.com/auth/documents, https://www.googleapis.com/auth/gmail.compose, .../gmail.send, .../gmail.labels).
* Service account with domain-wide delegation (for orgs): the MCP server impersonates a designated sender mailbox and a shared Docs owner.
* The agent's config only stores: docs_mcp_command / docs_mcp_url, gmail_mcp_command / gmail_mcp_url, and the target Google Doc IDs per product (or a title pattern to look them up).

4. Internal Agent Pipeline (non-MCP)

Everything in this section is local code inside the agent; it is deliberately not an MCP server because the MCP boundary is reserved for Google Workspace per the problem statement.

4.1 Modules

| Module        | Responsibility                                                                                                                             | Key libs                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| ingestion     | Pull App Store (iTunes RSS) + Play Store reviews for the product over 8–12 weeks; dedupe by stable id; PII-scrub (emails/phones)          | google-play-scraper, itunes-app-scraper, httpx      |
| storage       | Local persistence of raw reviews, embeddings, clusters, runs                                                                               | SQLite + sqlite-vec (or DuckDB + Parquet)           |
| clustering    | Embed → UMAP → HDBSCAN → medoid selection → keyphrase extraction (KeyBERT)                                                             | sentence-transformers, umap-learn, hdbscan, keybert |
| summarization | LLM calls to label each cluster as a theme, selectverbatimquotes, and generate action ideas;strict JSONvia function calling                | OpenAI/Anthropic SDK                                |
| renderer      | Convert the PulseSummary into (a) a structured Doc-request tree for the Google Docs MCP, and (b) an HTML+text email body for the Gmail MCP | jinja2, markdown-it-py                              |
| orchestrator  | ReAct-style loop that decides: ingest → cluster → summarize → render → MCP-append → MCP-email                                         | custom; optional langgraph                          |
| mcp_client    | Thin wrapper around the official MCP SDK; holds sessions to the two Google servers                                                         | mcp (python-sdk)                                    |

4.2 Canonical Types

class RawReview(BaseModel):

    id: str                  # sha1(source + external_id)

    product_key: str

    source: Literal["appstore", "playstore"]

    rating: int

    title: str | None

    body: str

    posted_at: datetime

    version: str | None

    language: str

    country: str

class Theme(BaseModel):

    id: str

    rank: int

    label: str

    description: str

    sentiment: Literal["negative", "mixed", "positive"]

    review_count: int

    representative_review_ids: list[str]

class PulseSummary(BaseModel):

    product: str

    window: Window            # start, end, weeks

    stats: PulseStats         # total_reviews, avg_rating, rating_delta_vs_prev

    top_themes: list[Theme]   # typically 3

    quotes: list[Quote]       # verbatim, validated against raw bodies

    action_ideas: list[ActionIdea]

    what_this_solves: list[AudienceValue]

4.3 Guardrails

* Reviews are treated as data, never instructions. They are passed to the LLM through structured message parts, never concatenated into system prompts.
* Verbatim-quote validator: every quote the LLM proposes must match a substring of some review.body (case-insensitive, whitespace-normalised). Non-matching quotes are dropped.
* PII scrub (regex: emails, phone numbers, Aadhaar-like numbers) happens before text reaches the LLM and before it reaches the Google Doc.
* Cost cap per run: hard stop if llm_tokens > N for the run.

---

5. Data Model & Local Storage

A single SQLite file per deployment (lightweight — the Google Doc is the durable, human-facing store):

CREATE TABLE products (key TEXT PRIMARY KEY, display TEXT,

    appstore_id TEXT, play_package TEXT,

    gdoc_id TEXT,            -- once discovered/created

    gmail_to TEXT);          -- csv distribution list

CREATE TABLE reviews (id TEXT PRIMARY KEY, product_key TEXT, source TEXT,

    rating INT, title TEXT, body TEXT, posted_at DATETIME,

    version TEXT, language TEXT, country TEXT,

    ingested_at DATETIME, raw_json TEXT);

CREATE TABLE review_embeddings (review_id TEXT PRIMARY KEY,

    embedding BLOB);   -- sqlite-vec

CREATE TABLE runs (id TEXT PRIMARY KEY, product_key TEXT,

    iso_week TEXT, window_start DATE, window_end DATE,

    status TEXT, metrics_json TEXT,

    gdoc_heading_id TEXT,           -- from Docs MCP

    gmail_message_id TEXT);         -- from Gmail MCP

CREATE TABLE themes (id TEXT PRIMARY KEY, run_id TEXT, rank INT,

    label TEXT, description TEXT, sentiment TEXT,

    review_count INT, representative_review_ids_json TEXT);

runs.gdoc_heading_id and runs.gmail_message_id are the proof of delivery — they only get written after the MCP tool call succeeds.

7. Idempotency & Re-runs

* Run key: run_id = sha1(product_key + iso_week).
* Doc-side idempotency: anchor string pulse-{product}-{iso_week} embedded in the Heading 1 text → a simple substring search on the Doc body decides whether to append.
* Email-side idempotency: custom header X-Pulse-Run-Id: {run_id} + Gmail search before send.
* Backfill CLI: pulse run --product groww --week 2026-W15 re-runs any past week; uses the same idempotency logic, so it's safe to re-run.
* Partial failure: if the Docs append succeeds but the Gmail send fails, the next run detects the Doc section is already there and proceeds directly to the Gmail step.

---

8. Security, Privacy & Governance

| Concern                          | Mitigation                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Google credentials               | Storedonlyinside the MCP servers (OAuth refresh token or service account JSON). The agent never sees them.   |
| Minimal OAuth scopes             | Docs: documents (no Drive). Gmail: gmail.compose + gmail.send + gmail.labels. No mail.google.com full scope. |
| PII in reviews                   | Regex scrub before LLM and before Google Doc.                                                                |
| Prompt injection via review body | Reviews passed as structured data parts; strict JSON response schemas; verbatim-quote validator.             |
| Accidental email blast in dev    | CONFIRM_SEND=true gate on gmail.send_message; default iscreate draft only.                                   |
| Auditability                     | runs table stores gdoc_heading_id and gmail_message_id; the Google Doc itself is the long-term audit log.    |
| MCP transport                    | stdio locally; SSE/HTTPS in deployment with mTLS or a private network.                                       |

## Implementation Plan

Weekly Product Review Pulse — Phase-wise Implementation Plan

Derived from docs/architecture.md. The build is split into 8 incremental phases. Each phase produces something independently testable and, from Phase 1 onward, demoable via the CLI. Each phase has a dedicated evaluations.md (how we prove it works) and edge-cases.md (what we must survive) under docs/phases/`<phase>`/.

---

Guiding Principles

1. Vertical slices, not horizontal layers. Every phase ends with a runnable command that exercises the new capability end-to-end (mocked where needed).
2. MCP boundary is sacred. Only Phase 5 and Phase 6 introduce MCP calls. Everything before is pure local code.
3. Idempotency from day one. Deterministic run_id = sha1(product_key + iso_week) is wired in Phase 0 and reused by every later phase.
4. Golden fixtures. Canonical raw reviews and a canonical PulseSummary live in tests/fixtures/ starting Phase 1 so later phases can test without network or LLM calls.
5. Fail loud, degrade never silently. Every phase defines its failure modes and treats "partially succeeded" as a red test.

---

Phase Summary

| Phase | Name                                  | Duration (rough) | Key deliverable                                                    | Blocks |
| ----- | ------------------------------------- | ---------------- | ------------------------------------------------------------------ | ------ |
| 0     | Foundations & Scaffolding             | 1–2 days        | Repo, config, SQLite schema, CLI skeleton, CI                      | All    |
| 1     | Review Ingestion                      | 2–3 days        | pulse ingest --product groww fills reviews table                   | 2      |
| 2     | Embeddings & Clustering               | 2–3 days        | pulse cluster --run`<id>` produces cluster assignments           | 3      |
| 3     | LLM Summarization                     | 3–4 days        | pulse summarize --run`<id>` produces validated PulseSummary JSON | 4      |
| 4     | Report & Email Rendering              | 2 days           | Doc-tree + HTML email artifacts on disk                            | 5, 6   |
| 5     | Google Docs MCP — Append             | 3–4 days        | Weekly section appended to running Google Doc, idempotent          | 6      |
| 6     | Gmail MCP — Deliver                  | 2–3 days        | Stakeholder email sent with deep link, idempotent                  | 7      |
| 7     | Orchestration, Scheduling & Hardening | 3 days           | Weekly cron, OTel traces, cost caps, runbook                       | —     |

Total: ~18–24 working days for a single engineer to reach production.

---

Phase 0 — Foundations & Scaffolding

Goal: everything except business logic. Any later phase should only need to add files, not fight the skeleton.

Scope

* Repo layout per architecture.md §11.
* pyproject.toml with uv; pinned deps for pydantic, sqlite-vec, jinja2, pytest, ruff, mypy.
* agent/config.py loading products.yaml via pydantic-settings; env via .env.
* agent/storage.py — create all tables (products, reviews, review_embeddings, runs, themes) from architecture.md §5.
* agent/__main__.py — Typer CLI with subcommands: ingest, cluster, summarize, render, publish, run.
* run_id helper + Window helper (ISO-week math, IST-aware).
* Dockerfile, docker-compose.yml (agent-only for now), GitHub Actions CI running lint + tests.
* Structured logging (structlog) with run_id context var.

Exit criteria

* uv run pulse --help prints all subcommands.
* uv run pulse init-db creates a fresh SQLite file with all tables.
* CI is green on an empty repo with two smoke tests.

Evaluations: docs/phases/phase-0-foundations/evaluations.md Edge cases: docs/phases/phase-0-foundations/edge-cases.md

---

Phase 1 — Review Ingestion

Goal: reliably pull and store 8–12 weeks of reviews for any supported product.

Scope

* agent/ingestion/appstore.py — iTunes RSS customerreviews feed, paginated (1..10), country-configurable.
* agent/ingestion/playstore.py — google-play-scraper wrapper with time-bounded pagination.
* Unified RawReview pydantic model; stable id = sha1(source + external_id).
* Dedup-upsert into reviews table.
* Regex PII scrubber (emails, phone numbers, Aadhaar-like) applied to body before persistence.
* Raw JSON snapshot written to data/raw/{product}/{run_id}.jsonl for audit.
* CLI: pulse ingest --product groww --weeks 10.

Exit criteria

* Fixture-replay test: feeding canned App Store + Play Store HTTP responses produces a deterministic reviews snapshot.
* Running the real command for groww returns ≥ 200 reviews (smoke test; gated behind a live-network flag).
* Re-running the same command within a minute is a no-op (0 inserts, some updates).

Evaluations: docs/phases/phase-1-ingestion/evaluations.md Edge cases: docs/phases/phase-1-ingestion/edge-cases.md

---

Phase 2 — Embeddings & Clustering

Goal: turn a pile of reviews into a small set of coherent clusters with representative members.

Scope

* phases/phase-2-clustering (pulse_clustering package); the agent CLI maps env settings via agent/cluster_settings.py (see docs/rules.md for layout rules).
  * Language filter (keep en), length filter (≥ 20 chars).
  * Embedding provider interface with two implementations: OpenAI text-embedding-3-small and local bge-small-en-v1.5 (sentence-transformers).
  * Batch embed with on-disk cache keyed by sha1(text).
  * UMAP (n_components=15, metric=cosine), HDBSCAN (min_cluster_size=8, configurable).
  * Medoid selection per cluster (closest vector to centroid) + 2 extra picks with rating variance.
  * KeyBERT keyphrases per cluster (top 8).
* Persist review_embeddings + a new clusters table (id, run_id, review_ids_json, keyphrases_json, medoid_review_id).
* CLI: pulse cluster --run `<id>`.

Exit criteria

* On the golden fixture (~400 reviews), HDBSCAN returns between 4 and 12 clusters; noise ratio < 35%.
* Determinism: fixed random seeds → same cluster assignments across runs (byte-identical).
* Embedding cache hit rate on a re-run is 100%.

Evaluations: docs/phases/phase-2-clustering/evaluations.md Edge cases: docs/phases/phase-2-clustering/edge-cases.md

---

Phase 3 — LLM Summarization

Goal: convert numeric clusters into named themes, verbatim quotes, and action ideas — with strong grounding guarantees.

Scope

* agent/summarization.py:
  * Pydantic response models for every LLM call; Groq (OpenAI-compatible chat.completions + json_object) or Anthropic structured JSON.
  * label_theme(keyphrases, medoid_reviews) -> Theme.
  * select_quotes(cluster_reviews) -> list[Quote] with verbatim validator: every returned string must be a normalized-whitespace substring of some review.body; non-matching quotes dropped, re-prompted once.
  * generate_action_ideas(themes) -> list[ActionIdea].
  * summarize_pulse(...) -> PulseSummary (final assembly, ranks top 3 themes by review_count × |sentiment weight|).
* LLM client wrapper with: retries, timeout, token/cost accounting (persisted to runs.metrics_json), per-run hard cap.
* PII re-scrub before any LLM call.
* CLI: pulse summarize --run `<id>` writes PulseSummary JSON to data/summaries/{run_id}.json.

Exit criteria

* On the golden fixture, 3 themes are produced; every quote passes the verbatim validator.
* Deterministic snapshot test using a mocked LLM (vcr.py-style) — PulseSummary JSON is byte-stable.
* Cost cap triggers a controlled PulseCostExceeded error, not a silent truncation.

Evaluations: docs/phases/phase-3-summarization/evaluations.md Edge cases: docs/phases/phase-3-summarization/edge-cases.md

---

Phase 4 — Report & Email Rendering

Goal: deterministic conversion of PulseSummary into (a) a Google Docs batchUpdate request tree and (b) an HTML+text email body.

Scope

* agent/renderer/docs_tree.py:

  * PulseSummary → list of batchUpdate requests matching the mapping table in architecture.md §3.1.
  * Anchor string pulse-{product}-{iso_week} embedded in the Heading 1 text.
  * Validates against templates/doc_section.schema.json.
* agent/renderer/email_html.py:
* Jinja2 template → HTML + plain-text; includes placeholder {DOC_DEEP_LINK} to be filled after Phase 5.
* Subject: [Weekly Pulse] {Product} — {ISO week} — {Top theme}.
* CLI: pulse render --run `<id>` writes data/artifacts/{run_id}/doc_requests.json + email.html + email.txt.
* No MCP calls here — pure local rendering.

Exit criteria

* Golden-image test: doc-request JSON and email HTML are byte-stable on fixture input.
* Schema validator rejects malformed summaries (missing themes, wrong sentiment enum).

Evaluations: docs/phases/phase-4-renderer/evaluations.md Edge cases: docs/phases/phase-4-renderer/edge-cases.md

---

Phase 5 — Google Docs MCP — Append Report

Goal: append the rendered report as a new dated section to a running Google Doc, idempotently, using only MCP.

Scope

* Choose and pin a Google Docs MCP server (community or official); add it to docker-compose.yml and infra/k8s/ manifests.
* agent/mcp_client/session.py — connect/close both MCP sessions (stdio locally, SSE in prod); validate tool schemas at handshake.
* agent/mcp_client/docs_ops.py:
  * resolve_document(product) -> docId — uses docs.search_documents / cache / docs.create_document on first run.
  * append_pulse_section(docId, doc_requests, anchor) -> {headingId, deep_link}:
    1. docs.get_document → check anchor substring in body → skip if present.
    2. docs.batch_update with the Phase-4 request tree.
    3. docs.get_document again → locate the new heading by anchor, return its headingId.
  * Persist runs.gdoc_heading_id + gdoc_id.
* CLI: pulse publish --run `<id>` --target docs.
* Integration tests use a mock MCP server that speaks real JSON-RPC and records requests.

Exit criteria

* Against the mock MCP server: first run creates a new section; second run is a no-op (anchor detected).
* Against a real Google Doc in a test Workspace: the report renders correctly (headings, bullets, italic quotes, "What This Solves" table).
* gdoc_heading_id is persisted and builds a working deep link.

Evaluations: docs/phases/phase-5-docs-mcp/evaluations.md Edge cases: docs/phases/phase-5-docs-mcp/edge-cases.md

---

Phase 6 — Gmail MCP — Deliver Email

Goal: send the stakeholder email with the Doc deep link, once per run, via the Gmail MCP server.

Scope

* Pin a Gmail MCP server; add to compose/k8s.
* agent/mcp_client/gmail_ops.py:
  * send_pulse_email(run_id, to, cc, bcc, html, text, deep_link):
    1. gmail.search_messages for X-Pulse-Run-Id:{run_id} — if found, skip.
    2. gmail.create_draft with custom header X-Pulse-Run-Id and label Pulse/{product}.
    3. If CONFIRM_SEND=true, gmail.send_message(draftId); otherwise stop at draft.
    4. Persist runs.gmail_message_id.
* Email body gets the real {DOC_DEEP_LINK} from Phase 5 substituted in.
* CLI: pulse publish --run `<id>` --target gmail and a combined --target both.

Exit criteria

* Mock MCP integration test: first run sends (draft→send); second run detects header and skips; runs.gmail_message_id populated exactly once.
* Dry-run default: without CONFIRM_SEND, a draft exists but no send occurs.
* Real Workspace smoke test: email arrives in a test inbox, deep link jumps to the new heading in the Doc.

Evaluations: docs/phases/phase-6-gmail-mcp/evaluations.md Edge cases: docs/phases/phase-6-gmail-mcp/edge-cases.md

---

Phase 7 — Orchestration, Scheduling & Hardening

Goal: the whole pipeline runs weekly, unattended, with observability, cost controls, and a written runbook.

Scope

* agent/orchestrator.py — top-level pulse run --product groww --weeks 10 chaining all phases with resumable checkpoints driven by runs.status.
* Scheduling: GitHub Actions workflow .github/workflows/weekly-pulse.yml (cron Mon 07:00 IST) running once per product in a matrix.
* Observability: OpenTelemetry spans around every module and every MCP tool call; run_id as a span attribute; export to OTLP.
* Metrics: pulse.reviews_ingested, pulse.clusters_formed, pulse.llm_tokens, pulse.llm_cost_usd, pulse.mcp_call_latency{tool}, pulse.publish_status.
* Alerts: ingestion drop > 50% WoW; avg rating delta > 1.0; LLM schema-validation failure rate > 2%; MCP call error rate > 1%.
* Runbook: docs/runbook.md covering: "email not sent", "duplicate section in Doc", "ingestion empty", "LLM cost spike", "MCP server crash", "token revoked".
* Backfill CLI: pulse run --product groww --week 2026-W15 re-runs any past week safely.

Exit criteria

* Dry-run weekly workflow passes in CI using mocked MCP servers.
* On a staging Workspace, one full unattended run end-to-end in < 5 minutes; total LLM cost tracked in runs.metrics_json and under the per-run cap.
* Kill the MCP server mid-run → orchestrator retries; second run completes and is still idempotent.

Evaluations: docs/phases/phase-7-orchestration/evaluations.md Edge cases: docs/phases/phase-7-orchestration/edge-cases.md

**
