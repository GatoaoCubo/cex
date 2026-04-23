"""
cex_sdk.workflow.loop -- Iterative step execution with condition.

CEX version: 9.1.0 | Pillar: P12 | 8F: PRODUCE (F6)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from cex_sdk.workflow.step import Step
from cex_sdk.workflow.types import StepInput, StepOutput, StepStatus


@dataclass
class Loop:
    """Execute a step repeatedly until condition is met or max_iterations reached."""

    name: Optional[str] = "Loop"
    step: Optional[Step] = None
    condition: Optional[Callable[[StepOutput], bool]] = None  # Return True to stop
    max_iterations: int = 10

    def run(self, input: StepInput) -> StepOutput:
        if not self.step:
            return StepOutput(status=StepStatus.SKIPPED, error="No step in loop")

        current_input = input
        last_output = StepOutput()

        for i in range(self.max_iterations):
            last_output = self.step.run(current_input)

            if self.condition and self.condition(last_output):
                last_output.metadata["loop_iterations"] = i + 1
                return last_output

            # Feed output back as input
            current_input = StepInput(
                content=last_output.content,
                session_state={**current_input.session_state, **last_output.session_state},
                previous_output=last_output.content,
            )

        last_output.metadata["loop_iterations"] = self.max_iterations
        last_output.metadata["loop_exhausted"] = True
        return last_output
