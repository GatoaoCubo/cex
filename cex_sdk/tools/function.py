"""
cex_sdk.tools.function -- Function wrapper with auto JSON Schema.

Absorbed from: agno/tools/function.py (1328 lines -> streamlined)
CEX version: 7.2.0 | Pillar: P04 | 8F: CALL (F5)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

import inspect
import json
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, get_type_hints

from cex_sdk.utils.log import log_error

# Python type -> JSON Schema type
_TYPE_MAP = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
    type(None): "null",
}


def _python_type_to_json_schema(tp: Any) -> Dict[str, Any]:
    """Convert a Python type annotation to JSON Schema."""
    origin = getattr(tp, "__origin__", None)
    if origin is list:
        args = getattr(tp, "__args__", ())
        items = _python_type_to_json_schema(args[0]) if args else {}
        return {"type": "array", "items": items}
    if origin is dict:
        return {"type": "object"}
    if tp in _TYPE_MAP:
        return {"type": _TYPE_MAP[tp]}
    return {"type": "string"}


@dataclass
class Function:
    """A callable function exposed to an LLM as a tool.

    Auto-generates JSON Schema from type hints and docstring.
    """

    name: str = ""
    description: str = ""
    parameters: Dict[str, Any] = field(default_factory=dict)
    entrypoint: Optional[Callable] = None

    # CEX-specific
    kind: str = "function_de"
    pillar: str = "P04"

    def __post_init__(self):
        if self.entrypoint and not self.name:
            self.name = self.entrypoint.__name__
        if self.entrypoint and not self.description:
            self.description = inspect.getdoc(self.entrypoint) or ""
        if self.entrypoint and not self.parameters:
            self.parameters = self._infer_parameters()

    def _infer_parameters(self) -> Dict[str, Any]:
        """Infer JSON Schema parameters from function signature."""
        if not self.entrypoint:
            return {}

        sig = inspect.signature(self.entrypoint)
        hints = get_type_hints(self.entrypoint) if self.entrypoint else {}

        properties: Dict[str, Any] = {}
        required: List[str] = []

        for param_name, param in sig.parameters.items():
            if param_name in ("sel", "cls", "run_context"):
                continue

            prop = _python_type_to_json_schema(hints.get(param_name, str))

            # Extract param description from docstring
            doc = inspect.getdoc(self.entrypoint) or ""
            for line in doc.split("\n"):
                stripped = line.strip()
                if stripped.startswith(f"{param_name}:") or stripped.startswith(f"{param_name} "):
                    prop["description"] = stripped.split(":", 1)[-1].strip() if ":" in stripped else stripped
                    break

            properties[param_name] = prop

            if param.default is inspect.Parameter.empty:
                required.append(param_name)

        schema: Dict[str, Any] = {
            "type": "object",
            "properties": properties,
        }
        if required:
            schema["required"] = required
        return schema

    def to_tool_schema(self) -> Dict[str, Any]:
        """Return the OpenAI/Anthropic-compatible tool schema."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description[:1024] if self.description else "",
                "parameters": self.parameters,
            },
        }

    def execute(self, **kwargs: Any) -> str:
        """Execute the function with given arguments."""
        if not self.entrypoint:
            return json.dumps({"error": f"No entrypoint for {self.name}"})
        try:
            result = self.entrypoint(**kwargs)
            if isinstance(result, str):
                return result
            return json.dumps(result, default=str)
        except Exception as e:
            log_error(f"Error executing {self.name}: {e}")
            return json.dumps({"error": str(e)})

    async def aexecute(self, **kwargs: Any) -> str:
        """Async execute."""
        if not self.entrypoint:
            return json.dumps({"error": f"No entrypoint for {self.name}"})
        import asyncio
        if asyncio.iscoroutinefunction(self.entrypoint):
            result = await self.entrypoint(**kwargs)
        else:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, lambda: self.entrypoint(**kwargs))
        return result if isinstance(result, str) else json.dumps(result, default=str)

    @classmethod
    def from_callable(cls, fn: Callable, **kwargs: Any) -> Function:
        """Create a Function from any callable."""
        return cls(entrypoint=fn, **kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "description": self.description, "parameters": self.parameters}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Function:
        return cls(name=data["name"], description=data.get("description", ""), parameters=data.get("parameters", {}))
