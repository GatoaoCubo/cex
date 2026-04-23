"""
cex_sdk.tools.mcp.client -- MCP (Model Context Protocol) client bridge.

Absorbed from: agno/tools/mcp/mcp.py
CEX version: 10.1.0 | Pillar: P04 | 8F: CALL (F5)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from typing import Any

from cex_sdk.tools.function import Function
from cex_sdk.tools.toolkit import Toolkit
from cex_sdk.utils.log import log_debug, log_error


class MCPTools(Toolkit):
    """Connect to an MCP server and expose its tools as CEX Functions.

    Usage:
        async with MCPTools(url="https://example.com/mcp") as tools:
            schemas = tools.get_tool_schemas()
            result = await tools.aexecute("tool_name", arg1="value")
    """

    def __init__(self, url: str, name: str = "mcp", timeout: int = 30):
        super().__init__(name=name, auto_register=False)
        self.url = url
        self.timeout = timeout
        self._session = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()

    async def connect(self) -> None:
        """Connect to MCP server and discover tools."""
        try:
            from mcp import ClientSession
            from mcp.client.streamable_http import streamablehttp_client
        except ImportError:
            raise ImportError("pip install mcp")

        transport = streamablehttp_client(self.url)
        read, write, _ = await transport.__aenter__()
        self._session = ClientSession(read, write)
        await self._session.__aenter__()
        await self._session.initialize()

        # Discover tools
        result = await self._session.list_tools()
        for tool in result.tools:
            fn = Function(
                name=tool.name,
                description=tool.description or "",
                parameters=tool.inputSchema if hasattr(tool, "inputSchema") else {},
            )
            self.functions[fn.name] = fn
            log_debug(f"MCP tool discovered: {fn.name}")

    async def disconnect(self) -> None:
        if self._session:
            await self._session.__aexit__(None, None, None)
            self._session = None

    async def aexecute(self, name: str, **kwargs: Any) -> str:
        """Execute an MCP tool."""
        if not self._session:
            return '{"error": "Not connected to MCP server"}'
        try:
            result = await self._session.call_tool(name, kwargs)
            if hasattr(result, "content"):
                return str(result.content[0].text if result.content else "")
            return str(result)
        except Exception as e:
            log_error(f"MCP tool {name} error: {e}")
            return f'{{"error": "{e}"}}'
