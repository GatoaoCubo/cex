"""
Module 3: Agent Dispatcher
===========================
Spawns and manages background agents for validation, deduplication,
and enrichment. Coordinates async agent execution.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from typing import Any

from cex_discovery_pipeline.agents.base_agent import AgentResult, BaseAgent
from cex_discovery_pipeline.core.context_engine import ContextConfig
from cex_discovery_pipeline.miners.base_miner import BusinessRecord

logger = logging.getLogger(__name__)


@dataclass
class DispatchResult:
    """Aggregated result from all dispatched agents."""

    records: list[BusinessRecord] = field(default_factory=list)
    agent_results: dict[str, AgentResult] = field(default_factory=dict)
    total_input: int = 0
    total_output: int = 0
    total_rejected: int = 0


class AgentDispatcher:
    """
    Manages background agent execution pipeline.
    Agents run in sequence: validate -> deduplicate -> enrich.
    Each stage filters/modifies records before passing to next.
    """

    def __init__(self, context: ContextConfig):
        self.context = context
        self._agents: list[BaseAgent] = []

    def register_agent(self, agent: BaseAgent) -> None:
        self._agents.append(agent)
        logger.info("Registered agent: %s", agent.AGENT_NAME)

    async def dispatch_sequential(
        self, records: list[BusinessRecord]
    ) -> DispatchResult:
        """
        Run agents sequentially: output of one feeds into the next.
        Order: validator -> deduplicator -> enricher.
        """
        result = DispatchResult(total_input=len(records))
        current_records = list(records)

        for agent in self._agents:
            logger.info(
                "[Dispatcher] Running %s on %d records",
                agent.AGENT_NAME, len(current_records),
            )
            current_records, agent_result = await agent.run(current_records)
            result.agent_results[agent.AGENT_NAME] = agent_result
            result.total_rejected += agent_result.rejected_count

        result.records = current_records
        result.total_output = len(current_records)
        logger.info(
            "[Dispatcher] Pipeline complete: %d in -> %d out (%d rejected)",
            result.total_input, result.total_output, result.total_rejected,
        )
        return result

    async def dispatch_parallel_agents(
        self,
        records: list[BusinessRecord],
        agents: list[BaseAgent],
    ) -> dict[str, tuple[list[BusinessRecord], AgentResult]]:
        """
        Run multiple independent agents in parallel on the same record set.
        Used when agents don't depend on each other's output.
        """
        tasks = {
            agent.AGENT_NAME: asyncio.create_task(agent.run(list(records)))
            for agent in agents
        }
        results: dict[str, tuple[list[BusinessRecord], AgentResult]] = {}
        for name, task in tasks.items():
            try:
                results[name] = await task
            except Exception as exc:
                logger.error("[Dispatcher] Agent %s failed: %s", name, exc)
                error_result = AgentResult(agent_name=name, errors=[str(exc)])
                results[name] = (records, error_result)
        return results
