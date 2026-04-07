#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_e2e_test.py -- E2E Stress Test Runner for CEX 8F Pipeline.

Feeds deliberately vague inputs to cex_8f_runner.py and validates:
  - F1-F8 trace fires correctly
  - Output files exist at expected paths
  - Quality scoring meets floor (>= 8.0)
  - Regression markers are not triggered

Modes:
  --quick   Dry-run only: verifies trace + prompt structure (no LLM calls)
  --full    Execute mode: actual LLM calls + quality scoring + gold comparison

Usage:
  python _tools/cex_e2e_test.py --scenario petshop
  python _tools/cex_e2e_test.py --scenario instagram --full
  python _tools/cex_e2e_test.py --all
  python _tools/cex_e2e_test.py --all --full
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

CONFIG_PATH = CEX_ROOT / "_docs" / "tests" / "e2e_config.yaml"
RESULTS_PATH = CEX_ROOT / "_docs" / "tests" / "e2e_results.json"
RUNNER_PATH = CEX_ROOT / "_tools" / "cex_8f_runner.py"

# F-labels expected in trace output
F_LABELS = ["CONSTRAIN", "BECOME", "INJECT", "REASON", "CALL", "PRODUCE", "GOVERN", "COLLABORATE"]


# ================================================================
# CONFIG LOADER
# ================================================================

def load_config() -> dict:
    """Load e2e_config.yaml."""
    if not CONFIG_PATH.exists():
        print(f"[FAIL] Config not found: {CONFIG_PATH}")
        sys.exit(1)
    try:
        # Use cex_shared if available, else fallback to yaml
        sys.path.insert(0, str(CEX_ROOT / "_tools"))
        try:
            from cex_shared import load_yaml
            return load_yaml(CONFIG_PATH)
        except ImportError:
            import yaml
            return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[FAIL] Config parse error: {e}")
        sys.exit(1)


# ================================================================
# RUNNER INVOCATION
# ================================================================

