# Repository Cleanup & Restructure Plan

> **Purpose.** A precise, step-by-step plan to clean and restructure the *Weekly Product Review Pulse* repository. This document is the spec; it will be **executed by a separate agent (Claude Sonnet)**. Authored by Claude Opus on 2026-06-09.
>
> **Golden rule for the implementing agent:** Do everything in order. Create git tags (Step 1) **before** deleting or moving anything. Verify the app still runs (Step 8) before committing the deletions. Never delete code that isn't recoverable from a tag you just created.

---

## 1. Context — What This Repo Is

An AI agent that ingests App Store / Play Store reviews for fintech products (Groww, INDMoney, etc.), uses an LLM to detect themes and produce a one-page weekly insight report, then delivers it via **MCP** to Google Docs (append a dated section) and Gmail (email a deep link). Built in 8 phases (0–7) per `Docs/Architecture.md` and `Docs/Implementation Plan.md`.

## 2. The Core Problem (verified)

The repository was built by **copying the entire project forward into a new folder for every phase**:

```
phases/
  phase-0-foundations/      agent/ (config, storage, cli skeleton)
  phase-1-ingestion/        agent/ (phase-0 + ingestion/)
  phase-2-clustering/       agent/ (phase-1 + clustering/)
  phase-3-summarization/    agent/ (phase-2 + summarization/)
  phase-4-renderer/         agent/ (phase-3 + renderer/)
  phase-5-docs-mcp/         agent/ (phase-4 + mcp_client/ + rest_client/ + services/docs-mcp/)
  phase-6-gmail-mcp/        agent/ (phase-5 + gmail_ops + services/gmail-mcp/)
  phase-7-orchestration/    agent/ (EVERYTHING + orchestrator.py + observability.py + uv.lock + tests/mocks/)
```

**Consequences:**
- `phase-7-orchestration/` is the complete, cumulative, runnable project. Phases 0–6 are **7 redundant, frozen-in-time copies** of earlier states of the same `agent/` package.
- The live CI workflow `.github/workflows/weekly-pulse.yml` already hard-codes `working-directory: phases/phase-7-orchestration`, confirming phase-7 is the real project.
- This layout was **never specified** by the Architecture or Implementation Plan. Both describe a *single* `agent/` package at the repo root with submodules added phase-by-phase, `tests/fixtures/`, and `docs/phases/<phase>/`. The `phases/phase-N/` tree is a build artifact, not a design.

**Other gaps found:**
- ❌ No root `README.md` (no entry point explaining the project).
- ❌ No root `CLAUDE.md` (no agent-onboarding / conventions file).
- ❌ No root `.gitignore` (each phase has its own; junk like `__pycache__`/`.venv`/`.env` is *not* tracked — but a root one is still needed after restructure).
- ⚠️ `Docs/` (capital D) vs the plan's `docs/` (lowercase) — inconsistent casing.
- ⚠️ Runbook lives at `phases/phase-7-orchestration/docs/runbook.md` instead of the planned root `docs/runbook.md`.
- ⚠️ `Docs/Architecture.md` references a "§11 repo layout" that does not exist in the file; section numbering also skips §2 and §6.
- ⚠️ Stray/untracked debugging files: `Docs/gemini_debugging_weekly_pulse.md`, `.github/workflows/failurelog.md`, plus committed postmortems.
- ⚠️ `.venv/` directories exist on disk inside `phases/phase-4`, `phase-6`, `phase-7` (large; untracked but should be cleaned).

## 3. Decisions (locked in with the repo owner)

| # | Decision | Choice |
|---|----------|--------|
| D1 | Keep the phase narrative or collapse to one project? | **Keep phases, but deduplicate.** The milestone story stays visible; the 7× code duplication is removed. |
| D2 | How is phase history preserved? | **Git tags per phase** (`phase-0`…`phase-7`), created from the *current* commit **before** restructuring. Non-destructive, zero disk cost, fully recoverable. |
| D3 | What do the `phases/phase-N/` folders become? | **Docs-only.** Each becomes a single `README.md` narrating what that phase added, its CLI command, exit criteria, and a pointer to its git tag + the real files in the root `agent/`. **No duplicated code.** |
| D4 | Where does the runnable code live? | **Once, at the repo root**, promoted from `phase-7-orchestration/`. |

## 4. Target Structure (after cleanup)

