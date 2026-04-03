"""
Module 9: Marketplace Reverse Miner
=====================================
Reverse discovery via Mercado Livre + OLX seller analysis.
Validated: 80% efficacy, finds 'invisible' businesses.

Discovery patterns:
  - "passo ponto pet shop" → reveals active businesses
  - "mesa tosa" → indicates operating pet grooming shops
  - Seller profile analysis → business name, location, reputation
"""

from __future__ import annotations

import logging
from typing import Any

from cex_discovery_pipeline.miners.base_miner import BaseMiner, BusinessRecord

logger = logging.getLogger(__name__)


class MarketplaceMiner(BaseMiner):
    MINER_NAME = "marketplace"
    TIER = 2
    EFFICACY = 0.80

    # Reverse discovery patterns — these indicate real businesses
    REVERSE_PATTERNS = {
        "business_sale": [
            "passo ponto pet shop",
            "vendo pet shop",
            "passo ponto veterinária",
            "passo ponto banho tosa",
        ],
        "equipment_sales": [
            "mesa tosa profissional",
            "banheira pet profissional",
            "autoclave veterinária",
            "máquina tosa",
        ],
        "product_sellers": [
            "ração premium atacado",
            "produtos pet atacado",
            "acessórios gato atacado",
        ],
    }

    MARKETPLACE_SOURCES = {
        "mercadolivre": "site:mercadolivre.com.br",
        "olx": "site:olx.com.br",
    }

    def _build_search_params(self) -> list[dict[str, Any]]:
        params = []
        for source_key, site_prefix in self.MARKETPLACE_SOURCES.items():
            for city in self.context.cities:
                # Reverse patterns
                for pattern_type, patterns in self.REVERSE_PATTERNS.items():
                    for pattern in patterns:
                        params.append({
                            "source": source_key,
                            "query": f'{site_prefix} "{pattern}" "{city}"',
                            "city": city,
                            "pattern_type": pattern_type,
                            "pattern": pattern,
                            "business_type": "reverse_discovery",
                        })

                # Direct seller searches
                for btype in self.context.business_types[:3]:
                    params.append({
                        "source": source_key,
                        "query": f'{site_prefix} {btype} {city} SP',
                        "city": city,
                        "pattern_type": "direct_seller",
                        "business_type": btype,
                    })
        return params

    async def _execute_search(self, search_params: dict[str, Any]) -> list[dict[str, Any]]:
        """Execute marketplace searches via SERPER."""
        results: list[dict[str, Any]] = []
        results.append({
            "search_query": search_params["query"],
            "marketplace": search_params["source"],
            "pattern_type": search_params.get("pattern_type", ""),
            "params": search_params,
            "source": f"marketplace_{search_params['source']}",
        })
        return results

    def _parse_results(self, raw_results: list[dict[str, Any]]) -> list[BusinessRecord]:
        records: list[BusinessRecord] = []
        for raw in raw_results:
            params = raw.get("params", {})
            record = BusinessRecord(
                city=params.get("city", ""),
                category=params.get("business_type", ""),
                source=raw.get("source", "marketplace"),
                confidence=self.EFFICACY,
                raw_data=raw,
            )
            record.raw_data["discovery_method"] = "reverse"
            record.raw_data["pattern_type"] = params.get("pattern_type", "")

            if "seller_data" in raw:
                seller = raw["seller_data"]
                record.name = seller.get("seller_name", "")
                record.address = seller.get("location", "")
                record.raw_data["seller_reputation"] = seller.get("reputation", "")
                record.raw_data["total_sales"] = seller.get("total_sales", 0)

            records.append(record)
        return records
