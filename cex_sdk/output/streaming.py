"""
cex_sdk.output.streaming -- Streaming output configuration and chunk handling.

kind: streaming_config
pillar: P05
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterator


class StreamMode(str, Enum):
    TEXT = "text"
    JSON = "json"
    SSE = "sse"  # Server-Sent Events
    WEBSOCKET = "websocket"


@dataclass
class StreamChunk:
    """Single unit from a streaming response."""
    index: int
    content: str
    delta: str = ""
    done: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class StreamingConfig:
    """
    kind: streaming_config
    pillar: P05
    Controls how LLM output is streamed to consumers.
    """
    mode: StreamMode = StreamMode.TEXT
    chunk_size: int = 256
    buffer_size: int = 4096
    timeout_ms: int = 30000
    heartbeat_ms: int = 5000
    include_usage: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def chunk_text(self, text: str) -> Iterator[StreamChunk]:
        """Split text into StreamChunks for simulated streaming."""
        words = text.split()
        buffer: list[str] = []
        idx = 0
        for i, word in enumerate(words):
            buffer.append(word)
            if len(" ".join(buffer)) >= self.chunk_size or i == len(words) - 1:
                chunk_text = " ".join(buffer)
                yield StreamChunk(
                    index=idx,
                    content=chunk_text,
                    delta=chunk_text,
                    done=(i == len(words) - 1),
                )
                buffer = []
                idx += 1