```
/                                  ← the single runnable project
├── README.md                      ← NEW: project entry point
├── CLAUDE.md                      ← NEW: agent onboarding / conventions
├── .gitignore                     ← NEW: root-level (from phase-7's .gitignore)
├── pyproject.toml                 ← from phase-7 (package "pulse", entry pulse=agent.__main__:app)
├── uv.lock                        ← from phase-7
├── Dockerfile                     ← from phase-7
├── docker-compose.yml             ← from phase-7
├── products.yaml                  ← from phase-7
├── .env.example                   ← from phases/.env.example
├── agent/                         ← THE package (from phase-7/agent)
│   ├── __main__.py, config.py, storage.py, models.py, helpers.py, logging_setup.py
│   ├── observability.py, orchestrator.py
│   ├── ingestion/  clustering/  summarization/  renderer/  mcp_client/  rest_client/
├── services/                      ← MCP servers (from phase-7/services)
│   ├── docs-mcp/   gmail-mcp/
├── templates/                     ← from phase-7/templates
├── tests/                         ← from phase-7/tests (incl. mocks/, fixtures/)
├── docs/                          ← renamed from Docs/ (lowercase, matches plan)
│   ├── Architecture.md
│   ├── Implementation-Plan.md
│   ├── Problem-Statement.md
│   ├── runbook.md                 ← moved from phase-7/docs/runbook.md
│   ├── MCP-server/                ← plan-a / plan-b
│   ├── phases/                    ← existing per-phase evaluations.md + edge-cases.md (KEEP)
│   └── postmortems/               ← consolidate debugging docs here (optional)
├── phases/                        ← DOCS-ONLY after cleanup
│   ├── README.md                  ← NEW: index of the phase journey
│   ├── phase-0-foundations/README.md   ← NEW: narrative + tag pointer
│   ├── …
│   └── phase-7-orchestration/README.md ← NEW
└── .github/workflows/
    └── weekly-pulse.yml           ← EDIT: drop working-directory: phases/phase-7-orchestration
```

> **Note on D1 nuance:** "Keep phases but deduplicate" is realized by making `phases/phase-N/` *documentation* (Step 5), not by keeping runnable code in each. Cumulative Python phases cannot be deduplicated as code without fragile shared-package overlays; the clean, robust form is one root package + a narrated, tagged journey. If the owner later insists each phase folder must be independently *runnable*, that is a separate, larger effort and should be rejected in favor of git tags (which already make every phase runnable via `git checkout phase-N`).

---

## 5. Execution Plan (ordered, for the implementing agent)

### Step 0 — Pre-flight
- Confirm working tree is committed/clean enough that the 3 untracked files (`.github/workflows/failurelog.md`, `Docs/gemini_debugging_weekly_pulse.md`, `phases/.env`) are accounted for. **Do not commit `phases/.env`** — it contains a real `PULSE_GROQ_API_KEY`. Ensure the new root `.gitignore` excludes it.
- Work on a branch: `git checkout -b chore/repo-restructure`.

### Step 1 — Tag every phase (DO THIS FIRST, before any move/delete)
Create one annotated tag per phase at the current `HEAD`, so each phase's full snapshot stays recoverable:
```
git tag -a phase-0 -m "Phase 0 — Foundations & Scaffolding (pre-restructure snapshot)"
git tag -a phase-1 -m "Phase 1 — Review Ingestion"
git tag -a phase-2 -m "Phase 2 — Embeddings & Clustering"
git tag -a phase-3 -m "Phase 3 — LLM Summarization"
git tag -a phase-4 -m "Phase 4 — Report & Email Rendering"
git tag -a phase-5 -m "Phase 5 — Google Docs MCP"
git tag -a phase-6 -m "Phase 6 — Gmail MCP"
git tag -a phase-7 -m "Phase 7 — Orchestration, Scheduling & Hardening"
```
> All eight phase snapshots live in the same current commit, so all tags point at the same SHA. That is fine and intentional — the *folders* `phases/phase-N/` ARE the snapshots, and the tags preserve them after the folders are reduced to docs. Anyone can `git show phase-2:phases/phase-2-clustering/agent/...` forever. (Push tags at the end: `git push --tags`.)

