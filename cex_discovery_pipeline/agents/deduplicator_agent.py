"""
Module 12: Cross-Source Deduplicator Agent
============================================
Intelligent duplicate detection across mining sources.
Uses fuzzy name matching + exact phone matching + address proximity.

Confidence weights:
  - phone_match: 0.8 (strongest signal — same phone = same business)
  - address_match: 0.6
  - name_match: 0.4

Target: <5% duplicate rate.
"""

from __future__ import annotations

import logging
import re
from difflib import SequenceMatcher
from typing import Any

from cex_discovery_pipeline.agents.base_agent import AgentResult, BaseAgent
from cex_discovery_pipeline.miners.base_miner import BusinessRecord

logger = logging.getLogger(__name__)


class DeduplicatorAgent(BaseAgent):
    AGENT_NAME = "deduplicator"

    # Match thresholds
    PHONE_WEIGHT = 0.8
    ADDRESS_WEIGHT = 0.6
    NAME_WEIGHT = 0.4
    DUPLICATE_THRESHOLD = 0.75  # Above this = duplicate

    async def process_batch(
        self, records: list[BusinessRecord]
    ) -> tuple[list[BusinessRecord], AgentResult]:
        """
        Remove duplicates from records. Keep the record with highest confidence.
        Merge data from duplicates into the keeper.
        """
        result = AgentResult(agent_name=self.AGENT_NAME)
        result.processed_count = len(records)

        if not records:
            return records, result

        # Phase 1: Exact phone dedup (fast pass)
        phone_groups = self._group_by_phone(records)

        # Phase 2: Fuzzy name+address dedup within each group
        unique: list[BusinessRecord] = []
        seen_indices: set[int] = set()

        for i, rec_a in enumerate(records):
            if i in seen_indices:
                continue

            duplicates = [rec_a]
            for j in range(i + 1, len(records)):
                if j in seen_indices:
                    continue
                rec_b = records[j]
                sim = self._similarity_score(rec_a, rec_b)
                if sim >= self.DUPLICATE_THRESHOLD:
                    duplicates.append(rec_b)
                    seen_indices.add(j)

            # Merge duplicates: keep highest confidence, merge missing fields
            merged = self._merge_duplicates(duplicates)
            unique.append(merged)
            seen_indices.add(i)

        result.modified_count = len(records) - len(unique)
        result.rejected_count = result.modified_count  # Rejected = removed dupes
        result.metadata["duplicate_rate"] = (
            result.rejected_count / max(len(records), 1)
        )

        logger.info(
            "[Dedup] %d records -> %d unique (%.1f%% duplicate rate)",
            len(records), len(unique),
            result.metadata["duplicate_rate"] * 100,
        )
        return unique, result

    def _group_by_phone(self, records: list[BusinessRecord]) -> dict[str, list[int]]:
        """Group record indices by normalized phone number."""
        groups: dict[str, list[int]] = {}
        for i, rec in enumerate(records):
            phone = self._normalize_phone(rec.phone)
            if phone:
                groups.setdefault(phone, []).append(i)
        return groups

    def _similarity_score(self, a: BusinessRecord, b: BusinessRecord) -> float:
        """
        Weighted similarity between two records.
        Uses phone (exact), name (fuzzy), address (fuzzy).
        """
        scores: list[tuple[float, float]] = []

        # Phone: exact match
        phone_a = self._normalize_phone(a.phone)
        phone_b = self._normalize_phone(b.phone)
        if phone_a and phone_b:
            phone_sim = 1.0 if phone_a == phone_b else 0.0
            scores.append((phone_sim, self.PHONE_WEIGHT))

        # Name: fuzzy match
        if a.name and b.name:
            name_sim = self._fuzzy_match(
                self._normalize_name(a.name),
                self._normalize_name(b.name),
            )
            scores.append((name_sim, self.NAME_WEIGHT))

        # Address: fuzzy match
        if a.address and b.address:
            addr_sim = self._fuzzy_match(
                self._normalize_address(a.address),
                self._normalize_address(b.address),
            )
            scores.append((addr_sim, self.ADDRESS_WEIGHT))

        if not scores:
            return 0.0

        total_weight = sum(w for _, w in scores)
        return sum(s * w for s, w in scores) / total_weight

    def _merge_duplicates(self, duplicates: list[BusinessRecord]) -> BusinessRecord:
        """
        Merge multiple duplicate records into one.
        Keep the record with highest confidence, fill missing fields from others.
        """
        if len(duplicates) == 1:
            return duplicates[0]

        # Sort by confidence (highest first)
        duplicates.sort(key=lambda r: r.confidence, reverse=True)
        keeper = duplicates[0]

        for donor in duplicates[1:]:
            # Fill missing fields from donor
            if not keeper.phone and donor.phone:
                keeper.phone = donor.phone
            if not keeper.address and donor.address:
                keeper.address = donor.address
            if not keeper.cep and donor.cep:
                keeper.cep = donor.cep
            if not keeper.email and donor.email:
                keeper.email = donor.email
            if not keeper.website and donor.website:
                keeper.website = donor.website
            if not keeper.cnpj and donor.cnpj:
                keeper.cnpj = donor.cnpj
            if not keeper.social_facebook and donor.social_facebook:
                keeper.social_facebook = donor.social_facebook
            if not keeper.social_instagram and donor.social_instagram:
                keeper.social_instagram = donor.social_instagram
            if donor.rating > keeper.rating:
                keeper.rating = donor.rating
            if donor.review_count > keeper.review_count:
                keeper.review_count = donor.review_count

        # Track merge history
        keeper.raw_data["merged_from"] = [d.source for d in duplicates]
        keeper.raw_data["merge_count"] = len(duplicates)
        # Boost confidence for multi-source confirmation
        keeper.confidence = min(1.0, keeper.confidence + 0.05 * (len(duplicates) - 1))

        return keeper

    @staticmethod
    def _normalize_phone(phone: str) -> str:
        """Strip to digits only for comparison."""
        if not phone:
            return ""
        digits = re.sub(r"\D", "", phone)
        # Remove country code if present
        if digits.startswith("55") and len(digits) > 11:
            digits = digits[2:]
        return digits

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Lowercase, strip common suffixes (LTDA, ME, EIRELI, etc.)."""
        n = name.lower().strip()
        for suffix in [" ltda", " me", " eireli", " epp", " s/a", " sa"]:
            n = n.replace(suffix, "")
        return re.sub(r"\s+", " ", n).strip()

    @staticmethod
    def _normalize_address(address: str) -> str:
        """Lowercase, standardize abbreviations."""
        a = address.lower().strip()
        replacements = {
            "rua ": "r. ", "avenida ": "av. ", "alameda ": "al. ",
            "travessa ": "tv. ", "praça ": "pç. ",
        }
        for full, abbrev in replacements.items():
            a = a.replace(full, abbrev)
        return a

    @staticmethod
    def _fuzzy_match(a: str, b: str) -> float:
        """SequenceMatcher ratio for fuzzy string comparison."""
        if not a or not b:
            return 0.0
        return SequenceMatcher(None, a, b).ratio()
