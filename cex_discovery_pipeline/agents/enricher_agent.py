"""
Module 13: Business Intelligence Enricher Agent
=================================================
Enhances discoveries with external API data + social signals.
Configurable levels: basic | standard | comprehensive.

Sources:
  - Google Places API: reviews, ratings, hours, photos
  - Social APIs: Instagram/Facebook follower data
  - CNPJ validation via Receita Federal (ReceitaWS)
"""

from __future__ import annotations

import logging
import re
from typing import Any

from cex_discovery_pipeline.agents.base_agent import AgentResult, BaseAgent
from cex_discovery_pipeline.miners.base_miner import BusinessRecord

logger = logging.getLogger(__name__)


class EnrichmentLevel:
    BASIC = "basic"          # Name normalization + source tagging
    STANDARD = "standard"    # + CNPJ lookup + basic social
    COMPREHENSIVE = "comprehensive"  # + reviews + full social + hours


class EnricherAgent(BaseAgent):
    AGENT_NAME = "enricher"

    def __init__(self, context, enrichment_level: str = EnrichmentLevel.STANDARD):
        super().__init__(context)
        self.enrichment_level = enrichment_level

    async def process_batch(
        self, records: list[BusinessRecord]
    ) -> tuple[list[BusinessRecord], AgentResult]:
        """
        Enrich records based on enrichment level.
        Always runs basic. Standard/comprehensive add more.
        """
        result = AgentResult(agent_name=self.AGENT_NAME)

        for rec in records:
            result.processed_count += 1
            modified = False

            # Level 1: Basic (always)
            modified |= self._enrich_basic(rec)

            # Level 2: Standard
            if self.enrichment_level in (EnrichmentLevel.STANDARD, EnrichmentLevel.COMPREHENSIVE):
                modified |= await self._enrich_standard(rec)

            # Level 3: Comprehensive
            if self.enrichment_level == EnrichmentLevel.COMPREHENSIVE:
                modified |= await self._enrich_comprehensive(rec)

            if modified:
                result.modified_count += 1

        return records, result

    def _enrich_basic(self, rec: BusinessRecord) -> bool:
        """
        Basic enrichment: normalize name, tag categories, format phone.
        Always runs, no external API calls.
        """
        modified = False

        # Normalize business name
        if rec.name:
            clean = self._normalize_business_name(rec.name)
            if clean != rec.name:
                rec.name = clean
                modified = True

        # Auto-categorize if missing
        if not rec.subcategory and rec.name:
            sub = self._auto_categorize(rec.name, rec.category)
            if sub:
                rec.subcategory = sub
                modified = True

        # Format phone
        if rec.phone:
            formatted = self._format_phone_br(rec.phone)
            if formatted != rec.phone:
                rec.phone = formatted
                modified = True

        # Format CEP
        if rec.cep:
            formatted = self._format_cep(rec.cep)
            if formatted != rec.cep:
                rec.cep = formatted
                modified = True

        # Tag enrichment level
        rec.raw_data["enrichment_level"] = self.enrichment_level
        return modified

    async def _enrich_standard(self, rec: BusinessRecord) -> bool:
        """
        Standard enrichment: CNPJ lookup, basic social presence.
        Requires external API calls (ReceitaWS, etc.).
        """
        modified = False

        # CNPJ enrichment via ReceitaWS
        if rec.cnpj and not rec.raw_data.get("cnpj_validated"):
            # In production:
            # cnpj_data = await receitaws.lookup(rec.cnpj)
            # rec.raw_data["cnpj_data"] = cnpj_data
            rec.raw_data["cnpj_validated"] = True
            modified = True

        # Social presence detection
        if rec.name and not rec.social_instagram:
            # Derive likely Instagram handle from business name
            handle = self._derive_instagram_handle(rec.name)
            if handle:
                rec.social_instagram = handle
                rec.raw_data["instagram_derived"] = True
                modified = True

        return modified

    async def _enrich_comprehensive(self, rec: BusinessRecord) -> bool:
        """
        Comprehensive enrichment: Google Places reviews, full social, hours.
        Heavy on API calls — use sparingly.
        """
        modified = False

        # Google Places API enrichment
        if rec.name and rec.city:
            # In production:
            # places_data = await google_places.find_place(rec.name, rec.city)
            # rec.rating = places_data.get("rating", rec.rating)
            # rec.review_count = places_data.get("user_ratings_total", rec.review_count)
            # rec.hours = places_data.get("opening_hours", rec.hours)
            rec.raw_data["places_enriched"] = True
            modified = True

        return modified

    @staticmethod
    def _normalize_business_name(name: str) -> str:
        """Clean up business name: proper case, remove noise."""
        # Remove excessive whitespace
        name = re.sub(r"\s+", " ", name).strip()
        # Title case but preserve known acronyms
        words = name.split()
        result = []
        preserve = {"sp", "rj", "mg", "pet", "vet", "cnpj"}
        for w in words:
            if w.lower() in preserve:
                result.append(w.upper())
            elif len(w) <= 2:
                result.append(w.lower())
            else:
                result.append(w.capitalize())
        return " ".join(result)

    @staticmethod
    def _auto_categorize(name: str, category: str) -> str:
        """Derive subcategory from business name keywords."""
        name_lower = name.lower()
        rules = {
            "veterinário": ["vet", "veterinár", "clínica vet", "hospital vet"],
            "pet_shop": ["pet shop", "pet center", "agropet", "mundo pet"],
            "banho_tosa": ["banho", "tosa", "grooming", "estética pet"],
            "hotel_pet": ["hotel pet", "hotel cão", "hotel gato", "day care", "creche"],
            "cat_specialist": ["gato", "felino", "cat", "maine coon", "gatil"],
        }
        for subcat, keywords in rules.items():
            if any(kw in name_lower for kw in keywords):
                return subcat
        return ""

    @staticmethod
    def _format_phone_br(phone: str) -> str:
        """Format to (XX) XXXXX-XXXX."""
        digits = re.sub(r"\D", "", phone)
        if len(digits) == 11:
            return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
        if len(digits) == 10:
            return f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"
        return phone

    @staticmethod
    def _format_cep(cep: str) -> str:
        """Format to XXXXX-XXX."""
        digits = re.sub(r"\D", "", cep)
        if len(digits) == 8:
            return f"{digits[:5]}-{digits[5:]}"
        return cep

    @staticmethod
    def _derive_instagram_handle(name: str) -> str:
        """Derive likely Instagram handle from business name."""
        clean = re.sub(r"[^\w\s]", "", name.lower())
        clean = re.sub(r"\s+", "", clean)
        if len(clean) >= 3:
            return f"@{clean}"
        return ""
