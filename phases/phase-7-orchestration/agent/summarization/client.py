"""LLM client abstraction: Anthropic + OpenAI backends, cost tracking, caps."""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from typing import Any, Optional, Protocol, runtime_checkable

import structlog

log = structlog.get_logger()

# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class PulseCostExceeded(Exception):
    """Raised when the per-run LLM token or cost cap is exceeded."""

    def __init__(self, message: str, partial_themes: list | None = None) -> None:
        super().__init__(message)
        self.partial_themes: list = partial_themes or []


class LLMSchemaError(Exception):
    """Raised when the LLM consistently returns invalid / schema-mismatched JSON."""


# ---------------------------------------------------------------------------
# Cost pricing table (USD per 1k tokens)
# ---------------------------------------------------------------------------

_PRICING: dict[str, tuple[float, float]] = {
    # Anthropic
    "claude-haiku-4-5-20251001": (0.00025, 0.00125),
    "claude-haiku-4-5":          (0.00025, 0.00125),
    "claude-sonnet-4-6":         (0.003,   0.015),
    "claude-opus-4-7":           (0.015,   0.075),
    # OpenAI
    "gpt-4o-mini":               (0.00015, 0.0006),
    "gpt-4o":                    (0.005,   0.015),
    # Groq  (prices as of 2026-05)
    "llama-3.3-70b-versatile":   (0.00059, 0.00079),
    "llama-3.1-8b-instant":      (0.00005, 0.00008),
    "llama3-70b-8192":           (0.00059, 0.00079),
    "mixtral-8x7b-32768":        (0.00027, 0.00027),
    "gemma2-9b-it":              (0.00020, 0.00020),
}


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

@dataclass
class RunMetrics:
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost_usd: float = 0.0
    call_count: int = 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "llm_tokens_prompt":     self.total_input_tokens,
            "llm_tokens_completion": self.total_output_tokens,
            "llm_cost_usd":          round(self.total_cost_usd, 6),
            "llm_calls":             self.call_count,
        }


# ---------------------------------------------------------------------------
# Protocol
# ---------------------------------------------------------------------------

@runtime_checkable
class LLMClient(Protocol):
    def call_structured(
        self,
        system: str,
        user: str,
        schema_name: str,
        schema: dict[str, Any],
    ) -> dict[str, Any]: ...

    @property
    def metrics(self) -> RunMetrics: ...


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _extract_json(raw: str) -> dict[str, Any]:
    """Strip prose wrapper and parse JSON. Raises ValueError if impossible."""
    # Try direct parse first
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    # Try extracting {...} block (EC3-1)
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError(f"No JSON object found in LLM response: {raw[:200]!r}")


# ---------------------------------------------------------------------------
# Anthropic backend
# ---------------------------------------------------------------------------

class AnthropicLLMClient:
    _MAX_RETRIES = 3
    _BACKOFF_SECS = (5.0, 10.0, 20.0)  # EC3-4

    def __init__(
        self,
        model: str = "claude-haiku-4-5-20251001",
        api_key: Optional[str] = None,
        max_cost_usd: float = 1.0,
        max_tokens_per_run: int = 100_000,
    ) -> None:
        from anthropic import Anthropic  # type: ignore[import-untyped]

        self._client = Anthropic(api_key=api_key)
        self._model = model
        self._max_cost = max_cost_usd
        self._max_tokens = max_tokens_per_run
        self._metrics = RunMetrics()

    @property
    def metrics(self) -> RunMetrics:
        return self._metrics

    def _check_cap(self) -> None:
        total = self._metrics.total_input_tokens + self._metrics.total_output_tokens
        if total >= self._max_tokens:
            raise PulseCostExceeded(
                f"Token limit {self._max_tokens} exceeded at {total} tokens"
            )
        if self._metrics.total_cost_usd >= self._max_cost:
            raise PulseCostExceeded(
                f"Cost limit ${self._max_cost} exceeded at ${self._metrics.total_cost_usd:.4f}"
            )

    def _record(self, input_tokens: int, output_tokens: int) -> None:
        in_rate, out_rate = _PRICING.get(self._model, (0.003, 0.015))
        cost = (input_tokens / 1000) * in_rate + (output_tokens / 1000) * out_rate
        self._metrics.total_input_tokens += input_tokens
        self._metrics.total_output_tokens += output_tokens
        self._metrics.total_cost_usd += cost
        self._metrics.call_count += 1
        log.debug(
            "llm_call_done",
            model=self._model,
            in_tok=input_tokens,
            out_tok=output_tokens,
            call_cost=round(cost, 6),
            run_cost=round(self._metrics.total_cost_usd, 6),
        )

    def call_structured(
        self,
        system: str,
        user: str,
        schema_name: str,
        schema: dict[str, Any],
    ) -> dict[str, Any]:
        self._check_cap()

        tool: dict[str, Any] = {
            "name": schema_name,
            "description": f"Return structured {schema_name} result",
            "input_schema": schema,
        }
        last_exc: Exception = RuntimeError("No attempts made")

        for attempt in range(self._MAX_RETRIES):
            try:
                response = self._client.messages.create(
                    model=self._model,
                    max_tokens=2048,
                    system=system,
                    messages=[{"role": "user", "content": user}],
                    tools=[tool],
                    tool_choice={"type": "tool", "name": schema_name},
                )
                self._record(response.usage.input_tokens, response.usage.output_tokens)
                for block in response.content:
                    if block.type == "tool_use":
                        return dict(block.input)
                raise LLMSchemaError("No tool_use block in response")
            except PulseCostExceeded:
                raise
            except LLMSchemaError as exc:
                last_exc = exc
                log.warning("llm_schema_error", attempt=attempt + 1, error=str(exc))
            except Exception as exc:
                last_exc = exc
                err_str = str(exc).lower()
                is_rate_limit = "429" in err_str or "rate" in err_str or "timeout" in err_str
                wait = self._BACKOFF_SECS[min(attempt, len(self._BACKOFF_SECS) - 1)]
                log.warning(
                    "llm_retry",
                    attempt=attempt + 1,
                    error=str(exc),
                    wait=wait,
                    rate_limit=is_rate_limit,
                )
                if attempt < self._MAX_RETRIES - 1:
                    time.sleep(wait)

        raise LLMSchemaError(
            f"LLM call '{schema_name}' failed after {self._MAX_RETRIES} retries: {last_exc}"
        )


