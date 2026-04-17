#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Python-Only Scorer -- L1 (structural) + L2 (rubric) without any LLM call.

Weights: L1 structural 30% + L2 rubric 30% = 60% total.
Only triggers LLM (L3 semantic, 40%) when L1+L2 avg >= 8.5.

This module is a lightweight alternative to cex_score.py's hybrid mode.
It reuses the same L1/L2 functions but wraps them in a simpler interface
designed for batch scoring at zero token cost.

Usage (import):
    from cex_score_python import score_fast, needs_llm
    result = score_fast("path/to/artifact.md")
    if needs_llm(result):
        # call cex_score.score_hybrid() for full 3-layer

Usage (CLI):
    python _tools/cex_score_python.py artifact.md
    python _tools/cex_score_python.py --batch N03_engineering/ --apply
    python _tools/cex_score_python.py --below 8.5 N0*/**/*.md
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any, Sequence

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_tools"))

from cex_score import score_structural, score_rubric, update_quality  # noqa: E402


# ================================================================
# H01-H07 Gate Checks (boolean Python functions)
# ================================================================

def _check_h01_frontmatter(content, fm):
    """H01: Valid YAML frontmatter exists."""
    return fm is not None


def _check_h02_required_fields(content, fm):
    """H02: Required fields present (id, kind, pillar)."""
    if not fm:
        return False
    return all(f in fm for f in ["id:", "kind:", "pillar:"])


def _check_h03_quality_null(content, fm):
    """H03: quality field exists (null or numeric)."""
    if not fm:
        return False
    return "quality:" in fm


def _check_h04_naming(path_str, fm):
    """H04: File follows naming convention (pillar prefix or nucleus prefix)."""
    name = Path(path_str).name
    # Accept: p01_*, kc_*, bld_*, n0*_, tpl_*, or any kind-prefixed name
    return bool(re.match(r'^(p\d{2}_|kc_|bld_|n0\d_|tpl_|cfg_|spec_|idx_)', name))


def _check_h05_no_placeholders(content, body):
    """H05: No TODO/TBD/FIXME placeholders in body."""
    hits = re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body)
    return len(hits) == 0


def _check_h06_min_size(content):
    """H06: Minimum content size (>= 200 bytes)."""
    return len(content.encode("utf-8")) >= 200


def _check_h07_ascii_if_code(path_str, content):
    """H07: If executable code file, must be ASCII-only."""
    ext = Path(path_str).suffix.lower()
    if ext not in (".py", ".ps1", ".sh", ".cmd", ".bat"):
        return True  # not code, skip check
    try:
        content.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def run_gates(
    path_str: str, content: str, fm_str: str | None, body: str
) -> tuple[int, int, list[str]]:
    """Run all H01-H07 gates. Returns (pass_count, total, failed_gates)."""
    gates = [
        ("H01", _check_h01_frontmatter(content, fm_str)),
        ("H02", _check_h02_required_fields(content, fm_str)),
        ("H03", _check_h03_quality_null(content, fm_str)),
        ("H04", _check_h04_naming(path_str, fm_str)),
        ("H05", _check_h05_no_placeholders(content, body)),
        ("H06", _check_h06_min_size(content)),
        ("H07", _check_h07_ascii_if_code(path_str, content)),
    ]
    passed = sum(1 for _, ok in gates if ok)
    failed = [gid for gid, ok in gates if not ok]
    return passed, len(gates), failed


# ================================================================
# Fast Scorer (L1 + L2 only, zero LLM tokens)
# ================================================================

