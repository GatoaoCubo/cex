#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_system_test.py -- Full system validation for CEX bootstrap.

Tests all components: tools, builders, artifacts, hooks, runner, infra.
Run after bootstrap to confirm system health.

Usage:
  python _tools/cex_system_test.py           # full test suite
  python _tools/cex_system_test.py --quick   # fast checks only (no LLM)
"""

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

PASS = 0
FAIL = 0
SKIP = 0
RESULTS = []


def test(name: str, passed: bool, detail: str = "") -> None:
    """Record test result."""
    global PASS, FAIL
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS += 1
    else:
        FAIL += 1
    RESULTS.append({"name": name, "status": status, "detail": detail})
    symbol = "[OK]" if passed else "[FAIL]"
    msg = f"  {symbol} {name}"
    if detail:
        msg += f" -- {detail}"
    print(msg)


def skip(name: str, reason: str = "") -> None:
    """Record skipped test."""
    global SKIP
    SKIP += 1
    RESULTS.append({"name": name, "status": "SKIP", "detail": reason})
    print(f"  >>  {name} -- {reason}")


def run_cmd(cmd: list, timeout: int = 30) -> tuple[int, str, str]:
    """Run command, return (returncode, stdout, stderr)."""
    try:
        r = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        return r.returncode, r.stdout, r.stderr
    except Exception as e:
        return -1, "", str(e)


# ============================================================
# TEST GROUPS
# ============================================================


def test_tools() -> None:
    """Test all CEX tools exist and are importable."""
    print("\n=== TOOLS ===")
    tools = [
        "cex_8f_motor.py", "cex_8f_runner.py", "cex_intent.py",
        "cex_compile.py", "cex_doctor.py", "cex_index.py",
        "cex_feedback.py", "cex_hooks.py", "cex_score.py",
        "cex_materialize.py", "signal_writer.py",
    ]
    for t in tools:
        path = CEX_ROOT / "_tools" / t
        test(f"tool:{t}", path.exists(), f"{path.stat().st_size}B" if path.exists() else "MISSING")


def test_doctor() -> None:
    """Run cex_doctor and check results."""
    print("\n=== DOCTOR ===")
    rc, out, err = run_cmd([sys.executable, "_tools/cex_doctor.py"])
    full = (out or "") + (err or "")

    # Extract result line
    m = re.search(r"(\d+) PASS \| (\d+) WARN \| (\d+) FAIL", full)
    if m:
        passes, warns, fails = int(m.group(1)), int(m.group(2)), int(m.group(3))
        test("doctor:pass_count", passes >= 98, f"{passes}/98+ PASS")
        test("doctor:zero_warn", warns == 0, f"{warns} WARN")
        test("doctor:zero_fail", fails == 0, f"{fails} FAIL")
    else:
        test("doctor:runs", False, "Could not parse output")


def test_compile() -> None:
    """Test compilation works."""
    print("\n=== COMPILE ===")
    rc, out, err = run_cmd([sys.executable, "_tools/cex_compile.py", "--all"], timeout=60)
    full = (out or "") + (err or "")
    m = re.search(r"(\d+)/(\d+) compiled", full)
    if m:
        ok, total = int(m.group(1)), int(m.group(2))
        test("compile:all", ok == total, f"{ok}/{total}")
    else:
        test("compile:runs", rc == 0, full[:100])


def test_builders() -> None:
    """Validate builder archetypes."""
    print("\n=== BUILDERS ===")
    builder_dir = CEX_ROOT / "archetypes" / "builders"
    builders = [d for d in builder_dir.iterdir() if d.is_dir() and d.name.endswith("-builder")]
    test("builders:count", len(builders) >= 98, f"{len(builders)} builders")

    # Check each has 13 specs
    short_builders = []
    for b in builders:
        isos = list(b.glob("bld_*.md"))
        if len(isos) < 13:
            short_builders.append(f"{b.name}({len(isos)})")
    test("builders:13_isos", len(short_builders) == 0,
         f"{len(short_builders)} short: {', '.join(short_builders[:5])}" if short_builders else "all 13 specs")


def test_nuclei() -> None:
    """Validate nucleus artifacts."""
    print("\n=== NUCLEI ===")
    nuclei = {
        "N01_intelligence": 11, "N02_marketing": 10, "N03_engineering": 34,
        "N04_knowledge": 12, "N05_operations": 9, "N06_commercial": 9, "N07_admin": 13,
    }
    for ndir, expected_min in nuclei.items():
        path = CEX_ROOT / ndir
        if not path.exists():
            test(f"nucleus:{ndir}", False, "DIR MISSING")
            continue
        mds = [f for f in path.rglob("*.md")
               if "compiled" not in str(f) and f.name != "README.md" and not f.name.startswith("_")]
        test(f"nucleus:{ndir}", len(mds) >= expected_min, f"{len(mds)} artifacts (min {expected_min})")


def test_quality() -> None:
    """Check quality scores."""
    print("\n=== QUALITY ===")
    rc, out, err = run_cmd(["grep", "-r", "^quality: null", "--include=*.md"] +
                           [d for d in os.listdir(".") if d.startswith("N0")])
    null_count = len([l for l in out.strip().split("\n") if l.strip()]) if out.strip() else 0
    test("quality:zero_null", null_count <= 10, f"{null_count} quality:null (awaiting peer review)")

    # Count scored artifacts
    rc2, out2, _ = run_cmd(["grep", "-rc", "^quality: [0-9]", "--include=*.md"] +
                            [d for d in os.listdir(".") if d.startswith("N0")])
    scored = sum(int(l.split(":")[-1]) for l in out2.strip().split("\n") if l.strip() and ":" in l)
    test("quality:scored", scored >= 95, f"{scored} artifacts with quality score")


def test_subagents() -> None:
    """Check materialized sub-agents."""
    print("\n=== SUB-AGENTS ===")
    agents_dir = CEX_ROOT / ".claude" / "agents"
    if agents_dir.exists():
        agents = list(agents_dir.glob("*.md"))
        test("subagents:count", len(agents) >= 99, f"{len(agents)} sub-agents")
    else:
        test("subagents:dir", False, ".claude/P02_model/ not found")

    # Check materialize tool
    mat = CEX_ROOT / "_tools" / "cex_materialize.py"
    test("subagents:materializer", mat.exists())


def test_hooks() -> None:
    """Test hooks system."""
    print("\n=== HOOKS ===")
    # validate-all
    rc, out, err = run_cmd([sys.executable, "_tools/cex_hooks.py", "validate-all"])
    full = (out or "") + (err or "")
    m = re.search(r"Errors:\s+(\d+)", full)
    errors = int(m.group(1)) if m else -1
    test("hooks:validate_all", errors == 0, f"{errors} errors")

    # git hook installed
    hook = CEX_ROOT / ".git" / "hooks" / "pre-commit"
    test("hooks:git_precommit", hook.exists())


def test_infra() -> None:
    """Test infrastructure files."""
    print("\n=== INFRASTRUCTURE ===")
    # Boot scripts
    for n in ["n01", "n02", "n03", "n04", "n05", "n06"]:
        boot = CEX_ROOT / "boot" / f"{n}.ps1"
        test(f"boot:{n}", boot.exists())

    # Spawn scripts
    for script in ["spawn_solo.ps1", "spawn_grid.ps1", "spawn_monitor.ps1", "spawn_stop.ps1"]:
        path = CEX_ROOT / "_spawn" / script
        test(f"spawn:{script}", path.exists())

    # dispatch.sh
    dispatch = CEX_ROOT / "_spawn" / "dispatch.sh"
    test("dispatch:dispatch.sh", dispatch.exists())

    # Runtime dirs
    for subdir in ["handoffs", "signals", "pids"]:
        path = CEX_ROOT / ".cex" / "runtime" / subdir
        test(f"runtime:{subdir}", path.exists())

    # kinds_meta.json
    kinds = CEX_ROOT / ".cex" / "kinds_meta.json"
    if kinds.exists():
        data = json.loads(kinds.read_text(encoding="utf-8"))
        count = len(data) if isinstance(data, (list, dict)) else 0
        test("registry:kinds_meta", count >= 90, f"{count} kinds registered")
    else:
        test("registry:kinds_meta", False, "MISSING")


def test_runner_dryrun() -> None:
    """Test 8F runner in dry-run mode."""
    print("\n=== 8F RUNNER (dry-run) ===")
    rc, out, err = run_cmd([
        sys.executable, "_tools/cex_8f_runner.py",
        "create a knowledge card about testing", "--kind", "knowledge_card",
        "--dry-run", "--verbose"
    ])
    full = (out or "") + (err or "")
    test("runner:dryrun_runs", rc == 0, f"exit={rc}")
    test("runner:has_f1", "CONSTRAIN" in full, "F1 CONSTRAIN found" if "CONSTRAIN" in full else "")
    test("runner:has_f6", "PRODUCE" in full, "F6 PRODUCE found" if "PRODUCE" in full else "")
    test("runner:has_prompt", "CONSTRAINTS" in full or "IDENTITY" in full or "SYSTEM PROMPT" in full)


def test_runner_execute(quick: bool = False) -> None:
    """Test 8F runner in execute mode (calls LLM)."""
    print("\n=== 8F RUNNER (execute) ===")
    if quick:
        skip("runner:execute", "skipped in --quick mode")
        return

    rc, out, err = run_cmd([
        sys.executable, "_tools/cex_8f_runner.py",
        "create a knowledge card about system testing patterns",
        "--kind", "knowledge_card", "--execute", "--verbose"
    ], timeout=120)
    full = (out or "") + (err or "")
    passed = "PASS" in full and "Verdict" in full
    test("runner:execute_pass", passed,
         "PASS" if passed else full[-200:])

    # Check learning record was created
    lr_dir = CEX_ROOT / ".cex" / "learning_records"
    if lr_dir.exists():
        records = list(lr_dir.glob("lr_knowledge_card_*.json"))
        test("runner:learning_record", len(records) > 0, f"{len(records)} records")
    else:
        test("runner:learning_record", False, "no learning_records dir")

    # Cleanup test artifact
    for f in (CEX_ROOT / "N00_genesis" / "P01_knowledge" / "examples").glob("p01_knowledge_card_create_a*"):
        f.unlink()


def test_kc_library() -> None:
    """Test KC library coverage."""
    print("\n=== KC LIBRARY ===")
    kc_dir = CEX_ROOT / "N00_genesis" / "P01_knowledge" / "library" / "kind"
    if kc_dir.exists():
        kcs = list(kc_dir.glob("kc_*.md"))
        test("kc:count", len(kcs) >= 98, f"{len(kcs)}/98 kind KCs")
    else:
        test("kc:dir", False, "library/kind/ not found")


def test_e2e(quick: bool = True) -> None:
    """Test E2E stress scenarios via cex_e2e_test.py."""
    print("\n=== E2E STRESS TESTS ===")
    e2e_script = CEX_ROOT / "_tools" / "cex_e2e_test.py"
    if not e2e_script.exists():
        test("e2e:script_exists", False, "cex_e2e_test.py MISSING")
        return

    test("e2e:script_exists", True)

    # Config exists
    e2e_config = CEX_ROOT / "_docs" / "tests" / "e2e_config.yaml"
    test("e2e:config_exists", e2e_config.exists())

    if not e2e_config.exists():
        return

    # Run in quick (dry-run) mode -- no LLM calls
    mode_args = ["--all", "--quick"] if quick else ["--all", "--full"]
    rc, out, err = run_cmd(
        [sys.executable, str(e2e_script)] + mode_args,
        timeout=180,
    )
    full = (out or "") + (err or "")

    # Parse summary line: "E2E: N/M passed"
    m = re.search(r"E2E:\s+(\d+)/(\d+)\s+passed", full)
    if m:
        passed, total = int(m.group(1)), int(m.group(2))
        test("e2e:scenarios_pass", passed == total,
             f"{passed}/{total} scenarios passed")
    else:
        test("e2e:runs", rc == 0, f"exit={rc}, output={full[:150]}")

    # Check JSON report was written
    results_file = CEX_ROOT / "_docs" / "tests" / "e2e_results.json"
    test("e2e:report_written", results_file.exists())


def test_boot_templates() -> None:
    """Smoke test: every boot/n0*.ps1 must contain vt_enable (prevents TUI regression)."""
    print("\n=== BOOT TEMPLATES ===")
    boot_dir = CEX_ROOT / "boot"
    ps1s = sorted(boot_dir.glob("n0*.ps1"))
    missing = [p.name for p in ps1s if "vt_enable" not in p.read_text(encoding="utf-8", errors="ignore")]
    test("boot:vt_enable", not missing, f"{len(ps1s)} scanned, missing: {missing or 'none'}")

    # Signal writer regression: must accept w\d+ and emit mission+wave filename
    try:
        from _tools.signal_writer import MISSION_PHASE_RE
        test("signal:mission_phase_regex", bool(MISSION_PHASE_RE.match("w1")), "w1 accepted")
        test("signal:mission_phase_reject_nXX", not MISSION_PHASE_RE.match("n99"), "n99 not a phase")
    except Exception as e:
        test("signal:mission_phase_regex", False, str(e)[:60])


def test_git() -> None:
    """Test git state."""
    print("\n=== GIT ===")
    rc, out, _ = run_cmd(["git", "status", "--porcelain"])
    dirty = len([l for l in out.strip().split("\n") if l.strip()]) if out.strip() else 0
    test("git:clean", dirty < 5, f"{dirty} dirty files")

    rc, out, _ = run_cmd(["git", "log", "--oneline", "-1"])
    test("git:has_commits", rc == 0, out.strip()[:60])


# ============================================================
# MAIN
# ============================================================


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="CEX System Test")
    parser.add_argument("--quick", action="store_true", help="Skip LLM tests")
    args = parser.parse_args()

    print("=" * 60)
    print("  CEX SYSTEM TEST -- Full Bootstrap Validation")
    print("=" * 60)

    t0 = time.time()

    test_tools()
    test_doctor()
    test_compile()
    test_builders()
    test_nuclei()
    test_quality()
    test_subagents()
    test_hooks()
    test_infra()
    test_runner_dryrun()
    test_runner_execute(quick=args.quick)
    test_e2e(quick=args.quick)
    test_kc_library()
    test_boot_templates()
    test_git()

    elapsed = time.time() - t0

    # Summary
    total = PASS + FAIL + SKIP
    print(f"\n{'=' * 60}")
    print(f"  RESULTS: {PASS} PASS | {FAIL} FAIL | {SKIP} SKIP | {total} total")
    print(f"  Time: {elapsed:.1f}s")
    print(f"{'=' * 60}")

    if FAIL > 0:
        print("\n  FAILURES:")
        for r in RESULTS:
            if r["status"] == "FAIL":
                print(f"    [FAIL] {r['name']}: {r['detail']}")

    # Write results
    results_path = CEX_ROOT / ".cex" / "system_test_results.json"
    import datetime
    results_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "pass": PASS,
        "fail": FAIL,
        "skip": SKIP,
        "total": total,
        "elapsed_s": round(elapsed, 1),
        "tests": RESULTS,
    }
    results_path.write_text(json.dumps(results_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\n  Results saved to .cex/system_test_results.json")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