# ---------------------------------------------------------------------------
# OpenAI backend (OpenAI-compatible: also works with Groq)
# ---------------------------------------------------------------------------

class OpenAILLMClient:
    _MAX_RETRIES = 3
    _BACKOFF_SECS = (5.0, 10.0, 20.0)

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        max_cost_usd: float = 1.0,
        max_tokens_per_run: int = 100_000,
    ) -> None:
        from openai import OpenAI  # type: ignore[import-untyped]

        self._client = OpenAI(api_key=api_key, base_url=base_url)
        self._model = model
        self._max_cost = max_cost_usd
        self._max_tokens = max_tokens_per_run
        self._metrics = RunMetrics()

    @property
    def metrics(self) -> RunMetrics:
        return self._metrics

    def _check_cap(self) -> None:
        total = self._metrics.total_input_tokens + self._metrics.total_output_tokens
        if total >= self._max_tokens:
            raise PulseCostExceeded(
                f"Token limit {self._max_tokens} exceeded at {total} tokens"
            )
        if self._metrics.total_cost_usd >= self._max_cost:
            raise PulseCostExceeded(
                f"Cost limit ${self._max_cost} exceeded at ${self._metrics.total_cost_usd:.4f}"
            )

    def _record(self, usage: Any) -> None:
        in_tok = getattr(usage, "prompt_tokens", 0)
        out_tok = getattr(usage, "completion_tokens", 0)
        in_rate, out_rate = _PRICING.get(self._model, (0.003, 0.015))
        cost = (in_tok / 1000) * in_rate + (out_tok / 1000) * out_rate
        self._metrics.total_input_tokens += in_tok
        self._metrics.total_output_tokens += out_tok
        self._metrics.total_cost_usd += cost
        self._metrics.call_count += 1

    def call_structured(
        self,
        system: str,
        user: str,
        schema_name: str,
        schema: dict[str, Any],
    ) -> dict[str, Any]:
        self._check_cap()
        last_exc: Exception = RuntimeError("No attempts made")

        for attempt in range(self._MAX_RETRIES):
            try:
                response = self._client.chat.completions.create(
                    model=self._model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    max_tokens=2048,
                )
                self._record(response.usage)
                raw = response.choices[0].message.content or ""
                return _extract_json(raw)
            except PulseCostExceeded:
                raise
            except (ValueError, json.JSONDecodeError) as exc:
                last_exc = exc
                log.warning("llm_json_parse_error", attempt=attempt + 1, error=str(exc))
            except Exception as exc:
                last_exc = exc
                wait = self._BACKOFF_SECS[min(attempt, len(self._BACKOFF_SECS) - 1)]
                log.warning("llm_retry", attempt=attempt + 1, wait=wait, error=str(exc))
                if attempt < self._MAX_RETRIES - 1:
                    time.sleep(wait)

        raise LLMSchemaError(
            f"LLM call '{schema_name}' failed after {self._MAX_RETRIES} retries: {last_exc}"
        )


# ---------------------------------------------------------------------------
# Groq backend  (OpenAI-compatible, uses openai SDK with Groq base URL)
# ---------------------------------------------------------------------------

_GROQ_BASE_URL = "https://api.groq.com/openai/v1"


