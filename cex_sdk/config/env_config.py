"""
cex_sdk.config.env_config -- Environment and secret configuration.

kind: env_config
kind: secret_config
pillar: P09
8F: F1 CONSTRAIN (load env) + F5 CALL (provider auth)
"""
# -*- coding: ascii -*-
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any


@dataclass
class SecretConfig:
    """
    kind: secret_config
    pillar: P09
    Manages secret references (never stores plaintext values).
    Values resolved at runtime from env vars or secret managers.
    """
    name: str
    env_key: str
    required: bool = True
    description: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def resolve(self) -> str | None:
        """Resolve secret from environment."""
        return os.environ.get(self.env_key)

    def is_available(self) -> bool:
        val = self.resolve()
        return val is not None and val.strip() != ""


@dataclass
class EnvConfig:
    """
    kind: env_config
    pillar: P09
    Typed environment configuration for a nucleus or tool.
    """
    nucleus: str = ""
    environment: str = "development"
    secrets: list[SecretConfig] = field(default_factory=list)
    overrides: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: str = "") -> str:
        if key in self.overrides:
            return self.overrides[key]
        return os.environ.get(key, default)

    def require(self, key: str) -> str:
        val = self.get(key)
        if not val:
            raise ValueError(f"Required env var not set: {key}")
        return val

    def validate_secrets(self) -> list[str]:
        """Return list of missing required secrets."""
        missing = []
        for s in self.secrets:
            if s.required and not s.is_available():
                missing.append(s.env_key)
        return missing

    def is_production(self) -> bool:
        return self.environment == "production"

    @classmethod
    def from_env(cls, nucleus: str = "") -> "EnvConfig":
        return cls(
            nucleus=nucleus,
            environment=os.environ.get("CEX_ENV", "development"),
        )
