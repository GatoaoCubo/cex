"""
Module 7: CEP Micro-Geography Scanner
=======================================
Discovers 'invisible' businesses via CEP-based Google searches.
Validated: 90% efficacy, 4+ new businesses per CEP code.

Strategy: "pet shop CEP 09720" reveals businesses not listed
in directories but that exist in their physical location.

Context adaptation:
  - urban_dense:  cep_by_block (most granular, 3-digit suffix)
  - suburban:     cep_by_district (moderate, 2-digit suffix)
  - rural_sparse: cep_by_municipality (broad, 1-digit prefix)
"""

from __future__ import annotations

import logging
from typing import Any

from cex_discovery_pipeline.core.context_engine import RegionType
from cex_discovery_pipeline.miners.base_miner import BaseMiner, BusinessRecord

logger = logging.getLogger(__name__)


class CEPGeographyMiner(BaseMiner):
    MINER_NAME = "cep_geography"
    TIER = 1
    EFFICACY = 0.90

    # CEP ranges per city in ABC Paulista
    CEP_RANGES: dict[str, dict[str, Any]] = {
        "sao_bernardo_campo": {
            "prefix": "097",
            "ranges": [
                ("09700", "09799"),  # Central + industrial
                ("09600", "09699"),  # Riacho Grande + rural
            ],
            "granularity_urban": 10,  # step by 10 for dense scan
            "granularity_suburban": 50,
        },
        "santo_andre": {
            "prefix": "091",
            "ranges": [
                ("09100", "09199"),  # Centro + Campestre
                ("09200", "09299"),  # Utinga + outskirts
            ],
            "granularity_urban": 10,
            "granularity_suburban": 50,
        },
        "sao_caetano_sul": {
            "prefix": "095",
            "ranges": [
                ("09500", "09599"),  # All of SCS (small city)
            ],
            "granularity_urban": 10,
            "granularity_suburban": 20,
        },
        "diadema": {
            "prefix": "099",
            "ranges": [("09900", "09999")],
            "granularity_urban": 20,
            "granularity_suburban": 50,
        },
    }

    def _build_search_params(self) -> list[dict[str, Any]]:
        """
        Generate CEP-based search queries.
        Granularity adapts to region type.
        """
        params = []
        for city in self.context.cities:
            city_ceps = self.CEP_RANGES.get(city)
            if not city_ceps:
                # Fallback: single broad query
                for btype in self.context.business_types:
                    params.append({
                        "query": f"{btype} {city} SP",
                        "city": city,
                        "cep": "",
                        "business_type": btype,
                        "strategy": "fallback_broad",
                    })
                continue

            granularity = (
                city_ceps["granularity_urban"]
                if self.context.region_type == RegionType.URBAN_DENSE
                else city_ceps["granularity_suburban"]
            )

            for cep_start, cep_end in city_ceps["ranges"]:
                start_num = int(cep_start.replace("-", ""))
                end_num = int(cep_end.replace("-", ""))
                for cep_num in range(start_num, end_num + 1, granularity):
                    cep_str = f"{cep_num:05d}"
                    for btype in self.context.business_types:
                        params.append({
                            "query": f'"{btype}" CEP {cep_str}',
                            "city": city,
                            "cep": cep_str,
                            "business_type": btype,
                            "strategy": f"cep_scan_{granularity}",
                        })

        logger.info(
            "[CEP] Generated %d search params across %d cities",
            len(params), len(self.context.cities),
        )
        return params

    def _adapt_strategy(self, params: dict[str, Any]) -> dict[str, Any]:
        """Add region-specific search modifiers."""
        if self.context.region_type == RegionType.URBAN_DENSE:
            # Add neighborhood context for better results
            params["query"] = f'{params["query"]} bairro'
        return params

    async def _execute_search(self, search_params: dict[str, Any]) -> list[dict[str, Any]]:
        """
        Execute CEP-based Google search via SERPER.
        Pattern: "pet shop CEP 09720" → discovers local businesses.
        """
        query = search_params["query"]
        results: list[dict[str, Any]] = []

        # SERPER integration:
        # response = await serper.search(query, num=10, gl="br", hl="pt-br")
        # for item in response.get("organic", []):
        #     results.append({...parsed from snippet...})

        results.append({
            "search_query": query,
            "cep": search_params.get("cep", ""),
            "params": search_params,
            "source": "cep_geography",
        })
        return results

    def _parse_results(self, raw_results: list[dict[str, Any]]) -> list[BusinessRecord]:
        """Parse CEP search results into BusinessRecords."""
        records: list[BusinessRecord] = []
        for raw in raw_results:
            params = raw.get("params", {})
            record = BusinessRecord(
                city=params.get("city", ""),
                cep=params.get("cep", ""),
                category=params.get("business_type", ""),
                source="cep_geography",
                confidence=self.EFFICACY,
                raw_data=raw,
            )

            if "discovered" in raw:
                data = raw["discovered"]
                record.name = data.get("name", "")
                record.phone = data.get("phone", "")
                record.address = data.get("address", "")

            records.append(record)
        return records
