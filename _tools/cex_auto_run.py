#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Autonomous Runner -- system-level orchestration + health + missions

For single-artifact production, prefer cex_run.py or cex_8f_runner.py.
This module handles system introspection and multi-nucleus coordination.

Usage:
  python _tools/cex_auto_run.py "build landing page for pet shop"
  python _tools/cex_auto_run.py --mission MISSION_NAME
  python _tools/cex_auto_run.py --status
  python _tools/cex_auto_run.py --health

Flow (single artifact):
  1. Discover providers (which are alive?)
  2. Select best model per nucleus (auto-fallback)
  3. Load sin lens for target nucleus
  4. Compose prompt: builders + ISOs + sin + memory + context
  5. Execute via crew_runner (8F pipeline)
  6. Validate output (doctor + compile + hooks)
  7. Score (peer review)
  8. Evolve if quality < threshold
  9. Signal complete

For multi-nucleus missions:
  1-2. Same discovery + model selection
  3. Write handoffs with sin-injected prompts
  4. Dispatch grid (session-aware)
  5. Monitor signals (blocking poll)
  6. Stop completed nuclei (session-aware)
  7. Consolidate (verify + score + archive)
  8. Report mission summary
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_tools"))

NUCLEUS_ORDER = ["n01", "n02", "n03", "n04", "n05", "n06", "n07"]


# ---------------------------------------------------------------------------
# Step 1-2: Provider Discovery
# ---------------------------------------------------------------------------

def discover_system() -> dict:
    """Discover all available providers and their status."""
    try:
        from cex_provider_discovery import discover_providers
        return discover_providers(use_cache=False)
    except Exception as e:
        return {"error": str(e)}


def get_best_model(nucleus: str, providers: dict = None) -> str:
    """Get the best available model for a nucleus."""
    try:
        from cex_model_resolver import resolve_model_for_tool
        _fallback = resolve_model_for_tool("cex_auto_run", "standard")["model"]
    except Exception:
        _fallback = "claude-sonnet-4-6"
    try:
        from cex_provider_discovery import get_best_provider
        return get_best_provider(nucleus, providers) or _fallback
    except Exception:
        return _fallback


# ---------------------------------------------------------------------------
# Step 3: Sin Lens
# ---------------------------------------------------------------------------

def get_sin_context(nucleus: str) -> dict:
    """Load sin identity for a nucleus."""
    try:
        from cex_theme import get_lens, get_prompt_injection, get_sin
        sin = get_sin(nucleus)
        return {
            "sin": sin.get("sin", "?"),
            "virtue": sin.get("virtue", "?"),
            "icon": sin.get("icon", "?"),
            "tagline": sin.get("tagline", ""),
            "injection": get_prompt_injection(nucleus),
            "lens": get_lens(nucleus),
        }
    except Exception:
        return {"sin": "?", "virtue": "?", "icon": "?", "tagline": "", "injection": "", "lens": ""}


# ---------------------------------------------------------------------------
# Health Check
# ---------------------------------------------------------------------------

def health_check() -> dict:
    """Full system health check: providers + sins + tools + doctor."""
    result = {
        "providers": {},
        "sins": {},
        "tools": {},
        "doctor": None,
    }

    # Providers
    print("\n  === Provider Discovery ===")
    providers = discover_system()
    alive = 0
    for name, info in providers.items():
        if isinstance(info, dict):
            status = info.get("status", "?")
            if status == "OK":
                alive += 1
            latency = info.get("latency_ms", -1)
            lat_str = f"{latency:.0f}ms" if latency >= 0 else "N/A"
            print(f"    {name:<12} {status:<8} {lat_str}")
            result["providers"][name] = status
    total = len([v for v in providers.values() if isinstance(v, dict)])
    print(f"    {alive}/{total} alive")

    # Sins
    print("\n  === Sin System ===")
    for nuc in NUCLEUS_ORDER:
        ctx = get_sin_context(nuc)
        print(f"    {nuc.upper()} {ctx['icon']} {ctx['virtue']:<25} {ctx['tagline']}")
        result["sins"][nuc] = ctx["virtue"]

    # Tools
    print("\n  === Tool Availability ===")
    tool_checks = [
        ("cex_theme", "Theme System"),
        ("cex_provider_discovery", "Provider Discovery"),
        ("cex_router", "Smart Router"),
        ("cex_crew_runner", "Crew Runner"),
        ("cex_8f_motor", "8F Motor"),
        ("cex_run", "Run Pipeline"),
        ("cex_compile", "Compiler"),
        ("cex_hooks", "Hooks"),
        ("cex_score", "Scorer"),
    ]
    for module_name, label in tool_checks:
        try:
            __import__(module_name)
            print(f"    {label:<25} OK")
            result["tools"][module_name] = "OK"
        except Exception as e:
            print(f"    {label:<25} FAIL ({e})")
            result["tools"][module_name] = f"FAIL: {e}"

    # Doctor (quick check)
    print("\n  === Doctor (quick) ===")
    try:
        r = subprocess.run(
            [sys.executable, str(ROOT / "_tools" / "cex_doctor.py")],
            capture_output=True, text=True, timeout=30, cwd=str(ROOT),
            encoding="utf-8", errors="replace",
        )
        # Count PASS/FAIL
        lines = r.stdout.split("\n")
        passes = sum(1 for l in lines if "PASS" in l)
        fails = sum(1 for l in lines if "FAIL" in l)
        print(f"    {passes} PASS, {fails} FAIL")
        result["doctor"] = {"pass": passes, "fail": fails}
    except Exception as e:
        print(f"    Doctor error: {e}")
        result["doctor"] = {"error": str(e)}

    # Summary
    print("\n  === Summary ===")
    all_ok = alive > 0 and all(v == "OK" for v in result["tools"].values())
    status = "HEALTHY" if all_ok else "DEGRADED"
    print(f"    System: {status}")
    print(f"    Providers: {alive}/{total}")
    print(f"    Tools: {sum(1 for v in result['tools'].values() if v == 'OK')}/{len(tool_checks)}")
    if result["doctor"] and isinstance(result["doctor"], dict):
        d = result["doctor"]
        if "pass" in d:
            print(f"    Doctor: {d['pass']} PASS / {d['fail']} FAIL")
    print()

    result["status"] = status
    return result


