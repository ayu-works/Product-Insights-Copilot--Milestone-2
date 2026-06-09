import sqlite3
from pathlib import Path

import structlog

log = structlog.get_logger()

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    key          TEXT PRIMARY KEY,
    display      TEXT NOT NULL,
    appstore_id  TEXT,
    play_package TEXT,
    gdoc_id      TEXT,
    gmail_to     TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS reviews (
    id           TEXT PRIMARY KEY,
    product_key  TEXT NOT NULL,
    source       TEXT NOT NULL CHECK (source IN ('appstore', 'playstore')),
    rating       INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title        TEXT,
    body         TEXT NOT NULL DEFAULT '',
    posted_at    DATETIME NOT NULL,
    version      TEXT,
    language     TEXT NOT NULL DEFAULT 'en',
    country      TEXT NOT NULL DEFAULT 'IN',
    ingested_at  DATETIME NOT NULL,
    raw_json     TEXT
);

CREATE TABLE IF NOT EXISTS review_embeddings (
    review_id  TEXT PRIMARY KEY,
    embedding  BLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS runs (
    id               TEXT PRIMARY KEY,
    product_key      TEXT NOT NULL,
    iso_week         TEXT NOT NULL,
    window_start     DATE NOT NULL,
    window_end       DATE NOT NULL,
    status           TEXT NOT NULL DEFAULT 'created',
    metrics_json     TEXT,
    gdoc_heading_id  TEXT,
    gmail_message_id TEXT
);

CREATE TABLE IF NOT EXISTS themes (
    id                             TEXT PRIMARY KEY,
    run_id                         TEXT NOT NULL,
    rank                           INTEGER NOT NULL,
    label                          TEXT NOT NULL,
    description                    TEXT NOT NULL,
    sentiment                      TEXT NOT NULL CHECK (sentiment IN ('negative', 'mixed', 'positive')),
    review_count                   INTEGER NOT NULL,
    representative_review_ids_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS clusters (
    id                             TEXT PRIMARY KEY,
    run_id                         TEXT NOT NULL,
    cluster_label                  INTEGER NOT NULL,
    review_ids_json                TEXT NOT NULL DEFAULT '[]',
    keyphrases_json                TEXT NOT NULL DEFAULT '[]',
    medoid_review_id               TEXT NOT NULL,
    representative_review_ids_json TEXT NOT NULL DEFAULT '[]'
);

CREATE INDEX IF NOT EXISTS idx_reviews_product_key ON reviews (product_key);
CREATE INDEX IF NOT EXISTS idx_reviews_posted_at   ON reviews (posted_at);
CREATE INDEX IF NOT EXISTS idx_runs_product_week   ON runs (product_key, iso_week);
CREATE INDEX IF NOT EXISTS idx_themes_run_id       ON themes (run_id);
CREATE INDEX IF NOT EXISTS idx_clusters_run_id     ON clusters (run_id);
"""


def get_connection(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn


def init_db(db_path: Path) -> None:
    conn = get_connection(db_path)
    try:
        with conn:
            conn.executescript(SCHEMA)
        log.info("db_initialised", path=str(db_path))
    finally:
        conn.close()


def table_names(db_path: Path) -> set[str]:
    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
        return {row["name"] for row in rows}
    finally:
        conn.close()
