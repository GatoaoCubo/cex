"""
cex_sdk.models.response -- Model response and tool execution dataclasses.

Absorbed from: agno/models/response.py
CEX version: 7.1.0
Pillar: P02 (Model)
8F function: CALL (F5)

# Originally from agno (https://github.com/agno-agi/agno)
# Licensed under MPL-2.0. Modified for CEX integration.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from time import time
from typing import Any, Dict, List, Optional

from cex_sdk.models.metrics import MessageMetrics, ToolCallMetrics


class ModelResponseEvent(str, Enum):
    tool_call_started = "ToolCallStarted"
    tool_call_completed = "ToolCallCompleted"
    assistant_response = "AssistantResponse"
    compression_started = "CompressionStarted"
    compression_completed = "CompressionCompleted"
    model_request_started = "ModelRequestStarted"
    model_request_completed = "ModelRequestCompleted"


@dataclass
class ToolExecution:
    """Result of executing a single tool call."""
    tool_call_id: Optional[str] = None
    tool_name: Optional[str] = None
    tool_args: Optional[Dict[str, Any]] = None
    tool_call_error: Optional[bool] = None
    result: Optional[str] = None
    metrics: Optional[ToolCallMetrics] = None
    stop_after_tool_call: bool = False
    requires_confirmation: Optional[bool] = None
    confirmed: Optional[bool] = None
    created_at: int = field(default_factory=lambda: int(time()))

    @property
    def is_paused(self) -> bool:
        return bool(self.requires_confirmation)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if self.metrics is not None:
            d["metrics"] = self.metrics.to_dict()
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ToolExecution:
        return cls(
            tool_call_id=data.get("tool_call_id"),
            tool_name=data.get("tool_name"),
            tool_args=data.get("tool_args"),
            tool_call_error=data.get("tool_call_error"),
            result=data.get("result"),
            stop_after_tool_call=data.get("stop_after_tool_call", False),
            requires_confirmation=data.get("requires_confirmation"),
            confirmed=data.get("confirmed"),
            metrics=ToolCallMetrics.from_dict(data["metrics"]) if data.get("metrics") else None,
        )


@dataclass
class ModelResponse:
    """Response from an LLM provider."""
    role: Optional[str] = None
    content: Optional[Any] = None
    parsed: Optional[Any] = None
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    tool_executions: Optional[List[ToolExecution]] = field(default_factory=list)
    event: str = ModelResponseEvent.assistant_response.value
    reasoning_content: Optional[str] = None
    response_usage: Optional[MessageMetrics] = None
    created_at: int = field(default_factory=lambda: int(time()))

    # Token summaries (for model_request_completed events)
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None
    time_to_first_token: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if self.tool_executions:
            d["tool_executions"] = [te.to_dict() for te in self.tool_executions]
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ModelResponse:
        if data.get("tool_executions"):
            data["tool_executions"] = [ToolExecution.from_dict(te) for te in data["tool_executions"]]
        if data.get("response_usage") and isinstance(data["response_usage"], dict):
            data["response_usage"] = MessageMetrics.from_dict(data["response_usage"])
        return cls(**data)
