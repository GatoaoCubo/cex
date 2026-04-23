"""
cex_sdk.config.rate_limit -- Rate limit configuration and enforcement.

kind: rate_limit_config
pillar: P09
8F: F5 CALL (throttle external calls)
"""
# -*- coding: ascii -*-
from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any


@dataclass
class RateLimitConfig:
    """
    kind: rate_limit_config
    pillar: P09
    Defines rate limit policy for a provider or endpoint.
    """
    name: str
    requests_per_minute: int = 60
    requests_per_day: int = 10000
    concurrent_limit: int = 5
    retry_after_ms: int = 1000
    burst_allowance: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def window_seconds(self) -> float:
        return 60.0 / max(self.requests_per_minute, 1)


class RateLimiter:
    """
    Token-bucket rate limiter enforcing RateLimitConfig.
    Thread-safety: single-process only (no distributed state).
    """

    def __init__(self, config: RateLimitConfig) -> None:
        self.config = config
        self._minute_window: deque[float] = deque()
        self._day_window: deque[float] = deque()
        self._concurrent = 0

    def _prune(self) -> None:
        now = time.monotonic()
        while self._minute_window and now - self._minute_window[0] > 60.0:
            self._minute_window.popleft()
        while self._day_window and now - self._day_window[0] > 86400.0:
            self._day_window.popleft()

    def is_allowed(self) -> bool:
        self._prune()
        if len(self._minute_window) >= self.config.requests_per_minute:
            return False
        if len(self._day_window) >= self.config.requests_per_day:
            return False
        if self._concurrent >= self.config.concurrent_limit:
            return False
        return True

    def acquire(self) -> bool:
        if not self.is_allowed():
            return False
        now = time.monotonic()
        self._minute_window.append(now)
        self._day_window.append(now)
        self._concurrent += 1
        return True

    def release(self) -> None:
        self._concurrent = max(0, self._concurrent - 1)

    def wait_time_ms(self) -> int:
        if self.is_allowed():
            return 0
        return self.config.retry_after_ms

    def stats(self) -> dict[str, Any]:
        self._prune()
        return {
            "name": self.config.name,
            "requests_last_minute": len(self._minute_window),
            "requests_today": len(self._day_window),
            "concurrent": self._concurrent,
            "limit_rpm": self.config.requests_per_minute,
            "limit_concurrent": self.config.concurrent_limit,
        }
