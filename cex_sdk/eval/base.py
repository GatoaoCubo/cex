"""
cex_sdk.eval.base -- Evaluation framework (pre_check / post_check).

Absorbed from: agno/eval/base.py
CEX version: 9.4.0 | Pillar: P07 | 8F: CONSTRAIN (F1) + GOVERN (F7)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class EvalResult:
    """Result of an evaluation check."""
    passed: bool = True
    score: float = 0.0
    notes: List[str] = field(default_factory=list)
    issues: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class BaseEval(ABC):
    """Abstract base class for evaluations.

    Integrates with CEX 8F pipeline:
    - pre_check runs at F1 CONSTRAIN (input validation)
    - post_check runs at F7 GOVERN (output validation)
    """

    @abstractmethod
    def pre_check(self, input_content: str, **context) -> EvalResult:
        """Validate input before processing (F1 CONSTRAIN)."""
        ...

    @abstractmethod
    def post_check(self, output_content: str, **context) -> EvalResult:
        """Validate output after processing (F7 GOVERN)."""
        ...

    async def async_pre_check(self, input_content: str, **context) -> EvalResult:
        return self.pre_check(input_content, **context)

    async def async_post_check(self, output_content: str, **context) -> EvalResult:
        return self.post_check(output_content, **context)


class QualityGateEval(BaseEval):
    """CEX quality gate -- checks frontmatter, size, structure.

    Maps to cex_score.py logic as a reusable BaseEval.
    """

    def __init__(self, min_quality: float = 8.0, min_bytes: int = 500):
        self.min_quality = min_quality
        self.min_bytes = min_bytes

    def pre_check(self, input_content: str, **context) -> EvalResult:
        issues = []
        if len(input_content.strip()) < 10:
            issues.append("Input too short (< 10 chars)")
        return EvalResult(passed=len(issues) == 0, issues=issues)

    def post_check(self, output_content: str, **context) -> EvalResult:
        issues = []
        notes = []
        score = 0.0

        size = len(output_content.encode("utf-8"))
        if size < self.min_bytes:
            issues.append(f"Output too small: {size}B < {self.min_bytes}B min")
        else:
            score += 2.0
            notes.append(f"Size OK: {size}B")

        # Check frontmatter
        if output_content.startswith("---"):
            score += 2.0
            notes.append("Has frontmatter")
        else:
            issues.append("Missing frontmatter")

        # Check headings
        headings = output_content.count("\n#")
        if headings >= 3:
            score += 2.0
            notes.append(f"{headings} headings")
        elif headings >= 1:
            score += 1.0

        # Check structure
        if "```" in output_content:
            score += 1.0
            notes.append("Has code blocks")
        if "|" in output_content and "---" in output_content:
            score += 1.0
            notes.append("Has tables")

        # Normalize to 10-point scale
        score = min(score / 8.0 * 10.0, 10.0)

        return EvalResult(
            passed=score >= self.min_quality and len(issues) == 0,
            score=score,
            notes=notes,
            issues=issues,
        )
