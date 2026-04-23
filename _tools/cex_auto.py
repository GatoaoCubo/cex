#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_auto.py -- Autonomous CEX Flywheel

The self-driving loop: diagnose -> plan -> execute -> validate -> learn -> repeat.

Modes:
  scan     -- Diagnose system, find gaps, suggest actions (read-only)
  plan     -- Generate an execution plan from gaps
  execute  -- Run the plan (build artifacts, fix issues)
  cycle    -- Full loop: scan -> plan -> execute -> validate (autonomous)

Usage:
  python _tools/cex_auto.py scan              # what needs work?
  python _tools/cex_auto.py plan              # generate action plan
  python _tools/cex_auto.py execute plan.json # run a plan
  python _tools/cex_auto.py cycle --max 5     # autonomous: up to 5 builds
  python _tools/cex_auto.py cycle --dry-run   # preview cycle without building
"""

import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))


# ============================================================
# SCAN -- Diagnose gaps
# ============================================================

def scan_system() -> dict:
    """Scan entire CEX system and identify gaps/actions needed."""
    gaps = []
    stats = {}

    # 1. Check quality:null artifacts
    r = subprocess.run(
        ["grep", "-r", "-l", "^quality: null", "--include=*.md"] +
        [d for d in os.listdir(".") if d.startswith("N0") and os.path.isdir(d)],
        capture_output=True, text=True
    )
    null_files = [f for f in r.stdout.strip().split("\n") if f.strip()]
    stats["quality_null"] = len(null_files)
    if null_files:
        for f in null_files[:10]:
            gaps.append({"type": "quality_null", "path": f, "priority": "medium",
                         "action": f"Evolve+score: python _tools/cex_evolve.py single {f} --target 8.5"})

    # 2. Check doctor
    r = subprocess.run([sys.executable, "_tools/cex_doctor.py"], capture_output=True, text=True, timeout=30,
                       encoding="utf-8", errors="replace")
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+) PASS \| (\d+) WARN \| (\d+) FAIL", full)
    if m:
        stats["doctor_pass"] = int(m.group(1))
        stats["doctor_warn"] = int(m.group(2))
        stats["doctor_fail"] = int(m.group(3))
        if int(m.group(2)) > 0:
            gaps.append({"type": "doctor_warn", "priority": "high",
                         "action": "Fix builder WARNs: check oversized specs"})
        if int(m.group(3)) > 0:
            gaps.append({"type": "doctor_fail", "priority": "critical",
                         "action": "Fix builder FAILs immediately"})

    # 3. Check hooks validation
    r = subprocess.run([sys.executable, "_tools/cex_hooks.py", "validate-all"],
                       capture_output=True, text=True, timeout=30,
                       encoding="utf-8", errors="replace")
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"Errors:\s+(\d+)", full)
    hook_errors = int(m.group(1)) if m else 0
    stats["hook_errors"] = hook_errors
    if hook_errors > 0:
        gaps.append({"type": "hook_errors", "priority": "high",
                     "action": f"Fix {hook_errors} hook validation errors"})

    # 4. Check nucleus coverage (each nucleus should have min artifacts)
    expected = {"N01": 11, "N02": 10, "N03": 34, "N04": 12, "N05": 9, "N06": 9, "N07": 13}
    for nprefix, min_count in expected.items():
        ndir = [d for d in os.listdir(".") if d.startswith(nprefix) and os.path.isdir(d)]
        if ndir:
            mds = [f for f in Path(ndir[0]).rglob("*.md")
                   if "compiled" not in str(f) and f.name != "README.md"]
            stats[f"{nprefix}_artifacts"] = len(mds)
            if len(mds) < min_count:
                gaps.append({"type": "nucleus_gap", "nucleus": nprefix,
                             "have": len(mds), "need": min_count, "priority": "medium",
                             "action": f"Build {min_count - len(mds)} more artifacts for {nprefix}"})

    # 5. Check for low-quality artifacts (< 8.5)
    r = subprocess.run(
        ["grep", "-r", "^quality:", "--include=*.md"] +
        [d for d in os.listdir(".") if d.startswith("N0") and os.path.isdir(d)],
        capture_output=True, text=True
    )
    low_quality = []
    for line in r.stdout.strip().split("\n"):
        if not line.strip():
            continue
        m2 = re.search(r"quality:\s*([\d.]+)", line)
        if m2:
            score = float(m2.group(1))
            if score < 8.5:
                filepath = line.split(":")[0]
                low_quality.append(filepath)
    stats["low_quality_count"] = len(low_quality)
    for f in low_quality[:5]:
        gaps.append({"type": "low_quality", "path": f, "priority": "low",
                     "action": f"Rebuild low-quality artifact: {f}"})

    # 6. Check compile
    r = subprocess.run([sys.executable, "_tools/cex_compile.py", "--all"],
                       capture_output=True, text=True, timeout=60,
                       encoding="utf-8", errors="replace")
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+)/(\d+) compiled", full)
    if m:
        stats["compile_ok"] = int(m.group(1))
        stats["compile_total"] = int(m.group(2))

    # 7. Check sub-agents match kinds
    agents_dir = CEX_ROOT / ".claude" / "agents"
    if agents_dir.exists():
        agents = list(agents_dir.glob("*.md"))
        stats["subagents"] = len(agents)
    kinds_meta = CEX_ROOT / ".cex" / "kinds_meta.json"
    if kinds_meta.exists():
        kinds = json.loads(kinds_meta.read_text(encoding="utf-8"))
        stats["kinds"] = len(kinds)

    # 8. Nucleus archetype completeness
    # Each nucleus should ideally have: agent, system_prompt, knowledge_card,
    # agent_card, dispatch_rule, workflow, quality_gate, scoring_rubric
    core_kinds = ["agent", "system_prompt", "knowledge_card", "agent_card",
                  "dispatch_rule", "workflow", "quality_gate"]
    for nprefix in ["N01", "N02", "N04", "N05", "N06", "N07"]:
        ndir = [d for d in os.listdir(".") if d.startswith(nprefix) and os.path.isdir(d)]
        if not ndir:
            continue
        # Get existing kinds
        r_kinds = subprocess.run(
            ["grep", "-r", "^kind:", "--include=*.md", ndir[0]],
            capture_output=True, text=True
        )
        existing_kinds = set()
        for line in r_kinds.stdout.strip().split("\n"):
            if line.strip() and "compiled" not in line:
                m_kind = re.search(r"kind:\s*(\S+)", line)
                if m_kind:
                    existing_kinds.add(m_kind.group(1))
        missing = [k for k in core_kinds if k not in existing_kinds]
        if missing:
            stats[f"{nprefix}_missing_kinds"] = missing
            for k in missing:
                gaps.append({
                    "type": "missing_kind", "nucleus": nprefix, "kind": k,
                    "priority": "low",
                    "action": f"Build {k} for {nprefix}: python _tools/cex_8f_runner.py 'create {k} for {nprefix}' --kind {k} --nucleus {nprefix} --execute"
                })

    # 9. Git cleanliness
    r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    dirty = len([l for l in r.stdout.strip().split("\n") if l.strip()])
    stats["git_dirty"] = dirty

    # 10. Model staleness check
    try:
        from cex_model_updater import check_staleness
        stale = check_staleness()
        stats["stale_models"] = len(stale)
        if stale:
            models_list = ", ".join(f"{s['nucleus']}={s['current']}" for s in stale)
            gaps.append({
                "type": "stale_models", "priority": "high",
                "action": f"Update {len(stale)} stale model(s): {models_list}. "
                          "Run: python _tools/cex_model_updater.py --full"
            })
    except Exception:
        stats["stale_models"] = -1  # updater not available

    return {"stats": stats, "gaps": gaps, "timestamp": datetime.datetime.now().isoformat()}


# ============================================================
# PLAN -- Generate actions from gaps
# ============================================================

def generate_plan(scan_result: dict) -> list[dict]:
    """Convert scan gaps into ordered execution plan."""
    gaps = scan_result["gaps"]

    # Sort by priority
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    gaps.sort(key=lambda g: priority_order.get(g.get("priority", "low"), 4))

    plan = []
    for i, gap in enumerate(gaps, 1):
        plan.append({
            "step": i,
            "type": gap["type"],
            "priority": gap.get("priority", "medium"),
            "action": gap.get("action", ""),
            "path": gap.get("path"),
        })

    return plan


# ============================================================
# EXECUTE -- Run plan steps
# ============================================================

def execute_step(step: dict, dry_run: bool = False) -> dict:
    """Execute a single plan step. Returns result."""
    result = {"step": step["step"], "type": step["type"], "success": False}

    if dry_run:
        result["success"] = True
        result["note"] = f"DRY-RUN: {step['action']}"
        return result

    if step["type"] == "quality_null" and step.get("path"):
        # AutoResearch: evolve (analyze + improve + score) in one pass
        r = subprocess.run(
            [sys.executable, "_tools/cex_evolve.py", "single", step["path"],
             "--target", "8.5", "--max-rounds", "2"],
            capture_output=True, text=True, timeout=60
        )
        result["success"] = r.returncode == 0
        result["output"] = ((r.stdout or "") + (r.stderr or "")).strip()[-200:]

    elif step["type"] == "low_quality" and step.get("path"):
        # AutoResearch: evolve the artifact until it improves
        r = subprocess.run(
            [sys.executable, "_tools/cex_evolve.py", "single", step["path"],
             "--target", "8.5", "--max-rounds", "3"],
            capture_output=True, text=True, timeout=60
        )
        result["output"] = ((r.stdout or "") + (r.stderr or "")).strip()[-200:]
        result["success"] = "KEEP" in r.stdout or "Target" in r.stdout
        result["note"] = f"Evolved: {step['path']}" if result["success"] else f"Could not improve: {step['path']}"

    elif step["type"] == "missing_kind":
        # Auto-build missing artifact for nucleus
        nucleus = step.get("nucleus", "")
        kind = step.get("kind", "")
        if nucleus and kind:
            cmd = [
                sys.executable, str(CEX_ROOT / "_tools" / "cex_8f_runner.py"),
                f"create {kind} for {nucleus} nucleus",
                "--kind", kind, "--nucleus", nucleus, "--execute"
            ]
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                full = (r.stdout or "") + (r.stderr or "")
                result["success"] = "PASS" in full
                result["output"] = full[-200:]
                result["note"] = f"Built {kind} for {nucleus}" if result["success"] else f"FAIL: {kind} for {nucleus}"
            except subprocess.TimeoutExpired:
                result["note"] = f"TIMEOUT building {kind} for {nucleus}"
            except Exception as e:
                result["note"] = str(e)
        else:
            result["note"] = "missing nucleus or kind in step"

    elif step["type"] in ("doctor_warn", "doctor_fail", "hook_errors"):
        result["success"] = False
        result["note"] = "Requires manual intervention or N03 dispatch"

    else:
        result["note"] = f"Unhandled action type: {step['type']}"

    return result


# ============================================================
# CYCLE -- Full autonomous loop
# ============================================================

def run_cycle(max_actions: int = 10, dry_run: bool = False) -> dict:
    """Full autonomous cycle: scan -> plan -> execute -> validate."""
    print(f"\n{'='*60}")
    print(f"  CEX AUTO CYCLE -- {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print(f"{'='*60}\n")

    # SCAN
    print("[>>] Scanning system...")
    scan = scan_system()
    stats = scan["stats"]
    print(f"   Stats: {json.dumps(stats, indent=2)}")
    print(f"   Gaps found: {len(scan['gaps'])}")

    if not scan["gaps"]:
        print("\n[OK] System is healthy. No gaps found.")
        return {"status": "healthy", "actions": 0, "scan": scan}

    # PLAN
    print("\n[>>] Generating plan...")
    plan = generate_plan(scan)
    plan = plan[:max_actions]
    for step in plan:
        symbol = {"critical": "[!!]", "high": "[!!]", "medium": "[..]", "low": "[OK]"}.get(step["priority"], "[--]")
        print(f"   {symbol} [{step['step']}] {step['action'][:80]}")

    # EXECUTE
    print(f"\n[>>] Executing {len(plan)} actions...")
    results = []
    passed = 0
    for step in plan:
        r = execute_step(step, dry_run)
        results.append(r)
        if r["success"]:
            passed += 1
            print(f"   [OK] [{step['step']}] {r.get('note', 'done')[:60]}")
        else:
            print(f"   [FAIL] [{step['step']}] {r.get('note', r.get('output', 'failed'))[:60]}")

    # VALIDATE
    print("\n[?] Post-cycle validation...")
    post_scan = scan_system()
    post_gaps = len(post_scan["gaps"])
    pre_gaps = len(scan["gaps"])
    delta = pre_gaps - post_gaps
    print(f"   Gaps: {pre_gaps} -> {post_gaps} (delta{delta:+d})")

    # COMMIT
    if not dry_run and passed > 0:
        subprocess.run(["git", "add", "-A"], capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"[AUTO] cycle: {passed}/{len(plan)} actions, {post_gaps} gaps remaining"],
            capture_output=True
        )
        print("   [>>] Changes committed")

    # Summary
    print(f"\n{'='*60}")
    print(f"  CYCLE COMPLETE: {passed}/{len(plan)} actions succeeded")
    print(f"  Gaps: {pre_gaps} -> {post_gaps}")
    print(f"{'='*60}")

    cycle_result = {
        "status": "complete",
        "actions_total": len(plan),
        "actions_passed": passed,
        "gaps_before": pre_gaps,
        "gaps_after": post_gaps,
        "timestamp": datetime.datetime.now().isoformat(),
    }

    # Save cycle result
    cycle_path = CEX_ROOT / ".cex" / "auto_cycle_results.json"
    cycle_path.write_text(json.dumps(cycle_result, indent=2), encoding="utf-8")

    return cycle_result


# ============================================================
# MAIN
# ============================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description="CEX Autonomous Flywheel")
    parser.add_argument("mode", choices=["scan", "plan", "execute", "cycle"],
                        help="Operation mode")
    parser.add_argument("--max", type=int, default=10, help="Max actions per cycle")
    parser.add_argument("--dry-run", action="store_true", help="Preview without executing")
    parser.add_argument("plan_file", nargs="?", help="Plan JSON file (for execute mode)")
    args = parser.parse_args()

    if args.mode == "scan":
        scan = scan_system()
        print(json.dumps(scan, indent=2, ensure_ascii=False))

    elif args.mode == "plan":
        scan = scan_system()
        plan = generate_plan(scan)
        print(json.dumps(plan, indent=2, ensure_ascii=False))

    elif args.mode == "execute":
        if not args.plan_file:
            print("ERROR: execute mode requires plan file", file=sys.stderr)
            sys.exit(1)
        plan = json.loads(Path(args.plan_file).read_text(encoding="utf-8"))
        for step in plan:
            r = execute_step(step, args.dry_run)
            status = "[OK]" if r["success"] else "[FAIL]"
            print(f"{status} [{step['step']}] {r.get('note', '')[:80]}")

    elif args.mode == "cycle":
        run_cycle(max_actions=args.max, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
