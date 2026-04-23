"""
cex_sdk.config.feature_flag -- Feature flag management.

kind: feature_flag
pillar: P09
8F: F1 CONSTRAIN (gate features) + F5 CALL (toggle check)
"""
# -*- coding: ascii -*-
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any


@dataclass
class FeatureFlag:
    """
    kind: feature_flag
    pillar: P09
    Single feature toggle with rollout percentage and targeting rules.
    """
    key: str
    enabled: bool = False
    rollout_pct: float = 0.0
    description: str = ""
    targeting: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_enabled(self, context: dict[str, Any] | None = None) -> bool:
        if not self.enabled:
            return False
        if self.rollout_pct >= 100.0:
            return True
        if self.rollout_pct <= 0.0:
            return False
        # Simple deterministic hash-based rollout
        if context and "user_id" in context:
            import hashlib
            h = int(hashlib.md5(f"{self.key}:{context['user_id']}".encode(), usedforsecurity=False).hexdigest(), 16)
            return (h % 100) < self.rollout_pct
        return self.rollout_pct >= 50.0

    @classmethod
    def from_env(cls, key: str, env_key: str | None = None) -> "FeatureFlag":
        """Read flag state from environment variable."""
        env = env_key or f"CEX_FLAG_{key.upper()}"
        val = os.environ.get(env, "false").lower()
        return cls(key=key, enabled=val in ("1", "true", "yes", "on"))


class FeatureFlagRegistry:
    """Registry of all feature flags. Loaded from config at F1 CONSTRAIN."""

    def __init__(self) -> None:
        self._flags: dict[str, FeatureFlag] = {}

    def register(self, flag: FeatureFlag) -> None:
        self._flags[flag.key] = flag

    def is_enabled(self, key: str, context: dict[str, Any] | None = None) -> bool:
        flag = self._flags.get(key)
        if flag is None:
            return False
        return flag.is_enabled(context)

    def get(self, key: str) -> FeatureFlag | None:
        return self._flags.get(key)

    def all_keys(self) -> list[str]:
        return sorted(self._flags.keys())

    def enabled_flags(self) -> list[str]:
        return [k for k, f in self._flags.items() if f.enabled]
