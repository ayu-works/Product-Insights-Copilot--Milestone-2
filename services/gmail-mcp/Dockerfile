FROM python:3.11-slim

RUN pip install uv --no-cache-dir

WORKDIR /app
COPY pyproject.toml .
RUN uv sync --no-dev --no-install-project

COPY server.py .

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8002
CMD ["python", "server.py", "--transport", "sse", "--port", "8002"]
