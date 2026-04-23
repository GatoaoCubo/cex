"""
cex_sdk.utils.timer -- High-resolution timer.

Absorbed from: agno/utils/timer.py
CEX version: 7.0.0
"""

from dataclasses import dataclass, field
from time import perf_counter
from typing import Optional


@dataclass
class Timer:
    """Simple elapsed-time tracker."""

    _start: Optional[float] = field(default=None, repr=False)
    elapsed: Optional[float] = None

    def start(self) -> "Timer":
        self._start = perf_counter()
        self.elapsed = None
        return self

    def stop(self) -> float:
        if self._start is not None:
            self.elapsed = perf_counter() - self._start
        return self.elapsed or 0.0

    def __enter__(self) -> "Timer":
        return self.start()

    def __exit__(self, *_) -> None:
        self.stop()
