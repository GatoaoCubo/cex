"""
cex_sdk.config.retry_policy -- Retry policy with exponential backoff.

kind: retry_policy
pillar: P09
8F: F5 CALL (resilient tool invocation)
"""
# -*- coding: ascii -*-
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable, TypeVar

T = TypeVar("T")


@dataclass
class RetryResult:
    """Outcome of a retry-wrapped call."""
    success: bool
    value: Any = None
    attempts: int = 0
    last_error: Exception | None = None
    total_wait_ms: float = 0.0


@dataclass
class RetryPolicy:
    """
    kind: retry_policy
    pillar: P09
    Exponential backoff with jitter for resilient external calls.
    8F: F5 CALL -- wraps provider calls, circuit breaker, fallback chain.
    """
    max_attempts: int = 3
    base_delay_ms: float = 500.0
    max_delay_ms: float = 30000.0
    backoff_multiplier: float = 2.0
    jitter: bool = True
    retryable_exceptions: tuple[type[Exception], ...] = field(
        default_factory=lambda: (Exception,)
    )
    metadata: dict[str, Any] = field(default_factory=dict)

    def _delay(self, attempt: int) -> float:
        delay = min(
            self.base_delay_ms * (self.backoff_multiplier ** attempt),
            self.max_delay_ms,
        )
        if self.jitter:
            import random
            delay *= 0.5 + random.random() * 0.5
        return delay

    def execute(self, fn: Callable[[], T]) -> RetryResult:
        """Execute fn with retry policy. Returns RetryResult."""
        total_wait = 0.0
        last_err: Exception | None = None
        for attempt in range(self.max_attempts):
            try:
                value = fn()
                return RetryResult(
                    success=True,
                    value=value,
                    attempts=attempt + 1,
                    total_wait_ms=total_wait,
                )
            except self.retryable_exceptions as e:
                last_err = e
                if attempt + 1 < self.max_attempts:
                    wait = self._delay(attempt)
                    time.sleep(wait / 1000.0)
                    total_wait += wait
        return RetryResult(
            success=False,
            attempts=self.max_attempts,
            last_error=last_err,
            total_wait_ms=total_wait,
        )

    @classmethod
    def aggressive(cls) -> "RetryPolicy":
        return cls(max_attempts=5, base_delay_ms=200.0, backoff_multiplier=1.5)

    @classmethod
    def conservative(cls) -> "RetryPolicy":
        return cls(max_attempts=2, base_delay_ms=2000.0, backoff_multiplier=3.0)

    @classmethod
    def no_retry(cls) -> "RetryPolicy":
        return cls(max_attempts=1, base_delay_ms=0.0)
