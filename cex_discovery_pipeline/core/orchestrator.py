"""
Module 2: Master Orchestrator — DiscoveryPipeline
===================================================
Main entry point. Coordinates parallel miners and background agents
based on ContextConfig. Accepts natural language via QueryProcessor.
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from cex_discovery_pipeline.agents.base_agent import AgentResult
from cex_discovery_pipeline.agents.deduplicator_agent import DeduplicatorAgent
from cex_discovery_pipeline.agents.enricher_agent import EnricherAgent
from cex_discovery_pipeline.agents.validator_agent import ValidatorAgent
from cex_discovery_pipeline.core.context_engine import ContextConfig, ContextEngine
from cex_discovery_pipeline.core.discovery_dispatcher import AgentDispatcher
from cex_discovery_pipeline.miners.base_miner import BaseMiner, BusinessRecord, MinerResult
from cex_discovery_pipeline.miners.tier1_premium.cep_geography_miner import CEPGeographyMiner
from cex_discovery_pipeline.miners.tier1_premium.facebook_business_miner import (
    FacebookBusinessMiner,
)
from cex_discovery_pipeline.miners.tier1_premium.google_maps_miner import GoogleMapsMiner
from cex_discovery_pipeline.miners.tier1_premium.yellow_pages_miner import YellowPagesMiner
from cex_discovery_pipeline.miners.tier2_support.delivery_apps_miner import DeliveryAppsMiner
from cex_discovery_pipeline.miners.tier2_support.marketplace_miner import MarketplaceMiner
from cex_discovery_pipeline.miners.tier2_support.waze_directory_miner import WazeDirectoryMiner

logger = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent / "output"

# Miner registry: key -> class
MINER_REGISTRY: dict[str, type[BaseMiner]] = {
    "google_maps": GoogleMapsMiner,
    "facebook_business": FacebookBusinessMiner,
    "yellow_pages": YellowPagesMiner,
    "cep_geography": CEPGeographyMiner,
    "delivery_apps": DeliveryAppsMiner,
    "marketplace": MarketplaceMiner,
    "waze": WazeDirectoryMiner,
}


@dataclass
class PipelineResult:
    """Full pipeline execution result."""

    businesses: list[BusinessRecord] = field(default_factory=list)
    miner_results: dict[str, MinerResult] = field(default_factory=dict)
    agent_results: dict[str, AgentResult] = field(default_factory=dict)
    total_raw: int = 0
    total_deduplicated: int = 0
    total_validated: int = 0
    total_enriched: int = 0
    execution_time_seconds: float = 0.0
    context: ContextConfig | None = None

    @property
    def yield_summary(self) -> dict[str, Any]:
        return {
            "total_discovered": self.total_raw,
            "after_dedup": self.total_deduplicated,
            "validated": self.total_validated,
            "final_count": len(self.businesses),
            "execution_time_s": round(self.execution_time_seconds, 1),
            "miners_used": list(self.miner_results.keys()),
            "agents_used": list(self.agent_results.keys()),
        }


class DiscoveryPipeline:
    """
    Main pipeline orchestrator.

    Usage:
        pipeline = DiscoveryPipeline()
        result = await pipeline.discover("Find pet shops in ABC Paulista")

    Or with explicit params:
        ctx = engine.build_context("abc_metropolitano", "pet_ecosystem")
        result = await pipeline.run(ctx)
    """

    def __init__(self, config_dir: Path | None = None):
        self.engine = ContextEngine(config_dir=config_dir)

    async def discover(
        self,
        query: str,
        *,
        region_key: str | None = None,
        niche_key: str | None = None,
    ) -> PipelineResult:
        """
        Natural language entry point.
        Parses query, builds context, runs pipeline.
        """
        from cex_discovery_pipeline.core.query_processor import QueryProcessor

        processor = QueryProcessor()
        parsed = processor.parse(query)

        r_key = region_key or parsed.get("region_key", "abc_metropolitano")
        n_key = niche_key or parsed.get("niche_key", "pet_ecosystem")
        business_types = parsed.get("business_types")

        context = self.engine.build_context(
            r_key, n_key, business_types=business_types,
        )
        return await self.run(context)

    async def run(self, context: ContextConfig) -> PipelineResult:
        """
        Execute full pipeline with the given context.

        Flow:
          1. Select miners based on technique_priorities
          2. Run miners in parallel waves (Tier 1 first, then Tier 2)
          3. Merge all raw results
          4. Run agent pipeline: validate -> deduplicate -> enrich
          5. Return consolidated PipelineResult
        """
        start = time.monotonic()
        result = PipelineResult(context=context)

        # ── Step 1: Select miners ────────────────────────────────
        selected_miners = self._select_miners(context)
        tier1 = [m for m in selected_miners if m.TIER == 1]
        tier2 = [m for m in selected_miners if m.TIER == 2]

        logger.info(
            "Pipeline starting: %d Tier1 + %d Tier2 miners, mode=%s",
            len(tier1), len(tier2), context.execution_mode.value,
        )

        # ── Step 2: Run miners in waves ──────────────────────────
        # Wave 1: Premium miners (parallel)
        all_records: list[BusinessRecord] = []
        if tier1:
            t1_results = await self._run_miners_parallel(
                tier1, context.max_parallel_miners
            )
            for mr in t1_results:
                result.miner_results[mr.miner_name] = mr
                all_records.extend(mr.businesses)

        # Wave 2: Support miners (parallel)
        if tier2 and context.execution_mode.value != "fast_scan":
            t2_results = await self._run_miners_parallel(
                tier2, context.max_parallel_miners
            )
            for mr in t2_results:
                result.miner_results[mr.miner_name] = mr
                all_records.extend(mr.businesses)

        result.total_raw = len(all_records)
        logger.info("Mining complete: %d raw records from %d miners",
                     result.total_raw, len(result.miner_results))

        # ── Step 3: Agent pipeline ───────────────────────────────
        dispatcher = AgentDispatcher(context)
        dispatcher.register_agent(ValidatorAgent(context))
        dispatcher.register_agent(DeduplicatorAgent(context))
        dispatcher.register_agent(EnricherAgent(context))

        dispatch_result = await dispatcher.dispatch_sequential(all_records)
        result.businesses = dispatch_result.records
        result.agent_results = dispatch_result.agent_results
        result.total_validated = dispatch_result.agent_results.get(
            "validator", AgentResult(agent_name="validator")
        ).processed_count
        result.total_deduplicated = dispatch_result.agent_results.get(
            "deduplicator", AgentResult(agent_name="deduplicator")
        ).processed_count
        result.total_enriched = dispatch_result.agent_results.get(
            "enricher", AgentResult(agent_name="enricher")
        ).processed_count

        result.execution_time_seconds = time.monotonic() - start

        # ── Step 4: Save output ──────────────────────────────────
        self._save_results(result, context)

        logger.info(
            "Pipeline complete: %d raw -> %d final in %.1fs",
            result.total_raw, len(result.businesses),
            result.execution_time_seconds,
        )
        return result

    def _select_miners(self, context: ContextConfig) -> list[BaseMiner]:
        """Instantiate miners based on technique priority order."""
        miners: list[BaseMiner] = []
        for tech_key in context.technique_priorities:
            miner_cls = MINER_REGISTRY.get(tech_key)
            if miner_cls:
                miners.append(miner_cls(context))
        if not miners:
            # Fallback: all miners
            miners = [cls(context) for cls in MINER_REGISTRY.values()]
        return miners

    async def _run_miners_parallel(
        self,
        miners: list[BaseMiner],
        max_parallel: int,
    ) -> list[MinerResult]:
        """Run miners with bounded concurrency."""
        semaphore = asyncio.Semaphore(max_parallel)
        results: list[MinerResult] = []

        async def _run_one(miner: BaseMiner) -> MinerResult:
            async with semaphore:
                return await miner.run()

        tasks = [asyncio.create_task(_run_one(m)) for m in miners]
        for coro in asyncio.as_completed(tasks):
            try:
                mr = await coro
                results.append(mr)
                logger.info(
                    "Miner %s: %d found (%.1fs)",
                    mr.miner_name, mr.total_found, mr.execution_time_seconds,
                )
            except Exception as exc:
                logger.error("Miner task failed: %s", exc)
        return results

    def _save_results(self, result: PipelineResult, context: ContextConfig) -> None:
        """Save results to output/ as JSON."""
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_file = OUTPUT_DIR / f"discovery_{context.region_name}_{context.niche_name}.json"

        records = []
        for biz in result.businesses:
            records.append({
                "name": biz.name,
                "phone": biz.phone,
                "address": biz.address,
                "city": biz.city,
                "cep": biz.cep,
                "category": biz.category,
                "source": biz.source,
                "rating": biz.rating,
                "review_count": biz.review_count,
                "website": biz.website,
                "cnpj": biz.cnpj,
                "social_facebook": biz.social_facebook,
                "social_instagram": biz.social_instagram,
                "confidence": biz.confidence,
            })

        output = {
            "summary": result.yield_summary,
            "context": {
                "region": context.region_name,
                "niche": context.niche_name,
                "mode": context.execution_mode.value,
                "region_type": context.region_type.value,
            },
            "businesses": records,
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        logger.info("Results saved to %s", output_file)
