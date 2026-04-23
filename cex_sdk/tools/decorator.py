"""
cex_sdk.tools.decorator -- @cex_tool decorator for registering tools.

CEX version: 7.2.0 | Pillar: P04 | 8F: CALL (F5)
"""

from __future__ import annotations

from functools import wraps
from typing import Any, Callable, Optional


def cex_tool(
    name: Optional[str] = None,
    description: Optional[str] = None,
    kind: str = "function_de",
    pillar: str = "P04",
) -> Callable:
    """Decorator to mark a method as an LLM-callable tool.

    Usage:
        class MyTools(Toolkit):
            @cex_tool(name="search", kind="function_de")
            def search(self, query: str) -> str:
                '''Search the CEX index.'''
                return do_search(query)
    """

    def decorator(fn: Callable) -> Callable:
        fn._cex_tool_meta = {
            "name": name or fn.__name__,
            "description": description or (fn.__doc__ or "").strip().split("\n")[0],
            "kind": kind,
            "pillar": pillar,
        }

        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return fn(*args, **kwargs)

        wrapper._cex_tool_meta = fn._cex_tool_meta
        return wrapper

    return decorator
