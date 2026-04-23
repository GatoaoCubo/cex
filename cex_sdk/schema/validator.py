"""
cex_sdk.schema.validator -- Artifact validation against schema and quality gates.

kind: validator
kind: output_validator
pillar: P06
8F: F7 GOVERN (H01-H07 gates, quality scoring)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from cex_sdk.schema.input_schema import InputSchema


@dataclass
class ValidatorResult:
    """
    kind: validator
    pillar: P06
    Result of a validation run: passed flag, score, errors, warnings.
    """
    passed: bool
    score: float
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    gates_passed: int = 0
    gates_total: int = 0

    @property
    def gate_ratio(self) -> str:
        return f"{self.gates_passed}/{self.gates_total}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "score": self.score,
            "errors": self.errors,
            "warnings": self.warnings,
            "gates": self.gate_ratio,
        }


@dataclass
class Validator:
    """
    kind: validator
    pillar: P06
    Runs H01-H07 quality gates and schema validation against an artifact payload.
    Wraps InputSchema validation with CEX-specific scoring (3-layer: structural,
    rubric, semantic). Used at F7 GOVERN in every 8F pipeline run.
    """
    name: str
    schema: InputSchema | None = None
    min_score: float = 8.0
    require_frontmatter: bool = True
    require_description: bool = True
    min_body_length: int = 100
    min_density: float = 0.85
    metadata: dict[str, Any] = field(default_factory=dict)

    # Gate weights (structural layer: 30%)
    _GATE_WEIGHT = 0.3 / 7

    def validate(self, payload: dict[str, Any]) -> ValidatorResult:
        errors: list[str] = []
        warnings: list[str] = []
        gates_passed = 0
        gates_total = 7

        # H01 -- frontmatter present
        if self.require_frontmatter:
            required_fm = {"id", "kind", "title"}
            missing = required_fm - set(payload.keys())
            if missing:
                errors.append(f"H01: missing frontmatter fields: {', '.join(sorted(missing))}")
            else:
                gates_passed += 1
        else:
            gates_passed += 1

        # H02 -- quality field must be null (not self-scored)
        quality = payload.get("quality")
        if quality is not None and quality != "null":
            warnings.append("H02: quality should be null (peer-review assigns score)")
        else:
            gates_passed += 1

        # H03 -- description present
        if self.require_description:
            desc = payload.get("description", "")
            if not desc or len(str(desc)) < 10:
                errors.append("H03: description missing or too short (< 10 chars)")
            else:
                gates_passed += 1
        else:
            gates_passed += 1

        # H04 -- body length
        body = payload.get("body", payload.get("content", ""))
        if isinstance(body, str) and len(body) < self.min_body_length:
            errors.append(f"H04: body too short ({len(body)} < {self.min_body_length} chars)")
        else:
            gates_passed += 1

        # H05 -- schema validation (if schema provided)
        if self.schema is not None:
            schema_errors = self.schema.validate(payload)
            if schema_errors:
                errors.extend([f"H05: {e}" for e in schema_errors])
            else:
                gates_passed += 1
        else:
            gates_passed += 1

        # H06 -- pillar field valid (P01-P12)
        pillar = payload.get("pillar", "")
        if pillar:
            valid_pillars = {f"P{i:02d}" for i in range(1, 13)}
            if pillar not in valid_pillars:
                warnings.append(f"H06: pillar '{pillar}' not in P01-P12")
            else:
                gates_passed += 1
        else:
            gates_passed += 1

        # H07 -- version field format
        version = payload.get("version", "")
        if version:
            parts = str(version).split(".")
            if len(parts) != 3 or not all(p.isdigit() for p in parts):
                warnings.append(f"H07: version '{version}' not semver (X.Y.Z)")
            else:
                gates_passed += 1
        else:
            gates_passed += 1

        # Structural score (30% weight, proportional to gates)
        structural = (gates_passed / gates_total) * 10.0 * 0.3

        # Rubric score (30% weight -- body density heuristic)
        if isinstance(body, str) and body:
            word_count = len(body.split())
            char_count = len(body)
            density = word_count / max(char_count / 5, 1)
            density_score = min(10.0, density * 10.0)
        else:
            density_score = 0.0
        rubric = density_score * 0.3

        # Semantic score (40% weight -- approximated structurally when no LLM)
        # Heuristic: presence of tables/sections/examples
        semantic_signals = 0
        if isinstance(body, str):
            if "|" in body:
                semantic_signals += 2  # table
            if "##" in body:
                semantic_signals += 2  # sections
            if "```" in body:
                semantic_signals += 2  # code block
            if "example" in body.lower():
                semantic_signals += 1
            if "kind:" in body.lower():
                semantic_signals += 1
            if "pillar:" in body.lower():
                semantic_signals += 1
            if "8" in body.lower() or "f1" in body.lower():
                semantic_signals += 1
        semantic = min(10.0, semantic_signals * 1.0) * 0.4

        score = round(structural + rubric + semantic, 1)
        passed = len(errors) == 0 and score >= self.min_score

        return ValidatorResult(
            passed=passed,
            score=score,
            errors=errors,
            warnings=warnings,
            gates_passed=gates_passed,
            gates_total=gates_total,
        )

    def is_valid(self, payload: dict[str, Any]) -> bool:
        return self.validate(payload).passed

    @classmethod
    def for_kind(cls, kind: str, pillar: str = "") -> "Validator":
        """Standard CEX artifact validator for a given kind."""
        return cls(
            name=f"validator_{kind}",
            require_frontmatter=True,
            require_description=True,
            min_score=8.0,
            min_body_length=200,
            metadata={"kind": kind, "pillar": pillar},
        )
