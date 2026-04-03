"""
CEX Advanced Business Discovery Pipeline
=========================================
15-module context-aware system for automated B2B business discovery.
Validated: 6-9x improvement vs manual methods (N01 research, 202+ businesses mapped).

Architecture:
    core/       - Context engine, orchestrator, dispatcher, query processor, analytics
    miners/     - 7 mining techniques (4 premium + 3 support)
    agents/     - 3 background agents (validator, deduplicator, enricher)
    config/     - 4 YAML configs (niches, regions, technique weights, quality gates)

Usage:
    from cex_discovery_pipeline import DiscoveryPipeline
    pipeline = DiscoveryPipeline()
    results = await pipeline.discover("Find pet shops in ABC Paulista")
"""

__version__ = "1.0.0"
__author__ = "N03 Builder Nucleus"

from cex_discovery_pipeline.core.context_engine import ContextEngine, ContextConfig
from cex_discovery_pipeline.core.orchestrator import DiscoveryPipeline
from cex_discovery_pipeline.core.discovery_dispatcher import AgentDispatcher
from cex_discovery_pipeline.core.query_processor import QueryProcessor
from cex_discovery_pipeline.core.analytics_engine import AnalyticsEngine

__all__ = [
    "DiscoveryPipeline",
    "ContextEngine",
    "ContextConfig",
    "AgentDispatcher",
    "QueryProcessor",
    "AnalyticsEngine",
]
