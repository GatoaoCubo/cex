"""
cex_sdk.memory.compression -- Context compression for tool outputs.

Absorbed from: agno/compression/manager.py (283 lines)
CEX version: 9.3.0 | Pillar: P10 | 8F: INJECT (F3)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from cex_sdk.utils.log import log_debug

DEFAULT_COMPRESSION_PROMPT = """\
You are compressing tool call results to save context space while preserving critical information.

ALWAYS PRESERVE:
* Specific facts: numbers, statistics, amounts, prices, quantities, metrics
* Temporal data: dates, times, timestamps (use short format: "Oct 21 2025")
* Entities: people, companies, products, locations, organizations
* Identifiers: URLs, IDs, codes, technical identifiers, versions
* Key quotes, citations, sources

COMPRESS TO ESSENTIALS:
* Descriptions: keep only key attributes
* Explanations: distill to core insight
* Lists: focus on most relevant items
* Background: minimal context only if critical

REMOVE ENTIRELY:
* Introductions, conclusions, transitions
* Hedging language ("might", "possibly", "appears to")
* Meta-commentary ("According to", "The results show")
* Formatting artifacts (markdown, HTML, JSON structure)
* Redundant or repetitive information
* Promotional language, filler words

Be concise while retaining all critical facts.
"""


@dataclass
class CompressionManager:
    """Compress tool outputs to save context window space.

    Uses an LLM to intelligently summarize long tool results.
    Falls back to truncation if no model is available.
    """

    model: Optional[Any] = None  # cex_sdk.models.base.Model
    compress_limit: int = 4000   # chars before compression triggers
    token_limit: int = 1000      # target compressed size in tokens
    instructions: Optional[str] = None
    stats: Dict[str, Any] = field(default_factory=dict)

    def compress(self, content: str, context: str = "") -> str:
        """Compress content if it exceeds the limit.

        Args:
            content: The text to compress.
            context: Optional context about what the agent is doing.

        Returns:
            Compressed text, or original if under limit.
        """
        if len(content) <= self.compress_limit:
            return content

        original_len = len(content)

        if self.model:
            return self._llm_compress(content, context)

        # Fallback: simple truncation with head + tail
        compressed = self._truncate(content)
        self._track(original_len, len(compressed))
        return compressed

    def _llm_compress(self, content: str, context: str) -> str:
        """Compress using LLM."""
        from cex_sdk.models.message import Message

        prompt = self.instructions or DEFAULT_COMPRESSION_PROMPT
        if context:
            prompt += f"\n\nAgent context: {context}"

        messages = [
            Message(role="system", content=prompt),
            Message(role="user", content=f"Compress this:\n\n{content}"),
        ]

        try:
            response = self.model.invoke(messages)
            compressed = response.content or content
            self._track(len(content), len(compressed))
            log_debug(f"Compressed {len(content)} -> {len(compressed)} chars")
            return compressed
        except Exception as e:
            log_debug(f"Compression failed: {e}, falling back to truncation")
            return self._truncate(content)

    def _truncate(self, content: str, ratio: float = 0.3) -> str:
        """Simple truncation: keep first and last portions."""
        target = int(self.compress_limit * ratio)
        half = target // 2
        return f"{content[:half]}\n\n[... {len(content) - target} chars compressed ...]\n\n{content[-half:]}"

    def _track(self, original: int, compressed: int) -> None:
        self.stats["total_original"] = self.stats.get("total_original", 0) + original
        self.stats["total_compressed"] = self.stats.get("total_compressed", 0) + compressed
        self.stats["compressions"] = self.stats.get("compressions", 0) + 1
