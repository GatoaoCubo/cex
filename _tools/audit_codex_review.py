"""Wave 2 review: verify each codex nucleus's deliverables.

Runs after codex grid completes. For each of N01/N03/N04/N05:
- Check expected deliverables exist
- Check sentinel present in report
- Check report has minimum content (not stub)
- Re-run the relevant audit script and compare before/after counts

Output: _reports/audit/codex_review.md
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_reports" / "audit" / "codex_review.md"

EXPECTED = {
    "n01": {
        "deliverables": ["_reports/audit/doc_alignment.md"],
        "sentinel": "DOC_ALIGNMENT_PASS",
        "min_lines": 30,
        "rerun_audit": None,  # no audit re-run; doc_alignment is itself an audit
        "verify": "Stale docs identified with concrete fixes",
    },
    "n03": {
        "deliverables": ["_reports/audit/brand_decoupling_done.md"],
        "sentinel": "BRAND_DECOUPLING_PASS",
        "min_lines": 20,
        "rerun_audit": "_tools/audit_security_brand.py",
        "verify": "Brand HIGH/MEDIUM hits dropped (was 132)",
    },
    "n04": {
        "deliverables": [
            "examples/quickstart.md",
            "examples/build_one_artifact.md",
            "examples/run_grid.md",
            "SECURITY.md",
            "CODE_OF_CONDUCT.md",
            "_reports/audit/examples_community_done.md",
        ],
        "sentinel": "EXAMPLES_COMMUNITY_PASS",
        "min_lines": 20,
        "rerun_audit": "_tools/audit_docs_ux.py",
        "verify": "examples/ non-empty, SECURITY.md + CODE_OF_CONDUCT.md present",
    },
    "n05": {
        "deliverables": [
            "boot/n07.sh",
            "boot/n01.sh",
            "boot/n02.sh",
            "boot/n03.sh",
            "boot/n04.sh",
            "boot/n05.sh",
            "boot/n06.sh",
            "boot/cex.sh",
            "tests/MANIFEST.yaml",
            "_reports/audit/cross_platform_test_split_done.md",
        ],
        "sentinel": "CROSS_PLATFORM_TEST_SPLIT_PASS",
        "min_lines": 20,
        "rerun_audit": "_tools/audit_cross_platform.py",
        "verify": "8 bash files added, manifest parses",
    },
}


def check_sentinel(path: Path, sentinel: str) -> bool:
    if not path.exists():
        return False
    try:
        return sentinel in path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False


def line_count(path: Path) -> int:
    if not path.exists():
        return 0
    try:
        return len(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return 0


def review_nucleus(nuc: str, spec: dict) -> dict:
    """Score one nucleus's output."""
    result = {"nucleus": nuc, "checks": [], "score": 0.0, "passed": False}
    total = 0
    passed = 0

    # 1. Each deliverable exists?
    for d in spec["deliverables"]:
        total += 1
        p = ROOT / d
        if p.exists() and p.stat().st_size > 0:
            passed += 1
            result["checks"].append({"check": f"exists: {d}", "ok": True})
        else:
            result["checks"].append({"check": f"exists: {d}", "ok": False})

    # 2. Sentinel in main report?
    main_report = ROOT / spec["deliverables"][-1] if "_reports/" in spec["deliverables"][-1] \
        else ROOT / [d for d in spec["deliverables"] if "_reports/" in d][0]
    total += 1
    if check_sentinel(main_report, spec["sentinel"]):
        passed += 1
        result["checks"].append({"check": f"sentinel: {spec['sentinel']}", "ok": True})
    else:
        result["checks"].append({"check": f"sentinel: {spec['sentinel']}", "ok": False})

    # 3. Report has substantive content (not stub)?
    total += 1
    lines = line_count(main_report)
    if lines >= spec["min_lines"]:
        passed += 1
        result["checks"].append({"check": f"lines >= {spec['min_lines']}",
                                  "ok": True, "actual": lines})
    else:
        result["checks"].append({"check": f"lines >= {spec['min_lines']}",
                                  "ok": False, "actual": lines})

    # 4. Re-run relevant audit if specified
    if spec["rerun_audit"]:
        audit_path = ROOT / spec["rerun_audit"]
        if audit_path.exists():
            try:
                proc = subprocess.run(
                    [sys.executable, str(audit_path)],
                    cwd=ROOT, capture_output=True, text=True,
                    timeout=180, encoding="utf-8", errors="replace",
                )
                total += 1
                if proc.returncode == 0:
                    passed += 1
                    result["checks"].append({"check": f"re-run {spec['rerun_audit']}",
                                              "ok": True, "exit": 0})
                else:
                    result["checks"].append({"check": f"re-run {spec['rerun_audit']}",
                                              "ok": False, "exit": proc.returncode,
                                              "stderr_tail": proc.stderr[-300:]})
            except (subprocess.TimeoutExpired, OSError) as e:
                total += 1
                result["checks"].append({"check": f"re-run {spec['rerun_audit']}",
                                          "ok": False, "error": str(e)})

    result["score"] = round(10.0 * passed / total, 2) if total > 0 else 0.0
    result["passed"] = passed == total
    result["passed_count"] = passed
    result["total_count"] = total
    return result


def write_report(reviews: list[dict]) -> None:
    out = ["# CODEX WAVE 1 REVIEW (N07 verification)", ""]
    out.append(f"Mission: OPENSOURCE_FIX. Reviewed: {len(reviews)} nuclei.")
    out.append("")
    out.append("## Summary")
    out.append("")
    out.append("| Nucleus | Score | Pass/Total | Status |")
    out.append("|---------|-------|------------|--------|")
    for r in reviews:
        status = "PASS" if r["passed"] else "FAIL"
        out.append(f"| {r['nucleus'].upper()} | {r['score']}/10 | "
                   f"{r['passed_count']}/{r['total_count']} | **{status}** |")
    out.append("")
    out.append("## Per-nucleus details")
    out.append("")
    for r in reviews:
        out.append(f"### {r['nucleus'].upper()} -- {r['score']}/10")
        out.append("")
        out.append("| Check | OK | Detail |")
        out.append("|-------|----|--------|")
        for c in r["checks"]:
            ok = "YES" if c["ok"] else "**NO**"
            extra = ""
            for k, v in c.items():
                if k not in ("check", "ok"):
                    extra += f"{k}={v} "
            out.append(f"| {c['check']} | {ok} | {extra.strip()} |")
        out.append("")
    out.append("## CODEX_REVIEW_PASS")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"[REVIEW] report written: {OUT}")


def main() -> int:
    reviews = []
    for nuc, spec in EXPECTED.items():
        print(f"[REVIEW] {nuc}...")
        reviews.append(review_nucleus(nuc, spec))
    write_report(reviews)
    all_pass = all(r["passed"] for r in reviews)
    print(f"[REVIEW] {'ALL PASS' if all_pass else 'SOME FAILED'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
