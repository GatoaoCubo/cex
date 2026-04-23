"""
cex_sdk.architecture.capability_registry -- Registry of all spawnable agents.

kind: capability_registry
pillar: P08
8F: F1 CONSTRAIN (capability resolution) + F5 CALL (agent discovery)
"""
# -*- coding: ascii -*-
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class CapabilityEntry:
    """Single agent/builder capability record."""
    agent_id: str
    nucleus: str
    pillar: str
    kinds: list[str]
    description: str = ""
    model: str = ""
    tools: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


class CapabilityRegistry:
    """
    kind: capability_registry
    pillar: P08
    Index of all spawnable agent builders. Queried during F1 CONSTRAIN
    to discover which agent should handle a given kind/pillar.

    Sources:
    - .claude/agents/{kind}-builder.md (sub-agents)
    - archetypes/builders/{kind}-builder/ (builder ISOs)
    - .cex/kinds_meta.json (canonical kind registry)
    """

    def __init__(self, entries: list[CapabilityEntry] | None = None) -> None:
        self._entries: dict[str, CapabilityEntry] = {}
        for e in (entries or []):
            self._entries[e.agent_id] = e

    def register(self, entry: CapabilityEntry) -> None:
        self._entries[entry.agent_id] = entry

    def query_by_kind(self, kind: str) -> list[CapabilityEntry]:
        return [e for e in self._entries.values() if kind in e.kinds]

    def query_by_pillar(self, pillar: str) -> list[CapabilityEntry]:
        return [e for e in self._entries.values() if e.pillar == pillar]

    def query_by_nucleus(self, nucleus: str) -> list[CapabilityEntry]:
        return [e for e in self._entries.values() if e.nucleus == nucleus]

    def get(self, agent_id: str) -> CapabilityEntry | None:
        return self._entries.get(agent_id)

    def all_kinds(self) -> list[str]:
        kinds: set[str] = set()
        for e in self._entries.values():
            kinds.update(e.kinds)
        return sorted(kinds)

    def count(self) -> int:
        return len(self._entries)

    @classmethod
    def from_kinds_meta(cls, kinds_meta_path: str | Path) -> "CapabilityRegistry":
        """Bootstrap registry from kinds_meta.json."""
        path = Path(kinds_meta_path)
        if not path.exists():
            return cls()
        with open(path, encoding="utf-8") as f:
            meta: dict[str, Any] = json.load(f)
        entries = []
        for kind, info in meta.items():
            entry = CapabilityEntry(
                agent_id=f"{kind}-builder",
                nucleus=info.get("nucleus", "n03"),
                pillar=info.get("pillar", ""),
                kinds=[kind],
                description=info.get("description", ""),
                model=info.get("model", ""),
            )
            entries.append(entry)
        return cls(entries)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": "capability_registry/v1",
            "count": self.count(),
            "entries": {
                aid: {
                    "nucleus": e.nucleus,
                    "pillar": e.pillar,
                    "kinds": e.kinds,
                    "description": e.description,
                }
                for aid, e in self._entries.items()
            },
        }
