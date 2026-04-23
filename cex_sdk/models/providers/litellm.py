"""
cex_sdk.models.providers.litellm -- Universal LLM fallback via LiteLLM.

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
class LiteLLM(Model):
    """Universal fallback -- supports 100+ providers via litellm."""

    id: str = "gpt-4o"
    provider: str = "LiteLLM"

    def invoke(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[Union[str, Dict[str, Any]]] = None,
        response_model: Optional[Type[BaseModel]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        try:
            import litellm
        except ImportError:
            raise ImportError("pip install litellm")

        timer = Timer().start()
        formatted = [{"role": m.role, "content": m.get_content_string()} for m in messages]

        call_params: Dict[str, Any] = {"model": self.id, "messages": formatted}
        if self.max_tokens:
            call_params["max_tokens"] = self.max_tokens
        if self.temperature is not None:
            call_params["temperature"] = self.temperature
        if tools:
            call_params["tools"] = tools

        response = litellm.completion(**call_params)
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
        )
