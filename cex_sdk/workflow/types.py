"""
cex_sdk.workflow.types -- Workflow type definitions.

CEX version: 9.1.0 | Pillar: P12 | 8F: PRODUCE (F6)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class OnError(str, Enum):
    RAISE = "raise"
    SKIP = "skip"
    RETRY = "retry"


class OnReject(str, Enum):
    RAISE = "raise"
    SKIP = "skip"


class StepStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class StepInput:
    """Input passed between workflow steps."""
    content: Any = None
    session_state: Dict[str, Any] = field(default_factory=dict)
    previous_output: Optional[Any] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class StepOutput:
    """Output from a workflow step."""
    content: Any = None
    session_state: Dict[str, Any] = field(default_factory=dict)
    status: StepStatus = StepStatus.COMPLETED
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
