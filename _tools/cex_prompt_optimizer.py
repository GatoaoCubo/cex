#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Prompt Optimizer -- score, rank, and improve builder prompts.

Analyzes bld_prompt specs against build outcomes (learning records),
identifies weak performers, and generates improvement suggestions.

Usage:
    python cex_prompt_optimizer.py --scan                  # Score all builders
    python cex_prompt_optimizer.py --analyze agent         # Analyze one builder
    python cex_prompt_optimizer.py --top 10 --worst        # Show worst performers
    python cex_prompt_optimizer.py --suggest agent         # Suggest improvements
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import find_builder_dir, load_iso

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDERS_ROOT = CEX_ROOT / "archetypes" / "builders"
LEARNING_DIR = CEX_ROOT / ".cex" / "learning_records"


# ---------------------------------------------------------------------------
# Builder Analysis
# ---------------------------------------------------------------------------


def scan_builders() -> list[dict]:
    """Scan all builder directories and score their spec completeness."""
    if not BUILDERS_ROOT.exists():
        return []

    iso_prefixes = [
        "bld_model", "bld_prompt",
        "bld_knowledge", "bld_eval", "bld_schema",
        "bld_output", "bld_tools",
        "bld_config", "bld_memory", "bld_architecture", "bld_orchestration",
    ]

    builders = []
    for bdir in sorted(BUILDERS_ROOT.iterdir()):
        if not bdir.is_dir() or not bdir.name.endswith("-builder"):
            continue

        kind = bdir.name.replace("-builder", "").replace("-", "_")
        files = list(bdir.glob("*.md"))

        # Check spec completeness
        present = set()
        for f in files:
            for prefix in iso_prefixes:
                if f.name.startswith(prefix):
                    present.add(prefix)
                    break

        # Score specs by content quality
        iso_scores = {}
        total_bytes = 0
        for prefix in iso_prefixes:
            text = load_iso(bdir, prefix, kind)
            if text:
                body = _strip_fm(text)
                iso_scores[prefix] = _score_iso_content(body, prefix)
                total_bytes += len(body.encode("utf-8"))
            else:
                iso_scores[prefix] = 0.0

        completeness = len(present) / len(iso_prefixes)
        avg_score = sum(iso_scores.values()) / len(iso_prefixes)

        builders.append({
            "kind": kind,
            "dir": str(bdir),
            "iso_count": len(present),
            "iso_total": len(iso_prefixes),
            "completeness": round(completeness, 3),
            "avg_score": round(avg_score, 3),
            "total_bytes": total_bytes,
            "iso_scores": iso_scores,
            "missing": [p for p in iso_prefixes if p not in present],
        })

    return builders


