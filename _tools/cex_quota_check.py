#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Quota Check -- Pre-flight probe for CLI availability.

Runs a cheap API call against each CLI to detect:
  - Binary missing (not installed)
  - Auth missing (logged out, no API key)
  - Quota exhausted (rate-limited, plan cap hit)
  - Network down (timeout)

Origin: 2026-04-11 multi-CLI test. Gemini-2.5-pro quota was exhausted
mid-wave with no warning. 2/6 gemini nuclei silently dropped. This tool
exists so the dispatch path can skip unhealthy CLIs BEFORE spawning.

Usage:
  python _tools/cex_quota_check.py --cli claude
  python _tools/cex_quota_check.py --all --json
  python _tools/cex_quota_check.py --all --timeout 15

Exit codes:
  0 - all probed CLIs healthy
  1 - at least one unhealthy (see JSON for details)
  2 - invocation error
"""

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent
CACHE_PATH = CEX_ROOT / ".cex" / "runtime" / "quota_cache.json"

# Probe commands: minimal API call per CLI that exercises auth + quota
# but stays under the free tier. Output is discarded; we only care about
# exit code + stderr patterns.
def _resolve_probe_model(cli, fallback):
    """Resolve probe model via cex_model_resolver, fallback to hardcoded."""
    try:
        from _tools.cex_model_resolver import get_preflight_model
        if cli == "claude":
            return get_preflight_model("cloud").get("model", fallback)
    except Exception:
        pass
    return fallback


PROBES = {
    "claude": {
        "cmd": ["claude", "--print", "--model",
                _resolve_probe_model("claude", "claude-haiku-4-5-20251001"), "ping"],
        "timeout": 20,
        "quota_patterns": ["rate limit", "quota", "exceeded", "429"],
        "auth_patterns": ["unauthorized", "401", "authenticate", "not logged in"],
    },
    "gemini": {
        "cmd": ["gemini", "--yolo", "-m", "gemini-2.5-flash-lite", "-p", "ping"],
        "timeout": 20,
        "quota_patterns": ["quota", "resourceexhausted", "rate limit", "429"],
        "auth_patterns": ["unauthorized", "401", "authenticate"],
    },
    "codex": {
        "cmd": ["codex", "exec", "--dangerously-bypass-approvals-and-sandbox", "ping"],
        "timeout": 30,
        "quota_patterns": ["rate limit", "quota", "429", "exceeded"],
        "auth_patterns": ["unauthorized", "401", "authenticate"],
    },
    "ollama": {
        "cmd": ["ollama", "list"],
        "timeout": 5,
        "quota_patterns": [],  # local, no quota
        "auth_patterns": [],
    },
}


def classify_error(stderr: str, patterns_quota: list, patterns_auth: list) -> str:
    """Categorize a failed probe by its stderr output."""
    low = stderr.lower()
    for p in patterns_quota:
        if p.lower() in low:
            return "quota"
    for p in patterns_auth:
        if p.lower() in low:
            return "auth"
    if "timeout" in low or "timed out" in low:
        return "timeout"
    if "not found" in low or "command not found" in low:
        return "missing"
    return "error"


def probe(cli: str, custom_timeout: int = 0) -> dict:
    """Probe a single CLI. Returns structured result."""
    if cli not in PROBES:
        return {"cli": cli, "status": "unknown", "reason": "no probe defined"}

    spec = PROBES[cli]
    timeout = custom_timeout or spec["timeout"]

    # Binary presence check first (cheapest)
    binary = spec["cmd"][0]
    if not shutil.which(binary):
        return {
            "cli": cli,
            "status": "missing",
            "reason": f"binary not on PATH: {binary}",
            "elapsed_ms": 0,
        }

    start = time.time()
    try:
        r = subprocess.run(
            spec["cmd"],
            capture_output=True,
            text=True,
            timeout=timeout,
            errors="replace",
        )
        elapsed_ms = int((time.time() - start) * 1000)

        if r.returncode == 0:
            return {
                "cli": cli,
                "status": "healthy",
                "reason": "probe succeeded",
                "elapsed_ms": elapsed_ms,
            }

        reason = classify_error(
            (r.stderr or "") + (r.stdout or ""),
            spec["quota_patterns"],
            spec["auth_patterns"],
        )
        return {
            "cli": cli,
            "status": reason,
            "reason": (r.stderr or r.stdout or "")[:300].strip(),
            "elapsed_ms": elapsed_ms,
            "exit_code": r.returncode,
        }
    except subprocess.TimeoutExpired:
        return {
            "cli": cli,
            "status": "timeout",
            "reason": f"no response within {timeout}s",
            "elapsed_ms": timeout * 1000,
        }
    except Exception as e:
        return {
            "cli": cli,
            "status": "error",
            "reason": str(e)[:200],
            "elapsed_ms": int((time.time() - start) * 1000),
        }


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(data: dict):
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cli", default="", help="Probe only this CLI")
    ap.add_argument("--all", action="store_true", help="Probe all known CLIs")
    ap.add_argument("--json", action="store_true", help="Emit JSON report")
    ap.add_argument("--timeout", type=int, default=0, help="Override probe timeout (seconds)")
    ap.add_argument("--cache", action="store_true", help="Save results to quota_cache.json")
    ap.add_argument("--use-cache", type=int, default=0,
                    help="Reuse cached results if newer than N seconds")
    args = ap.parse_args()

    if not args.cli and not args.all:
        ap.error("--cli <name> OR --all required")

    targets = [args.cli] if args.cli else list(PROBES.keys())

    # Cache hit check
    if args.use_cache > 0:
        cache = load_cache()
        now = time.time()
        cache_ts = cache.get("_timestamp", 0)
        if now - cache_ts < args.use_cache:
            cached_results = {k: v for k, v in cache.items() if k != "_timestamp"}
            if all(t in cached_results for t in targets):
                results = [cached_results[t] for t in targets]
                if args.json:
                    print(json.dumps({"results": results, "cached": True}, indent=2))
                else:
                    for r in results:
                        print(f"  {r['cli']:8} {r['status']:10} (cached) {r.get('reason', '')[:60]}")
                return 0 if all(r.get("status") == "healthy" for r in results) else 1

    results = []
    for cli in targets:
        r = probe(cli, args.timeout)
        results.append(r)

    if args.cache:
        cache = {r["cli"]: r for r in results}
        cache["_timestamp"] = time.time()
        save_cache(cache)

    all_healthy = all(r["status"] == "healthy" for r in results)

    if args.json:
        print(json.dumps({"results": results, "all_healthy": all_healthy}, indent=2))
    else:
        for r in results:
            mark = "[OK]" if r["status"] == "healthy" else "[--]"
            print(f"  {mark} {r['cli']:8} {r['status']:10} {r.get('elapsed_ms', 0)}ms  {r.get('reason', '')[:50]}")

    return 0 if all_healthy else 1


if __name__ == "__main__":
    sys.exit(main())
