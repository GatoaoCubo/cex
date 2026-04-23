"""
cex_sdk.models.providers.openrouter -- OpenRouter multi-provider.

CEX version: 7.1.0 | Pillar: P02 | 8F: CALL (F5)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel

from cex_sdk.models.base import Model
from cex_sdk.models.message import Message
from cex_sdk.models.response import ModelResponse
from cex_sdk.utils.timer import Timer


@dataclass
class OpenRouter(Model):
    """OpenRouter -- access 200+ models via one API key."""

    id: str = "anthropic/claude-sonnet-4"
    provider: str = "OpenRouter"
    api_key: Optional[str] = None
    base_url: str = "https://openrouter.ai/api/v1"

    def _get_client(self):
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("pip install openai")
        import os
        return OpenAI(
            api_key=self.api_key or os.environ.get("OPENROUTER_API_KEY"),
            base_url=self.base_url,
        )

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

        formatted = [{"role": m.role, "content": m.get_content_string()} for m in messages]
        call_params: Dict[str, Any] = {"model": self.id, "messages": formatted}
        if self.max_tokens:
            call_params["max_tokens"] = self.max_tokens
        if self.temperature is not None:
            call_params["temperature"] = self.temperature
        if tools:
            call_params["tools"] = tools

        response = client.chat.completions.create(**call_params)
        choice = response.choices[0]

        usage = {
            "input_tokens": response.usage.prompt_tokens if response.usage else 0,
            "output_tokens": response.usage.completion_tokens if response.usage else 0,
            "total_tokens": response.usage.total_tokens if response.usage else 0,
        }

        return ModelResponse(
            role="assistant",
            content=choice.message.content or "",
            response_usage=self._make_metrics(usage, timer),
            input_tokens=usage["input_tokens"],
            output_tokens=usage["output_tokens"],
            total_tokens=usage["total_tokens"],
        )
