"""
cex_sdk.models.base -- Abstract base class for all LLM providers.

Absorbed from: agno/models/base.py (3051 lines -> streamlined to ~200)
CEX version: 7.1.0
Pillar: P02 (Model)
8F function: CALL (F5)

# Originally from agno (https://github.com/agno-agi/agno)
# Licensed under MPL-2.0. Modified for CEX integration.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional, Type, Union

try:
    from pydantic import BaseModel
except ImportError:
    BaseModel = None  # pydantic optional; pip install cex-tools[sdk-core]

from cex_sdk.models.message import Message
from cex_sdk.models.metrics import MessageMetrics, ModelType
from cex_sdk.models.response import ModelResponse
from cex_sdk.utils.timer import Timer


@dataclass
class Model(ABC):
    """Abstract base for all LLM providers.

    Subclasses implement invoke() and optionally invoke_stream().
    """

    id: str
    name: Optional[str] = None
    provider: Optional[str] = None
    model_type: ModelType = ModelType.MODEL

    # Generation parameters
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    stop: Optional[List[str]] = None

    # System prompt injected by model
    system_prompt: Optional[str] = None

    # Tool control
    _tool_choice: Optional[Union[str, Dict[str, Any]]] = None

    # Structured output
    response_format: Optional[Any] = None

    # Retry config
    max_retries: int = 3
    retry_delay: float = 1.0

    def get_provider(self) -> str:
        return self.provider or self.__class__.__name__

    @abstractmethod
    def invoke(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[Union[str, Dict[str, Any]]] = None,
        response_model: Optional[Type[BaseModel]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Send messages to LLM and return response (sync)."""
        ...

    def invoke_stream(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Iterator[ModelResponse]:
        """Stream responses from LLM. Default falls back to invoke()."""
        yield self.invoke(messages, tools=tools, **kwargs)

    async def ainvoke(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        response_model: Optional[Type[BaseModel]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Async invoke. Default wraps sync in thread."""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: self.invoke(messages, tools=tools, response_model=response_model, **kwargs),
        )

    def _build_params(self, **overrides: Any) -> Dict[str, Any]:
        """Build provider-specific parameters dict."""
        params: Dict[str, Any] = {"model": self.id}
        if self.temperature is not None:
            params["temperature"] = self.temperature
        if self.max_tokens is not None:
            params["max_tokens"] = self.max_tokens
        if self.top_p is not None:
            params["top_p"] = self.top_p
        if self.stop:
            params["stop"] = self.stop
        params.update(overrides)
        return params

    def _make_metrics(self, usage: Dict[str, Any], timer: Timer) -> MessageMetrics:
        """Create MessageMetrics from provider usage dict + timer."""
        timer.stop()
        return MessageMetrics(
            input_tokens=usage.get("input_tokens", 0) or usage.get("prompt_tokens", 0),
            output_tokens=usage.get("output_tokens", 0) or usage.get("completion_tokens", 0),
            total_tokens=usage.get("total_tokens", 0),
            cache_read_tokens=usage.get("cache_read_input_tokens", 0) or usage.get("cache_read_tokens", 0),
            cache_write_tokens=usage.get("cache_creation_input_tokens", 0) or usage.get("cache_write_tokens", 0),
            duration=timer.elapsed,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, provider={self.get_provider()!r})"
