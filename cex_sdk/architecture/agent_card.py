"""
cex_sdk.architecture.agent_card -- Agent Card (A2A standard identity).

kind: agent_card
pillar: P08
8F: F1 CONSTRAIN (agent identity resolution)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentCapability:
    """Single capability declaration for an agent."""
    name: str
    description: str
    pillar: str = ""
    kinds: list[str] = field(default_factory=list)
    tools: list[str] = field(default_factory=list)


def _resolve_default_model(nucleus: str) -> str:
    """Resolve default model for a nucleus via model resolver."""
    try:
        from _tools.cex_model_resolver import get_model_string
        return get_model_string(nucleus)
    except Exception:
        return "claude-sonnet-4-6"


@dataclass
class AgentCard:
    """
    A2A-compatible agent identity card.

    kind: agent_card
    pillar: P08
    Encodes nucleus identity, capabilities, sin lens, and routing metadata.
    """
    agent_id: str
    nucleus: str
    role: str
    sin_lens: str
    model: str = ""
    context_window: int = 200000
    capabilities: list[AgentCapability] = field(default_factory=list)
    tools: list[str] = field(default_factory=list)
    pillars: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.model:
            self.model = _resolve_default_model(self.nucleus)

    def to_dict(self) -> dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "nucleus": self.nucleus,
            "role": self.role,
            "sin_lens": self.sin_lens,
            "model": self.model,
            "context_window": self.context_window,
            "capabilities": [
                {
                    "name": c.name,
                    "description": c.description,
                    "pillar": c.pillar,
                    "kinds": c.kinds,
                }
                for c in self.capabilities
            ],
            "pillars": self.pillars,
            "tools": self.tools,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AgentCard":
        caps = [
            AgentCapability(
                name=c["name"],
                description=c.get("description", ""),
                pillar=c.get("pillar", ""),
                kinds=c.get("kinds", []),
            )
            for c in data.get("capabilities", [])
        ]
        return cls(
            agent_id=data["agent_id"],
            nucleus=data.get("nucleus", ""),
            role=data.get("role", ""),
            sin_lens=data.get("sin_lens", ""),
            model=data.get("model", "") or _resolve_default_model(data.get("nucleus", "")),
            context_window=data.get("context_window", 200000),
            capabilities=caps,
            tools=data.get("tools", []),
            pillars=data.get("pillars", []),
        )
