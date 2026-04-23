"""
cex_sdk.models.message -- Message dataclass for LLM conversations.

Absorbed from: agno/models/message.py
CEX version: 7.1.0
Pillar: P02 (Model)
8F function: CALL (F5)

# Originally from agno (https://github.com/agno-agi/agno)
# Licensed under MPL-2.0. Modified for CEX integration.
"""

from __future__ import annotations

import json
from time import time
from typing import Any, Dict, List, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from cex_sdk.models.metrics import MessageMetrics


class MessageReferences(BaseModel):
    """References added to user message for RAG."""
    query: str
    references: Optional[List[Union[Dict[str, Any], str]]] = None
    time: Optional[float] = None


class Citations(BaseModel):
    """Citations for the message."""
    raw: Optional[Any] = None
    search_queries: Optional[List[str]] = None
    urls: Optional[List[Dict[str, Any]]] = None
    documents: Optional[List[Dict[str, Any]]] = None


class Message(BaseModel):
    """Message sent to / received from an LLM."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    role: str  # system | user | assistant | tool
    content: Optional[Union[List[Any], str]] = None
    compressed_content: Optional[str] = None
    name: Optional[str] = None
    tool_call_id: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None

    # Reasoning
    reasoning_content: Optional[str] = None

    # Provider-specific data
    provider_data: Optional[Dict[str, Any]] = None

    # Citations
    citations: Optional[Citations] = None

    # --- Not sent to API ---
    tool_name: Optional[str] = None
    tool_args: Optional[Any] = None
    tool_call_error: Optional[bool] = None
    stop_after_tool_call: bool = False
    from_history: bool = False
    metrics: MessageMetrics = Field(default_factory=MessageMetrics)
    references: Optional[MessageReferences] = None
    created_at: int = Field(default_factory=lambda: int(time()))
    temporary: bool = False

    model_config = ConfigDict(extra="allow", arbitrary_types_allowed=True)

    def get_content_string(self) -> str:
        if isinstance(self.content, str):
            return self.content
        if isinstance(self.content, list):
            if len(self.content) > 0 and isinstance(self.content[0], dict) and "text" in self.content[0]:
                return self.content[0].get("text", "")
            return json.dumps(self.content)
        return ""

    def content_is_valid(self) -> bool:
        return self.content is not None and len(self.content) > 0

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "id": self.id,
            "role": self.role,
            "content": self.content,
            "name": self.name,
            "tool_call_id": self.tool_call_id,
            "tool_calls": self.tool_calls,
            "reasoning_content": self.reasoning_content,
            "created_at": self.created_at,
        }
        return {k: v for k, v in d.items() if v is not None}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Message:
        if "metrics" in data and isinstance(data["metrics"], dict):
            data["metrics"] = MessageMetrics.from_dict(data["metrics"])
        return cls(**data)
