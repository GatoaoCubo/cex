"""
cex_sdk.models.metrics -- Token, cost and timing metrics for LLM calls.

Absorbed from: agno/metrics.py
CEX version: 7.1.0
Pillar: P02 (Model)
8F function: GOVERN (F7)

# Originally from agno (https://github.com/agno-agi/agno)
# Licensed under MPL-2.0. Modified for CEX integration.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from dataclasses import fields as dc_fields
from enum import Enum
from typing import Any, Dict, List, Optional

from cex_sdk.utils.timer import Timer


class ModelType(str, Enum):
    """Functional role of a model within an agent run."""
    MODEL = "model"
    OUTPUT_MODEL = "output_model"
    PARSER_MODEL = "parser_model"
    MEMORY_MODEL = "memory_model"
    REASONING_MODEL = "reasoning_model"
    COMPRESSION_MODEL = "compression_model"
    LEARNING_MODEL = "learning_model"


# ---------------------------------------------------------------------------
# Base Metrics
# ---------------------------------------------------------------------------

@dataclass
class BaseMetrics:
    """Token consumption metrics shared across all metric types."""
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    reasoning_tokens: int = 0
    cost: Optional[float] = None


# ---------------------------------------------------------------------------
# Model Metrics
# ---------------------------------------------------------------------------

@dataclass
class ModelMetrics(BaseMetrics):
    """Metrics for a specific model, aggregated by (provider, id)."""
    id: str = ""
    provider: str = ""
    provider_metrics: Optional[Dict[str, Any]] = None

    def accumulate(self, other: ModelMetrics) -> None:
        self.input_tokens += other.input_tokens or 0
        self.output_tokens += other.output_tokens or 0
        self.total_tokens += other.total_tokens or 0
        self.cache_read_tokens += other.cache_read_tokens or 0
        self.cache_write_tokens += other.cache_write_tokens or 0
        self.reasoning_tokens += other.reasoning_tokens or 0
        if other.cost is not None:
            self.cost = (self.cost or 0) + other.cost

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        return {k: v for k, v in d.items()
                if v is not None and (not isinstance(v, int) or v != 0)}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ModelMetrics:
        valid = {f.name for f in dc_fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in valid})


# ---------------------------------------------------------------------------
# Tool Call Metrics
# ---------------------------------------------------------------------------

@dataclass
class ToolCallMetrics:
    """Metrics for tool execution -- timing only."""
    timer: Optional[Timer] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    duration: Optional[float] = None

    def start_timer(self) -> None:
        if self.timer is None:
            self.timer = Timer()
        self.timer.start()
        from time import time
        if self.start_time is None:
            self.start_time = time()

    def stop_timer(self, set_duration: bool = True) -> None:
        if self.timer is not None:
            self.timer.stop()
            if set_duration:
                self.duration = self.timer.elapsed
        from time import time
        if self.end_time is None:
            self.end_time = time()

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d.pop("timer", None)
        return {k: v for k, v in d.items() if v is not None}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ToolCallMetrics:
        valid = {f.name for f in dc_fields(cls)} - {"timer"}
        return cls(**{k: v for k, v in data.items() if k in valid})


# ---------------------------------------------------------------------------
# Message Metrics
# ---------------------------------------------------------------------------

@dataclass
class MessageMetrics(BaseMetrics):
    """Message-level metrics -- token counts and timing."""
    timer: Optional[Timer] = None
    duration: Optional[float] = None
    time_to_first_token: Optional[float] = None
    provider_metrics: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d.pop("timer", None)
        return {k: v for k, v in d.items()
                if v is not None and (not isinstance(v, int) or v != 0)}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> MessageMetrics:
        valid = {f.name for f in dc_fields(cls)} - {"timer"}
        return cls(**{k: v for k, v in data.items() if k in valid})

    def start_timer(self) -> None:
        if self.timer is None:
            self.timer = Timer()
        self.timer.start()

    def stop_timer(self, set_duration: bool = True) -> None:
        if self.timer is not None:
            self.timer.stop()
            if set_duration:
                self.duration = self.timer.elapsed

    def set_time_to_first_token(self) -> None:
        if self.timer is not None and self.time_to_first_token is None:
            self.time_to_first_token = self.timer.elapsed


# ---------------------------------------------------------------------------
# Run Metrics
# ---------------------------------------------------------------------------

@dataclass
class RunMetrics(BaseMetrics):
    """Run-level metrics with per-model breakdown."""
    timer: Optional[Timer] = None
    time_to_first_token: Optional[float] = None
    duration: Optional[float] = None
    details: Optional[Dict[str, List[ModelMetrics]]] = None
    additional_metrics: Optional[Dict[str, Any]] = None

    def start_timer(self) -> None:
        if self.timer is None:
            self.timer = Timer()
        self.timer.start()

    def stop_timer(self, set_duration: bool = True) -> None:
        if self.timer is not None:
            self.timer.stop()
            if set_duration:
                self.duration = self.timer.elapsed

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d.pop("timer", None)
        return {k: v for k, v in d.items()
                if v is not None and (not isinstance(v, int) or v != 0)
                and (not isinstance(v, (dict, list)) or len(v) > 0)}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> RunMetrics:
        valid = {f.name for f in dc_fields(cls)} - {"timer"}
        filtered = {k: v for k, v in data.items() if k in valid}
        if "details" in filtered and filtered["details"] is not None:
            converted: Dict[str, List[ModelMetrics]] = {}
            for mt, mml in filtered["details"].items():
                converted[mt] = [ModelMetrics.from_dict(m) if isinstance(m, dict) else m for m in mml]
            filtered["details"] = converted
        return cls(**filtered)


# Backward-compat alias
Metrics = RunMetrics