# ---------------------------------------------------------------------------
# Status
# ---------------------------------------------------------------------------

def show_status():
    """Show current system status: providers + nuclei + missions."""
    print("\n  === CEX Autonomous Runner Status ===\n")

    # Providers (cached)
    try:
        from cex_provider_discovery import discover_providers
        providers = discover_providers(use_cache=True)
        alive = sum(1 for p in providers.values() if isinstance(p, dict) and p.get("status") == "OK")
        total = len([v for v in providers.values() if isinstance(v, dict)])
        print(f"  Providers: {alive}/{total} alive")
    except Exception:
        print("  Providers: discovery unavailable")

    # Nucleus processes
    pid_file = ROOT / ".cex" / "runtime" / "pids" / "spawn_pids.txt"
    if pid_file.exists():
        lines = [l.strip() for l in pid_file.read_text(encoding="utf-8").splitlines() if l.strip()]
        print(f"  Active nuclei: {len(lines)} process(es)")
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                print(f"    PID {parts[0]} -- {parts[1]} ({parts[2]})")
    else:
        print("  Active nuclei: none")

    # Signals
    signal_dir = ROOT / ".cex" / "runtime" / "signals"
    if signal_dir.exists():
        signals = list(signal_dir.glob("*.json"))
        if signals:
            print(f"  Signals: {len(signals)}")
            for s in sorted(signals)[-5:]:
                print(f"    {s.name}")

    # Handoffs
    handoff_dir = ROOT / ".cex" / "runtime" / "handoffs"
    if handoff_dir.exists():
        handoffs = list(handoff_dir.glob("*.md"))
        if handoffs:
            print(f"  Pending handoffs: {len(handoffs)}")

    print()


# ---------------------------------------------------------------------------
# Single Artifact Build
# ---------------------------------------------------------------------------

def build_single(intent: str, verbose: bool = True) -> dict:
    """Full autonomous single artifact build via cex_run.py."""
    if verbose:
        print(f"\n  === Autonomous: Building '{intent}' ===\n")

    # Step 1-2: Discover
    providers = discover_system()
    nucleus = os.environ.get("CEX_NUCLEUS", "n03").lower()
    model = get_best_model(nucleus, providers)
    if verbose:
        alive = sum(1 for p in providers.values() if isinstance(p, dict) and p.get("status") == "OK")
        print(f"  [1] Providers: {alive} alive. Model: {model}")

    # Step 3: Sin lens
    sin_ctx = get_sin_context(nucleus)
    if verbose:
        print(f"  [2] Sin: {sin_ctx['icon']} {sin_ctx['virtue']}")

    # Step 4-9: Delegate to cex_run.py
    if verbose:
        print("  [3] Delegating to cex_run pipeline...")

    try:
        from cex_run import run as cex_run
        result = cex_run(intent, quality=9.0, execute=False, verbose=verbose)
        return result
    except Exception as e:
        return {"error": str(e), "intent": intent}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CEX Autonomous Runner -- fully autonomous pipeline orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("intent", nargs="?", help="Natural language intent for single build")
    parser.add_argument("--mission", metavar="NAME", help="Execute a named mission plan")
    parser.add_argument("--status", action="store_true", help="Show current system status")
    parser.add_argument("--health", action="store_true", help="Full system health check")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    if args.health:
        result = health_check()
        if args.json:
            print(json.dumps(result, indent=2, default=str))
        return

    if args.status:
        show_status()
        return

    if args.mission:
        plan_path = ROOT / ".cex" / "runtime" / "plans" / f"plan_{args.mission}.md"
        if not plan_path.exists():
            # Try with MISSION_ prefix
            plan_path = ROOT / ".cex" / "runtime" / "plans" / f"MISSION_{args.mission}.md"
        if plan_path.exists():
            print(f"\n  Mission plan found: {plan_path.name}")
            print("  [TODO] Multi-nucleus mission execution via cex_mission_runner.py")
            print(f"  For now, use: python _tools/cex_mission_runner.py --plan {plan_path} --mission {args.mission}")
        else:
            print(f"  [ERROR] Mission plan not found: {args.mission}")
            print("  Available plans:")
            plans_dir = ROOT / ".cex" / "runtime" / "plans"
            if plans_dir.exists():
                for p in plans_dir.glob("*.md"):
                    print(f"    {p.name}")
        return

    if args.intent:
        result = build_single(args.intent)
        if args.json:
            output = {k: v for k, v in result.items() if k != "prompt"}
            print(json.dumps(output, indent=2, default=str))
        return

    parser.print_help()


if __name__ == "__main__":
    main()
