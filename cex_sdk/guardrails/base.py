"""
cex_sdk.guardrails.base -- Abstract base for guardrails.

Absorbed from: agno/guardrails/base.py
CEX version: 7.3.0 | Pillar: P07 | 8F: CONSTRAIN (F1) + GOVERN (F7)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class GuardrailError(Exception):
    """Raised when a guardrail check fails."""

    def __init__(self, message: str, trigger: str = "unknown"):
        super().__init__(message)
        self.trigger = trigger


class InputGuardrailError(GuardrailError):
    """Raised on input check failure (F1 CONSTRAIN)."""


class OutputGuardrailError(GuardrailError):
    """Raised on output check failure (F7 GOVERN)."""


class BaseGuardrail(ABC):
    """Abstract base class for all guardrails.

    Guardrails check input (F1 CONSTRAIN) or output (F7 GOVERN)
    and raise GuardrailError if the check fails.
    """

    @abstractmethod
    def check(self, content: str) -> Optional[str]:
        """Check content. Returns sanitized content or raises GuardrailError.

        Args:
            content: The text to check.

        Returns:
            Sanitized content (if masking) or None (if pass-through).

        Raises:
            InputGuardrailError: If input fails the check.
            OutputGuardrailError: If output fails the check.
        """
        ...

    async def async_check(self, content: str) -> Optional[str]:
        """Async check. Default wraps sync."""
        return self.check(content)
