#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Provider Discovery -- detect available LLM providers

Usage:
  python _tools/cex_provider_discovery.py --status     # check all providers
  python _tools/cex_provider_discovery.py --json        # JSON output
  python _tools/cex_provider_discovery.py --provider anthropic  # check one

Checks:
  1. Anthropic: ANTHROPIC_API_KEY set + API ping
  2. Google: GEMINI_API_KEY or OAuth token + API ping
  3. OpenAI: OPENAI_API_KEY set + API ping
  4. Ollama: localhost:11434 ping (no key needed)

Reads: .cex/P09_config/nucleus_models.yaml (for fallback config)
       .cex/router_config.yaml (for ping URLs)
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
ROUTER_CONFIG = ROOT / ".cex" / "router_config.yaml"
NUCLEUS_MODELS = ROOT / ".cex" / "config" / "nucleus_models.yaml"
CACHE_PATH = ROOT / ".cex" / "runtime" / "provider_cache.json"
CACHE_TTL_SECONDS = 300  # 5 minutes


# ---------------------------------------------------------------------------
# Provider definitions (fallback if no router_config.yaml)
# ---------------------------------------------------------------------------

def _build_default_providers():
    """Build DEFAULT_PROVIDERS using model resolver when available."""
    _fallback = {
        "anthropic": {
            "ping_url": "https://api.anthropic.com/v1/messages",
            "api_key_env": "ANTHROPIC_API_KEY",
            "models": ["claude-opus-4-6", "claude-sonnet-4-6", "claude-haiku-4-5-20251001"],
        },
        "google": {
            "ping_url": "https://generativelanguage.googleapis.com/v1/models",
            "api_key_env": "GEMINI_API_KEY",
            "models": ["gemini-2.5-pro", "gemini-2.0-flash"],
        },
        "openai": {
            "ping_url": "https://api.openai.com/v1/models",
            "api_key_env": "OPENAI_API_KEY",
            "models": ["gpt-4.1", "gpt-4.1-mini"],
        },
        "ollama": {
            "ping_url": "http://localhost:11434/api/tags",
            "api_key_env": "",
            "models": ["llama3:70b", "llama3:8b"],
        },
    }
    try:
        from cex_model_resolver import get_ollama_config, load_nucleus_models
        nm = load_nucleus_models()
        if nm:
            # Gather unique Anthropic models from nucleus configs
            anthropic_models = set()
            for nuc in ("n01", "n02", "n03", "n04", "n05", "n06", "n07"):
                ncfg = nm.get(nuc, {})
                m = ncfg.get("model", "")
                if m.startswith("claude"):
                    anthropic_models.add(m)
            if anthropic_models:
                _fallback["anthropic"]["models"] = sorted(anthropic_models)
            # Ollama models from config
            ollama_cfg = get_ollama_config()
            ollama_models = ollama_cfg.get("models", {})
            if ollama_models:
                _fallback["ollama"]["models"] = [
                    v for v in ollama_models.values() if v
                ]
    except Exception:
        pass
    return _fallback


DEFAULT_PROVIDERS = _build_default_providers()