def score_fast(path: str | os.PathLike[str], verbose: bool = False) -> dict[str, Any]:
    """Score artifact using L1 (structural) + L2 (rubric) only.

    Returns dict:
        {
            "path": str,
            "score": float,        # weighted L1+L2 (0-10 scale, clamped 7.0-9.3)
            "structural": float,   # L1 score
            "rubric": float,       # L2 score
            "gates_passed": int,
            "gates_total": int,
            "gates_failed": list,
            "needs_llm": bool,     # True if avg >= 8.5 (L3 would add value)
            "notes": list,
        }
    """
    path = str(path)
    if not os.path.exists(path):
        return {
            "path": path, "score": 0.0, "structural": 0.0, "rubric": 0.0,
            "gates_passed": 0, "gates_total": 7, "gates_failed": ["MISSING"],
            "needs_llm": False, "notes": ["MISSING"],
        }

    content = open(path, "r", encoding="utf-8").read()
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    fm_str = fm_match.group(1) if fm_match else None
    body = content[fm_match.end():] if fm_match else content

    # L1: Structural
    struct_raw, struct_notes = score_structural(path)
    structural = round(8.0 + (struct_raw / 10.0) * 1.3, 2)
    structural = min(max(structural, 7.0), 9.3)

    # L2: Rubric
    rubric_raw, rubric_dims, rubric_notes = score_rubric(path)
    rubric = round(8.0 + (rubric_raw / 10.0) * 1.3, 2)
    rubric = min(max(rubric, 7.0), 9.5)

    # H01-H07 gates
    gates_passed, gates_total, gates_failed = run_gates(
        path, content, fm_str, body
    )

    # Gate penalty: each failed gate reduces score by 0.15
    gate_penalty = len(gates_failed) * 0.15

    # Weighted blend: 50% structural + 50% rubric (since no L3)
    raw_score = structural * 0.5 + rubric * 0.5 - gate_penalty
    score = round(min(max(raw_score, 7.0), 9.3), 1)

    avg_12 = (structural + rubric) / 2.0

    all_notes = struct_notes + rubric_notes
    if gates_failed:
        all_notes.append("gates_failed: %s" % ",".join(gates_failed))

    if verbose:
        print("  [L1] structural: %.2f" % structural)
        print("  [L2] rubric:     %.2f (%d dims)" % (rubric, len(rubric_dims)))
        print("  [HG] gates:      %d/%d (failed: %s)" % (
            gates_passed, gates_total,
            ",".join(gates_failed) if gates_failed else "none"))
        print("  [  ] avg L1+L2:  %.2f -> needs_llm=%s" % (
            avg_12, avg_12 >= 8.5))

    return {
        "path": path,
        "score": score,
        "structural": structural,
        "rubric": rubric,
        "gates_passed": gates_passed,
        "gates_total": gates_total,
        "gates_failed": gates_failed,
        "needs_llm": avg_12 >= 8.5,
        "notes": all_notes,
    }


def needs_llm(result: dict[str, Any]) -> bool:
    """Check if a score_fast result warrants L3 semantic scoring."""
    return result.get("needs_llm", False)


# ================================================================
# Batch Scorer
# ================================================================

def score_batch(
    paths: Sequence[str | os.PathLike[str]], verbose: bool = False
) -> list[dict[str, Any]]:
    """Score multiple artifacts. Returns list of result dicts."""
    results = []
    for p in paths:
        p = str(p).strip()
        if not p or not p.endswith(".md"):
            continue
        results.append(score_fast(p, verbose=verbose))
    return results


# ================================================================
# CLI
# ================================================================

def _find_artifacts(targets):
    """Expand directories into .md files with frontmatter."""
    files = []
    for t in targets:
        t = t.strip()
        if not t:
            continue
        p = Path(t)
        if p.is_file() and p.suffix == ".md":
            files.append(str(p))
        elif p.is_dir():
            for md in sorted(p.rglob("*.md")):
                # Skip hidden dirs and non-artifact files
                if any(part.startswith(".") for part in md.parts):
                    continue
                files.append(str(md))
    return files


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX Python-Only Scorer (L1+L2, zero LLM tokens)"
    )
    parser.add_argument("files", nargs="*", help="Files or directories to score")
    parser.add_argument("--apply", action="store_true",
                        help="Write scores to quality: field in files")
    parser.add_argument("--below", type=float, default=0,
                        help="Only show artifacts scoring below threshold")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show per-artifact scoring details")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON")
    args = parser.parse_args()

    if not args.files:
        # Default: score all nucleus artifacts
        args.files = [d for d in os.listdir(".")
                      if d.startswith("N0") and os.path.isdir(d)]

    files = _find_artifacts(args.files)
    if not files:
        print("No .md artifacts found.")
        return

    results = score_batch(files, verbose=args.verbose)

    if args.below > 0:
        results = [r for r in results if r["score"] < args.below]

    if args.json:
        import json
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    # Table output
    print("%5s | %4s | %4s | %3s/%1s | %-30s | Path" % (
        "Score", "L1", "L2", "HG", "T", "Notes"))
    print("-" * 100)

    for r in sorted(results, key=lambda x: x["score"]):
        notes_str = "; ".join(r["notes"][:3]) if r["notes"] else "OK"
        llm_tag = " *" if r["needs_llm"] else ""
        print("%5.1f | %4.1f | %4.1f | %d/%d  | %-30s | %s%s" % (
            r["score"], r["structural"], r["rubric"],
            r["gates_passed"], r["gates_total"],
            notes_str[:30], r["path"], llm_tag))

    # Summary
    scores = [r["score"] for r in results]
    if scores:
        print("\n" + "=" * 100)
        print("Total: %d artifacts" % len(scores))
        print("Avg:   %.2f" % (sum(scores) / len(scores)))
        print("9.0+:  %d" % sum(1 for s in scores if s >= 9.0))
        print("8.5+:  %d" % sum(1 for s in scores if s >= 8.5))
        print("<8.5:  %d" % sum(1 for s in scores if s < 8.5))
        llm_candidates = sum(1 for r in results if r["needs_llm"])
        print("Need LLM (L3): %d" % llm_candidates)

    if args.apply:
        updated = 0
        for r in results:
            if update_quality(r["path"], r["score"]):
                updated += 1
        print("\nApplied scores to %d/%d files." % (updated, len(results)))


if __name__ == "__main__":
    main()
