"""
cex_sdk.tracing.exporter -- Trace exporter for 8F pipeline observability.

CEX version: 10.3.0 | 8F: GOVERN (F7)
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

from cex_sdk.utils.timer import Timer


@dataclass
class Span:
    """A single trace span (maps to one 8F function or workflow step)."""
    name: str
    span_id: str = ""
    parent_id: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    duration_ms: Optional[float] = None
    status: str = "ok"  # ok | error
    attributes: Dict[str, Any] = field(default_factory=dict)
    events: List[Dict[str, Any]] = field(default_factory=list)

    _timer: Optional[Timer] = field(default=None, repr=False)

    def __post_init__(self):
        if not self.span_id:
            from uuid import uuid4
            self.span_id = str(uuid4())[:8]

    def start(self) -> Span:
        self._timer = Timer().start()
        self.start_time = datetime.now().isoformat()
        return self

    def end(self, status: str = "ok") -> Span:
        if self._timer:
            self._timer.stop()
            self.duration_ms = (self._timer.elapsed or 0) * 1000
        self.end_time = datetime.now().isoformat()
        self.status = status
        return self

    def add_event(self, name: str, **attrs) -> None:
        self.events.append({"name": name, "time": datetime.now().isoformat(), **attrs})


@dataclass
class Trace:
    """A complete trace (maps to one 8F pipeline run)."""
    trace_id: str = ""
    name: str = ""
    spans: List[Span] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.trace_id:
            from uuid import uuid4
            self.trace_id = str(uuid4())[:12]

    def span(self, name: str, parent_id: Optional[str] = None) -> Span:
        s = Span(name=name, parent_id=parent_id).start()
        self.spans.append(s)
        return s

    def to_dict(self) -> Dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "name": self.name,
            "spans": [asdict(s) for s in self.spans],
            "metadata": self.metadata,
        }


class TraceExporter:
    """Export traces to file or stdout."""

    def __init__(self, output_dir: Optional[str] = None):
        self.output_dir = output_dir or os.path.join(".cex", "traces")

    def export(self, trace: Trace) -> str:
        """Export trace to JSON file. Returns filepath."""
        os.makedirs(self.output_dir, exist_ok=True)
        filename = f"trace_{trace.trace_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(trace.to_dict(), f, indent=2, ensure_ascii=False)
        return filepath

    def print_trace(self, trace: Trace) -> None:
        """Print trace summary to stdout."""
        print(f"\n{'='*60}")
        print(f"Trace: {trace.name} ({trace.trace_id})")
        print(f"{'='*60}")
        for s in trace.spans:
            indent = "  " if s.parent_id else ""
            status_icon = "\u2713" if s.status == "ok" else "[X]"
            dur = f"{s.duration_ms:.0f}ms" if s.duration_ms else "?"
            print(f"{indent}{status_icon} {s.name} [{dur}]")
            for k, v in s.attributes.items():
                print(f"{indent}  {k}: {v}")
        print(f"{'='*60}\n")
