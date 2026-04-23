"""
cex_sdk.schema.data_contract -- Producer/consumer data contract.

kind: data_contract
pillar: P06
8F: F1 CONSTRAIN + F8 COLLABORATE (inter-nucleus interface contract)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from cex_sdk.schema.input_schema import InputSchema


class VersionPolicy(str, Enum):
    STRICT = "strict"       # breaking changes require major bump
    COMPATIBLE = "compatible"  # additive changes only, no major bump
    LOOSE = "loose"         # no version enforcement


@dataclass
class ContractVersion:
    """Semantic version with compatibility policy."""
    major: int = 1
    minor: int = 0
    patch: int = 0
    policy: VersionPolicy = VersionPolicy.COMPATIBLE

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def is_compatible_with(self, other: "ContractVersion") -> bool:
        if self.policy == VersionPolicy.STRICT:
            return self.major == other.major and self.minor == other.minor
        if self.policy == VersionPolicy.COMPATIBLE:
            return self.major == other.major and self.minor >= other.minor
        return True


@dataclass
class DataContract:
    """
    kind: data_contract
    pillar: P06
    Schema-level producer/consumer agreement with typed fields,
    numeric SLAs, and versioning policy. Used at nucleus handoff points
    to enforce LLM-to-LLM interface correctness.
    """
    name: str
    producer: str
    consumer: str
    version: ContractVersion = field(default_factory=ContractVersion)
    input_schema: InputSchema | None = None
    output_schema: InputSchema | None = None
    sla_latency_ms: int = 5000
    sla_availability_pct: float = 99.0
    description: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate_input(self, payload: dict[str, Any]) -> list[str]:
        if self.input_schema is None:
            return []
        return self.input_schema.validate(payload)

    def validate_output(self, payload: dict[str, Any]) -> list[str]:
        if self.output_schema is None:
            return []
        return self.output_schema.validate(payload)

    def is_compatible(self, other_version: ContractVersion) -> bool:
        return self.version.is_compatible_with(other_version)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "version": str(self.version),
            "producer": self.producer,
            "consumer": self.consumer,
            "sla_latency_ms": self.sla_latency_ms,
            "sla_availability_pct": self.sla_availability_pct,
            "input_schema": self.input_schema.to_json_schema() if self.input_schema else None,
            "output_schema": self.output_schema.to_json_schema() if self.output_schema else None,
        }