### Step 2 — Promote phase-7 to the repo root
Move (preserve history with `git mv`) every runnable artifact from `phases/phase-7-orchestration/` to the repo root:
- `agent/`, `services/`, `templates/`, `tests/`
- `pyproject.toml`, `uv.lock`, `Dockerfile`, `docker-compose.yml`, `products.yaml`
- `.gitignore` → root `.gitignore` (this is the canonical ignore file)
- `docs/runbook.md` → root `docs/runbook.md` (see Step 4)

After moving, update `pyproject.toml`:
- `description` — drop "Phase 7:" prefix; make it the project description.
- consider bumping `version` to `1.0.0` (it's now the whole product, not a phase).
- Keep `[project.scripts] pulse = "agent.__main__:app"` and `[tool.hatch.build.targets.wheel] packages = ["agent"]` — both already correct for a root layout.

Move `phases/.env.example` → root `.env.example`.

### Step 3 — Delete the redundant phase code
Delete the now-redundant cumulative copies (recoverable via the Step 1 tags):
- `phases/phase-0-foundations/` … `phases/phase-6-gmail-mcp/` — **entire folders.**
- `phases/phase-7-orchestration/` — everything *except* nothing (it's been moved out in Step 2); delete the empty shell.
- Also delete on-disk junk if present: any `.venv/`, `__pycache__/`, `.pytest_cache/` left behind.

> Replace them with docs-only folders in Step 5. Net effect: `phases/` shrinks from ~8 full project copies to ~9 small README files.

### Step 4 — Normalize the docs folder
- Rename `Docs/` → `docs/` (lowercase, to match Architecture/Plan references and the moved `runbook.md`). On case-insensitive Windows + git, do this via `git mv Docs docs_tmp` then `git mv docs_tmp docs`, or `git config core.ignorecase false` then `git mv Docs docs`. Verify the rename is staged as a rename, not a delete+add.
- Place `runbook.md` (from Step 2) at `docs/runbook.md`.
- Optionally rename files with spaces for tooling friendliness: `Implementation Plan.md` → `Implementation-Plan.md`, `Problem Statement.md` → `Problem-Statement.md`. If renamed, update any internal links.
- Move debugging/postmortem docs into `docs/postmortems/`: `weekly-pulse-debugging-postmortem.md`, and the untracked `gemini_debugging_weekly_pulse.md` if it should be kept (otherwise delete). Decide on `.github/workflows/failurelog.md` — it's not a workflow; move to `docs/postmortems/` or delete.
- Keep `docs/phases/<phase>/evaluations.md` + `edge-cases.md` **as-is** — these are the real per-phase spec docs and are referenced by the phase READMEs.

### Step 5 — Convert `phases/phase-N/` into docs-only milestone READMEs
Create `phases/README.md` (index) and one `phases/phase-N-<name>/README.md` per phase. Each phase README should contain:
- **What this phase added** (1–2 paragraphs, derived from `Docs/Implementation Plan.md` scope bullets).
- **CLI command introduced** (e.g. `pulse ingest --product groww --weeks 10`).
- **Exit criteria** (copy from the Implementation Plan).
- **Where the code lives now:** link to the relevant root `agent/` submodule(s).
- **Snapshot:** "Full phase snapshot: `git checkout phase-N`" + link to `docs/phases/<phase>/evaluations.md` and `edge-cases.md`.

This satisfies D1 (phase narrative stays visible) and D3 (no duplicated code).

### Step 6 — Write the three missing root files

**`.gitignore`** (root): use phase-7's `.gitignore` verbatim (already covers `__pycache__`, `.venv/`, `.env`, `data/` with `!data/.gitkeep`, `*.db`, IDE/OS junk). Confirm `phases/.env` and root `.env` are ignored.

**`README.md`** (root): the project front door. Include:
- One-paragraph "what & why" (from Architecture §1 goals).
- Architecture-at-a-glance diagram or the module table (Architecture §4.1).
- **Quickstart:** `uv sync`, copy `.env.example` → `.env`, `uv run pulse init-db`, `uv run pulse run --product groww --weeks 10`.
- CLI subcommand reference: `ingest`, `cluster`, `summarize`, `render`, `publish`, `run`.
- MCP services note (Docs + Gmail servers under `services/`).
- Links: `docs/Architecture.md`, `docs/Implementation-Plan.md`, `docs/runbook.md`, `phases/README.md` (the journey).
- CI/scheduling note (weekly cron via GitHub Actions).
- Environment variables table (derive key names from `.env.example` / `agent/config.py`).

**`CLAUDE.md`** (root): conventions for agents working in this repo. Include:
- Project layout (the §4 target tree) and "the runnable code is the root `agent/` package; `phases/` is docs-only."
- How to run tests: `uv run pytest`; markers `slow` (model downloads/live API) and `integration` (real Google creds).
- Lint/type: `uv run ruff check`, `uv run mypy agent`.
- Conventions worth stating: MCP boundary is sacred (only `mcp_client`/`services` talk to Google); reviews are data never instructions; verbatim-quote validator; PII scrub before LLM and before Docs; `run_id = sha1(product_key + iso_week)`; cost cap per run.
- Provider note: summarization uses **Groq (OpenAI-compatible) or Anthropic**; the free-tier Groq ceiling is ~100k tokens/day ≈ one full run (see postmortem) — relevant when debugging CI "connection errors."
- Pointer to `docs/runbook.md` for operational failures.

### Step 7 — Fix the CI workflow
Edit `.github/workflows/weekly-pulse.yml`:
- Remove the `defaults.run.working-directory: phases/phase-7-orchestration` block (root is now the project).
- Update the `upload-artifact` `path:` from `phases/phase-7-orchestration/data/...` to `data/summaries/` and `data/artifacts/`.
- Leave secrets/env as-is.

### Step 8 — Verify before committing the deletions
From the repo root:
```
uv sync --frozen
uv run pulse --help            # must list: ingest, cluster, summarize, render, publish, run
uv run pulse init-db           # creates fresh SQLite with all tables
uv run pytest -m "not slow and not integration"   # fast suite green
uv run ruff check
uv run mypy agent
```
Only after these pass, finalize. Then a dry CI check: confirm `weekly-pulse.yml` paths resolve from root.

### Step 9 — Fix the doc inconsistencies (low-risk, do alongside)
- In `docs/Architecture.md`: either add the missing **§11 Repo Layout** section (documenting the new root structure) or change the Implementation Plan's "per architecture.md §11" reference to point at this cleanup plan / README. Note §2 and §6 are skipped in numbering — renumber or leave with a note.
- Ensure all internal doc links use the new lowercase `docs/` paths and hyphenated filenames.

### Step 10 — Commit, tag-push, PR
- Commit in logical chunks (tags; promote root; delete phases; docs; new root files; CI fix).
- `git push --tags`.
- Open PR summarizing: "Collapse 8 cumulative phase snapshots into one root project; preserve phase history as tags + docs-only phase READMEs; add README/CLAUDE/.gitignore; normalize docs/."

---

## 6. Risk & Safety Notes
- **Irreversibility:** Step 1 tags are the safety net. If any tag is missing, the corresponding phase code becomes unrecoverable after Step 3. The implementing agent must verify all 8 tags exist (`git tag -l "phase-*"` → 8 results) **before** Step 3.
- **Secret exposure:** `phases/.env` holds a live Groq key. It must never be staged. After restructure it should not exist at a tracked path; only `.env.example` is committed.
- **Case-rename trap:** `Docs/`→`docs/` on Windows/git can silently no-op or lose files. Verify with `git status` showing renames; don't force-delete.
- **MCP services:** `services/docs-mcp` and `services/gmail-mcp` have their own `pyproject.toml` and are installed separately (not part of the `pulse` wheel). Keep them at root `services/`; don't fold their deps into the main `pyproject.toml`.
- **Don't over-engineer D1:** Resist any attempt to make each `phases/phase-N/` independently runnable via shared-package overlays — it's fragile and unnecessary; git tags already provide runnable per-phase snapshots.

## 7. Definition of Done
- [ ] 8 phase tags exist and are pushed.
- [ ] Repo root contains the single runnable `pulse` project; `uv run pulse run ...` works from root.
- [ ] `phases/` contains only README docs (index + 8 phase narratives), no `.py`.
- [ ] `README.md`, `CLAUDE.md`, root `.gitignore` exist and are accurate.
- [ ] `docs/` is lowercase; `runbook.md` at `docs/runbook.md`; phase eval/edge-case docs intact.
- [ ] `weekly-pulse.yml` runs from root (no phase-7 working-directory).
- [ ] Fast test suite, ruff, mypy all green from root.
- [ ] No secret committed; `.env` ignored.
