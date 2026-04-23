"""
cex_sdk.workflow.condition -- Conditional branching.

CEX version: 9.1.0 | Pillar: P12 | 8F: PRODUCE (F6)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from cex_sdk.workflow.step import Step
from cex_sdk.workflow.types import StepInput, StepOutput, StepStatus


@dataclass
class Condition:
    """Branch execution based on a condition."""

    name: Optional[str] = "Condition"
    check: Optional[Callable[[StepInput], bool]] = None
    on_true: Optional[Step] = None
    on_false: Optional[Step] = None

    def run(self, input: StepInput) -> StepOutput:
        if not self.check:
            return StepOutput(status=StepStatus.SKIPPED, error="No condition check")

        result = self.check(input)
        step = self.on_true if result else self.on_false

        if not step:
            return StepOutput(
                status=StepStatus.SKIPPED,
                metadata={"condition_result": result, "branch": "true" if result else "false"},
            )

        output = step.run(input)
        output.metadata["condition_result"] = result
        output.metadata["branch"] = "true" if result else "false"
        return output
