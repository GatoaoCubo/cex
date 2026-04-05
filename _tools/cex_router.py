#!/usr/bin/env python3
"""CEX Smart Router — Config-driven, health-checked provider routing.

Pattern: OpenClaude SmartRouter (smart_router.py)
Adapted for CEX nucleus routing with YAML config.

Features:
  - Async health pings on startup
  - EMA latency tracking from real requests
  - Automatic fallback when primary is unhealthy
  - Strategy scoring: latency / cost / balanced
  - Self-healing: unhealthy providers rechecked

Usage:
    from cex_router import get_router
    router = get_router()
    route = router.resolve_nucleus("N03_builder")
    # → {"provider": "anthropic", "model": "claude-opus-4-20250514", "api_key": "sk-..."}

CLI:
    python cex_router.py --status
    python cex_router.py --resolve N03_builder
    python cex_router.py --ping
"""

import argparse
import asyncio
import logging
import os
import sys
import time
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, List

logger = logging.getLogger(__name__)

CEX_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = CEX_ROOT / ".cex" / "router_config.yaml"


@dataclass
class Provider:
    """A configured LLM provider with health tracking."""
    name: str
    ping_url: str
    api_key_env: str
    cost_per_1k: float
    models: dict
    healthy: bool = True
    avg_latency_ms: float = 9999.0
    request_count: int = 0
    error_count: int = 0

    @property
    def api_key(self) -> Optional[str]:
        if not self.api_key_env:
            return None
        return os.getenv(self.api_key_env)

    @property
    def is_configured(self) -> bool:
        """Local providers (ollama) need no API key."""
        if self.name in ("ollama", "atomic-chat"):
            return True
        return bool(self.api_key)

    @property
    def error_rate(self) -> float:
        return self.error_count / max(1, self.request_count)

    def score(self, strategy: str = "balanced") -> float:
        """Lower score = better provider.

        strategy: 'latency' | 'cost' | 'balanced'
        """
        if not self.healthy or not self.is_configured:
            return float("inf")

        latency = self.avg_latency_ms / 1000.0
        cost = self.cost_per_1k * 100
        penalty = self.error_rate * 500

        if strategy == "latency":
            return latency + penalty
        elif strategy == "cost":
            return cost + penalty
        return (latency * 0.5 + cost * 0.5) + penalty


