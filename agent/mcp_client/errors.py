"""Custom exceptions for MCP session and tool call failures."""


class MCPConnectionError(Exception):
    """Raised when the MCP server subprocess cannot be started or the connection drops."""


class MCPToolMissing(Exception):
    """Raised during handshake when a required tool is absent from the server's tool list."""


class MCPPermissionError(Exception):
    """Raised when a tool call returns an HTTP 403 / permission-denied error."""


class MCPResponseError(Exception):
    """Raised when a tool call returns an unexpected or malformed response."""


class MCPAuthError(Exception):
    """Raised when the MCP server reports an authentication/token failure."""
