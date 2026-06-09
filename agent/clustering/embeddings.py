"""Embedding providers and on-disk cache keyed by sha1(text)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

import numpy as np
import structlog

log = structlog.get_logger()

_EMBED_BATCH_SIZE = 100


# ---------------------------------------------------------------------------
# Provider protocol
# ---------------------------------------------------------------------------

@runtime_checkable
class EmbeddingProvider(Protocol):
    @property
    def name(self) -> str: ...
    @property
    def dimensions(self) -> int: ...
    def embed_batch(self, texts: list[str]) -> list[list[float]]: ...


# ---------------------------------------------------------------------------
# Providers
# ---------------------------------------------------------------------------

class OpenAIEmbeddingProvider:
    _MODEL = "text-embedding-3-small"

    def __init__(self, api_key: str | None = None) -> None:
        from openai import OpenAI  # type: ignore[import-untyped]
        self._client = OpenAI(api_key=api_key)

    @property
    def name(self) -> str:
        return "openai"

    @property
    def dimensions(self) -> int:
        return 1536

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        resp = self._client.embeddings.create(model=self._MODEL, input=texts)
        return [item.embedding for item in resp.data]


class LocalEmbeddingProvider:
    _MODEL = "BAAI/bge-small-en-v1.5"

    def __init__(self) -> None:
        from sentence_transformers import SentenceTransformer  # type: ignore[import-untyped]
        self._model = SentenceTransformer(self._MODEL)

    @property
    def name(self) -> str:
        return "local"

    @property
    def dimensions(self) -> int:
        return 384

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        vecs: Any = self._model.encode(texts, show_progress_bar=False)
        return vecs.tolist()


def get_provider(provider_name: str, api_key: str | None = None) -> EmbeddingProvider:
    if provider_name == "openai":
        return OpenAIEmbeddingProvider(api_key=api_key)
    if provider_name == "local":
        return LocalEmbeddingProvider()
    raise ValueError(f"Unknown embedding provider: {provider_name!r}")


# ---------------------------------------------------------------------------
# On-disk cache  (sha1(text) → float list, stored as JSON)
# ---------------------------------------------------------------------------

class EmbeddingCache:
    def __init__(self, cache_path: Path) -> None:
        self._path = cache_path
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._data: dict[str, list[float]] = {}
        self._dirty = False
        self._load()

    def _load(self) -> None:
        if not self._path.exists():
            return
        try:
            with self._path.open("r", encoding="utf-8") as fh:
                self._data = json.load(fh)
        except Exception as exc:
            log.warning("cache_load_failed", path=str(self._path), error=str(exc))
            self._data = {}

    @staticmethod
    def _key(text: str) -> str:
        return hashlib.sha1(text.encode()).hexdigest()

    def get(self, text: str) -> list[float] | None:
        return self._data.get(self._key(text))

    def set(self, text: str, embedding: list[float]) -> None:
        self._data[self._key(text)] = embedding
        self._dirty = True

    def flush(self) -> None:
        if not self._dirty:
            return
        tmp = self._path.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(self._data, fh)
        tmp.replace(self._path)
        self._dirty = False

    def __len__(self) -> int:
        return len(self._data)


# ---------------------------------------------------------------------------
# Batch embed with cache
# ---------------------------------------------------------------------------

def embed_reviews(
    texts: list[str],
    provider: EmbeddingProvider,
    cache: EmbeddingCache,
) -> tuple[np.ndarray, int, int]:
    """Embed *texts* using *provider*, consulting *cache* first.

    Returns (embeddings_array, cache_hits, cache_misses).
    embeddings_array shape: (len(texts), provider.dimensions)
    """
    result: list[list[float] | None] = [None] * len(texts)
    to_embed: list[tuple[int, str]] = []
    hits = 0

    for i, text in enumerate(texts):
        cached = cache.get(text)
        if cached is not None:
            result[i] = cached
            hits += 1
        else:
            to_embed.append((i, text))

    misses = len(to_embed)
    log.info("embedding_cache_lookup", hits=hits, misses=misses)

    if to_embed:
        for batch_start in range(0, len(to_embed), _EMBED_BATCH_SIZE):
            batch = to_embed[batch_start : batch_start + _EMBED_BATCH_SIZE]
            batch_idx = batch_start // _EMBED_BATCH_SIZE + 1
            total_batches = (len(to_embed) + _EMBED_BATCH_SIZE - 1) // _EMBED_BATCH_SIZE
            try:
                vecs = provider.embed_batch([t for _, t in batch])
            except Exception as exc:
                raise RuntimeError(
                    f"Embedding failed at batch {batch_idx}/{total_batches}: {exc}"
                ) from exc
            for (idx, text), vec in zip(batch, vecs):
                result[idx] = vec
                cache.set(text, vec)
        cache.flush()
        log.info("embedding_cache_hits", embedding_cache_hits=hits, embedding_cache_misses=misses)

    arr = np.array([v for v in result if v is not None], dtype=np.float32)
    return arr, hits, misses
