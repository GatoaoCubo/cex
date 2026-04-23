"""
cex_sdk.models.providers.ollama -- Local Ollama models.

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


@dataclass
class Ollama(Model):
    """Local Ollama models."""

    id: str = "llama3.1"
    provider: str = "Ollama"
    host: str = "http://localhost:11434"

    def _get_client(self):
        try:
            import ollama
        except ImportError:
            raise ImportError("pip install ollama")
        return ollama.Client(host=self.host)

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
        params: Dict[str, Any] = {"model": self.id, "messages": formatted}
        if tools:
            params["tools"] = tools

        response = client.chat(**params)

        usage = {
            "input_tokens": getattr(response, "prompt_eval_count", 0) or 0,
            "output_tokens": getattr(response, "eval_count", 0) or 0,
            "total_tokens": (getattr(response, "prompt_eval_count", 0) or 0)
                          + (getattr(response, "eval_count", 0) or 0),
        }

        content = response.message.content if hasattr(response, "message") else str(response)

        return ModelResponse(
            role="assistant",
            content=content,
            response_usage=self._make_metrics(usage, timer),
            input_tokens=usage["input_tokens"],
            output_tokens=usage["output_tokens"],
        )

    def invoke_stream(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Iterator[ModelResponse]:
        client = self._get_client()
        formatted = [{"role": m.role, "content": m.get_content_string()} for m in messages]
        stream = client.chat(model=self.id, messages=formatted, stream=True)
        for chunk in stream:
            if hasattr(chunk, "message"):
                yield ModelResponse(role="assistant", content=chunk.message.content or "")
