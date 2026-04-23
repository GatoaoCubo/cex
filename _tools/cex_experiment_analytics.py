#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cex_experiment_analytics.py -- Aggregate experiment results into trends.

Reads .cex/experiments/results.tsv + diff_log.jsonl and produces:
  - Convergence rate by kind (rounds to reach target)
  - Best/worst deltas (biggest positive/negative impact)
  - Success rate by hypothesis type
  - Quality distribution histogram (text-based)
  - Top 10 most-improved artifacts
  - Top 10 stubbornly-low artifacts

GDP decision: format=tsv (append to existing, grep-friendly, zero deps)

Usage:
    python _tools/cex_experiment_analytics.py                # full report
    python _tools/cex_experiment_analytics.py --kind agent    # filter by kind
    python _tools/cex_experiment_analytics.py --since 2026-04-01
    python _tools/cex_experiment_analytics.py --format tsv
    python _tools/cex_experiment_analytics.py --diff-log      # analyze diff_log.jsonl
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

RESULTS_FILE = CEX_ROOT / ".cex" / "experiments" / "results.tsv"
DIFF_LOG_FILE = CEX_ROOT / ".cex" / "experiments" / "diff_log.jsonl"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


# ------------------------------------------------------------------
# Data loading
# ------------------------------------------------------------------

def load_results(since: str | None = None) -> list[dict]:
    """Load results.tsv into list of dicts.

    TSV columns: timestamp, file, round, quality, density, status, description
    """
    if not RESULTS_FILE.exists():
        return []

    records = []
    lines = RESULTS_FILE.read_text(encoding="utf-8").strip().split("\n")
    if len(lines) < 2:
        return []

    header = lines[0].split("\t")
    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) < 6:
            continue

        rec = {}
        for i, col in enumerate(header):
            rec[col.strip()] = parts[i].strip() if i < len(parts) else ""

        # Parse types
        try:
            rec["quality"] = float(rec.get("quality", 0))
        except ValueError:
            rec["quality"] = 0.0
        try:
            rec["density"] = float(rec.get("density", 0))
        except ValueError:
            rec["density"] = 0.0
        try:
            rec["round"] = int(rec.get("round", 0))
        except ValueError:
            rec["round"] = 0

        # Date filter
        if since:
            ts = rec.get("timestamp", "")
            if ts < since:
                continue

        records.append(rec)

    return records


def load_diff_log(since: str | None = None) -> list[dict]:
    """Load diff_log.jsonl into list of dicts."""
    if not DIFF_LOG_FILE.exists():
        return []

    records = []
    for line in DIFF_LOG_FILE.read_text(encoding="utf-8").strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue

        if since and rec.get("timestamp", "") < since:
            continue
        records.append(rec)

    return records


def extract_kind_from_path(filepath: str) -> str:
    """Best-effort kind extraction from file path."""
    # Try reading frontmatter (expensive but accurate)
    fp = CEX_ROOT / filepath
    if fp.exists():
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")[:500]
            match = re.search(r"^kind:\s*(.+)$", text, re.MULTILINE)
            if match:
                return match.group(1).strip().strip('"').strip("'")
        except (OSError, PermissionError):
            pass

    # Heuristic from filename
    name = Path(filepath).stem
    if name.startswith("kc_"):
        return "knowledge_card"
    if name.startswith("bld_"):
        return "builder_iso"
    if name.startswith("p02_agent_"):
        return "agent"
    if name.startswith("p03_sp_"):
        return "system_prompt"
    return "unknown"


# ------------------------------------------------------------------
# Analytics
# ------------------------------------------------------------------

