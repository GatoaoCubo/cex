#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_mission.py -- Mission Executor: high-level goal -> decomposed tasks -> artifacts.

The capstone of CEX autonomy. Takes a mission description, decomposes it into
concrete artifact-building tasks, and executes them via 8F Runner.

Modes:
  decompose  -- Break mission into artifact intents (read-only)
  execute    -- Decompose + build all artifacts
  status     -- Check progress of running mission

Usage:
  python _tools/cex_mission.py decompose "build analytics dashboard system"
  python _tools/cex_mission.py execute "build content marketing pipeline" --nucleus N02
  python _tools/cex_mission.py execute --from-file mission.md
  python _tools/cex_mission.py status
"""

import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

# Core artifact kinds that make up a complete system
SYSTEM_TEMPLATE = [
    {"kind": "agent", "desc": "core identity and capabilities"},
    {"kind": "system_prompt", "desc": "LLM behavior rules"},
    {"kind": "knowledge_card", "desc": "domain knowledge distilled"},
    {"kind": "agent_card", "desc": "deployment specification"},
    {"kind": "dispatch_rule", "desc": "routing rules for this domain"},
    {"kind": "workflow", "desc": "execution pipeline with steps"},
    {"kind": "quality_gate", "desc": "validation gates for output"},
]

EXTENDED_KINDS = [
    {"kind": "scoring_rubric", "desc": "quality scoring dimensions"},
    {"kind": "prompt_template", "desc": "reusable prompt patterns"},
    {"kind": "action_prompt", "desc": "quick execution prompts"},
    {"kind": "pattern", "desc": "architectural patterns"},
    {"kind": "dag", "desc": "dependency graph"},
]

# Mission complexity -> how many kinds to generate
COMPLEXITY = {
    "minimal": SYSTEM_TEMPLATE[:4],          # agent, system_prompt, KC, agent_card
    "standard": SYSTEM_TEMPLATE,             # 7 core kinds
    "full": SYSTEM_TEMPLATE + EXTENDED_KINDS, # 12 kinds
}


def decompose_mission(mission: str, nucleus: str = None,
                      complexity: str = "standard") -> list[dict]:
    """Decompose a mission into concrete artifact-building intents."""
    kinds = COMPLEXITY.get(complexity, COMPLEXITY["standard"])
    tasks = []

    for i, k in enumerate(kinds, 1):
        intent = f"create {k['kind']} for {mission} -- {k['desc']}"
        task = {
            "step": i,
            "kind": k["kind"],
            "intent": intent,
            "nucleus": nucleus,
            "priority": "high" if i <= 4 else "medium",
        }
        tasks.append(task)

    return tasks


def execute_task(task: dict, dry_run: bool = False) -> dict:
    """Execute a single decomposed task via 8F Runner."""
    cmd = [
        sys.executable, str(CEX_ROOT / "_tools" / "cex_8f_runner.py"),
        task["intent"], "--kind", task["kind"],
    ]
    if task.get("nucleus"):
        cmd.extend(["--nucleus", task["nucleus"]])
    if dry_run:
        cmd.append("--dry-run")
    else:
        cmd.append("--execute")

    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        elapsed = time.time() - t0
        full = r.stdout + r.stderr
        passed = "PASS" in full and "Verdict" in full

        # Extract output path
        path = None
        for line in full.split("\n"):
            if "Output:" in line:
                path = line.split("Output:")[-1].strip()
                break

        return {
            "step": task["step"],
            "kind": task["kind"],
            "passed": passed or dry_run,
            "path": path,
            "elapsed_s": round(elapsed, 1),
        }
    except subprocess.TimeoutExpired:
        return {"step": task["step"], "kind": task["kind"], "passed": False,
                "elapsed_s": 180, "error": "TIMEOUT"}
    except Exception as e:
        return {"step": task["step"], "kind": task["kind"], "passed": False,
                "elapsed_s": 0, "error": str(e)}


def run_mission(mission: str, nucleus: str = None, complexity: str = "standard",
                dry_run: bool = False) -> dict:
    """Full mission execution: decompose -> execute -> validate -> commit."""
    print(f"\n{'='*60}")
    print(f"  CEX MISSION EXECUTOR -- {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print(f"{'='*60}")
    print(f"  Mission: {mission}")
    print(f"  Nucleus: {nucleus or 'auto'}")
    print(f"  Complexity: {complexity}")

    # DECOMPOSE
    print("\n[>>] Decomposing mission...")
    tasks = decompose_mission(mission, nucleus, complexity)
    print(f"   Generated {len(tasks)} tasks:")
    for t in tasks:
        print(f"   [{t['step']}] {t['kind']:20s} -- {t['intent'][:50]}...")

    # EXECUTE
    print("\n[>>] Executing tasks...")
    results = []
    passed = 0
    failed = 0

    for task in tasks:
        print(f"\n   [{task['step']}/{len(tasks)}] Building {task['kind']}...")
        result = execute_task(task, dry_run)
        results.append(result)

        if result["passed"]:
            passed += 1
            path = result.get("path", "N/A")
            print(f"   [OK] PASS ({result['elapsed_s']}s) -> {path}")
        else:
            failed += 1
            err = result.get("error", "gates failed")
            print(f"   [FAIL] FAIL ({result['elapsed_s']}s) -- {err}")

    # VALIDATE
    if not dry_run and passed > 0:
        print("\n[?] Post-mission validation...")
        r = subprocess.run(
            [sys.executable, "_tools/cex_hooks.py", "validate-all"],
            capture_output=True, text=True, timeout=30
        )
        full = r.stdout + r.stderr
        m = re.search(r"Errors:\s+(\d+)", full)
        hook_errors = int(m.group(1)) if m else -1
        print(f"   Hooks: {hook_errors} errors")

        # Git commit
        subprocess.run(["git", "add", "-A"], capture_output=True)
        subprocess.run(
            ["git", "commit", "-m",
             f"[MISSION] {mission[:50]} -- {passed}/{len(tasks)} artifacts built"],
            capture_output=True
        )
        print("   [>>] Mission committed to git")

    # SUMMARY
    total_time = sum(r["elapsed_s"] for r in results)
    print(f"\n{'='*60}")
    print("  MISSION COMPLETE")
    print(f"  Results: {passed} PASS | {failed} FAIL | {len(tasks)} total")
    print(f"  Time: {total_time:.0f}s ({total_time/60:.1f}min)")
    print(f"{'='*60}")

    # Save mission report
    report = {
        "mission": mission,
        "nucleus": nucleus,
        "complexity": complexity,
        "timestamp": datetime.datetime.now().isoformat(),
        "passed": passed,
        "failed": failed,
        "total": len(tasks),
        "elapsed_s": round(total_time, 1),
        "results": results,
    }

    reports_dir = CEX_ROOT / ".cex" / "mission_reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"mission_{ts}.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  Report saved to {report_path.relative_to(CEX_ROOT)}")

    return report


def show_status():
    """Show status of recent missions."""
    reports_dir = CEX_ROOT / ".cex" / "mission_reports"
    if not reports_dir.exists():
        print("No missions executed yet.")
        return

    reports = sorted(reports_dir.glob("mission_*.json"), reverse=True)
    if not reports:
        print("No mission reports found.")
        return

    print(f"\n{'='*60}")
    print(f"  RECENT MISSIONS ({len(reports)} total)")
    print(f"{'='*60}\n")

    for rp in reports[:5]:
        data = json.loads(rp.read_text(encoding="utf-8"))
        status = "[OK]" if data["failed"] == 0 else "[WARN]"
        print(f"  {status} {data['timestamp'][:16]}")
        print(f"     Mission: {data['mission'][:50]}")
        print(f"     Results: {data['passed']}/{data['total']} PASS | {data['elapsed_s']}s")
        print()


def main():
    import argparse
    parser = argparse.ArgumentParser(description="CEX Mission Executor")
    parser.add_argument("mode", choices=["decompose", "execute", "status"],
                        help="Operation mode")
    parser.add_argument("mission", nargs="?", help="Mission description")
    parser.add_argument("--nucleus", help="Target nucleus (N01-N07)")
    parser.add_argument("--complexity", choices=["minimal", "standard", "full"],
                        default="standard", help="How many artifact kinds to generate")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--from-file", help="Read mission from file")
    args = parser.parse_args()

    if args.mode == "status":
        show_status()
        return

    mission = args.mission
    if args.from_file:
        mission = Path(args.from_file).read_text(encoding="utf-8").strip()
    if not mission:
        print("ERROR: mission description required", file=sys.stderr)
        sys.exit(1)

    if args.mode == "decompose":
        tasks = decompose_mission(mission, args.nucleus, args.complexity)
        print(json.dumps(tasks, indent=2, ensure_ascii=False))

    elif args.mode == "execute":
        run_mission(mission, args.nucleus, args.complexity, args.dry_run)


if __name__ == "__main__":
    main()