class CexRouter:
    """Routes nucleus requests to optimal providers."""

    def __init__(self, config_path: Path = CONFIG_PATH):
        self.config = self._load_config(config_path)
        self.providers: dict[str, Provider] = {}
        self.strategy = self.config.get("strategy", "balanced")
        self.fallback_enabled = self.config.get("fallback", True)
        self._initialized = False
        self._build_providers()

    def _load_config(self, path: Path) -> dict:
        if path.exists():
            try:
                return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            except Exception as e:
                logger.warning(f"Failed to load router config: {e}")
        return {}

    def _build_providers(self):
        for name, cfg in self.config.get("providers", {}).items():
            self.providers[name] = Provider(
                name=name,
                ping_url=cfg.get("ping_url", ""),
                api_key_env=cfg.get("api_key_env", ""),
                cost_per_1k=cfg.get("cost_per_1k", 0),
                models=cfg.get("models", {}),
            )

    async def initialize(self):
        """Ping all providers and establish health baseline."""
        tasks = [self._ping(p) for p in self.providers.values()]
        await asyncio.gather(*tasks, return_exceptions=True)
        available = [
            p.name for p in self.providers.values()
            if p.healthy and p.is_configured
        ]
        logger.info(f"CexRouter ready. Available: {available}")
        self._initialized = True

    async def _ping(self, provider: Provider):
        """Measure latency to a provider's health endpoint."""
        if not provider.is_configured:
            provider.healthy = False
            return

        try:
            import httpx
        except ImportError:
            # httpx not available — mark as healthy if configured (assume OK)
            provider.healthy = provider.is_configured
            provider.avg_latency_ms = 500.0  # Assumed
            return

        headers = {}
        if provider.api_key:
            headers["Authorization"] = f"Bearer {provider.api_key}"

        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                start = time.monotonic()
                resp = await client.get(provider.ping_url, headers=headers)
                elapsed = (time.monotonic() - start) * 1000

                if resp.status_code in (200, 400, 401, 403):
                    provider.healthy = True
                    provider.avg_latency_ms = elapsed
                    logger.info(
                        f"CexRouter: {provider.name} OK ({elapsed:.0f}ms)"
                    )
                else:
                    provider.healthy = False
                    logger.warning(
                        f"CexRouter: {provider.name} unhealthy (status={resp.status_code})"
                    )
        except Exception as e:
            provider.healthy = False
            logger.warning(f"CexRouter: {provider.name} unreachable — {e}")

    def resolve_nucleus(self, nucleus: str) -> dict:
        """Resolve nucleus to provider + model + key.

        Tries primary first, then fallback chain.
        Env var overrides: CEX_{NUCLEUS}_MODEL, CEX_{NUCLEUS}_PROVIDER

        Returns:
            {"provider": name, "model": model_name, "api_key": key}

        Raises:
            RuntimeError if no healthy provider available.
        """
        # Check env var override first (backward compat)
        nuc_upper = nucleus.upper().replace("_", "")
        env_model = os.getenv(f"CEX_{nuc_upper}_MODEL")
        env_provider = os.getenv(f"CEX_{nuc_upper}_PROVIDER")
        if env_model and env_provider:
            p = self.providers.get(env_provider)
            return {
                "provider": env_provider,
                "model": env_model,
                "api_key": p.api_key if p else "",
            }

        routing = self.config.get("nucleus_routing", {})
        nuc_config = routing.get(nucleus, {})

        primary_name = nuc_config.get("primary", "anthropic")
        model_tier = nuc_config.get("model_tier", "sonnet")
        fallbacks = nuc_config.get("fallback", [])

        # Try primary
        primary = self.providers.get(primary_name)
        if primary and primary.healthy and primary.is_configured:
            model = self._resolve_model(primary, model_tier)
            return {
                "provider": primary.name,
                "model": model,
                "api_key": primary.api_key or "",
            }

        # Try fallbacks
        if self.fallback_enabled:
            for fb_name in fallbacks:
                fb = self.providers.get(fb_name)
                if fb and fb.healthy and fb.is_configured:
                    model = self._resolve_model(fb, model_tier)
                    logger.warning(f"Fallback: {nucleus} → {fb.name}/{model}")
                    return {
                        "provider": fb.name,
                        "model": model,
                        "api_key": fb.api_key or "",
                    }

        raise RuntimeError(
            f"No healthy provider for {nucleus}. "
            f"Primary: {primary_name} (healthy={primary.healthy if primary else 'N/A'}). "
            f"Fallbacks: {fallbacks}"
        )

    def _resolve_model(self, provider: Provider, tier: str) -> str:
        """Resolve model tier to actual model name."""
        if tier in provider.models:
            return provider.models[tier]
        # Fallback: try first available model
        if provider.models:
            return next(iter(provider.models.values()))
        return "unknown"

    def record_result(self, provider_name: str, success: bool, duration_ms: float):
        """Update provider stats after a request (EMA latency, error tracking)."""
        p = self.providers.get(provider_name)
        if not p:
            return

        p.request_count += 1

        if success:
            alpha = 0.3  # Weight for new observation
            p.avg_latency_ms = alpha * duration_ms + (1 - alpha) * p.avg_latency_ms
        else:
            p.error_count += 1
            if p.request_count >= 3 and p.error_rate > 0.7:
                p.healthy = False
                logger.warning(
                    f"{provider_name} marked unhealthy "
                    f"(error rate: {p.error_rate:.0%})"
                )

    def status(self) -> list[dict]:
        """Provider status dashboard."""
        return [
            {
                "provider": p.name,
                "healthy": "OK" if p.healthy else "FAIL",
                "configured": "OK" if p.is_configured else "NO",
                "latency_ms": round(p.avg_latency_ms, 1),
                "cost/1k": p.cost_per_1k,
                "requests": p.request_count,
                "errors": p.error_count,
                "score": round(p.score(self.strategy), 3)
                         if p.healthy and p.is_configured else "N/A",
            }
            for p in self.providers.values()
        ]


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_router: Optional[CexRouter] = None


def get_router() -> CexRouter:
    """Get the singleton router instance."""
    global _router
    if _router is None:
        _router = CexRouter()
    return _router


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="CEX Smart Router")
    parser.add_argument("--status", action="store_true", help="Show provider status")
    parser.add_argument("--resolve", metavar="NUCLEUS", help="Resolve nucleus to provider")
    parser.add_argument("--ping", action="store_true", help="Ping all providers")
    args = parser.parse_args()

    router = get_router()

    if args.ping:
        print("Pinging providers...")
        asyncio.run(router.initialize())
        args.status = True  # Show status after ping

    if args.status:
        print(f"\n=== CexRouter Status (strategy: {router.strategy}) ===\n")
        print(f"  {'Provider':12s} {'Health':>6s} {'Config':>6s} {'Latency':>9s} {'Cost':>6s} {'Reqs':>5s} {'Errs':>5s} {'Score':>7s}")
        print(f"  {'-'*60}")
        for row in router.status():
            print(
                f"  {row['provider']:12s} {row['healthy']:>6s} {row['configured']:>6s} "
                f"{row['latency_ms']:>8.1f}ms {row['cost/1k']:>5.3f} "
                f"{row['requests']:>5d} {row['errors']:>5d} {str(row['score']):>7s}"
            )

    elif args.resolve:
        try:
            result = router.resolve_nucleus(args.resolve)
            print(f"\n  Nucleus:  {args.resolve}")
            print(f"  Provider: {result['provider']}")
            print(f"  Model:    {result['model']}")
            print(f"  API Key:  {'***' + result['api_key'][-4:] if result['api_key'] else 'N/A'}")
        except RuntimeError as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
