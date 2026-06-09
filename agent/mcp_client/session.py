"""MCP session management — stdio transport (FastMCP subprocess).

Usage:
    async with open_docs_session(command) as session:
        result = await session.call_tool("docs_get_document", {"doc_id": "..."})

The session validates tool schemas at handshake time (E5-7 / E6-7).
For SSE transport (production), swap stdio_client for sse_client and pass
the server URL instead of a command string.
"""

from __future__ import annotations

import shlex
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from agent.mcp_client.errors import MCPConnectionError, MCPToolMissing

log = structlog.get_logger()

_DOCS_REQUIRED_TOOLS = frozenset({
    "docs_get_document",
    "docs_batch_update",
    "docs_create_document",
    "docs_search_documents",
})

_GMAIL_REQUIRED_TOOLS = frozenset({
    "gmail_search_messages",
    "gmail_create_draft",
    "gmail_send_message",
    "gmail_modify_labels",
    "gmail_create_label",
})


@asynccontextmanager
async def open_docs_session(command: str) -> AsyncIterator[ClientSession]:
    """Open a validated MCP session to the Docs FastMCP server."""
    async with _open_session(command, _DOCS_REQUIRED_TOOLS, "docs") as session:
        yield session


@asynccontextmanager
async def open_gmail_session(command: str) -> AsyncIterator[ClientSession]:
    """Open a validated MCP session to the Gmail FastMCP server."""
    async with _open_session(command, _GMAIL_REQUIRED_TOOLS, "gmail") as session:
        yield session


@asynccontextmanager
async def _open_session(
    command: str,
    required_tools: frozenset[str],
    label: str,
) -> AsyncIterator[ClientSession]:
    """Connect to an MCP server via stdio, validate tools, yield the session.

    E5-7 / E6-7: raises MCPToolMissing("<tool>") if any required tool is absent.
    EC5-2 / EC6-1: raises MCPConnectionError if the subprocess fails to start.
    """
    parts = shlex.split(command)
    params = StdioServerParameters(command=parts[0], args=parts[1:])

    try:
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                tools_resp = await session.list_tools()
                available = {t.name for t in tools_resp.tools}

                for tool in required_tools:
                    if tool not in available:
                        raise MCPToolMissing(
                            f"{label} MCP server is missing required tool: {tool!r}. "
                            f"Available tools: {sorted(available)}"
                        )

                log.info(
                    "mcp_session_ready",
                    server=label,
                    tools=sorted(available),
                )
                yield session

    except (MCPToolMissing, MCPConnectionError):
        raise
    except Exception as exc:
        raise MCPConnectionError(
            f"Could not start {label} MCP server ({command!r}): {exc}"
        ) from exc
