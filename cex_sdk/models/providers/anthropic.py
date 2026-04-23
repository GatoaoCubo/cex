"""
cex_sdk.models.providers.anthropic -- Claude provider.

CEX version: 7.1.0 | Pillar: P02 | 8F: CALL (F5)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional, Type, Union

from pydantic import BaseModel

from cex_sdk.models.base import Model
from cex_sdk.models.message import Message
from cex_sdk.models.response import ModelResponse
from cex_sdk.utils.timer import Timer


def _resolve_claude_default() -> str:
    """Resolve default Claude model via model resolver."""
    try:
        from _tools.cex_model_resolver import get_model_string
        return get_model_string("n03")
    except Exception:
        return "claude-sonnet-4-6"


@dataclass
class Claude(Model):
    """Anthropic Claude models."""

    id: str = ""
    provider: str = "Anthropic"
    max_tokens: int = 8192
    api_key: Optional[str] = None

    def __post_init__(self):
        if not self.id:
            self.id = _resolve_claude_default()

    def _get_client(self):
        try:
            import anthropic
        except ImportError:
            raise ImportError("pip install anthropic")
        import os
        key = self.api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        return anthropic.Anthropic(api_key=key)

    def _format_messages(self, messages: List[Message]):
        system = None
        formatted = []
        for m in messages:
            if m.role == "system":
                system = m.get_content_string()
            else:
                formatted.append({"role": m.role, "content": m.get_content_string()})
        return system, formatted

    def invoke(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[Union[str, Dict[str, Any]]] = None,
        response_model: Optional[Type[BaseModel]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        client = self._get_client()
        system, formatted = self._format_messages(messages)
        timer = Timer().start()

        params = self._build_params(**kwargs)
        params.pop("model")
        call_params: Dict[str, Any] = {
            "model": self.id,
            "messages": formatted,
            "max_tokens": params.pop("max_tokens", self.max_tokens),
        }
        if system:
            call_params["system"] = system
        if self.temperature is not None:
            call_params["temperature"] = self.temperature
        if tools:
            call_params["tools"] = tools
        if tool_choice:
            call_params["tool_choice"] = tool_choice

        response = client.messages.create(**call_params)

        content = ""
        tool_calls = []
        for block in response.content:
            if block.type == "text":
                content += block.text
            elif block.type == "tool_use":
                tool_calls.append({
                    "id": block.id,
                    "type": "function",
                    "function": {"name": block.name, "arguments": block.input},
                })

        usage = {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
            "cache_read_input_tokens": getattr(response.usage, "cache_read_input_tokens", 0),
            "cache_creation_input_tokens": getattr(response.usage, "cache_creation_input_tokens", 0),
        }

        return ModelResponse(
            role="assistant",
            content=content,
            tool_calls=tool_calls,
            response_usage=self._make_metrics(usage, timer),
            input_tokens=usage["input_tokens"],
            output_tokens=usage["output_tokens"],
            total_tokens=usage["total_tokens"],
        )

    def invoke_stream(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Iterator[ModelResponse]:
        client = self._get_client()
        system, formatted = self._format_messages(messages)
        timer = Timer().start()

        call_params: Dict[str, Any] = {
            "model": self.id,
            "messages": formatted,
            "max_tokens": self.max_tokens,
        }
        if system:
            call_params["system"] = system
        if tools:
            call_params["tools"] = tools

        with client.messages.stream(**call_params) as stream:
            for text in stream.text_stream:
                yield ModelResponse(role="assistant", content=text)

            final = stream.get_final_message()

        usage = {
            "input_tokens": final.usage.input_tokens,
            "output_tokens": final.usage.output_tokens,
            "total_tokens": final.usage.input_tokens + final.usage.output_tokens,
        }
        yield ModelResponse(
            role="assistant",
            content="",
            response_usage=self._make_metrics(usage, timer),
        )