def convergence_by_kind(records: list[dict]) -> dict[str, dict]:
    """How many rounds does each kind take to reach target?

    Returns {kind: {avg_rounds, min_rounds, max_rounds, count, success_rate}}
    """
    by_kind = defaultdict(list)

    # Group by file, find successful experiments
    by_file = defaultdict(list)
    for r in records:
        by_file[r.get("file", "")].append(r)

    for filepath, file_records in by_file.items():
        kind = extract_kind_from_path(filepath)
        keeps = [r for r in file_records if r.get("status") == "keep"]
        max_round = max((r["round"] for r in file_records), default=0)
        final_q = max((r["quality"] for r in keeps), default=0) if keeps else 0
        by_kind[kind].append({
            "rounds": max_round,
            "final_quality": final_q,
            "success": final_q >= 9.0,
        })

    result = {}
    for kind, experiments in sorted(by_kind.items()):
        rounds = [e["rounds"] for e in experiments]
        successes = sum(1 for e in experiments if e["success"])
        result[kind] = {
            "count": len(experiments),
            "avg_rounds": round(sum(rounds) / len(rounds), 1) if rounds else 0,
            "min_rounds": min(rounds) if rounds else 0,
            "max_rounds": max(rounds) if rounds else 0,
            "success_rate": round(successes / len(experiments) * 100, 1) if experiments else 0,
        }

    return result


def quality_distribution(records: list[dict]) -> dict[str, int]:
    """Histogram of quality scores (buckets: 0-5, 5-6, 6-7, 7-8, 8-9, 9-10)."""
    buckets = {"0-5": 0, "5-6": 0, "6-7": 0, "7-8": 0, "8-9": 0, "9-10": 0}

    # Get latest quality per file
    latest = {}
    for r in records:
        fp = r.get("file", "")
        q = r.get("quality", 0)
        if fp and q > 0:
            if fp not in latest or r.get("timestamp", "") > latest[fp].get("timestamp", ""):
                latest[fp] = r

    for r in latest.values():
        q = r.get("quality", 0)
        if q < 5:
            buckets["0-5"] += 1
        elif q < 6:
            buckets["5-6"] += 1
        elif q < 7:
            buckets["6-7"] += 1
        elif q < 8:
            buckets["7-8"] += 1
        elif q < 9:
            buckets["8-9"] += 1
        else:
            buckets["9-10"] += 1

    return buckets


def top_improved(records: list[dict], n: int = 10) -> list[dict]:
    """Top N most-improved artifacts (biggest quality delta)."""
    by_file = defaultdict(list)
    for r in records:
        by_file[r.get("file", "")].append(r)

    deltas = []
    for filepath, file_records in by_file.items():
        qualities = [r["quality"] for r in file_records if r["quality"] > 0]
        if len(qualities) >= 2:
            delta = max(qualities) - min(qualities)
            deltas.append({
                "file": filepath,
                "delta": round(delta, 1),
                "min_q": min(qualities),
                "max_q": max(qualities),
                "rounds": len(file_records),
            })

    deltas.sort(key=lambda x: x["delta"], reverse=True)
    return deltas[:n]


def stubbornly_low(records: list[dict], threshold: float = 8.0, n: int = 10) -> list[dict]:
    """Top N artifacts that remain below threshold despite multiple rounds."""
    by_file = defaultdict(list)
    for r in records:
        by_file[r.get("file", "")].append(r)

    stuck = []
    for filepath, file_records in by_file.items():
        rounds = len(file_records)
        if rounds < 2:
            continue
        latest_q = max((r["quality"] for r in file_records if r["quality"] > 0), default=0)
        if latest_q < threshold and latest_q > 0:
            stuck.append({
                "file": filepath,
                "quality": latest_q,
                "rounds": rounds,
                "discards": sum(1 for r in file_records if r.get("status") == "discard"),
            })

    stuck.sort(key=lambda x: x["rounds"], reverse=True)
    return stuck[:n]