def _strip_fm(text: str) -> str:
    """Remove frontmatter."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end + 3:].strip()
    return text


def _score_iso_content(body: str, prefix: str) -> float:
    """Score individual builder spec content quality (0-10)."""
    if not body.strip():
        return 0.0

    score = 5.0  # Base score for existing content
    chars = len(body)
    lines = body.count("\n") + 1

    # Size scoring
    if chars > 500:
        score += 1.0
    if chars > 1500:
        score += 0.5
    if chars > 3000:
        score += 0.5

    # Structure scoring
    if "##" in body:
        score += 0.5
    if "|" in body and "---" in body:  # Tables
        score += 0.5
    if "```" in body:  # Code blocks
        score += 0.3

    # Prefix-specific scoring
    if prefix == "bld_prompt" and lines > 10:
        score += 0.5
    if prefix == "bld_eval" and body.count("---") >= 2:
        score += 0.5
    if prefix == "bld_schema" and ("required" in body.lower() or "pattern" in body.lower()):
        score += 0.5

    # Penalty for stub content
    if chars < 200:
        score -= 1.0
    if "TODO" in body or "STUB" in body or "placeholder" in body.lower():
        score -= 2.0

    return round(max(0.0, min(10.0, score)), 1)


# ---------------------------------------------------------------------------
# Learning Record Analysis
# ---------------------------------------------------------------------------


def load_learning_records() -> list[dict]:
    """Load all learning records and aggregate by kind."""
    if not LEARNING_DIR.exists():
        return []

    records = []
    for f in sorted(LEARNING_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            records.append(data)
        except (json.JSONDecodeError, OSError):
            continue
    return records


def aggregate_by_kind(records: list[dict]) -> dict[str, dict]:
    """Aggregate learning records by kind: pass/fail rates, common failures."""
    by_kind: dict[str, dict] = defaultdict(lambda: {
        "total": 0, "passed": 0, "failed": 0,
        "avg_retries": 0.0, "common_issues": defaultdict(int),
        "avg_time_ms": 0.0, "times": [],
    })

    for rec in records:
        kind = rec.get("kind", "unknown")
        k = by_kind[kind]
        k["total"] += 1

        verdict = rec.get("verdict", {})
        if verdict.get("passed"):
            k["passed"] += 1
        else:
            k["failed"] += 1
            for issue in verdict.get("issues", []):
                k["common_issues"][issue] += 1

        k["avg_retries"] += verdict.get("retries", 0)

        # Timing
        total_ms = sum(rec.get("timings", {}).values())
        if total_ms > 0:
            k["times"].append(total_ms)

    # Finalize averages
    for kind, k in by_kind.items():
        if k["total"] > 0:
            k["avg_retries"] = round(k["avg_retries"] / k["total"], 2)
            k["pass_rate"] = round(k["passed"] / k["total"], 3)
        if k["times"]:
            k["avg_time_ms"] = round(sum(k["times"]) / len(k["times"]), 0)
        k["common_issues"] = dict(k["common_issues"])
        del k["times"]

    return dict(by_kind)


# ---------------------------------------------------------------------------
# Improvement Suggestions
# ---------------------------------------------------------------------------


def suggest_improvements(kind: str) -> list[str]:
    """Generate improvement suggestions for a builder based on analysis."""
    bdir = find_builder_dir(kind)
    if not bdir:
        return [f"Builder not found for kind '{kind}'"]

    suggestions = []
    kind_slug = kind.replace("-", "_")

    # Check prompt quality
    instr = load_iso(bdir, "bld_prompt", kind_slug)
    if not instr:
        suggestions.append("CRITICAL: Missing bld_prompt spec -- builder has no production guide")
    else:
        body = _strip_fm(instr)
        if len(body) < 500:
            suggestions.append(
                "bld_prompt is thin (<500 chars). Add: step-by-step process, "
                "field decision rules, density targets, section requirements"
            )
        if "density" not in body.lower():
            suggestions.append("bld_prompt doesn't mention density target (should be >= 0.85)")
        if "frontmatter" not in body.lower():
            suggestions.append("bld_prompt doesn't mention frontmatter requirements")

    # Check eval
    examples = load_iso(bdir, "bld_eval", kind_slug)
    if not examples:
        suggestions.append("Missing bld_eval -- no few-shot guidance for LLM")
    else:
        body = _strip_fm(examples)
        example_count = body.count("## Example") + body.count("### Example")
        if example_count < 2:
            suggestions.append(f"Only {example_count} example(s) found -- add 2-3 diverse examples")

    # Check schema
    schema = load_iso(bdir, "bld_schema", kind_slug)
    if not schema:
        suggestions.append("Missing bld_schema -- no structural contract for validation")
    else:
        body = _strip_fm(schema)
        if "required" not in body.lower():
            suggestions.append("bld_schema doesn't list required fields")
        if "pattern" not in body.lower() and "regex" not in body.lower():
            suggestions.append("bld_schema doesn't define ID pattern regex")

    # Check eval quality gate
    qg = load_iso(bdir, "bld_eval", kind_slug)
    if not qg:
        suggestions.append("Missing bld_eval -- no kind-specific quality criteria")

    # Check memory
    memory = load_iso(bdir, "bld_memory", kind_slug)
    if not memory:
        suggestions.append("No bld_memory -- builder has no persistent learning. Consider creating one.")

    # Check learning records
    records = load_learning_records()
    kind_records = [r for r in records if r.get("kind") == kind]
    if kind_records:
        failed = [r for r in kind_records if not r.get("verdict", {}).get("passed")]
        if failed:
            issues = defaultdict(int)
            for r in failed:
                for i in r.get("verdict", {}).get("issues", []):
                    issues[i] += 1
            top_issues = sorted(issues.items(), key=lambda x: -x[1])[:3]
            suggestions.append(
                f"Learning records show {len(failed)}/{len(kind_records)} failures. "
                f"Top issues: {'; '.join(f'{i[0]} ({i[1]}x)' for i in top_issues)}"
            )

    if not suggestions:
        suggestions.append("Builder looks complete. Consider enriching examples with more diversity.")

    return suggestions


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Prompt Optimizer -- builder analysis & improvement")
    parser.add_argument("--scan", action="store_true", help="Score all builders")
    parser.add_argument("--analyze", "-a", help="Analyze specific builder (kind name)")
    parser.add_argument("--suggest", "-s", help="Suggest improvements for a builder")
    parser.add_argument("--top", type=int, default=20, help="Number of results")
    parser.add_argument("--worst", action="store_true", help="Sort by worst score first")
    parser.add_argument("--records", action="store_true", help="Show learning record analysis")
    args = parser.parse_args()

    if args.scan:
        builders = scan_builders()
        if args.worst:
            builders.sort(key=lambda b: b["avg_score"])
        else:
            builders.sort(key=lambda b: -b["avg_score"])

        print(f"\n=== Builder Analysis ({len(builders)} builders) ===\n")
        print(f"  {'Kind':30s} {'specs':>5s} {'Complete':>8s} {'Score':>6s} {'Bytes':>7s}")
        print(f"  {'-' * 60}")
        for b in builders[:args.top]:
            print(
                f"  {b['kind']:30s} {b['iso_count']:>2d}/13"
                f" {b['completeness']:>7.0%} {b['avg_score']:>6.1f}"
                f" {b['total_bytes']:>6d}B"
            )

        # Summary stats
        avg_completeness = sum(b["completeness"] for b in builders) / len(builders) if builders else 0
        avg_score = sum(b["avg_score"] for b in builders) / len(builders) if builders else 0
        print(f"\n  Avg completeness: {avg_completeness:.0%}")
        print(f"  Avg spec score:    {avg_score:.1f}/10")
        return

    if args.analyze:
        bdir = find_builder_dir(args.analyze)
        if not bdir:
            print(f"Builder not found: {args.analyze}")
            sys.exit(1)

        builders = scan_builders()
        target = next((b for b in builders if b["kind"] == args.analyze.replace("-", "_")), None)
        if not target:
            print(f"Builder not found in scan: {args.analyze}")
            sys.exit(1)

        print(f"\n=== Builder Analysis: {target['kind']} ===\n")
        print(f"  Directory:    {target['dir']}")
        print(f"  specs:         {target['iso_count']}/13 ({target['completeness']:.0%})")
        print(f"  Avg Score:    {target['avg_score']:.1f}/10")
        print(f"  Total Size:   {target['total_bytes']:,} bytes")

        if target["missing"]:
            print("\n  Missing specs:")
            for m in target["missing"]:
                print(f"    - {m}")

        print("\n  Spec Scores:")
        for prefix, score in sorted(target["iso_scores"].items(), key=lambda x: x[1]):
            bar = "#" * int(score)
            status = "MISSING" if score == 0 else ""
            print(f"    {prefix:30s} {score:>4.1f} {bar} {status}")
        return

    if args.suggest:
        suggestions = suggest_improvements(args.suggest)
        print(f"\n=== Improvement Suggestions: {args.suggest} ===\n")
        for i, s in enumerate(suggestions, 1):
            print(f"  {i}. {s}")
        return

    if args.records:
        records = load_learning_records()
        by_kind = aggregate_by_kind(records)
        print(f"\n=== Learning Records Analysis ({len(records)} records) ===\n")
        print(f"  {'Kind':30s} {'Total':>5s} {'Pass%':>6s} {'Retries':>8s} {'Time':>8s}")
        print(f"  {'-' * 60}")
        for kind, stats in sorted(by_kind.items(), key=lambda x: x[1].get("pass_rate", 0)):
            print(
                f"  {kind:30s} {stats['total']:>5d}"
                f" {stats.get('pass_rate', 0):>5.0%}"
                f" {stats['avg_retries']:>7.1f}"
                f" {stats['avg_time_ms']:>7.0f}ms"
            )
        return

    parser.print_help()


if __name__ == "__main__":
    main()
