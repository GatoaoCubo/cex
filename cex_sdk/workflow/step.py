"""
cex_sdk.workflow.step -- Single unit of work in a workflow.

Absorbed from: agno/workflow/step.py
CEX version: 9.1.0 | Pillar: P12 | 8F: PRODUCE (F6)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Optional, Union
from uuid import uuid4

from cex_sdk.workflow.types import OnError, StepInput, StepOutput, StepStatus


@dataclass
class Step:
    """A single unit of work in a workflow pipeline.

    Can wrap an executor function, or reference a CEX nucleus.
    """

    name: Optional[str] = None
    step_id: str = field(default_factory=lambda: str(uuid4()))
    description: Optional[str] = None

    # Executor: a callable that takes StepInput -> StepOutput
    executor: Optional[Callable[[StepInput], Union[StepOutput, Any]]] = None

    # CEX-specific: nucleus reference
    nucleus: Optional[str] = None  # e.g., "n03"
    kind: Optional[str] = None     # CEX kind

    # Config
    max_retries: int = 3
    on_error: OnError = OnError.RAISE
    skip_on_failure: bool = False

    def run(self, input: StepInput) -> StepOutput:
        """Execute the step."""
        if not self.executor:
            return StepOutput(status=StepStatus.SKIPPED, error="No executor")

        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                result = self.executor(input)
                if isinstance(result, StepOutput):
                    return result
                return StepOutput(content=result, status=StepStatus.COMPLETED)
            except Exception as e:
                last_error = str(e)
                if attempt == self.max_retries:
                    break

        if self.on_error == OnError.SKIP or self.skip_on_failure:
            return StepOutput(status=StepStatus.SKIPPED, error=last_error)
        if self.on_error == OnError.RAISE:
            raise RuntimeError(f"Step {self.name} failed: {last_error}")
        return StepOutput(status=StepStatus.FAILED, error=last_error)

    async def arun(self, input: StepInput) -> StepOutput:
        """Async execute."""
        import asyncio
        if self.executor and asyncio.iscoroutinefunction(self.executor):
            result = await self.executor(input)
            return result if isinstance(result, StepOutput) else StepOutput(content=result)
        return await asyncio.get_event_loop().run_in_executor(None, lambda: self.run(input))
