"""
Base Agent — abstract class for all background processing agents.
Validator, Deduplicator, and Enricher extend this.
"""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from cex_discovery_pipeline.core.context_engine import ContextConfig
from cex_discovery_pipeline.miners.base_miner import BusinessRecord

logger = logging.getLogger(__name__)


@dataclass
class AgentResult:
    """Output from a background agent."""

    agent_name: str
    processed_count: int = 0
    modified_count: int = 0
    rejected_count: int = 0
    execution_time_seconds: float = 0.0
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class BaseAgent(ABC):
    """
    Abstract base for background processing agents.
    Subclasses implement process_batch().
    """

    AGENT_NAME: str = "base_agent"

    def __init__(self, context: ContextConfig):
        self.context = context

    @abstractmethod
    async def process_batch(
        self, records: list[BusinessRecord]
    ) -> tuple[list[BusinessRecord], AgentResult]:
        """
        Process a batch of records. Returns (processed_records, result).
        Implementations may modify, filter, or enrich records.
        """
        ...

    async def run(self, records: list[BusinessRecord]) -> tuple[list[BusinessRecord], AgentResult]:
        """Execute with timing and error handling."""
        start = time.monotonic()
        try:
            processed, result = await self.process_batch(records)
        except Exception as exc:
            logger.error("[%s] Fatal error: %s", self.AGENT_NAME, exc)
            result = AgentResult(
                agent_name=self.AGENT_NAME,
                errors=[str(exc)],
            )
            processed = records  # pass through on failure
        result.execution_time_seconds = time.monotonic() - start
        logger.info(
            "[%s] Done: %d processed, %d modified, %d rejected, %.1fs",
            self.AGENT_NAME, result.processed_count,
            result.modified_count, result.rejected_count,
            result.execution_time_seconds,
        )
        return processed, result
