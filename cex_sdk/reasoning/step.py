"""
cex_sdk.reasoning.step -- Structured reasoning steps.

Absorbed from: agno/reasoning/step.py
CEX version: 9.5.0 | Pillar: P03 | 8F: REASON (F4)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class NextAction(str, Enum):
    CONTINUE = "continue"
    VALIDATE = "validate"
    FINAL_ANSWER = "final_answer"
    RESET = "reset"


class ReasoningStep(BaseModel):
    """A single step in a chain-of-thought reasoning process."""

    title: Optional[str] = Field(None, description="Concise title summarizing the step's purpose")
    action: Optional[str] = Field(None, description="The action to take (first person: 'I will...')")
    result: Optional[str] = Field(None, description="The result of executing the action")
    reasoning: Optional[str] = Field(None, description="Thought process and considerations")
    next_action: Optional[NextAction] = Field(None, description="What to do next")
    confidence: Optional[float] = Field(None, description="Confidence score (0.0 to 1.0)")

    # CEX integration
    cex_function: Optional[str] = Field(None, description="8F function this step maps to (F1-F8)")
    nucleus: Optional[str] = Field(None, description="CEX nucleus (N01-N07)")


class ReasoningTrace(BaseModel):
    """Complete reasoning trace for an artifact production."""

    steps: List[ReasoningStep] = Field(default_factory=list, description="Ordered reasoning steps")
    final_answer: Optional[str] = None
    total_confidence: Optional[float] = None

    def add_step(self, **kwargs) -> ReasoningStep:
        step = ReasoningStep(**kwargs)
        self.steps.append(step)
        return step

    def get_confidence(self) -> float:
        """Average confidence across all steps."""
        scored = [s.confidence for s in self.steps if s.confidence is not None]
        return sum(scored) / len(scored) if scored else 0.0

    def should_ask_user(self, threshold: float = 0.7) -> bool:
        """Returns True if confidence is below threshold -> trigger GDP."""
        return self.get_confidence() < threshold

    def to_markdown(self) -> str:
        """Render reasoning trace as markdown."""
        lines = ["## Reasoning Trace\n"]
        for i, step in enumerate(self.steps, 1):
            lines.append(f"### Step {i}: {step.title or 'Untitled'}")
            if step.reasoning:
                lines.append(f"**Thinking:** {step.reasoning}")
            if step.action:
                lines.append(f"**Action:** {step.action}")
            if step.result:
                lines.append(f"**Result:** {step.result}")
            if step.confidence is not None:
                lines.append(f"**Confidence:** {step.confidence:.0%}")
            lines.append("")
        if self.final_answer:
            lines.append(f"### Final Answer\n{self.final_answer}")
        return "\n".join(lines)
