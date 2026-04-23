"""
cex_sdk.tools.toolkit -- Base class for tool collections.

Absorbed from: agno/tools/toolkit.py (382 lines -> streamlined)
CEX version: 7.2.0 | Pillar: P04 | 8F: CALL (F5)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from collections import OrderedDict
from inspect import getmembers, ismethod
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from cex_sdk.tools.function import Function
from cex_sdk.utils.log import log_debug


class Toolkit:
    """Base class for tool collections.

    Subclass and add methods -- they auto-register as LLM tools.
    Use @cex_tool decorator or set auto_register=True.

    Usage:
        class MyTools(Toolkit):
            def search(self, query: str) -> str:
                '''Search the index.'''
                return do_search(query)

        tools = MyTools(name="search_tools")
        schemas = tools.get_tool_schemas()  # For LLM tool_use
    """

    def __init__(
        self,
        name: str = "toolkit",
        tools: Sequence[Union[Callable, Function]] = (),
        instructions: Optional[str] = None,
        include_tools: Optional[List[str]] = None,
        exclude_tools: Optional[List[str]] = None,
        auto_register: bool = True,
    ):
        self.name = name
        self.functions: Dict[str, Function] = OrderedDict()
        self.instructions = instructions
        self._include = set(include_tools) if include_tools else None
        self._exclude = set(exclude_tools) if exclude_tools else set()

        # Register explicit tools
        for tool in tools:
            if isinstance(tool, Function):
                self._register(tool)
            elif callable(tool):
                self._register(Function.from_callable(tool))

        # Auto-register decorated methods
        if auto_register and not tools:
            self._auto_register()

    def _should_include(self, name: str) -> bool:
        if name.startswith("_"):
            return False
        if name in self._exclude:
            return False
        if self._include is not None:
            return name in self._include
        return True

    def _register(self, fn: Function) -> None:
        if self._should_include(fn.name):
            self.functions[fn.name] = fn
            log_debug(f"Registered tool: {self.name}.{fn.name}")

    def _auto_register(self) -> None:
        """Auto-discover and register public methods as tools."""
        for method_name, method in getmembers(self, predicate=ismethod):
            if method_name.startswith("_"):
                continue
            if method_name in ("get_tool_schemas", "execute", "get_instructions"):
                continue
            if not self._should_include(method_name):
                continue

            # Check for @cex_tool decorator
            if hasattr(method, "_cex_tool_meta"):
                meta = method._cex_tool_meta
                fn = Function(
                    name=meta.get("name", method_name),
                    description=meta.get("description", ""),
                    entrypoint=method,
                    kind=meta.get("kind", "function_de"),
                )
            else:
                fn = Function.from_callable(method)
            self._register(fn)

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        """Return all tool schemas for LLM tool_use."""
        return [fn.to_tool_schema() for fn in self.functions.values()]

    def execute(self, name: str, **kwargs: Any) -> str:
        """Execute a tool by name."""
        fn = self.functions.get(name)
        if not fn:
            return f'{{"error": "Unknown tool: {name}"}}'
        return fn.execute(**kwargs)

    async def aexecute(self, name: str, **kwargs: Any) -> str:
        """Async execute a tool by name."""
        fn = self.functions.get(name)
        if not fn:
            return f'{{"error": "Unknown tool: {name}"}}'
        return await fn.aexecute(**kwargs)

    def get_instructions(self) -> Optional[str]:
        return self.instructions

    def __len__(self) -> int:
        return len(self.functions)

    def __repr__(self) -> str:
        tools = ", ".join(self.functions.keys())
        return f"Toolkit(name={self.name!r}, tools=[{tools}])"
