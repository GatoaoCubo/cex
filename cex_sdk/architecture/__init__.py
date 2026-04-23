"""
cex_sdk.architecture -- Architecture and System Design Components

CEX version: 10.2.0 | Pillar: P08 (Architecture) | 8F: CONSTRAIN (F1) + REASON (F4)

Kinds covered: agent_card, component_map, decision_record, diagram, capability_registry

Usage:
  from cex_sdk.architecture import AgentCard, ComponentMap, CapabilityRegistry
"""

# kind: agent_card
# kind: component_map
# kind: decision_record
# kind: capability_registry
# kind: diagram
# pillar: P08

from cex_sdk.architecture.agent_card import AgentCapability, AgentCard
from cex_sdk.architecture.capability_registry import CapabilityRegistry
from cex_sdk.architecture.component_map import (Component, ComponentMap,
                                                ComponentRelation)
from cex_sdk.architecture.decision_record import DecisionRecord, DecisionStatus

__all__ = [
    "AgentCard",
    "AgentCapability",
    "ComponentMap",
    "Component",
    "ComponentRelation",
    "DecisionRecord",
    "DecisionStatus",
    "CapabilityRegistry",
]
