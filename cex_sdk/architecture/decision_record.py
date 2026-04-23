"""
cex_sdk.architecture.decision_record -- Architecture Decision Records (ADR).

kind: decision_record
pillar: P08
8F: F4 REASON (decision capture) + F8 COLLABORATE (persistence)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class DecisionStatus(str, Enum):
    PROPOSED = "proposed"
    ACCEPTED = "accepted"
    SUPERSEDED = "superseded"
    DEPRECATED = "deprecated"
    REJECTED = "rejected"


@dataclass
class DecisionRecord:
    """
    kind: decision_record
    pillar: P08
    Captures architectural decisions with context, options, and rationale.
    Follows ADR format (Nygard 2011).
    """
    id: str
    title: str
    status: DecisionStatus = DecisionStatus.PROPOSED
    context: str = ""
    decision: str = ""
    consequences: str = ""
    options_considered: list[str] = field(default_factory=list)
    supersedes: list[str] = field(default_factory=list)
    nucleus: str = ""
    pillar: str = "P08"
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_markdown(self) -> str:
        lines = [
            f"# ADR {self.id}: {self.title}",
            "",
            f"**Status**: {self.status.value}",
            "",
            "## Context",
            self.context,
            "",
            "## Decision",
            self.decision,
            "",
        ]
        if self.options_considered:
            lines += ["## Options Considered", ""]
            for opt in self.options_considered:
                lines.append(f"- {opt}")
            lines.append("")
        lines += ["## Consequences", self.consequences]
        if self.supersedes:
            lines += ["", "## Supersedes", ", ".join(self.supersedes)]
        return "\n".join(lines)

    @property
    def is_active(self) -> bool:
        return self.status == DecisionStatus.ACCEPTED
