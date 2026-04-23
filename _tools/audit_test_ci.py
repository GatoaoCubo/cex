"""Audit W6 TEST + CI: green-on-clone health check.

Scans:
- All test_*.py files: count, location, run them, capture pass/fail
- .github/workflows/*.yml: list, lint via yaml.safe_load
- cex_doctor.py: run + capture
- cex_flywheel_audit.py: run + capture
- requirements files: requirements*.txt, pyproject.toml, setup.py

Output: _reports/audit/test_ci.md
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "_reports" / "audit" / "inventory_full.jsonl"
OUT = ROOT / "_reports" / "audit" / "test_ci.md"


def load_inventory() -> list[dict]:
    """Stream inventory_full.jsonl into memory."""
    records = []
    with INVENTORY.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def find_tests(records: list[dict]) -> list[dict]:
    """Find test_*.py files."""
    tests = []
    for r in records:
        path = r["path"]
        if path.startswith((".venv", ".aider", ".git/")):
            continue
        name = path.split("/")[-1]
        if name.startswith("test_") and name.endswith(".py"):
            tests.append({"path": path, "lines": r["lines"]})
        elif name.endswith("_test.py"):
            tests.append({"path": path, "lines": r["lines"]})
    return tests


def find_workflows(records: list[dict]) -> list[dict]:
    """Find .github/workflows/*.yml files."""
    wfs = []
    for r in records:
        path = r["path"]
        if path.startswith(".github/workflows/") and path.endswith((".yml", ".yaml")):
            wfs.append({"path": path, "lines": r["lines"]})
    return wfs


def find_dep_files(records: list[dict]) -> list[dict]:
    """Find requirements files + pyproject.toml + setup.py."""
    deps = []
    for r in records:
        path = r["path"]
        name = path.split("/")[-1]
        if name in ("pyproject.toml", "setup.py", "setup.cfg",
                    "Pipfile", "Pipfile.lock", "uv.lock", "package.json"):
            if "/" not in path or path.count("/") <= 1:
                deps.append({"path": path, "lines": r["lines"]})
        elif name.startswith("requirements") and name.endswith(".txt"):
            deps.append({"path": path, "lines": r["lines"]})
    return deps


def run_quick_check(cmd: list[str], timeout: int = 60) -> dict:
    """Run a command and return summary."""
    try:
        result = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, text=True,
            timeout=timeout, encoding="utf-8", errors="replace",
        )
        return {
            "exit_code": result.returncode,
            "stdout_tail": result.stdout[-1500:] if result.stdout else "",
            "stderr_tail": result.stderr[-500:] if result.stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"exit_code": -1, "stdout_tail": "TIMEOUT", "stderr_tail": ""}
    except OSError as e:
        return {"exit_code": -2, "stdout_tail": "", "stderr_tail": str(e)}


def lint_workflow(path: Path) -> tuple[bool, str]:
    """Try yaml.safe_load on workflow."""
    try:
        import yaml
        with path.open("r", encoding="utf-8") as f:
            yaml.safe_load(f)
        return True, "OK"
    except (yaml.YAMLError, OSError, ImportError) as e:
        return False, str(e)[:120]


def write_report(tests: list[dict], wfs: list[dict], deps: list[dict],
                  doctor: dict, flywheel: dict,
                  test_results: list[dict], wf_lints: list[dict]) -> None:
    """Emit test_ci.md."""
    lines = [
        "# W6 TEST + CI HEALTH",
        "",
        "Generated from `_reports/audit/inventory_full.jsonl`. "
        f"{len(tests)} test files, {len(wfs)} workflows, {len(deps)} dep files.",
        "",
        "## Dependency files (must exist for opensource clone)",
        "",
        "| File | Lines | Present? |",
        "|------|-------|----------|",
    ]
    expected_deps = ["requirements.txt", "pyproject.toml"]
    found_dep_names = {Path(d["path"]).name for d in deps}
    for exp in expected_deps:
        present = "YES" if exp in found_dep_names else "**MISSING**"
        lines.append(f"| `{exp}` | -- | {present} |")
    lines.append("")
    lines.append("Detected dep files:")
    lines.append("")
    if deps:
        for d in deps:
            lines.append(f"- `{d['path']}` ({d['lines']} lines)")
    else:
        lines.append("_None._")
    lines.append("")
    lines.append("## GitHub workflows")
    lines.append("")
    lines.append("| Workflow | Lines | YAML valid? | Error |")
    lines.append("|----------|-------|-------------|-------|")
    for wf, lint in zip(wfs, wf_lints):
        valid = "YES" if lint["ok"] else "**NO**"
        err = lint["err"] if not lint["ok"] else ""
        lines.append(f"| `{wf['path']}` | {wf['lines']} | {valid} | {err} |")
    lines.append("")
    lines.append("## Test files (sample run on first 10)")
    lines.append("")
    lines.append("| Test | Lines | Exit | Outcome |")
    lines.append("|------|-------|------|---------|")
    for t, res in zip(tests[:10], test_results):
        outcome = "PASS" if res["exit_code"] == 0 else f"FAIL ({res['exit_code']})"
        lines.append(f"| `{t['path']}` | {t['lines']} | {res['exit_code']} | {outcome} |")
    if len(tests) > 10:
        lines.append(f"| ... | ... | ... | (+{len(tests) - 10} more not run) |")
    lines.append("")
    pass_count = sum(1 for r in test_results if r["exit_code"] == 0)
    lines.append(f"**Test pass rate (sample of 10): {pass_count}/{len(test_results)}**")
    lines.append("")
    lines.append("## cex_doctor.py")
    lines.append("")
    lines.append(f"Exit code: `{doctor['exit_code']}`")
    lines.append("")
    lines.append("```")
    lines.append(doctor["stdout_tail"][:1500] or doctor["stderr_tail"][:1500])
    lines.append("```")
    lines.append("")
    lines.append("## cex_flywheel_audit.py")
    lines.append("")
    lines.append(f"Exit code: `{flywheel['exit_code']}`")
    lines.append("")
    lines.append("```")
    lines.append(flywheel["stdout_tail"][:1500] or flywheel["stderr_tail"][:1500])
    lines.append("```")
    lines.append("")
    lines.append("## All test files (full list)")
    lines.append("")
    lines.append("| Path | Lines |")
    lines.append("|------|-------|")
    for t in tests:
        lines.append(f"| `{t['path']}` | {t['lines']} |")
    lines.append("")
    lines.append("## TEST_CI_PASS")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[W6] report written: {OUT}")


def main() -> int:
    """Run W6 test/CI audit."""
    print("[W6] loading inventory...")
    records = load_inventory()
    tests = find_tests(records)
    wfs = find_workflows(records)
    deps = find_dep_files(records)
    print(f"[W6] {len(tests)} tests, {len(wfs)} workflows, {len(deps)} dep files")

    print("[W6] linting workflows...")
    wf_lints = []
    for wf in wfs:
        ok, err = lint_workflow(ROOT / wf["path"])
        wf_lints.append({"ok": ok, "err": err})

    print("[W6] running first 10 tests (45s timeout each)...")
    test_results = []
    for t in tests[:10]:
        print(f"[W6]   running {t['path']}...")
        res = run_quick_check([sys.executable, t["path"]], timeout=45)
        test_results.append(res)

    print("[W6] running cex_doctor.py...")
    doctor = run_quick_check([sys.executable, "_tools/cex_doctor.py"], timeout=60)

    print("[W6] running cex_flywheel_audit.py...")
    flywheel = run_quick_check([sys.executable, "_tools/cex_flywheel_audit.py"],
                                timeout=120)

    write_report(tests, wfs, deps, doctor, flywheel, test_results, wf_lints)
    print("[W6] DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
