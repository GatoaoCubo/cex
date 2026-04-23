"""
cex_sdk.workflow.parallel -- Parallel step execution.

CEX version: 9.1.0 | Pillar: P12 | 8F: PRODUCE (F6)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from cex_sdk.workflow.step import Step
from cex_sdk.workflow.types import StepInput, StepOutput, StepStatus


@dataclass
class Parallel:
    """Execute multiple steps in parallel (ThreadPoolExecutor)."""

    name: Optional[str] = "Parallel"
    steps: List[Step] = field(default_factory=list)
    max_workers: int = 4

    def __init__(self, *args, name: Optional[str] = None, max_workers: int = 4):
        steps = []
        resolved_name = name or "Parallel"
        for arg in args:
            if isinstance(arg, str) and not steps:
                resolved_name = arg
            elif isinstance(arg, Step):
                steps.append(arg)
        self.name = resolved_name
        self.steps = steps
        self.max_workers = max_workers

    def run(self, input: StepInput) -> Dict[str, StepOutput]:
        """Execute all steps in parallel, return {step_name: output}."""
        results: Dict[str, StepOutput] = {}

        with ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            futures = {
                pool.submit(step.run, input): step
                for step in self.steps
            }
            for future in as_completed(futures):
                step = futures[future]
                try:
                    results[step.name or step.step_id] = future.result()
                except Exception as e:
                    results[step.name or step.step_id] = StepOutput(
                        status=StepStatus.FAILED, error=str(e)
                    )

        return results
