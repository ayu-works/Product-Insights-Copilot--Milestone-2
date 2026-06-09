# Phase 0 — Foundations & Scaffolding: Edge Cases

## What We Must Survive

---

### EC0-1: SQLite File Already Exists

**Scenario:** `pulse init-db` is run a second time on an existing database that already has rows.

**Expected behaviour:**
- No tables are dropped or recreated.
- Existing rows are preserved.
- Command exits 0 with a log line: `"db already initialised, skipping"`.

**How to verify:** Insert a dummy row into `products`, re-run `init-db`, confirm the row still exists.

---

### EC0-2: Missing `.env` File

**Scenario:** `.env` file does not exist at startup.

**Expected behaviour:**
- Agent starts normally using defaults and env vars already exported in the shell.
- A warning is logged: `".env not found, using environment variables only"`.
- Does NOT raise `FileNotFoundError`.

---

### EC0-3: Malformed `products.yaml`

**Scenario:** `products.yaml` has a product entry missing the required `key` field.

**Expected behaviour:**
- `pydantic-settings` raises a `ValidationError` with a human-readable message naming the missing field.
- The agent exits with code 1 before doing any work.
- No partial state is written to the database.

---

### EC0-4: Invalid `LOG_LEVEL` Env Var

**Scenario:** `LOG_LEVEL=VERBOSE` (not a valid Python logging level).

**Expected behaviour:**
- Falls back to `INFO` with a warning log: `"Unknown LOG_LEVEL 'VERBOSE', defaulting to INFO"`.
- Does NOT crash.

---

### EC0-5: `PULSE_DB_PATH` Points to a Read-Only Directory

**Scenario:** `PULSE_DB_PATH=/etc/pulse/pulse.db` on a system where `/etc/pulse/` is not writable.

**Expected behaviour:**
- `init-db` raises a clear `PermissionError` with the path in the message.
- Does NOT create a fallback database silently in a different location.

---

### EC0-6: Concurrent `init-db` Calls

**Scenario:** Two processes run `pulse init-db` simultaneously on the same file.

**Expected behaviour:**
- SQLite's built-in locking serialises the writes.
- Both processes exit 0; no corruption, no duplicate tables.

---

### EC0-7: Windows Path Separators

**Scenario:** Project runs on Windows (this project's development environment is Windows 11).

**Expected behaviour:**
- All file paths in `config.py` and `storage.py` use `pathlib.Path` rather than string concatenation, so forward/backward slash differences are handled automatically.
- `data/raw/`, `data/summaries/`, `data/artifacts/` directories are created with `mkdir(parents=True, exist_ok=True)`.

---

### EC0-8: Python Version Mismatch

**Scenario:** Developer has Python 3.10 installed but `pyproject.toml` requires `>=3.11`.

**Expected behaviour:**
- `uv` shows a clear error: `"Requires Python >=3.11, found 3.10"`.
- No cryptic `ImportError` at runtime.
