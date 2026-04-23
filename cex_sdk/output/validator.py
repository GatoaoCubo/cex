"""
cex_sdk.output.validator -- Output validation against schema and quality gates.

kind: output_validator
pillar: P05
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

REQUIRED_FRONTMATTER = {"id", "kind", "pillar", "title", "quality"}
MIN_QUALITY = 8.0
MIN_DENSITY = 0.78


@dataclass
class ValidationResult:
    passed: bool = True
    score: float = 0.0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def fail(self, reason: str) -> None:
        self.passed = False
        self.errors.append(reason)

    def warn(self, reason: str) -> None:
        self.warnings.append(reason)


class OutputValidator:
    """
    Validate artifact output against CEX quality gates (F7 GOVERN).

    kind: output_validator
    pillar: P05
    8F position: F7 GOVERN
    """

    def __init__(
        self,
        min_quality: float = MIN_QUALITY,
        min_density: float = MIN_DENSITY,
        required_fields: set[str] | None = None,
    ) -> None:
        self.min_quality = min_quality
        self.min_density = min_density
        self.required_fields = required_fields or REQUIRED_FRONTMATTER

    def validate(self, frontmatter: dict[str, Any], body: str) -> ValidationResult:
        result = ValidationResult()

        # H01: required frontmatter fields
        missing = self.required_fields - set(frontmatter.keys())
        if missing:
            result.fail(f"missing_frontmatter: {sorted(missing)}")

        # H02: quality field
        q = frontmatter.get("quality")
        if q is None:
            result.warn("quality_null: assign peer-review score")
        elif isinstance(q, (int, float)) and float(q) < self.min_quality:
            result.fail(f"quality_below_threshold: {q} < {self.min_quality}")

        # H03: body not empty
        if not body or len(body.strip()) < 100:
            result.fail("body_too_short: < 100 chars")

        # H04: density (non-blank lines / total lines)
        lines = body.splitlines()
        if lines:
            non_blank = sum(1 for l in lines if l.strip())
            density = non_blank / len(lines)
            result.score = density
            if density < self.min_density:
                result.warn(f"density_low: {density:.2f} < {self.min_density}")

        return result

    def validate_batch(
        self, artifacts: list[dict[str, Any]]
    ) -> dict[str, ValidationResult]:
        results = {}
        for art in artifacts:
            aid = art.get("frontmatter", {}).get("id", "unknown")
            results[aid] = self.validate(
                art.get("frontmatter", {}), art.get("body", "")
            )
        return results
