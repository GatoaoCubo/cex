"""
Module 1: Context-Aware Discovery Configuration Engine
=======================================================
Analyzes region, niche, and market characteristics to auto-configure
pipeline execution strategy. Every downstream module reads ContextConfig.
"""

from __future__ import annotations

import logging
import math
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

CONFIG_DIR = Path(__file__).parent.parent / "config"


class RegionType(Enum):
    URBAN_DENSE = "urban_dense"
    SUBURBAN_SPREAD = "suburban_spread"
    RURAL_SPARSE = "rural_sparse"
    METROPOLITAN = "metropolitan"


class NicheLevel(Enum):
    BROAD_ECOSYSTEM = "broad_ecosystem"
    FOCUSED_SPECIALTY = "focused_specialty"
    ULTRA_NICHE = "ultra_niche"


class ExecutionMode(Enum):
    COMPREHENSIVE = "comprehensive"
    FAST_SCAN = "fast_scan"
    PREMIUM_DEEP = "premium_deep"


class MarketMaturity(Enum):
    ESTABLISHED = "established"
    EMERGING = "emerging"
    SATURATED = "saturated"


class DataAvailability(Enum):
    RICH = "rich"
    MODERATE = "moderate"
    SPARSE = "sparse"


@dataclass
class ContextConfig:
    """Immutable context passed to every pipeline module."""

    region_type: RegionType = RegionType.URBAN_DENSE
    niche_level: NicheLevel = NicheLevel.BROAD_ECOSYSTEM
    execution_mode: ExecutionMode = ExecutionMode.COMPREHENSIVE
    market_maturity: MarketMaturity = MarketMaturity.ESTABLISHED
    data_availability: DataAvailability = DataAvailability.RICH

    # Region specifics
    region_name: str = ""
    cities: list[str] = field(default_factory=list)
    population: int = 0
    business_density: str = "medium"  # high | medium | low

    # Niche specifics
    niche_name: str = ""
    business_types: list[str] = field(default_factory=list)
    primary_keywords: list[str] = field(default_factory=list)
    secondary_keywords: list[str] = field(default_factory=list)

    # Technique config (filled by engine)
    technique_priorities: list[str] = field(default_factory=list)
    max_parallel_miners: int = 4
    timeout_seconds: int = 7200  # 2h default

    # Quality thresholds
    phone_confidence_threshold: float = 0.85
    address_confidence_threshold: float = 0.80
    similarity_threshold: float = 0.75
    existence_confidence: float = 0.70