def hypothesis_success_rate(records: list[dict]) -> dict[str, dict]:
    """Success rate grouped by hypothesis/description prefix."""
    by_type = defaultdict(lambda: {"keep": 0, "discard": 0, "crash": 0})

    for r in records:
        status = r.get("status", "")
        desc = r.get("description", "").split(":")[0].strip()
        if not desc or status == "skip":
            continue
        # Normalize hypothesis type
        desc_lower = desc.lower()
        if "density" in desc_lower or "filler" in desc_lower:
            htype = "density_improvement"
        elif "frontmatter" in desc_lower or "field" in desc_lower:
            htype = "frontmatter_fix"
        elif "table" in desc_lower:
            htype = "table_addition"
        elif "polish" in desc_lower or "format" in desc_lower:
            htype = "formatting"
        elif "tag" in desc_lower:
            htype = "tag_fix"
        elif "tldr" in desc_lower:
            htype = "tldr_fix"
        else:
            htype = desc[:30]

        by_type[htype][status] += 1

    result = {}
    for htype, counts in sorted(by_type.items()):
        total = counts["keep"] + counts["discard"] + counts["crash"]
        result[htype] = {
            "keep": counts["keep"],
            "discard": counts["discard"],
            "crash": counts["crash"],
            "total": total,
            "success_rate": round(counts["keep"] / total * 100, 1) if total > 0 else 0,
        }
    return result


def diff_log_analysis(diff_records: list[dict]) -> dict:
    """Analyze diff_log.jsonl for cluster evolution patterns."""
    if not diff_records:
        return {"status": "no diff_log data"}

    total = len(diff_records)
    kept = sum(1 for r in diff_records if r.get("kept", False))
    discarded = total - kept

    deltas = [r.get("delta", 0) for r in diff_records if r.get("delta") is not None]
    avg_delta = round(sum(deltas) / len(deltas), 2) if deltas else 0

    cluster_sizes = [r.get("cluster_size", 1) for r in diff_records if r.get("cluster_size")]
    avg_cluster = round(sum(cluster_sizes) / len(cluster_sizes), 1) if cluster_sizes else 0

    return {
        "total_experiments": total,
        "kept": kept,
        "discarded": discarded,
        "keep_rate": round(kept / total * 100, 1) if total > 0 else 0,
        "avg_delta": avg_delta,
        "avg_cluster_size": avg_cluster,
    }


# ------------------------------------------------------------------
# Report generation
# ------------------------------------------------------------------