def run_8f(intent: str, kind: str, execute: bool = False,
           timeout: int = 300) -> dict:
    """Run cex_8f_runner.py and capture output.

    Returns dict with keys: returncode, stdout, stderr, elapsed_ms
    """
    cmd = [
        sys.executable, str(RUNNER_PATH),
        intent,
        "--kind", kind,
        "--verbose",
    ]
    if execute:
        cmd.append("--execute")
    else:
        cmd.append("--dry-run")

    t0 = time.perf_counter()
    try:
        result = subprocess.run(
            cmd, capture_output=True, timeout=timeout,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        elapsed = (time.perf_counter() - t0) * 1000
        stdout = result.stdout.decode("utf-8", errors="replace") if result.stdout else ""
        stderr = result.stderr.decode("utf-8", errors="replace") if result.stderr else ""
        return {
            "returncode": result.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "elapsed_ms": round(elapsed),
        }
    except subprocess.TimeoutExpired:
        elapsed = (time.perf_counter() - t0) * 1000
        return {
            "returncode": -1,
            "stdout": "",
            "stderr": f"TIMEOUT after {timeout}s",
            "elapsed_ms": round(elapsed),
        }
    except Exception as e:
        return {
            "returncode": -2,
            "stdout": "",
            "stderr": str(e),
            "elapsed_ms": 0,
        }


# ================================================================
# TRACE PARSER
# ================================================================

def parse_trace(output: str) -> dict:
    """Extract F1-F8 trace info from runner output.

    Returns dict: {
        'functions_fired': ['F1', 'F2', ...],
        'kind': str,
        'pillar': str,
        'verdict': 'PASS'|'FAIL'|'UNKNOWN',
        'gates_passed': int,
        'gates_total': int,
        'retries': int,
        'artifact_words': int,
        'output_path': str,
        'has_prompt': bool,
    }
    """
    trace = {
        "functions_fired": [],
        "kind": "",
        "pillar": "",
        "verdict": "UNKNOWN",
        "gates_passed": 0,
        "gates_total": 0,
        "retries": 0,
        "artifact_words": 0,
        "output_path": "",
        "has_prompt": False,
    }

    # Detect which F-functions fired
    for i, label in enumerate(F_LABELS, 1):
        if label in output:
            trace["functions_fired"].append(f"F{i}")

    # Extract kind from banner
    m = re.search(r"CEX 8F Runner \|\s*(\S+)\s*\|\s*(\S+)", output)
    if m:
        trace["kind"] = m.group(1)
        trace["pillar"] = m.group(2)

    # Verdict line
    m = re.search(r"Verdict:\s+(PASS|FAIL)\s*\((\d+)/(\d+)\s+gates,\s*(\d+)\s+retries\)", output)
    if m:
        trace["verdict"] = m.group(1)
        trace["gates_passed"] = int(m.group(2))
        trace["gates_total"] = int(m.group(3))
        trace["retries"] = int(m.group(4))

    # Artifact size
    m = re.search(r"Artifact:\s+(\d+)\s+words", output)
    if m:
        trace["artifact_words"] = int(m.group(1))

    # Output path
    m = re.search(r"Output:\s+(.+?)$", output, re.MULTILINE)
    if m:
        trace["output_path"] = m.group(1).strip()

    # Prompt presence (dry-run mode)
    trace["has_prompt"] = ("STRUCTURED PROMPT" in output or
                           "CONSTRAINTS" in output or
                           "IDENTITY" in output or
                           "INSTRUCTION" in output)

    return trace


# ================================================================
# QUALITY SCORING
# ================================================================

def score_artifact(path: str) -> float:
    """Score artifact using cex_score.py structural scorer. Returns 0-10."""
    try:
        sys.path.insert(0, str(CEX_ROOT / "_tools"))
        from cex_score import score_artifact as _score
        score, _notes = _score(path)
        return score
    except Exception as e:
        print(f"    [WARN] scoring failed: {e}")
        return 0.0


# ================================================================
# GOLD COMPARISON
# ================================================================

def compare_gold(artifact_path: str, gold_path: str) -> dict:
    """Compare produced artifact against gold standard.

    Returns: {match: bool, similarity: float, notes: str}
    """
    gold_full = CEX_ROOT / gold_path
    if not gold_full.exists():
        return {"match": False, "similarity": 0.0,
                "notes": f"gold standard not found: {gold_path}"}

    try:
        artifact = Path(artifact_path).read_text(encoding="utf-8")
        gold = gold_full.read_text(encoding="utf-8")
    except Exception as e:
        return {"match": False, "similarity": 0.0, "notes": str(e)}

    # Simple structural similarity: check if key sections from gold exist
    gold_headings = set(re.findall(r"^##\s+(.+)$", gold, re.MULTILINE))
    artifact_headings = set(re.findall(r"^##\s+(.+)$", artifact, re.MULTILINE))

    if not gold_headings:
        return {"match": True, "similarity": 1.0,
                "notes": "gold has no headings to compare"}

    overlap = gold_headings & artifact_headings
    similarity = len(overlap) / len(gold_headings) if gold_headings else 0.0

    return {
        "match": similarity >= 0.5,
        "similarity": round(similarity, 2),
        "notes": f"{len(overlap)}/{len(gold_headings)} sections match",
    }


# ================================================================
# SCENARIO RUNNER
# ================================================================

def run_scenario(name: str, config: dict, execute: bool = False) -> dict:
    """Run a single E2E scenario. Returns result dict."""
    scenario = config["scenarios"].get(name)
    if not scenario:
        return {"name": name, "status": "SKIP", "reason": f"scenario '{name}' not in config"}

    global_floor = config.get("quality_floor", 8.0)
    floor = scenario.get("quality_floor", global_floor)
    timeout = config.get("timeout_full" if execute else "timeout_quick", 120)
    input_text = scenario["input"]
    expected_kinds = scenario.get("expected_kinds", [])

    print(f"\n  --- Scenario: {name} ---")
    print(f"  Input: \"{input_text}\"")
    print(f"  Mode: {'FULL (LLM)' if execute else 'QUICK (dry-run)'}")
    print(f"  Expected kinds: {expected_kinds}")

    result = {
        "name": name,
        "input": input_text,
        "mode": "full" if execute else "quick",
        "status": "PASS",
        "checks": [],
        "kinds_tested": [],
        "total_elapsed_ms": 0,
    }

    all_passed = True

    # Run 8F for each expected kind
    for kind in expected_kinds:
        kind_result = {
            "kind": kind,
            "checks": [],
            "score": None,
            "trace": None,
        }

        # Run the 8F pipeline
        run_out = run_8f(input_text, kind, execute=execute, timeout=timeout)
        result["total_elapsed_ms"] += run_out["elapsed_ms"]
        full_output = run_out["stdout"] + "\n" + run_out["stderr"]

        # Parse trace
        trace = parse_trace(full_output)
        kind_result["trace"] = trace

        # CHECK 1: Runner exits without crash
        runner_ok = run_out["returncode"] == 0
        kind_result["checks"].append({
            "check": "runner_exits_clean",
            "passed": runner_ok,
            "detail": f"exit={run_out['returncode']}" + (
                f" stderr={run_out['stderr'][:100]}" if not runner_ok else ""),
        })
        if not runner_ok:
            all_passed = False
            print(f"    [FAIL] {kind}: runner crashed (exit={run_out['returncode']})")

        # CHECK 2: F1 CONSTRAIN fires
        f1_ok = "F1" in trace["functions_fired"]
        kind_result["checks"].append({
            "check": "f1_constrain_fires",
            "passed": f1_ok,
            "detail": f"functions={trace['functions_fired']}",
        })
        if not f1_ok:
            all_passed = False
            print(f"    [FAIL] {kind}: F1 CONSTRAIN did not fire")

        # CHECK 3: F2 BECOME fires (builder loaded)
        f2_ok = "F2" in trace["functions_fired"]
        kind_result["checks"].append({
            "check": "f2_become_fires",
            "passed": f2_ok,
            "detail": "",
        })
        if not f2_ok:
            all_passed = False
            print(f"    [FAIL] {kind}: F2 BECOME did not fire")

        # CHECK 4: F3 INJECT fires (knowledge loaded)
        f3_ok = "F3" in trace["functions_fired"]
        kind_result["checks"].append({
            "check": "f3_inject_fires",
            "passed": f3_ok,
            "detail": "",
        })

        # CHECK 5: Prompt/artifact was produced
        produced = trace["has_prompt"] or trace["artifact_words"] > 0
        kind_result["checks"].append({
            "check": "artifact_produced",
            "passed": produced,
            "detail": f"words={trace['artifact_words']}, has_prompt={trace['has_prompt']}",
        })
        if not produced:
            all_passed = False
            print(f"    [FAIL] {kind}: no artifact/prompt produced")

        if execute:
            # CHECK 6: F7 gates pass
            verdict_ok = trace["verdict"] == "PASS"
            kind_result["checks"].append({
                "check": "f7_gates_pass",
                "passed": verdict_ok,
                "detail": f"verdict={trace['verdict']} gates={trace['gates_passed']}/{trace['gates_total']}",
            })
            if not verdict_ok:
                all_passed = False
                print(f"    [FAIL] {kind}: F7 verdict={trace['verdict']}")

            # CHECK 7: Output file exists
            out_path = trace["output_path"]
            file_exists = bool(out_path) and Path(out_path).exists()
            kind_result["checks"].append({
                "check": "output_file_exists",
                "passed": file_exists,
                "detail": out_path or "no path in trace",
            })
            if not file_exists:
                all_passed = False
                print(f"    [FAIL] {kind}: output file missing")

            # CHECK 8: Quality score meets floor
            if file_exists:
                q_score = score_artifact(out_path)
                kind_result["score"] = q_score
                score_ok = q_score >= floor
                kind_result["checks"].append({
                    "check": "quality_floor",
                    "passed": score_ok,
                    "detail": f"score={q_score}, floor={floor}",
                })
                if not score_ok:
                    all_passed = False
                    print(f"    [FAIL] {kind}: quality {q_score} < {floor}")

                # CHECK 9: Gold standard comparison (if available)
                gold_path = scenario.get("gold_standard", "")
                if gold_path:
                    gold_result = compare_gold(out_path, gold_path)
                    kind_result["checks"].append({
                        "check": "gold_comparison",
                        "passed": gold_result["match"],
                        "detail": gold_result["notes"],
                    })
                    if not gold_result["match"]:
                        print(f"    [WARN] {kind}: gold mismatch ({gold_result['notes']})")
        else:
            # Quick mode: verify prompt structure has key sections
            has_identity = "IDENTITY" in full_output
            has_constraints = "CONSTRAINTS" in full_output or "CONSTRAIN" in full_output
            has_instruction = "INSTRUCTION" in full_output
            has_task = "TASK" in full_output
            prompt_ok = has_constraints and (has_identity or has_instruction or has_task)
            kind_result["checks"].append({
                "check": "prompt_structure",
                "passed": prompt_ok,
                "detail": (f"identity={has_identity}, constraints={has_constraints}, "
                           f"instruction={has_instruction}, task={has_task}"),
            })
            if not prompt_ok:
                all_passed = False
                print(f"    [FAIL] {kind}: prompt missing key sections")

        # Summary for this kind
        checks_passed = sum(1 for c in kind_result["checks"] if c["passed"])
        checks_total = len(kind_result["checks"])
        status_sym = "[OK]" if checks_passed == checks_total else "[FAIL]"
        score_str = f" score={kind_result['score']}" if kind_result["score"] else ""
        print(f"    {status_sym} {kind}: {checks_passed}/{checks_total} checks{score_str} ({run_out['elapsed_ms']}ms)")

        result["kinds_tested"].append(kind_result)

    result["status"] = "PASS" if all_passed else "FAIL"
    return result


# ================================================================
# REPORT
# ================================================================

def write_report(results: list, config: dict) -> None:
    """Write JSON report to _docs/tests/e2e_results.json."""
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = total - passed

    # Compute average quality across all scored kinds
    all_scores = []
    for r in results:
        for k in r.get("kinds_tested", []):
            if k.get("score") is not None:
                all_scores.append(k["score"])
    avg_quality = round(sum(all_scores) / len(all_scores), 1) if all_scores else None

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": config.get("version", "1.0.0"),
        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed,
            "avg_quality": avg_quality,
        },
        "scenarios": results,
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  Report saved: {RESULTS_PATH}")


