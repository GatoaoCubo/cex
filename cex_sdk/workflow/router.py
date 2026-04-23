"""
cex_sdk.workflow.router -- Dynamic routing between steps.

CEX version: 9.1.0 | Pillar: P12 | 8F: REASON (F4)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, Optional

from cex_sdk.workflow.step import Step
from cex_sdk.workflow.types import StepInput, StepOutput, StepStatus


@dataclass
class Router:
    """Route to different steps based on a routing function.

    Maps to CEX nucleus routing (N01-N07) or kind-based routing.
    """

    name: Optional[str] = "Router"
    route_fn: Optional[Callable[[StepInput], str]] = None
    routes: Dict[str, Step] = field(default_factory=dict)
    default: Optional[Step] = None

    def run(self, input: StepInput) -> StepOutput:
        if not self.route_fn:
            return StepOutput(status=StepStatus.SKIPPED, error="No routing function")

        route_key = self.route_fn(input)
        step = self.routes.get(route_key, self.default)

        if not step:
            return StepOutput(
                status=StepStatus.FAILED,
                error=f"No route for '{route_key}'",
                metadata={"route": route_key},
            )

        output = step.run(input)
        output.metadata["route"] = route_key
        return output
