#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX CLI Resolver -- YAML-driven CLI selection with fallback chain.

Reads .cex/P09_config/nucleus_models.yaml and resolves which CLI/model/flags
to use for a given nucleus. Supports:
  - Primary CLI (first working from fallback_chain)
  - --prefer override (operator picks a CLI explicitly)
  - --pre-check (runs quota/binary probe before returning a winner)
  - --json (structured output for PowerShell consumption)

This is the "L2 config" layer of the 3-level routing model:
  L1 explicit  -- spawn_grid.ps1 -cli gemini (operator override)
  L2 YAML      -- this tool + nucleus_models.yaml fallback_chain (default)
  L3 router    -- cex_router.py with health-checked providers (smart mode)

Usage:
  python _tools/cex_cli_resolver.py --nucleus n03
  python _tools/cex_cli_resolver.py --nucleus n03 --prefer gemini
  python _tools/cex_cli_resolver.py --nucleus n03 --pre-check --json

Exit codes:
  0 - resolved successfully
  1 - no valid CLI found (all fallbacks exhausted)
  2 - nucleus not in config
  3 - config file missing
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[FAIL] PyYAML not installed. pip install pyyaml", file=sys.stderr)
    sys.exit(3)

CEX_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = CEX_ROOT / ".cex" / "config" / "nucleus_models.yaml"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(f"[FAIL] Missing config: {CONFIG_PATH}", file=sys.stderr)
        sys.exit(3)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def probe_cli(cli_name: str) -> tuple[bool, str]:
    """Check whether a CLI binary is installed and reachable.

    Returns (ok, reason).
    Does NOT call the API (expensive); just checks binary presence.
    For real API quota checks, see cex_quota_check.py.
    """
    if cli_name == "ollama":
        # ollama is a daemon; check the CLI
        binary = "ollama"
    elif cli_name == "claude":
        binary = "claude"
    elif cli_name == "gemini":
        binary = "gemini"
    elif cli_name == "codex":
        binary = "codex"
    else:
        return False, f"unknown CLI: {cli_name}"

    path = shutil.which(binary)
    if not path:
        return False, f"binary not on PATH: {binary}"
    return True, path


def build_entry(cli_name: str, model: str, flags: str) -> dict:
    """Build a resolved entry."""
    return {
        "cli": cli_name,
        "model": model,
        "flags": flags or "",
    }


def resolve_nucleus(config: dict, nucleus: str, prefer: str = "",
                    pre_check: bool = False) -> dict:
    """Resolve the CLI to use for a nucleus.

    Returns dict with {cli, model, flags, chain_step, available}.
    chain_step: "primary" | "fallback_N" | "none"
    available: list of probe results for all entries (if pre_check)
    """
    nuc_cfg = config.get(nucleus.lower())
    if not nuc_cfg:
        return {
            "error": f"nucleus not in config: {nucleus}",
            "cli": "",
            "model": "",
            "flags": "",
            "chain_step": "none",
        }

    # Build the chain: [primary] + fallback_chain + [fallback] (legacy)
    chain = []
    try:
        from cex_model_resolver import resolve_model as _resolve_mdl
        _default_model = _resolve_mdl(nucleus)["model"]
    except Exception:
        _default_model = "claude-opus-4-6"
    primary = build_entry(
        nuc_cfg.get("cli", "claude"),
        nuc_cfg.get("model", _default_model),
        nuc_cfg.get("flags", ""),
    )
    primary["chain_step"] = "primary"
    chain.append(primary)

    fc = nuc_cfg.get("fallback_chain") or []
    for i, entry in enumerate(fc):
        if not isinstance(entry, dict):
            continue
        e = build_entry(
            entry.get("cli", ""),
            entry.get("model", ""),
            entry.get("flags", ""),
        )
        e["chain_step"] = f"fallback_{i+1}"
        chain.append(e)

    # Legacy single fallback (if fallback_chain missing)
    if not fc:
        legacy = nuc_cfg.get("fallback")
        if isinstance(legacy, dict):
            e = build_entry(
                legacy.get("cli", ""),
                legacy.get("model", ""),
                legacy.get("flags", ""),
            )
            e["chain_step"] = "fallback_legacy"
            chain.append(e)

    # Apply --prefer override: move matching entries to front
    if prefer:
        prefer = prefer.lower()
        preferred = [e for e in chain if e["cli"] == prefer]
        rest = [e for e in chain if e["cli"] != prefer]
        chain = preferred + rest

    # Walk chain, optionally pre-checking each
    available = []
    chosen = None
    for entry in chain:
        if pre_check:
            ok, reason = probe_cli(entry["cli"])
            entry_result = dict(entry)
            entry_result["probe_ok"] = ok
            entry_result["probe_reason"] = reason
            available.append(entry_result)
            if ok and chosen is None:
                chosen = entry
        else:
            if chosen is None:
                chosen = entry
            available.append(entry)

    if chosen is None:
        return {
            "error": "no working CLI in chain",
            "cli": "",
            "model": "",
            "flags": "",
            "chain_step": "none",
            "available": available,
        }

    result = dict(chosen)
    result["nucleus"] = nucleus
    if pre_check:
        result["available"] = available
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--nucleus", required=True, help="Nucleus id (n01..n07)")
    ap.add_argument("--prefer", default="", help="Operator override CLI (claude|gemini|codex|ollama)")
    ap.add_argument("--pre-check", action="store_true", help="Probe each chain entry before resolving")
    ap.add_argument("--json", action="store_true", help="Emit JSON (for PowerShell consumption)")
    args = ap.parse_args()

    cfg = load_config()
    result = resolve_nucleus(cfg, args.nucleus, args.prefer, args.pre_check)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result.get("error"):
            print(f"[FAIL] {result['error']}")
            sys.exit(1)
        print(f"[OK] {args.nucleus}: {result['cli']} ({result['chain_step']})")
        print(f"  model: {result['model']}")
        print(f"  flags: {result['flags']}")
        if args.pre_check and "available" in result:
            print("  chain:")
            for e in result["available"]:
                mark = "[OK]" if e.get("probe_ok") else "[--]"
                print(f"    {mark} {e['chain_step']:15} {e['cli']:8} {e['model']}")

    sys.exit(0 if not result.get("error") else 1)


if __name__ == "__main__":
    main()