class ContextEngine:
    """
    Analyzes region + niche + market to produce a ContextConfig
    that drives all downstream module behavior.
    """

    def __init__(self, config_dir: Path | None = None):
        self._config_dir = config_dir or CONFIG_DIR
        self._niche_defs: dict[str, Any] = {}
        self._region_profiles: dict[str, Any] = {}
        self._technique_weights: dict[str, Any] = {}
        self._quality_gates: dict[str, Any] = {}
        self._load_configs()

    def _load_configs(self) -> None:
        for name, attr in [
            ("niche_definitions.yaml", "_niche_defs"),
            ("region_profiles.yaml", "_region_profiles"),
            ("technique_weights.yaml", "_technique_weights"),
            ("quality_gates.yaml", "_quality_gates"),
        ]:
            path = self._config_dir / name
            if path.exists():
                with open(path, encoding="utf-8") as f:
                    setattr(self, attr, yaml.safe_load(f) or {})
                logger.info("Loaded config: %s", name)
            else:
                logger.warning("Config not found: %s", path)

    # ── Region Analysis ──────────────────────────────────────────

    def analyze_region(self, region_key: str) -> dict[str, Any]:
        """Return region profile with type classification."""
        profile = self._region_profiles.get("profiles", {}).get(region_key, {})
        if not profile:
            logger.warning("Unknown region %s, using defaults", region_key)
            return {"type": "urban_dense", "population": 0, "business_density": "medium"}
        return profile

    def classify_region_type(self, population: int, area_km2: float = 1.0) -> RegionType:
        density = population / max(area_km2, 0.1)
        if density > 5000:
            return RegionType.URBAN_DENSE
        if density > 1000:
            return RegionType.SUBURBAN_SPREAD
        return RegionType.RURAL_SPARSE

    # ── Niche Analysis ───────────────────────────────────────────

    def analyze_niche(self, niche_key: str) -> dict[str, Any]:
        """Return niche definition with business types and keywords."""
        niches = self._niche_defs.get("niches", {})
        return niches.get(niche_key, {})

    def classify_niche_level(self, business_types: list[str]) -> NicheLevel:
        count = len(business_types)
        if count >= 6:
            return NicheLevel.BROAD_ECOSYSTEM
        if count >= 3:
            return NicheLevel.FOCUSED_SPECIALTY
        return NicheLevel.ULTRA_NICHE

    # ── Technique Prioritization ─────────────────────────────────

    def prioritize_techniques(
        self, region_type: RegionType, niche_level: NicheLevel
    ) -> list[str]:
        """Return ordered list of miner keys based on context."""
        weights = self._technique_weights.get("techniques", {})
        if not weights:
            return [
                "google_maps", "facebook_business", "yellow_pages",
                "cep_geography", "delivery_apps", "marketplace", "waze",
            ]

        scored: list[tuple[str, float]] = []
        for tech_key, tech_cfg in weights.items():
            base = tech_cfg.get("base_weight", 0.5)
            region_mod = tech_cfg.get("region_modifiers", {}).get(region_type.value, 0.0)
            niche_mod = tech_cfg.get("niche_modifiers", {}).get(niche_level.value, 0.0)
            scored.append((tech_key, base + region_mod + niche_mod))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [t[0] for t in scored]

    # ── Execution Strategy ───────────────────────────────────────

    def determine_execution_mode(
        self,
        niche_level: NicheLevel,
        estimated_market_size: int,
    ) -> ExecutionMode:
        if niche_level == NicheLevel.ULTRA_NICHE:
            return ExecutionMode.PREMIUM_DEEP
        if estimated_market_size > 500:
            return ExecutionMode.COMPREHENSIVE
        return ExecutionMode.FAST_SCAN

    def estimate_market_size(
        self, population: int, niche_key: str
    ) -> int:
        """Rough estimate: businesses = population * niche_density_factor."""
        density_factors = {
            "pet_ecosystem": 0.0003,  # ~1 pet biz per 3,300 people
            "restaurant": 0.001,
            "beauty": 0.0005,
            "auto": 0.0004,
        }
        factor = density_factors.get(niche_key, 0.0003)
        return max(1, math.ceil(population * factor))

    # ── Main Entry ───────────────────────────────────────────────

    def build_context(
        self,
        region_key: str,
        niche_key: str,
        *,
        business_types: list[str] | None = None,
        execution_mode: ExecutionMode | None = None,
    ) -> ContextConfig:
        """
        Build a complete ContextConfig from region + niche keys.
        This is the main entry point — returns the config that
        every downstream module will consume.
        """
        # Region
        region_profile = self.analyze_region(region_key)
        region_type = RegionType(region_profile.get("type", "urban_dense"))
        population = region_profile.get("population", 0)
        cities = region_profile.get("cities", [region_key])
        density = region_profile.get("business_density", "medium")

        # Niche
        niche_def = self.analyze_niche(niche_key)
        all_types = business_types or (
            niche_def.get("core_types", [])
            + niche_def.get("specialized_types", [])
        )
        niche_level = self.classify_niche_level(all_types)
        primary_kw = niche_def.get("search_patterns", {}).get("primary_keywords", [])
        secondary_kw = niche_def.get("search_patterns", {}).get("secondary_keywords", [])

        # Technique priorities
        technique_priorities = self.prioritize_techniques(region_type, niche_level)

        # Execution mode
        est_market = self.estimate_market_size(population, niche_key)
        mode = execution_mode or self.determine_execution_mode(niche_level, est_market)

        # Quality gates from config
        gates = self._quality_gates.get("thresholds", {})

        # Parallel limits by mode
        parallel_map = {
            ExecutionMode.COMPREHENSIVE: 4,
            ExecutionMode.FAST_SCAN: 6,
            ExecutionMode.PREMIUM_DEEP: 2,
        }

        timeout_map = {
            ExecutionMode.COMPREHENSIVE: 14400,  # 4h
            ExecutionMode.FAST_SCAN: 3600,        # 1h
            ExecutionMode.PREMIUM_DEEP: 7200,     # 2h
        }

        config = ContextConfig(
            region_type=region_type,
            niche_level=niche_level,
            execution_mode=mode,
            market_maturity=MarketMaturity(
                region_profile.get("market_maturity", "established")
            ),
            data_availability=DataAvailability(
                region_profile.get("data_availability", "moderate")
            ),
            region_name=region_key,
            cities=cities,
            population=population,
            business_density=density,
            niche_name=niche_key,
            business_types=all_types,
            primary_keywords=primary_kw,
            secondary_keywords=secondary_kw,
            technique_priorities=technique_priorities,
            max_parallel_miners=parallel_map.get(mode, 4),
            timeout_seconds=timeout_map.get(mode, 7200),
            phone_confidence_threshold=gates.get("phone_confidence", 0.85),
            address_confidence_threshold=gates.get("address_confidence", 0.80),
            similarity_threshold=gates.get("similarity", 0.75),
            existence_confidence=gates.get("existence", 0.70),
        )

        logger.info(
            "Context built: region=%s (%s), niche=%s (%s), mode=%s, "
            "techniques=%d, market_est=%d",
            region_key, region_type.value, niche_key, niche_level.value,
            mode.value, len(technique_priorities), est_market,
        )
        return config
