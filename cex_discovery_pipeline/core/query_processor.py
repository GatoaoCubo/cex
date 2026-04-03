"""
Module 14: Natural Language Query Processor
=============================================
Converts plain-language requests to pipeline configurations.

Examples:
  "Find pet shops in ABC Paulista"
    -> region_key=abc_metropolitano, niche_key=pet_ecosystem, business_types=[pet_shop]

  "Discover cat hotels in São Paulo"
    -> region_key=sao_paulo, niche_key=pet_ecosystem, business_types=[hotel_gato]
"""

from __future__ import annotations

import logging
import re
from typing import Any

logger = logging.getLogger(__name__)


# ── Keyword -> Semantic Mapping ──────────────────────────────────

REGION_KEYWORDS: dict[str, list[str]] = {
    "abc_metropolitano": [
        "abc", "abc paulista", "grande abc", "abcdmrr",
    ],
    "sao_bernardo_campo": [
        "são bernardo", "sao bernardo", "sbc", "s.b.campo",
    ],
    "santo_andre": [
        "santo andré", "santo andre", "sa",
    ],
    "sao_caetano_sul": [
        "são caetano", "sao caetano", "scs",
    ],
    "diadema": ["diadema"],
    "maua": ["mauá", "maua"],
    "sao_paulo": [
        "são paulo", "sao paulo", "sp", "capital",
    ],
    "grande_sao_paulo": [
        "grande são paulo", "grande sp", "rmsp",
        "região metropolitana",
    ],
}

NICHE_KEYWORDS: dict[str, list[str]] = {
    "pet_ecosystem": [
        "pet", "animal", "veterinário", "veterinaria",
        "gato", "cachorro", "cão", "felino",
        "banho", "tosa", "ração",
    ],
    "restaurant": [
        "restaurante", "comida", "alimentação",
        "lanchonete", "pizzaria", "padaria",
    ],
    "beauty": [
        "salão", "beleza", "cabeleireiro", "estética",
        "manicure", "barbearia",
    ],
    "auto": [
        "auto", "mecânica", "oficina", "funilaria",
        "borracharia", "autopeças",
    ],
}

BUSINESS_TYPE_KEYWORDS: dict[str, list[str]] = {
    "pet_shop": ["pet shop", "petshop", "loja pet", "agropet"],
    "clinica_vet": ["clínica veterinária", "veterinário", "vet", "clínica vet"],
    "banho_tosa": ["banho e tosa", "banho tosa", "grooming", "estética animal"],
    "hotel_pet": ["hotel pet", "hotel cachorro", "hotel cão", "day care pet", "creche pet"],
    "hotel_gato": ["hotel gato", "hotel felino", "cat hotel", "gatil hotel"],
    "hospital_vet": ["hospital veterinário", "hospital vet", "emergência vet", "24h vet"],
    "cat_cafe": ["cat café", "cat cafe", "café de gatos"],
    "breeder": ["criador", "gatil", "canil", "breeder"],
}


class QueryProcessor:
    """
    Parses natural language discovery requests into structured configs
    that the ContextEngine can consume.
    """

    def parse(self, query: str) -> dict[str, Any]:
        """
        Parse a natural language query into pipeline parameters.

        Returns dict with keys:
          - region_key: str
          - niche_key: str
          - business_types: list[str] | None
          - filters: dict[str, Any]
        """
        q = query.lower().strip()

        result: dict[str, Any] = {
            "region_key": self._detect_region(q),
            "niche_key": self._detect_niche(q),
            "business_types": self._detect_business_types(q),
            "filters": self._detect_filters(q),
            "original_query": query,
        }

        logger.info(
            "[QueryProcessor] Parsed: region=%s, niche=%s, types=%s",
            result["region_key"], result["niche_key"],
            result["business_types"],
        )
        return result

    def _detect_region(self, query: str) -> str:
        """Find best matching region from query."""
        best_match = "abc_metropolitano"  # Default for GATO3
        best_score = 0

        for region_key, keywords in REGION_KEYWORDS.items():
            for kw in keywords:
                if kw in query:
                    score = len(kw)  # Longer match = more specific
                    if score > best_score:
                        best_score = score
                        best_match = region_key
        return best_match

    def _detect_niche(self, query: str) -> str:
        """Find best matching niche from query."""
        scores: dict[str, int] = {}
        for niche_key, keywords in NICHE_KEYWORDS.items():
            for kw in keywords:
                if kw in query:
                    scores[niche_key] = scores.get(niche_key, 0) + 1

        if scores:
            return max(scores, key=scores.get)
        return "pet_ecosystem"  # Default for GATO3

    def _detect_business_types(self, query: str) -> list[str] | None:
        """Detect specific business types mentioned in query."""
        found: list[str] = []
        for btype, keywords in BUSINESS_TYPE_KEYWORDS.items():
            for kw in keywords:
                if kw in query:
                    if btype not in found:
                        found.append(btype)
                    break
        return found if found else None

    def _detect_filters(self, query: str) -> dict[str, Any]:
        """Detect additional filters: premium, 24h, etc."""
        filters: dict[str, Any] = {}

        if any(w in query for w in ["premium", "luxo", "alto padrão"]):
            filters["tier"] = "premium"
        if any(w in query for w in ["24h", "24 horas", "emergência"]):
            filters["hours"] = "24h"
        if any(w in query for w in ["delivery", "entrega"]):
            filters["has_delivery"] = True
        if any(w in query for w in ["online", "e-commerce"]):
            filters["has_online"] = True

        # Quantity hints
        qty_match = re.search(r"(?:top|melhores)\s+(\d+)", query)
        if qty_match:
            filters["limit"] = int(qty_match.group(1))

        return filters