def generate_report(
    records: list[dict],
    diff_records: list[dict],
    fmt: str = "md",
    kind_filter: str | None = None,
) -> str:
    """Generate full analytics report."""
    if kind_filter:
        records = [r for r in records if extract_kind_from_path(r.get("file", "")) == kind_filter]

    lines = []

    # Summary stats
    total = len(records)
    keeps = sum(1 for r in records if r.get("status") == "keep")
    discards = sum(1 for r in records if r.get("status") == "discard")
    crashes = sum(1 for r in records if r.get("status") == "crash")
    skips = sum(1 for r in records if r.get("status") == "skip")

    lines.append("# CEX Experiment Analytics")
    lines.append("")
    lines.append(f"Total experiments: {total}")
    lines.append(f"Keep: {keeps} | Discard: {discards} | Crash: {crashes} | Skip: {skips}")
    if total > 0:
        lines.append(f"Success rate: {keeps / max(1, keeps + discards + crashes) * 100:.1f}%")
    lines.append("")

    # Convergence by kind
    conv = convergence_by_kind(records)
    if conv:
        lines.append("## Convergence by Kind")
        lines.append("")
        lines.append("| Kind | Experiments | Avg Rounds | Success Rate |")
        lines.append("|------|-----------|-----------|-------------|")
        for kind, stats in sorted(conv.items(), key=lambda x: -x[1]["count"]):
            lines.append(
                f"| {kind} | {stats['count']} | {stats['avg_rounds']} | "
                f"{stats['success_rate']}% |"
            )
        lines.append("")

    # Quality distribution
    dist = quality_distribution(records)
    if any(v > 0 for v in dist.values()):
        lines.append("## Quality Distribution")
        lines.append("")
        max_count = max(dist.values()) or 1
        for bucket, count in dist.items():
            bar = "#" * int(count / max_count * 40) if count > 0 else ""
            lines.append(f"  {bucket:>5s} | {bar:40s} {count}")
        lines.append("")

    # Hypothesis success rates
    hyp = hypothesis_success_rate(records)
    if hyp:
        lines.append("## Hypothesis Success Rates")
        lines.append("")
        lines.append("| Hypothesis | Keep | Discard | Crash | Rate |")
        lines.append("|-----------|------|---------|-------|------|")
        for htype, stats in sorted(hyp.items(), key=lambda x: -x[1]["success_rate"]):
            lines.append(
                f"| {htype[:30]} | {stats['keep']} | {stats['discard']} | "
                f"{stats['crash']} | {stats['success_rate']}% |"
            )
        lines.append("")

    # Top improved
    improved = top_improved(records)
    if improved:
        lines.append("## Top 10 Most Improved")
        lines.append("")
        lines.append("| File | Delta | Min Q | Max Q | Rounds |")
        lines.append("|------|-------|-------|-------|--------|")
        for item in improved:
            name = Path(item["file"]).name
            lines.append(
                f"| {name} | +{item['delta']} | {item['min_q']} | "
                f"{item['max_q']} | {item['rounds']} |"
            )
        lines.append("")

    # Stubbornly low
    stuck = stubbornly_low(records)
    if stuck:
        lines.append("## Top 10 Stubbornly Low (< 8.0 after multiple rounds)")
        lines.append("")
        lines.append("| File | Quality | Rounds | Discards |")
        lines.append("|------|---------|--------|----------|")
        for item in stuck:
            name = Path(item["file"]).name
            lines.append(
                f"| {name} | {item['quality']} | {item['rounds']} | "
                f"{item['discards']} |"
            )
        lines.append("")

    # Diff log analysis
    diff_stats = diff_log_analysis(diff_records)
    if diff_stats.get("total_experiments", 0) > 0:
        lines.append("## Cluster Evolution (from diff_log.jsonl)")
        lines.append("")
        lines.append(f"Total: {diff_stats['total_experiments']}")
        lines.append(f"Keep rate: {diff_stats['keep_rate']}%")
        lines.append(f"Avg delta: {diff_stats['avg_delta']:+.2f}")
        lines.append(f"Avg cluster size: {diff_stats['avg_cluster_size']}")
        lines.append("")

    return "\n".join(lines)


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Experiment analytics for CEX autoresearch loop",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--kind", help="Filter by artifact kind")
    parser.add_argument("--since", help="Filter by date (YYYY-MM-DD)")
    parser.add_argument("--format", choices=["md", "tsv"], default="md",
                        help="Output format (default: md)")
    parser.add_argument("--diff-log", action="store_true",
                        help="Analyze diff_log.jsonl only")
    args = parser.parse_args()

    if args.diff_log:
        diff_records = load_diff_log(since=args.since)
        stats = diff_log_analysis(diff_records)
        if args.format == "tsv":
            for k, v in stats.items():
                print(f"{k}\t{v}")
        else:
            print(json.dumps(stats, indent=2))
        return

    records = load_results(since=args.since)
    diff_records = load_diff_log(since=args.since)

    if not records:
        print("[ANALYTICS] No experiment data found in results.tsv")
        print(f"  Expected: {RESULTS_FILE}")
        sys.exit(0)

    report = generate_report(records, diff_records, fmt=args.format, kind_filter=args.kind)

    if args.format == "tsv":
        # Simplified TSV output
        print("metric\tvalue")
        print(f"total_experiments\t{len(records)}")
        keeps = sum(1 for r in records if r.get("status") == "keep")
        print(f"keeps\t{keeps}")
        print(f"success_rate\t{keeps / max(1, len(records)) * 100:.1f}")
    else:
        print(report)


if __name__ == "__main__":
    main()
