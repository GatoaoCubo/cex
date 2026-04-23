#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Model Updater -- Self-healing model discovery and update.

Queries provider APIs for available models, compares against
nucleus_models.yaml, and suggests or applies updates automatically.

Usage:
    python cex_model_updater.py --check          # Show stale models
    python cex_model_updater.py --discover        # Query APIs for latest
    python cex_model_updater.py --apply           # Auto-update nucleus_models.yaml
    python cex_model_updater.py --propagate       # After update, fix all references
    python cex_model_updater.py --full            # discover + apply + propagate

How it works:
    1. DISCOVER: Calls /v1/models on each provider API
    2. COMPARE:  Matches current config against discovered models
    3. SUGGEST:  Shows what's outdated, what's new
    4. APPLY:    Updates nucleus_models.yaml (single source of truth)
    5. PROPAGATE: Rewrites all stale references across repo

Self-heal integration:
    - flywheel_monitor.ps1 calls --check weekly
    - cex_auto.py cycle calls --check on each run
    - Manual: run --full after subscription changes
"""

import argparse
import json
import logging
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml

logger = logging.getLogger(__name__)

CEX_ROOT = Path(__file__).resolve().parent.parent
NUCLEUS_MODELS = CEX_ROOT / ".cex" / "config" / "nucleus_models.yaml"
MODEL_CACHE = CEX_ROOT / ".cex" / "cache" / "discovered_models.json"
SKIP_DIRS = {".git", "__pycache__", "node_modules", "_archive", "compiled"}
UPDATE_EXTENSIONS = {".py", ".yaml", ".yml", ".cmd", ".md", ".json", ".sh", ".ps1"}


# -- Model family definitions ------------------------------------------------

@dataclass
class ModelFamily:
    """A model family with known versions, ordered newest-first."""
    provider: str
    prefix: str
    tier: str
    api_env: str
    discover_url: str
    known_versions: list = field(default_factory=list)

FAMILIES = [
    ModelFamily(
        provider="anthropic", prefix="claude-opus", tier="opus",
        api_env="ANTHROPIC_API_KEY",
        discover_url="https://api.anthropic.com/v1/models",
        known_versions=["claude-opus-4-6", "claude-opus-4-20250514"],
    ),
    ModelFamily(
        provider="anthropic", prefix="claude-sonnet", tier="sonnet",
        api_env="ANTHROPIC_API_KEY",
        discover_url="https://api.anthropic.com/v1/models",
        known_versions=["claude-sonnet-4-6", "claude-sonnet-4-20250514"],
    ),
    ModelFamily(
        provider="anthropic", prefix="claude-haiku", tier="haiku",
        api_env="ANTHROPIC_API_KEY",
        discover_url="https://api.anthropic.com/v1/models",
        known_versions=["claude-haiku-4-5-20251001", "claude-haiku-4-5-20250901"],
    ),
    ModelFamily(
        provider="google", prefix="gemini", tier="large",
        api_env="GOOGLE_API_KEY",
        discover_url="https://generativelanguage.googleapis.com/v1beta/models",
        known_versions=["gemini-2.5-pro", "gemini-2.0-pro", "gemini-1.5-pro"],
    ),
    ModelFamily(
        provider="openai", prefix="gpt-4", tier="large",
        api_env="OPENAI_API_KEY",
        discover_url="https://api.openai.com/v1/models",
        known_versions=["gpt-4.1", "gpt-4o", "gpt-4-turbo"],
    ),
]


# -- Discovery ----------------------------------------------------------------

def _validate_url(url):
    """Reject non-HTTP schemes and private/loopback IPs (SSRF guard)."""
    import socket
    import urllib.parse
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("URL scheme %r not allowed" % parsed.scheme)
    hostname = (parsed.hostname or "").lower()
    if hostname in ("localhost", "[::]", "[::1]"):
        raise ValueError("Loopback hostname %r not allowed" % hostname)
    try:
        ip = socket.gethostbyname(parsed.hostname)
        parts = ip.split(".")
        if (parts[0] in ("10", "127")
                or (parts[0] == "172" and 16 <= int(parts[1]) <= 31)
                or (parts[0] == "192" and parts[1] == "168")
                or ip.startswith("169.254")
                or ip == "0.0.0.0"
                or ip == "::1"):
            raise ValueError("Private IP %s not allowed" % ip)
    except socket.gaierror:
        pass


def _http_get_json(url: str, headers: dict = None, timeout: int = 15) -> dict:
    """Simple HTTP GET returning parsed JSON. No external deps required."""
    import urllib.request
    _validate_url(url)
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def discover_anthropic(api_key: str) -> list[dict]:
    """Query Anthropic /v1/models for available models."""
    try:
        data = _http_get_json(
            "https://api.anthropic.com/v1/models",
            headers={"x-api-key": api_key, "anthropic-version": "2023-06-01"},
        )
        return [
            {"id": m["id"], "provider": "anthropic", "created": m.get("created_at", "")}
            for m in data.get("data", [])
            if "claude" in m.get("id", "")
        ]
    except Exception as e:
        logger.warning(f"Anthropic discovery failed: {e}")
        return []


def discover_openai(api_key: str) -> list[dict]:
    """Query OpenAI /v1/models."""
    try:
        data = _http_get_json(
            "https://api.openai.com/v1/models",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        return [
            {"id": m["id"], "provider": "openai", "created": m.get("created", 0)}
            for m in data.get("data", [])
            if m["id"].startswith(("gpt-4", "gpt-3", "o1", "o3", "o4"))
        ]
    except Exception as e:
        logger.warning(f"OpenAI discovery failed: {e}")
        return []


def discover_google(api_key: str) -> list[dict]:
    """Query Google AI /v1beta/models."""
    try:
        data = _http_get_json(
            f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}",
        )
        return [
            {"id": m["name"].replace("models/", ""), "provider": "google", "created": ""}
            for m in data.get("models", [])
            if "gemini" in m.get("name", "")
        ]
    except Exception as e:
        logger.warning(f"Google discovery failed: {e}")
        return []


def discover_all() -> list[dict]:
    """Run discovery on all configured providers."""
    all_models = []

    key = os.getenv("ANTHROPIC_API_KEY", "")
    if key:
        print("  Querying Anthropic API...")
        models = discover_anthropic(key)
        all_models.extend(models)
        print(f"    Found {len(models)} Claude models")
    else:
        print("  [skip] ANTHROPIC_API_KEY not set")

    key = os.getenv("OPENAI_API_KEY", "")
    if key:
        print("  Querying OpenAI API...")
        models = discover_openai(key)
        all_models.extend(models)
        print(f"    Found {len(models)} GPT/O-series models")
    else:
        print("  [skip] OPENAI_API_KEY not set")

    key = os.getenv("GOOGLE_API_KEY", "") or os.getenv("GOOGLE_AI_API_KEY", "")
    if key:
        print("  Querying Google AI API...")
        models = discover_google(key)
        all_models.extend(models)
        print(f"    Found {len(models)} Gemini models")
    else:
        print("  [skip] GOOGLE_API_KEY not set")

    # Cache results
    MODEL_CACHE.parent.mkdir(parents=True, exist_ok=True)
    cache_data = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "models": all_models}
    MODEL_CACHE.write_text(json.dumps(cache_data, indent=2), encoding="utf-8")
    print(f"\n  Cached {len(all_models)} models -> {MODEL_CACHE.relative_to(CEX_ROOT)}")

    return all_models


# -- Check / Compare ----------------------------------------------------------

def load_current_config() -> dict:
    """Load nucleus_models.yaml."""
    if not NUCLEUS_MODELS.exists():
        return {}
    return yaml.safe_load(NUCLEUS_MODELS.read_text(encoding="utf-8")) or {}


def _match_family(model_id: str) -> Optional[ModelFamily]:
    """Find which family a model belongs to."""
    for fam in FAMILIES:
        if model_id.startswith(fam.prefix) or model_id in fam.known_versions:
            return fam
    return None


def _enrich_families_from_cache():
    """If we have cached discovery results, add new model IDs to families."""
    if not MODEL_CACHE.exists():
        return
    try:
        cache = json.loads(MODEL_CACHE.read_text(encoding="utf-8"))
        for m in cache.get("models", []):
            mid = m["id"]
            for fam in FAMILIES:
                if mid.startswith(fam.prefix) and mid not in fam.known_versions:
                    # Insert at position based on ID (newer versions usually sort later)
                    fam.known_versions.insert(0, mid)
                    logger.info(f"Discovered new model: {mid} (family: {fam.prefix})")
    except Exception:
        pass


def check_staleness() -> list[dict]:
    """Compare current config against known latest versions."""
    _enrich_families_from_cache()
    config = load_current_config()
    stale = []

    for nuc_id, nuc_cfg in config.items():
        if not isinstance(nuc_cfg, dict) or not nuc_id.startswith("n0"):
            continue

        # Check primary model
        model = nuc_cfg.get("model", "")
        if model:
            fam = _match_family(model)
            if fam:
                latest = fam.known_versions[0]
                if model != latest:
                    stale.append({
                        "nucleus": nuc_id, "current": model,
                        "latest": latest, "provider": fam.provider, "tier": fam.tier,
                    })

        # Check fallback models
        for fb_key in ("fallback", "fallback_local"):
            fb = nuc_cfg.get(fb_key, {})
            if isinstance(fb, dict):
                fb_model = fb.get("model", "")
                fam = _match_family(fb_model)
                if fam and fb_model != fam.known_versions[0]:
                    stale.append({
                        "nucleus": f"{nuc_id}.{fb_key}", "current": fb_model,
                        "latest": fam.known_versions[0], "provider": fam.provider,
                        "tier": fam.tier,
                    })

    return stale


def scan_repo_references() -> dict[str, int]:
    """Count all model ID references across the repo."""
    all_ids = set()
    for fam in FAMILIES:
        all_ids.update(fam.known_versions)

    counts = {}
    for root, dirs, files in os.walk(CEX_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fname in files:
            fpath = Path(root) / fname
            if fpath.suffix not in UPDATE_EXTENSIONS:
                continue
            try:
                text = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            for mid in all_ids:
                c = text.count(mid)
                if c > 0:
                    counts[mid] = counts.get(mid, 0) + c
    return counts


# -- Apply --------------------------------------------------------------------

def apply_updates(stale: list[dict], dry_run: bool = False) -> int:
    """Update nucleus_models.yaml with latest model versions."""
    if not stale:
        print("  All models are current. Nothing to update.")
        return 0

    text = NUCLEUS_MODELS.read_text(encoding="utf-8")
    applied = 0

    for entry in stale:
        old, new = entry["current"], entry["latest"]
        if old in text:
            text = text.replace(old, new)
            applied += 1
            verb = "WOULD update" if dry_run else "Updated"
            print(f"  {verb}: {entry['nucleus']} {old} -> {new}")

    if not dry_run and applied > 0:
        NUCLEUS_MODELS.write_text(text, encoding="utf-8")
        print(f"\n  Applied {applied} updates to nucleus_models.yaml")

    return applied


# -- Propagate ----------------------------------------------------------------

def build_replacement_map() -> dict[str, str]:
    """Build old->new replacement map from all families."""
    replacements = {}
    for fam in FAMILIES:
        latest = fam.known_versions[0]
        for old_ver in fam.known_versions[1:]:
            replacements[old_ver] = latest
    return replacements


def propagate(replacements: dict[str, str], dry_run: bool = False) -> int:
    """Replace old model IDs across the entire repo."""
    changed = 0
    for root, dirs, files in os.walk(CEX_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fname in files:
            fpath = Path(root) / fname
            if fpath.suffix not in UPDATE_EXTENSIONS:
                continue
            try:
                text = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            original = text
            for old, new in replacements.items():
                text = text.replace(old, new)

            if text != original:
                count = sum(original.count(old) for old in replacements)
                rel = fpath.relative_to(CEX_ROOT)
                if dry_run:
                    print(f"  WOULD change: {rel} ({count} refs)")
                else:
                    fpath.write_text(text, encoding="utf-8")
                    print(f"  Changed: {rel} ({count} refs)")
                changed += 1

    return changed


# -- CLI ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CEX Model Updater -- Self-healing model discovery",
    )
    parser.add_argument("--check", action="store_true", help="Check for stale models")
    parser.add_argument("--discover", action="store_true", help="Query provider APIs")
    parser.add_argument("--apply", action="store_true", help="Update nucleus_models.yaml")
    parser.add_argument("--propagate", action="store_true", help="Fix all stale refs in repo")
    parser.add_argument("--full", action="store_true", help="discover + check + apply + propagate")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes only")
    parser.add_argument("--json", action="store_true", help="Output as JSON (for flywheel)")
    args = parser.parse_args()

    if not any([args.check, args.discover, args.apply, args.propagate, args.full]):
        args.check = True

    # -- Discover --
    if args.discover or args.full:
        print("\n=== MODEL DISCOVERY ===")
        discovered = discover_all()
        if discovered:
            print("\n  Discovered models:")
            for m in sorted(discovered, key=lambda x: (x["provider"], x["id"])):
                print(f"    [{m['provider']:10s}] {m['id']}")

    # -- Check --
    if args.check or args.full:
        print("\n=== STALENESS CHECK ===")
        stale = check_staleness()

        if args.json:
            print(json.dumps({"stale": stale, "count": len(stale)}))
            return

        if stale:
            print(f"\n  Found {len(stale)} stale model reference(s):\n")
            for s in stale:
                print(f"    {s['nucleus']:20s} {s['current']:30s} -> {s['latest']}")
        else:
            print("  All models are current.")

        print("\n  Repo-wide model references:")
        refs = scan_repo_references()
        for model_id, count in sorted(refs.items(), key=lambda x: -x[1]):
            is_stale = any(s["current"] == model_id for s in stale)
            marker = " [STALE]" if is_stale else ""
            print(f"    {model_id:35s} {count:4d} refs{marker}")

    # -- Apply --
    if args.apply or args.full:
        print("\n=== APPLY UPDATES ===")
        stale = check_staleness()
        apply_updates(stale, dry_run=args.dry_run)

    # -- Propagate --
    if args.propagate or args.full:
        print("\n=== PROPAGATE ===")
        replacements = build_replacement_map()
        if replacements:
            print(f"  Replacement map ({len(replacements)} entries):")
            for old, new in replacements.items():
                print(f"    {old} -> {new}")
            print()
            changed = propagate(replacements, dry_run=args.dry_run)
            verb = "Would change" if args.dry_run else "Changed"
            print(f"\n  {verb}: {changed} files")
        else:
            print("  No propagation needed.")

    print()


if __name__ == "__main__":
    main()
