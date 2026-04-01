"""
cex_sdk.guardrails.prompt_injection — Prompt injection detection.

Absorbed from: agno/guardrails/prompt_injection.py
CEX version: 7.3.0 | Pillar: P07 | 8F: CONSTRAIN (F1)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from typing import List, Optional

from cex_sdk.guardrails.base import BaseGuardrail, InputGuardrailError


# Default injection patterns (EN + PT-BR)
DEFAULT_PATTERNS = [
    # English — core injection patterns
    "ignore previous instructions",
    "ignore all previous instructions",
    "ignore your instructions",
    "ignore all instructions",
    "ignore the above",
    "disregard previous",
    "disregard all previous",
    "you are now a",
    "forget everything above",
    "forget your instructions",
    "developer mode",
    "override safety",
    "disregard guidelines",
    "system prompt",
    "jailbreak",
    "act as if",
    "pretend you are",
    "roleplay as",
    "simulate being",
    "bypass restrictions",
    "ignore safeguards",
    "admin override",
    "root access",
    "forget everything",
    "do not follow",
    "new instructions",
    # Portuguese — BR injection patterns
    "ignore instruções anteriores",
    "ignore todas as instruções",
    "esqueça tudo acima",
    "esqueça suas instruções",
    "modo desenvolvedor",
    "finja que você é",
    "ignore as regras",
    "desative as proteções",
    "aja como se fosse",
    "modo administrador",
    "acesso root",
    "ignore as diretrizes",
    "desconsidere tudo",
    "novas instruções",
]


class PromptInjectionGuardrail(BaseGuardrail):
    """Detect prompt injection attempts.

    Args:
        patterns: Custom patterns list. Defaults to DEFAULT_PATTERNS.
    """

    def __init__(self, patterns: Optional[List[str]] = None):
        self.patterns = patterns or DEFAULT_PATTERNS

    def check(self, content: str) -> Optional[str]:
        lower = content.lower()
        for pattern in self.patterns:
            if pattern in lower:
                raise InputGuardrailError(
                    f"Potential prompt injection detected: '{pattern}'",
                    trigger="prompt_injection",
                )
        return None