def _load_router_config() -> dict:
    """Load provider definitions from router_config.yaml if available."""
    if not ROUTER_CONFIG.exists() or yaml is None:
        return DEFAULT_PROVIDERS

    try:
        with open(ROUTER_CONFIG, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
        providers = cfg.get("providers", {})
        result = {}
        for name, pcfg in providers.items():
            models_dict = pcfg.get("models", {})
            model_list = list(models_dict.values()) if isinstance(models_dict, dict) else models_dict
            result[name] = {
                "ping_url": pcfg.get("ping_url", ""),
                "api_key_env": pcfg.get("api_key_env", ""),
                "models": model_list,
            }
        return result if result else DEFAULT_PROVIDERS
    except Exception:
        return DEFAULT_PROVIDERS


def _check_provider(name: str, cfg: dict) -> dict:
    """Check a single provider's availability.

    Returns dict with: provider, status, latency_ms, has_key, models, error
    """
    result = {
        "provider": name,
        "status": "UNKNOWN",
        "latency_ms": -1,
        "has_key": False,
        "models": cfg.get("models", []),
        "error": None,
    }

    # Key check (ollama needs no key)
    key_env = cfg.get("api_key_env", "")
    if key_env:
        api_key = os.environ.get(key_env, "")
        result["has_key"] = bool(api_key)
        if not api_key:
            result["status"] = "NO_KEY"
            result["error"] = f"Environment variable {key_env} not set"
            return result
    else:
        result["has_key"] = True  # No key needed (e.g., ollama)

    # Ping check
    ping_url = cfg.get("ping_url", "")
    if not ping_url:
        result["status"] = "NO_URL"
        result["error"] = "No ping URL configured"
        return result

    try:
        import urllib.error
        import urllib.request

        headers = {}
        if key_env:
            api_key = os.environ.get(key_env, "")
            if name == "anthropic":
                headers["x-api-key"] = api_key
                headers["anthropic-version"] = "2023-06-01"
            elif api_key:
                headers["Authorization"] = f"Bearer {api_key}"

        req = urllib.request.Request(ping_url, headers=headers, method="GET")
        start = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                elapsed = (time.monotonic() - start) * 1000
                result["latency_ms"] = round(elapsed, 1)
                result["status"] = "OK"
        except urllib.error.HTTPError as e:
            elapsed = (time.monotonic() - start) * 1000
            result["latency_ms"] = round(elapsed, 1)
            # 400/401/403/405 = reachable (auth rejected but server alive)
            if e.code in (400, 401, 403, 405):
                result["status"] = "OK"
            else:
                result["status"] = "FAIL"
                result["error"] = f"HTTP {e.code}"
    except urllib.error.URLError as e:
        result["status"] = "FAIL"
        result["error"] = f"Unreachable: {e.reason}"
    except Exception as e:
        result["status"] = "FAIL"
        result["error"] = str(e)[:100]

    return result


def discover_providers(use_cache: bool = True) -> dict:
    """Discover all available providers.

    Returns dict keyed by provider name with status info.
    Uses cached results if available and fresh (< 5min).
    """
    # Check cache
    if use_cache and CACHE_PATH.exists():
        try:
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                cached = json.load(f)
            age = time.time() - cached.get("timestamp", 0)
            if age < CACHE_TTL_SECONDS:
                return cached.get("providers", {})
        except Exception:
            pass

    # Fresh discovery
    provider_defs = _load_router_config()
    results = {}
    for name, cfg in provider_defs.items():
        results[name] = _check_provider(name, cfg)

    # Save cache
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump({"timestamp": time.time(), "providers": results}, f, indent=2)
    except Exception:
        pass

    return results


def get_best_provider(nucleus: str, providers: dict = None) -> str | None:
    """Get the best available model for a nucleus.

    Reads nucleus_models.yaml for primary assignment, checks if that provider
    is alive, falls back if not.

    Returns model string or None.
    """
    if providers is None:
        providers = discover_providers()

    # Load nucleus config for primary/fallback
    if yaml is None or not NUCLEUS_MODELS.exists():
        # No config -- use first available provider
        for name, info in providers.items():
            if info.get("status") == "OK":
                models = info.get("models", [])
                return models[0] if models else None
        return None

    try:
        with open(NUCLEUS_MODELS, "r", encoding="utf-8") as f:
            nuc_cfg = yaml.safe_load(f) or {}
    except Exception:
        return None

    nuc_key = nucleus.lower()[:3]
    cfg = nuc_cfg.get(nuc_key, {})
    try:
        from cex_model_resolver import resolve_model as _res_mdl
        _prov_default = _res_mdl(nucleus)["model"]
    except Exception:
        _prov_default = "claude-sonnet-4-6"
    primary_model = cfg.get("model", _prov_default)

    # Check if primary provider is alive
    # Infer provider from model name
    provider_name = _infer_provider(primary_model)
    prov_status = providers.get(provider_name, {})
    if prov_status.get("status") == "OK":
        return primary_model

    # Try fallback
    fb = cfg.get("fallback", {})
    if fb:
        fb_model = fb.get("model", "")
        fb_provider = _infer_provider(fb_model)
        fb_status = providers.get(fb_provider, {})
        if fb_status.get("status") == "OK":
            return fb_model

    # Last resort: any alive provider
    for name, info in providers.items():
        if info.get("status") == "OK":
            models = info.get("models", [])
            return models[0] if models else None

    return None


def _infer_provider(model: str) -> str:
    """Infer provider from model name."""
    model_lower = model.lower()
    if "claude" in model_lower or "opus" in model_lower or "sonnet" in model_lower or "haiku" in model_lower:
        return "anthropic"
    if "gemini" in model_lower:
        return "google"
    if "gpt" in model_lower or "o3" in model_lower or "o4" in model_lower:
        return "openai"
    if "llama" in model_lower or "qwen" in model_lower or "mistral" in model_lower:
        return "ollama"
    return "anthropic"  # default


def print_status(providers: dict):
    """Print provider status table."""
    print(f"\n  {'Provider':<12} {'Status':<8} {'Key':<6} {'Latency':<12} {'Models'}")
    print(f"  {'-'*65}")
    for name, info in providers.items():
        status = info.get("status", "?")
        has_key = "YES" if info.get("has_key") else "NO"
        latency = info.get("latency_ms", -1)
        lat_str = f"{latency:.0f}ms" if latency >= 0 else "N/A"
        models = info.get("models", [])
        model_str = ", ".join(models[:3])
        if len(models) > 3:
            model_str += f" (+{len(models)-3})"

        # Status indicator
        indicator = "OK" if status == "OK" else status

        print(f"  {name:<12} {indicator:<8} {has_key:<6} {lat_str:<12} {model_str}")

    # Summary
    alive = sum(1 for p in providers.values() if p.get("status") == "OK")
    total = len(providers)
    print(f"\n  {alive}/{total} providers available")
    if alive == 0:
        print("  [WARN] No providers available! Check API keys and network.")
    print()


def main():
    parser = argparse.ArgumentParser(description="CEX Provider Discovery")
    parser.add_argument("--status", action="store_true", help="Check all providers")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--provider", metavar="NAME", help="Check one provider")
    parser.add_argument("--no-cache", action="store_true", help="Skip cache")
    parser.add_argument("--best", metavar="N0X", help="Get best model for nucleus")
    args = parser.parse_args()

    if args.best:
        providers = discover_providers(use_cache=not args.no_cache)
        best = get_best_provider(args.best, providers)
        if args.json:
            print(json.dumps({"nucleus": args.best, "best_model": best}))
        else:
            print(f"  Best model for {args.best.upper()}: {best or 'NONE'}")
        return

    if args.provider:
        defs = _load_router_config()
        cfg = defs.get(args.provider)
        if not cfg:
            print(f"  [ERROR] Unknown provider: {args.provider}")
            print(f"  Available: {', '.join(defs.keys())}")
            sys.exit(1)
        result = _check_provider(args.provider, cfg)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_status({args.provider: result})
        return

    providers = discover_providers(use_cache=not args.no_cache)
    if args.json:
        print(json.dumps(providers, indent=2))
    else:
        print_status(providers)


if __name__ == "__main__":
    main()
