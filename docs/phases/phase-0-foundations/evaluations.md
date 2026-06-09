# Phase 0 — Foundations & Scaffolding: Evaluations

## How We Prove It Works

---

### E0-1: CLI Help Output

**What to run:**
```bash
uv run pulse --help
```

**Pass condition:**
- Exits with code 0.
- Output lists all subcommands: `ingest`, `cluster`, `summarize`, `render`, `publish`, `run`, `init-db`.
- Each subcommand has a one-line description.

---

### E0-2: Database Initialization

**What to run:**
```bash
uv run pulse init-db
```

**Pass condition:**
- A fresh SQLite file is created at the configured path (default: `data/pulse.db`).
- Running `.tables` via `sqlite3` returns exactly: `products`, `reviews`, `review_embeddings`, `runs`, `themes`.
- Running `PRAGMA table_info(reviews)` returns all columns defined in `architecture.md §5`.
- Re-running `init-db` on an existing database is a no-op (idempotent — uses `CREATE TABLE IF NOT EXISTS`).

---

### E0-3: Config Loading

**What to run:**
```bash
uv run pulse config-check
```
(or a unit test that instantiates `agent/config.py`)

**Pass condition:**
- `products.yaml` is parsed correctly into a list of `ProductConfig` objects.
- Each product has: `key`, `display`, `appstore_id`, `play_package`, `gmail_to`.
- Missing required fields in `products.yaml` raise a descriptive `ValidationError`, not a silent `None`.
- `.env` overrides are applied (e.g., `PULSE_DB_PATH` overrides the default db path).

---

### E0-4: run_id Determinism

**What to test (unit test):**
```python
assert run_id("groww", "2026-W16") == run_id("groww", "2026-W16")
assert run_id("groww", "2026-W16") != run_id("groww", "2026-W17")
assert run_id("groww", "2026-W16") != run_id("indmoney", "2026-W16")
```

**Pass condition:**
- Same inputs always produce the same 40-char hex SHA-1 string.
- Different product or week always produces a different string.

---

### E0-5: ISO-Week Window Helper

**What to test (unit test):**
```python
w = Window.from_iso_week("2026-W16")
assert w.start == date(2026, 4, 13)
assert w.end == date(2026, 4, 19)
assert w.weeks == 1
```

**Pass condition:**
- `Window.from_iso_week` returns correct Monday–Sunday boundaries in IST-aware date objects.
- `Window.last_n_weeks(10)` returns a window covering the 10 most recent complete ISO weeks relative to today.

---

### E0-6: CI Pipeline

**What to check:**
- Push a commit; GitHub Actions workflow runs automatically.

**Pass condition:**
- `ruff check .` exits 0 (no lint errors).
- `mypy agent/` exits 0 (no type errors on the skeleton).
- `pytest tests/` exits 0 with at least 2 smoke tests passing:
  - `test_init_db_creates_all_tables`
  - `test_run_id_is_deterministic`

---

### E0-7: Structured Logging

**What to test:**
- Instantiate the logger and emit a log line; capture stdout.

**Pass condition:**
- Log output is valid JSON (structlog JSON renderer).
- Every log line contains `run_id` when emitted inside a run context.
- Log level is configurable via `LOG_LEVEL` env var.
