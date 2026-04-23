"""
cex_sdk.architecture.component_map -- System component graph.

kind: component_map
pillar: P08
8F: F4 REASON (architecture planning)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Component:
    """Single system component in the architecture map."""
    id: str
    name: str
    kind: str
    pillar: str
    nucleus: str = ""
    description: str = ""
    tools: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ComponentRelation:
    """Directed relationship between two components."""
    source: str
    target: str
    label: str = ""
    protocol: str = ""


@dataclass
class ComponentMap:
    """
    kind: component_map
    pillar: P08
    Represents the full architecture of a nucleus or system area.
    """
    id: str
    nucleus: str
    title: str
    components: list[Component] = field(default_factory=list)
    relations: list[ComponentRelation] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def add_relation(self, source: str, target: str, label: str = "") -> None:
        self.relations.append(ComponentRelation(source=source, target=target, label=label))

    def get_by_pillar(self, pillar: str) -> list[Component]:
        return [c for c in self.components if c.pillar == pillar]

    def get_dependencies(self, component_id: str) -> list[Component]:
        comp = next((c for c in self.components if c.id == component_id), None)
        if not comp:
            return []
        return [c for c in self.components if c.id in comp.depends_on]

    def to_mermaid(self) -> str:
        """Export as Mermaid graph diagram."""
        lines = ["graph TD"]
        for c in self.components:
            label = f"{c.id}[{c.name}]"
            lines.append(f"  {label}")
        for r in self.relations:
            arrow = f"  {r.source} -->|{r.label}| {r.target}" if r.label else f"  {r.source} --> {r.target}"
            lines.append(arrow)
        return "\n".join(lines)
