"""
Base Miner — abstract class for all discovery mining techniques.
Every miner (Tier 1 premium + Tier 2 support) extends this.
"""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from cex_discovery_pipeline.core.context_engine import ContextConfig

logger = logging.getLogger(__name__)


@dataclass
class BusinessRecord:
    """Single discovered business entry."""

    name: str = ""
    phone: str = ""
    address: str = ""
    city: str = ""
    state: str = "SP"
    cep: str = ""
    category: str = ""
    subcategory: str = ""
    source: str = ""
    source_url: str = ""
    rating: float = 0.0
    review_count: int = 0
    hours: str = ""
    website: str = ""
    email: str = ""
    cnpj: str = ""
    social_facebook: str = ""
    social_instagram: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    confidence: float = 0.0
    raw_data: dict[str, Any] = field(default_factory=dict)


@dataclass
class MinerResult:
    """Output from a single miner execution."""

    miner_name: str
    businesses: list[BusinessRecord] = field(default_factory=list)
    total_found: int = 0
    new_discoveries: int = 0
    execution_time_seconds: float = 0.0
    queries_executed: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def success_rate(self) -> float:
        if self.queries_executed == 0:
            return 0.0
        error_count = len(self.errors)
        return max(0.0, (self.queries_executed - error_count) / self.queries_executed)


class BaseMiner(ABC):
    """
    Abstract base for all discovery miners.
    Subclasses implement _execute_search() and _parse_results().
    The run() method handles timing, error collection, and context adaptation.
    """

    MINER_NAME: str = "base"
    TIER: int = 0  # 1 = premium, 2 = support
    EFFICACY: float = 0.0  # Validated efficacy percentage

    def __init__(self, context: ContextConfig):
        self.context = context
        self._start_time: float = 0.0

    @abstractmethod
    async def _execute_search(
        self, search_params: dict[str, Any]
    ) -> list[dict[str, Any]]:
        """Execute the actual search. Returns raw results."""
        ...

    @abstractmethod
    def _parse_results(
        self, raw_results: list[dict[str, Any]]
    ) -> list[BusinessRecord]:
        """Parse raw API/scrape results into BusinessRecords."""
        ...

    def _build_search_params(self) -> list[dict[str, Any]]:
        """
        Build search parameter sets based on context.
        Default: one query per (business_type, city) pair.
        Override in subclasses for miner-specific strategies.
        """
        params = []
        for city in self.context.cities:
            for btype in self.context.business_types:
                params.append({
                    "city": city,
                    "business_type": btype,
                    "keywords": self.context.primary_keywords,
                    "secondary_keywords": self.context.secondary_keywords,
                    "region_type": self.context.region_type.value,
                    "niche_level": self.context.niche_level.value,
                })
        return params

    def _adapt_strategy(self, params: dict[str, Any]) -> dict[str, Any]:
        """
        Context-aware strategy adaptation.
        Subclasses override to change behavior per region type.
        """
        return params

    async def run(self) -> MinerResult:
        """
        Main execution entry. Builds params, runs searches,
        parses results, returns MinerResult with timing.
        """
        self._start_time = time.monotonic()
        result = MinerResult(miner_name=self.MINER_NAME)
        all_records: list[BusinessRecord] = []

        search_param_sets = self._build_search_params()
        logger.info(
            "[%s] Starting with %d search param sets",
            self.MINER_NAME, len(search_param_sets),
        )

        for params in search_param_sets:
            adapted = self._adapt_strategy(params)
            result.queries_executed += 1
            try:
                raw = await self._execute_search(adapted)
                records = self._parse_results(raw)
                all_records.extend(records)
            except Exception as exc:
                msg = f"Search failed for {adapted}: {exc}"
                logger.warning("[%s] %s", self.MINER_NAME, msg)
                result.errors.append(msg)

        result.businesses = all_records
        result.total_found = len(all_records)
        result.execution_time_seconds = time.monotonic() - self._start_time

        logger.info(
            "[%s] Complete: %d found, %d errors, %.1fs",
            self.MINER_NAME, result.total_found,
            len(result.errors), result.execution_time_seconds,
        )
        return result
