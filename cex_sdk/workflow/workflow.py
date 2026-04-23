"""
cex_sdk.workflow.workflow -- Workflow orchestrator.

CEX version: 9.1.0 | Pillar: P12 | 8F: PRODUCE (F6)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from cex_sdk.utils.log import log_debug, log_error, log_info
from cex_sdk.utils.timer import Timer
from cex_sdk.workflow.condition import Condition
from cex_sdk.workflow.loop import Loop
from cex_sdk.workflow.parallel import Parallel
from cex_sdk.workflow.router import Router
from cex_sdk.workflow.step import Step
from cex_sdk.workflow.types import StepInput, StepOutput, StepStatus

WorkflowStep = Union[Step, Parallel, Loop, Condition, Router]


@dataclass
class Workflow:
    """Orchestrate a sequence of steps into a pipeline.

    Integrates with CEX 8F pipeline: each F1-F8 function can be a Step.

    Usage:
        pipeline = Workflow(
            name="8F Pipeline",
            steps=[
                Step(name="F1_CONSTRAIN", executor=constrain),
                Parallel(
                    Step(name="F3_INJECT", executor=inject),
                    Step(name="F4_REASON", executor=reason),
                ),
                Step(name="F6_PRODUCE", executor=produce),
                Condition(
                    check=lambda s: s.session_state.get("quality", 0) >= 8.0,
                    on_true=Step(name="F8_COLLABORATE", executor=collab),
                    on_false=Step(name="RETRY", executor=retry),
                ),
            ],
        )
        result = pipeline.run(StepInput(content="create agent"))
    """

    name: str = "Workflow"
    steps: List[WorkflowStep] = field(default_factory=list)
    description: Optional[str] = None

    def run(self, input: Optional[StepInput] = None) -> StepOutput:
        """Execute all steps sequentially (parallel steps handled internally)."""
        if input is None:
            input = StepInput()

        timer = Timer().start()
        current_input = input
        last_output = StepOutput()
        step_results: Dict[str, Any] = {}

        log_info(f"Workflow '{self.name}' starting with {len(self.steps)} steps")

        for i, step in enumerate(self.steps):
            step_name = getattr(step, "name", None) or f"step_{i}"
            log_debug(f"  -> {step_name}")

            try:
                if isinstance(step, Step):
                    last_output = step.run(current_input)
                elif isinstance(step, Parallel):
                    parallel_results = step.run(current_input)
                    # Merge all parallel outputs
                    merged_state = dict(current_input.session_state)
                    merged_content = {}
                    for name, output in parallel_results.items():
                        merged_state.update(output.session_state)
                        merged_content[name] = output.content
                    last_output = StepOutput(
                        content=merged_content,
                        session_state=merged_state,
                    )
                elif isinstance(step, (Loop, Condition, Router)):
                    last_output = step.run(current_input)
                else:
                    log_error(f"Unknown step type: {type(step)}")
                    continue

                step_results[step_name] = last_output

                # Propagate state
                current_input = StepInput(
                    content=last_output.content,
                    session_state={**current_input.session_state, **last_output.session_state},
                    previous_output=last_output.content,
                )

                if last_output.status == StepStatus.FAILED:
                    log_error(f"  [X] {step_name} FAILED: {last_output.error}")
                    break

            except Exception as e:
                log_error(f"  [X] {step_name} ERROR: {e}")
                last_output = StepOutput(status=StepStatus.FAILED, error=str(e))
                break

        timer.stop()
        last_output.metadata["workflow_name"] = self.name
        last_output.metadata["workflow_duration"] = timer.elapsed
        last_output.metadata["steps_executed"] = len(step_results)
        last_output.metadata["step_results"] = {k: v.status.value for k, v in step_results.items()}

        log_info(f"Workflow '{self.name}' completed in {timer.elapsed:.2f}s")
        return last_output
