"""
cex_sdk.guardrails.pii -- PII detection guardrail.

Absorbed from: agno/guardrails/pii.py
CEX version: 7.3.0 | Pillar: P07 | 8F: CONSTRAIN (F1)
# Originally from agno. Licensed under MPL-2.0.

Detects: SSN, credit cards, email, phone (US + BR: CPF, CNPJ, CEP).
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Pattern

from cex_sdk.guardrails.base import BaseGuardrail, InputGuardrailError


class PIIDetectionGuardrail(BaseGuardrail):
    """Detect PII in input text.

    Args:
        mask_pii: If True, mask PII instead of raising error.
        enable_*: Toggle individual PII types.
        custom_patterns: Additional regex patterns {name: pattern}.
    """

    def __init__(
        self,
        mask_pii: bool = False,
        enable_ssn: bool = True,
        enable_credit_card: bool = True,
        enable_email: bool = True,
        enable_phone: bool = True,
        enable_cpf: bool = True,
        enable_cnpj: bool = True,
        custom_patterns: Optional[Dict[str, Pattern[str]]] = None,
    ):
        self.mask_pii = mask_pii
        self.patterns: Dict[str, Pattern[str]] = {}

        if enable_ssn:
            self.patterns["SSN"] = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
        if enable_credit_card:
            self.patterns["CreditCard"] = re.compile(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b")
        if enable_email:
            self.patterns["Email"] = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
        if enable_phone:
            self.patterns["Phone"] = re.compile(r"\b\d{3}[\s.-]?\d{3}[\s.-]?\d{4}\b")
        # Brazilian PII
        if enable_cpf:
            self.patterns["CPF"] = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
        if enable_cnpj:
            self.patterns["CNPJ"] = re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b")

        if custom_patterns:
            self.patterns.update(custom_patterns)

    def check(self, content: str) -> Optional[str]:
        detected: List[str] = []
        for pii_type, pattern in self.patterns.items():
            if pattern.search(content):
                detected.append(pii_type)

        if not detected:
            return None

        if self.mask_pii:
            masked = content
            for pii_type in detected:
                masked = self.patterns[pii_type].sub(
                    lambda m: "*" * len(m.group(0)), masked
                )
            return masked

        raise InputGuardrailError(
            f"PII detected: {', '.join(detected)}",
            trigger="pii_detection",
        )
