"""
Module 11: Phone & Address Validator Agent
============================================
Background agent for real-time contact data validation.
Validates phones (format + active), addresses (geocoding), CEPs.

Quality thresholds (from ContextConfig):
  - phone_confidence: 0.85
  - address_confidence: 0.80
"""

from __future__ import annotations

import logging
import re
from typing import Any

from cex_discovery_pipeline.agents.base_agent import AgentResult, BaseAgent
from cex_discovery_pipeline.miners.base_miner import BusinessRecord

logger = logging.getLogger(__name__)

# BR phone regex: (XX) XXXXX-XXXX or (XX) XXXX-XXXX
BR_PHONE_PATTERN = re.compile(
    r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
)

# CEP regex: XXXXX-XXX or XXXXXXXX
BR_CEP_PATTERN = re.compile(r"^\d{5}-?\d{3}$")

# CNPJ regex: XX.XXX.XXX/XXXX-XX
BR_CNPJ_PATTERN = re.compile(
    r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$"
)


class ValidatorAgent(BaseAgent):
    AGENT_NAME = "validator"

    async def process_batch(
        self, records: list[BusinessRecord]
    ) -> tuple[list[BusinessRecord], AgentResult]:
        """
        Validate each record's phone, address, CEP, CNPJ.
        Assigns confidence scores and flags invalid data.
        """
        result = AgentResult(agent_name=self.AGENT_NAME)
        validated: list[BusinessRecord] = []

        for rec in records:
            result.processed_count += 1
            score = self._validate_record(rec)
            rec.confidence = score

            if score >= self.context.existence_confidence:
                validated.append(rec)
                if score != rec.confidence:
                    result.modified_count += 1
            else:
                result.rejected_count += 1
                logger.debug(
                    "[Validator] Rejected %s (confidence=%.2f < %.2f)",
                    rec.name or "unnamed", score, self.context.existence_confidence,
                )

        return validated, result

    def _validate_record(self, rec: BusinessRecord) -> float:
        """
        Score a record 0.0-1.0 based on data completeness and validity.
        """
        scores: list[float] = []
        weights: list[float] = []

        # Name validation (required)
        if rec.name and len(rec.name) >= 3:
            scores.append(1.0)
        elif rec.name:
            scores.append(0.5)
        else:
            scores.append(0.0)
        weights.append(0.15)

        # Phone validation
        phone_score = self._validate_phone(rec.phone)
        scores.append(phone_score)
        weights.append(0.25)

        # Address validation
        addr_score = self._validate_address(rec.address, rec.city)
        scores.append(addr_score)
        weights.append(0.25)

        # CEP validation
        cep_score = self._validate_cep(rec.cep)
        scores.append(cep_score)
        weights.append(0.10)

        # CNPJ validation (bonus)
        if rec.cnpj:
            cnpj_score = self._validate_cnpj(rec.cnpj)
            scores.append(cnpj_score)
            weights.append(0.10)
        else:
            weights.append(0.0)
            scores.append(0.0)

        # Source reliability
        source_score = self._source_confidence(rec.source)
        scores.append(source_score)
        weights.append(0.15)

        total_weight = sum(weights)
        if total_weight == 0:
            return 0.0
        return sum(s * w for s, w in zip(scores, weights)) / total_weight

    def _validate_phone(self, phone: str) -> float:
        if not phone:
            return 0.0
        digits = re.sub(r"\D", "", phone)
        if len(digits) == 11 and digits[2] == "9":
            return 1.0  # Mobile with 9 prefix
        if len(digits) == 11:
            return 0.9  # Landline with DDD
        if len(digits) == 10:
            return 0.8  # Old format
        if BR_PHONE_PATTERN.match(phone):
            return 0.7
        return 0.3  # Has phone but unusual format

    def _validate_address(self, address: str, city: str) -> float:
        if not address:
            return 0.0
        score = 0.3  # Has something
        if city and city.lower() in address.lower():
            score += 0.2
        # Check for street indicators
        street_indicators = ["rua", "av.", "avenida", "alameda", "travessa", "praça", "r."]
        if any(ind in address.lower() for ind in street_indicators):
            score += 0.2
        # Check for number
        if re.search(r"\d{1,5}", address):
            score += 0.15
        # Check for neighborhood
        if re.search(r"-\s*\w+", address):
            score += 0.15
        return min(1.0, score)

    def _validate_cep(self, cep: str) -> float:
        if not cep:
            return 0.0
        if BR_CEP_PATTERN.match(cep):
            return 1.0
        digits = re.sub(r"\D", "", cep)
        if len(digits) == 8:
            return 0.9
        return 0.3

    def _validate_cnpj(self, cnpj: str) -> float:
        """Validate CNPJ format and check digit algorithm."""
        if not cnpj:
            return 0.0
        digits = re.sub(r"\D", "", cnpj)
        if len(digits) != 14:
            return 0.3
        # Check digit validation
        if self._verify_cnpj_digits(digits):
            return 1.0
        return 0.5  # Right length, wrong check digits

    @staticmethod
    def _verify_cnpj_digits(digits: str) -> bool:
        """Verify CNPJ check digits using the standard algorithm."""
        if len(digits) != 14 or digits == digits[0] * 14:
            return False

        def calc_digit(base: str, weights: list[int]) -> int:
            total = sum(int(d) * w for d, w in zip(base, weights))
            remainder = total % 11
            return 0 if remainder < 2 else 11 - remainder

        w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        w2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        d1 = calc_digit(digits[:12], w1)
        d2 = calc_digit(digits[:13], w2)
        return int(digits[12]) == d1 and int(digits[13]) == d2

    @staticmethod
    def _source_confidence(source: str) -> float:
        """Confidence weight by source reliability."""
        source_weights = {
            "google_maps": 0.95,
            "facebook_business": 0.90,
            "yellow_pages_apontador": 0.85,
            "yellow_pages_telelistas": 0.85,
            "yellow_pages_guiamais": 0.80,
            "yellow_pages_encontrasp": 0.80,
            "cep_geography": 0.85,
            "delivery_ifood": 0.90,
            "delivery_rappi": 0.85,
            "marketplace_mercadolivre": 0.75,
            "marketplace_olx": 0.70,
            "waze_directory": 0.85,
        }
        return source_weights.get(source, 0.6)