class GroqLLMClient:
    """Groq-hosted open-source models via OpenAI-compatible chat completions."""

    _MAX_RETRIES = 3
    _BACKOFF_SECS = (5.0, 10.0, 20.0)

    def __init__(
        self,
        model: str = "llama-3.3-70b-versatile",
        api_key: Optional[str] = None,
        max_cost_usd: float = 1.0,
        max_tokens_per_run: int = 100_000,
    ) -> None:
        from openai import OpenAI  # type: ignore[import-untyped]

        self._client = OpenAI(api_key=api_key, base_url=_GROQ_BASE_URL)
        self._model = model
        self._max_cost = max_cost_usd
        self._max_tokens = max_tokens_per_run
        self._metrics = RunMetrics()

    @property
    def metrics(self) -> RunMetrics:
        return self._metrics

    def _check_cap(self) -> None:
        total = self._metrics.total_input_tokens + self._metrics.total_output_tokens
        if total >= self._max_tokens:
            raise PulseCostExceeded(
                f"Token limit {self._max_tokens} exceeded at {total} tokens"
            )
        if self._metrics.total_cost_usd >= self._max_cost:
            raise PulseCostExceeded(
                f"Cost limit ${self._max_cost} exceeded at ${self._metrics.total_cost_usd:.4f}"
            )

    def _record(self, usage: Any) -> None:
        in_tok = getattr(usage, "prompt_tokens", 0)
        out_tok = getattr(usage, "completion_tokens", 0)
        in_rate, out_rate = _PRICING.get(self._model, (0.00059, 0.00079))
        cost = (in_tok / 1000) * in_rate + (out_tok / 1000) * out_rate
        self._metrics.total_input_tokens += in_tok
        self._metrics.total_output_tokens += out_tok
        self._metrics.total_cost_usd += cost
        self._metrics.call_count += 1
        log.debug(
            "llm_call_done",
            model=self._model,
            in_tok=in_tok,
            out_tok=out_tok,
            call_cost=round(cost, 6),
            run_cost=round(self._metrics.total_cost_usd, 6),
        )

    def call_structured(
        self,
        system: str,
        user: str,
        schema_name: str,
        schema: dict[str, Any],
    ) -> dict[str, Any]:
        self._check_cap()
        last_exc: Exception = RuntimeError("No attempts made")

        for attempt in range(self._MAX_RETRIES):
            try:
                response = self._client.chat.completions.create(
                    model=self._model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": system + " Always respond with valid JSON."},
                        {"role": "user", "content": user},
                    ],
                    max_tokens=2048,
                )
                self._record(response.usage)
                raw = response.choices[0].message.content or ""
                return _extract_json(raw)
            except PulseCostExceeded:
                raise
            except (ValueError, json.JSONDecodeError) as exc:
                last_exc = exc
                log.warning("llm_json_parse_error", attempt=attempt + 1, error=str(exc))
            except Exception as exc:
                last_exc = exc
                wait = self._BACKOFF_SECS[min(attempt, len(self._BACKOFF_SECS) - 1)]
                log.warning(
                    "llm_retry",
                    provider="groq",
                    model=self._model,
                    attempt=attempt + 1,
                    wait=wait,
                    error=str(exc),
                )
                if attempt < self._MAX_RETRIES - 1:
                    time.sleep(wait)

        raise LLMSchemaError(
            f"Groq call '{schema_name}' failed after {self._MAX_RETRIES} retries: {last_exc}"
        )


# ---------------------------------------------------------------------------
# Mock client for tests
# ---------------------------------------------------------------------------

class MockLLMClient:
    """Returns pre-canned responses in order. Supports simulated cost cap."""

    def __init__(
        self,
        responses: list[dict[str, Any]],
        tokens_per_call: int = 100,
        fail_after_calls: Optional[int] = None,
    ) -> None:
        self._responses = list(responses)
        self._idx = 0
        self._tokens = tokens_per_call
        self._fail_after = fail_after_calls
        self._metrics = RunMetrics()
        self._last_system: str = ""
        self._last_user: str = ""

    @property
    def metrics(self) -> RunMetrics:
        return self._metrics

    def call_structured(
        self,
        system: str,
        user: str,
        schema_name: str,
        schema: dict[str, Any],
    ) -> dict[str, Any]:
        self._last_system = system
        self._last_user = user

        if self._fail_after is not None and self._metrics.call_count >= self._fail_after:
            total = self._metrics.total_input_tokens + self._metrics.total_output_tokens
            raise PulseCostExceeded(
                f"Token limit {self._fail_after * self._tokens} exceeded at {total} tokens"
            )

        if self._idx >= len(self._responses):
            raise IndexError(
                f"MockLLMClient: responses exhausted at call #{self._idx} "
                f"(schema={schema_name})"
            )

        result = self._responses[self._idx]
        self._idx += 1
        self._metrics.call_count += 1
        self._metrics.total_input_tokens += self._tokens
        self._metrics.total_output_tokens += self._tokens // 2
        in_rate, out_rate = _PRICING.get("claude-haiku-4-5-20251001", (0.00025, 0.00125))
        self._metrics.total_cost_usd += (
            (self._tokens / 1000) * in_rate + (self._tokens / 2 / 1000) * out_rate
        )
        return result
