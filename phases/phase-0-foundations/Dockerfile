FROM python:3.11-slim AS builder

RUN pip install uv --no-cache-dir

WORKDIR /app
COPY pyproject.toml .

# Install only runtime dependencies (no dev group)
RUN uv sync --no-dev --no-install-project

# ---- runtime image ----
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY . .

ENV PATH="/app/.venv/bin:$PATH"
ENV PULSE_DB_PATH=/data/pulse.db

VOLUME ["/data"]

ENTRYPOINT ["pulse"]
CMD ["--help"]