# ================================================================
# MAIN
# ================================================================

def main() -> int:
    parser = argparse.ArgumentParser(description="CEX E2E Stress Test Runner")
    parser.add_argument("--scenario", metavar="NAME", help="Run single scenario (petshop, instagram, docs)")
    parser.add_argument("--all", action="store_true", help="Run all scenarios")
    parser.add_argument("--quick", action="store_true", default=True, help="Dry-run mode (default)")
    parser.add_argument("--full", action="store_true", help="Execute mode with LLM calls")
    args = parser.parse_args()

    if not args.scenario and not args.all:
        parser.print_help()
        return 1

    config = load_config()
    scenarios = config.get("scenarios", {})
    execute = args.full

    # Select scenarios
    if args.all:
        names = list(scenarios.keys())
    elif args.scenario:
        if args.scenario not in scenarios:
            print(f"[FAIL] Unknown scenario: {args.scenario}")
            print(f"  Available: {', '.join(scenarios.keys())}")
            return 1
        names = [args.scenario]
    else:
        names = []

    mode_str = "FULL" if execute else "QUICK"
    print("=" * 60)
    print(f"  CEX E2E Stress Test -- {mode_str} mode")
    print(f"  Scenarios: {len(names)} ({', '.join(names)})")
    print("=" * 60)

    t0 = time.time()
    results = []

    for name in names:
        result = run_scenario(name, config, execute=execute)
        results.append(result)

    elapsed = time.time() - t0

    # Write JSON report
    write_report(results, config)

    # Summary
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed
    total_kinds = sum(len(r.get("kinds_tested", [])) for r in results)

    # Compute avg quality
    all_scores = []
    for r in results:
        for k in r.get("kinds_tested", []):
            if k.get("score") is not None:
                all_scores.append(k["score"])
    avg_str = f" (avg quality: {sum(all_scores)/len(all_scores):.1f})" if all_scores else ""

    print(f"\n{'=' * 60}")
    print(f"  E2E: {passed}/{len(results)} passed{avg_str}")
    print(f"  Kinds tested: {total_kinds}")
    print(f"  Time: {elapsed:.1f}s")
    print(f"{'=' * 60}")

    if failed > 0:
        print("\n  FAILURES:")
        for r in results:
            if r["status"] == "FAIL":
                print(f"    [FAIL] {r['name']}")
                for k in r.get("kinds_tested", []):
                    for c in k.get("checks", []):
                        if not c["passed"]:
                            print(f"      - {k['kind']}/{c['check']}: {c['detail'][:80]}")

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
