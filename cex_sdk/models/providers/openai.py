"""
cex_sdk.models.providers.openai -- OpenAI GPT provider.

CEX version: 7.1.0 | Pillar: P02 | 8F: CALL (F5)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel

from cex_sdk.models.base import Model
from cex_sdk.models.message import Message
from cex_sdk.models.response import ModelResponse
from cex_sdk.utils.timer import Timer


@dataclass
class GPT(Model):
    """OpenAI GPT models."""

    id: str = "gpt-4o"
    provider: str = "OpenAI"
    api_key: Optional[str] = None

    def _get_client(self):
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("pip install openai")
        import os
        return OpenAI(api_key=self.api_key or os.environ.get("OPENAI_API_KEY"))

    def _format_messages(self, messages: List[Message]) -> List[Dict[str, str]]:
        return [{"role": m.role, "content": m.get_content_string()} for m in messages]

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
        timer = Timer().start()

        call_params: Dict[str, Any] = {
            "model": self.id,
            "messages": self._format_messages(messages),
        }
        if self.max_tokens:
            call_params["max_tokens"] = self.max_tokens
        if self.temperature is not None:
            call_params["temperature"] = self.temperature
        if tools:
            call_params["tools"] = tools
        if tool_choice:
            call_params["tool_choice"] = tool_choice

        response = client.chat.completions.create(**call_params)
        choice = response.choices[0]

        tool_calls = []
        if choice.message.tool_calls:
            for tc in choice.message.tool_calls:
                tool_calls.append({
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": json.loads(tc.function.arguments) if isinstance(tc.function.arguments, str) else tc.function.arguments,
                    },
                })

        usage = {
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }

        return ModelResponse(
            role="assistant",
            content=choice.message.content or "",
            tool_calls=tool_calls,
            response_usage=self._make_metrics(usage, timer),
            input_tokens=usage["input_tokens"],
            output_tokens=usage["output_tokens"],
            total_tokens=usage["total_tokens"],
        )
