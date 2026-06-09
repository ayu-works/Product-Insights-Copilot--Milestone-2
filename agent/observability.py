"""OpenTelemetry tracing for the orchestrator (Phase 7).

Spans are best-effort: if the OTLP endpoint is unreachable (EC7-7), export
failures are caught and logged as warnings — the pipeline must keep running.
Set ``PULSE_OTEL_EXPORTER_ENDPOINT`` to enable export; otherwise spans are
recorded in-process only (no export attempted).
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Iterator

import structlog

log = structlog.get_logger()

_MAX_EXPORT_FAILURES = 3
_export_failures = 0
_tracer: Any = None


def _get_tracer() -> Any:
    """Lazily build a tracer. Returns None if the OTel SDK is unavailable."""
    global _tracer
    if _tracer is not None:
        return _tracer

    try:
        from opentelemetry import trace
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        from agent.config import settings

        provider = TracerProvider(resource=Resource.create({"service.name": "pulse-orchestrator"}))

        endpoint = getattr(settings, "otel_exporter_endpoint", None)
        if endpoint:
            from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

            exporter = OTLPSpanExporter(endpoint=endpoint)
            provider.add_span_processor(_GuardedBatchSpanProcessor(exporter))

        trace.set_tracer_provider(provider)
        _tracer = trace.get_tracer("pulse.orchestrator")
    except Exception as exc:  # pragma: no cover - defensive: OTel SDK missing/misconfigured
        log.warning("otel_init_failed", error=str(exc))
        _tracer = False

    return _tracer or None


class _GuardedBatchSpanProcessor:
    """Wraps BatchSpanProcessor so export failures never crash the pipeline (EC7-7)."""

    def __init__(self, exporter: Any) -> None:
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        self._inner = BatchSpanProcessor(exporter)

    def on_start(self, span: Any, parent_context: Any = None) -> None:
        self._inner.on_start(span, parent_context)

    def on_end(self, span: Any) -> None:
        global _export_failures
        if _export_failures >= _MAX_EXPORT_FAILURES:
            return
        try:
            self._inner.on_end(span)
        except Exception as exc:
            _export_failures += 1
            log.warning(
                "otel_export_failed",
                error=str(exc),
                attempt=_export_failures,
                msg="Traces lost but run continues.",
            )

    def shutdown(self) -> None:
        try:
            self._inner.shutdown()
        except Exception as exc:
            log.warning("otel_shutdown_failed", error=str(exc))

    def force_flush(self, timeout_millis: int = 30_000) -> bool:
        try:
            return bool(self._inner.force_flush(timeout_millis))
        except Exception:
            return False


@contextmanager
def span(name: str, **attributes: Any) -> Iterator[None]:
    """Open an OTel span named e.g. ``pulse.ingest`` or ``mcp.docs.batch_update``.

    No-ops gracefully if the OTel SDK isn't available or export is failing —
    spans are local-only in that case (EC7-7: traces lost but run continues).
    """
    tracer = _get_tracer()
    if tracer is None:
        yield
        return

    with tracer.start_as_current_span(name) as otel_span:
        for key, value in attributes.items():
            otel_span.set_attribute(key, value)
        try:
            yield
        except Exception as exc:
            otel_span.record_exception(exc)
            otel_span.set_attribute("error", True)
            raise
