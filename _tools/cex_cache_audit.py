#!/usr/bin/env python3
"""
---
kind: cli_tool
pillar: P07
nucleus: N05
quality: null
---
CEX Cache Audit -- inspect Anthropic prompt-cache breakpoints and transcript hit rates.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

DEFAULT_TRANSCRIPTS_DIR = (
    Path.home()
    / ".claude"
    / "projects"
    / "C--Users-CEX-Documents-GitHub-cex"
)

# Pricing as of 2026-04-16
INPUT_COST_PER_MTOK = 3.00
OUTPUT_COST_PER_MTOK = 15.00
CACHE_READ_COST_PER_MTOK = 0.30
CACHE_WRITE_COST_PER_MTOK = 3.75


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit Anthropic prompt cache usage from local Claude Code transcripts."
    )
    parser.add_argument(
        "--transcripts",
        default=str(DEFAULT_TRANSCRIPTS_DIR),
        help="Directory containing Claude Code .jsonl session transcripts.",
    )
    parser.add_argument(
        "--last",
        type=int,
        default=10,
        help="Analyze only the last N session files by modified time.",
    )
    parser.add_argument(
        "--breakpoints",
        action="store_true",
        help="Print detected cache_control breakpoint locations.",
    )
    parser.add_argument(
        "--hit-rate",
        action="store_true",
        help="Print aggregate hit-rate metrics.",
    )
    parser.add_argument(
        "--breakdown",
        action="store_true",
        help="Print a per-session token and savings breakdown.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON.",
    )
    return parser.parse_args()


def iter_ephemeral_breakpoints(value: Any, path: str = "") -> list[dict[str, str]]:
    matches: list[dict[str, str]] = []
    if isinstance(value, dict):
        if value.get("cache_control", {}).get("type") == "ephemeral":
            matches.append(
                {
                    "path": path or "$",
                    "type": value["cache_control"]["type"],
                }
            )
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else key
            matches.extend(iter_ephemeral_breakpoints(child, child_path))
    elif isinstance(value, list):
        for idx, child in enumerate(value):
            child_path = f"{path}[{idx}]" if path else f"[{idx}]"
            matches.extend(iter_ephemeral_breakpoints(child, child_path))
    return matches


def session_hit_rate(reads: int, writes: int, uncached: int) -> float:
    total = reads + writes + uncached
    if total <= 0:
        return 0.0
    return reads / total


def dollars_from_tokens(tokens: int, delta_per_mtok: float) -> float:
    return (tokens * delta_per_mtok) / 1_000_000.0


def net_savings(reads: int, writes: int) -> float:
    saved = dollars_from_tokens(reads, INPUT_COST_PER_MTOK - CACHE_READ_COST_PER_MTOK)
    premium = dollars_from_tokens(writes, CACHE_WRITE_COST_PER_MTOK - INPUT_COST_PER_MTOK)
    return saved - premium


def classify_breakpoint_discipline(sessions: list[dict[str, Any]]) -> str:
    if not sessions:
        return "poor"
    compliant = 0
    for session in sessions:
        count = session["breakpoint_count"]
        if 1 <= count <= 4:
            compliant += 1
    ratio = compliant / len(sessions)
    if ratio >= 0.8:
        return "good"
    if ratio >= 0.5:
        return "fair"
    return "poor"


def build_recommendations(summary: dict[str, Any]) -> list[str]:
    recommendations: list[str] = []
    hit_rate = summary["hit_rate"]
    reads = summary["cache_read_input_tokens"]
    writes = summary["cache_creation_input_tokens"]
    uncached = summary["input_tokens"]
    total = reads + writes + uncached
    uncached_ratio = (uncached / total) if total else 0.0
    write_ratio = (writes / total) if total else 0.0

    if hit_rate < 0.60:
        recommendations.append("consider a more stable boot prefix to improve reuse")
    if write_ratio > 0.20:
        recommendations.append("cache writes are high; consolidate breakpoints")
    if uncached_ratio > 0.30:
        recommendations.append("uncached input is large; inspect dynamic prompt sections")
    if not recommendations:
        recommendations.append("cache behavior looks stable; keep breakpoint placement consistent")
    return recommendations


def collect_sessions(transcripts_dir: Path, last_n: int) -> list[Path]:
    if not transcripts_dir.exists() or not transcripts_dir.is_dir():
        return []
    files = sorted(
        transcripts_dir.glob("*.jsonl"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    return files[: max(last_n, 0)]


def analyze_session(path: Path) -> dict[str, Any]:
    reads = 0
    writes = 0
    uncached = 0
    output_tokens = 0
    cache_events = 0
    skipped_lines = 0
    breakpoint_hits: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                payload = json.loads(raw_line)
            except json.JSONDecodeError:
                skipped_lines += 1
                continue

            hits = iter_ephemeral_breakpoints(payload)
            if hits:
                role = payload.get("type") or payload.get("message", {}).get("role") or "unknown"
                for hit in hits:
                    breakpoint_hits.append(
                        {
                            "line": line_number,
                            "role": role,
                            "path": hit["path"],
                            "type": hit["type"],
                        }
                    )

            message = payload.get("message", {})
            usage = message.get("usage") if isinstance(message, dict) else None
            role = message.get("role") if isinstance(message, dict) else None
            if role != "assistant" or not isinstance(usage, dict):
                continue

            reads += int(usage.get("cache_read_input_tokens", 0) or 0)
            writes += int(usage.get("cache_creation_input_tokens", 0) or 0)
            uncached += int(usage.get("input_tokens", 0) or 0)
            output_tokens += int(usage.get("output_tokens", 0) or 0)
            cache_events += 1

    hit_rate = session_hit_rate(reads, writes, uncached)
    return {
        "session": path.stem,
        "path": str(path),
        "mtime": path.stat().st_mtime,
        "cache_read_input_tokens": reads,
        "cache_creation_input_tokens": writes,
        "input_tokens": uncached,
        "output_tokens": output_tokens,
        "cache_events": cache_events,
        "hit_rate": hit_rate,
        "net_saved_usd": net_savings(reads, writes),
        "skipped_lines": skipped_lines,
        "breakpoints": breakpoint_hits,
        "breakpoint_count": len(breakpoint_hits),
    }


def summarize(sessions: list[dict[str, Any]], transcripts_dir: Path, last_n: int) -> dict[str, Any]:
    reads = sum(session["cache_read_input_tokens"] for session in sessions)
    writes = sum(session["cache_creation_input_tokens"] for session in sessions)
    uncached = sum(session["input_tokens"] for session in sessions)
    output_tokens = sum(session["output_tokens"] for session in sessions)
    skipped_lines = sum(session["skipped_lines"] for session in sessions)
    cache_events = sum(session["cache_events"] for session in sessions)
    total_breakpoints = sum(session["breakpoint_count"] for session in sessions)

    summary = {
        "transcripts_dir": str(transcripts_dir),
        "requested_last": last_n,
        "sessions_analyzed": len(sessions),
        "cache_read_input_tokens": reads,
        "cache_creation_input_tokens": writes,
        "input_tokens": uncached,
        "output_tokens": output_tokens,
        "cache_events": cache_events,
        "skipped_lines": skipped_lines,
        "breakpoint_count": total_breakpoints,
        "hit_rate": session_hit_rate(reads, writes, uncached),
        "net_saved_usd": net_savings(reads, writes),
        "breakpoint_discipline": classify_breakpoint_discipline(sessions),
    }
    summary["recommendations"] = build_recommendations(summary)
    return summary


def print_summary_table(sessions: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    print(f"=== CACHE AUDIT (last {summary['sessions_analyzed']} sessions) ===")
    print()
    print(
        "%-30s %-9s %-9s %-9s %-9s %-9s"
        % ("Session", "Hit Rate", "Reads", "Writes", "Uncached", "Net Saved")
    )
    print("-" * 79)
    for session in sessions:
        label = session["session"]
        if len(label) > 30:
            label = label[:28] + ".."
        print(
            "%-30s %8.1f%% %9s %9s %9s %9s"
            % (
                label,
                session["hit_rate"] * 100.0,
                f"{session['cache_read_input_tokens']:,}",
                f"{session['cache_creation_input_tokens']:,}",
                f"{session['input_tokens']:,}",
                "$%.2" % session["net_saved_usd"],
            )
        )
    print()
    print(
        "Total: hit rate %.1f%% | net saved $%.2f across %d sessions"
        % (
            summary["hit_rate"] * 100.0,
            summary["net_saved_usd"],
            summary["sessions_analyzed"],
        )
    )
    print("Breakpoint discipline: %s" % summary["breakpoint_discipline"])
    print()
    print("Recommendations:")
    for item in summary["recommendations"]:
        print("- %s" % item)
    if summary["skipped_lines"]:
        print("- skipped malformed jsonl lines: %d" % summary["skipped_lines"])


def print_hit_rate(summary: dict[str, Any]) -> None:
    print("Cache hit rate: %.2f%%" % (summary["hit_rate"] * 100.0))
    print("Cache reads: %s" % f"{summary['cache_read_input_tokens']:,}")
    print("Cache writes: %s" % f"{summary['cache_creation_input_tokens']:,}")
    print("Uncached input: %s" % f"{summary['input_tokens']:,}")
    print("0 cache events" if summary["cache_events"] == 0 else "Cache events: %d" % summary["cache_events"])


def print_breakdown(sessions: list[dict[str, Any]]) -> None:
    print(
        "%-30s %-9s %-9s %-9s %-9s %-9s"
        % ("Session", "Reads", "Writes", "Uncached", "Output", "Net Saved")
    )
    print("-" * 79)
    for session in sessions:
        label = session["session"]
        if len(label) > 30:
            label = label[:28] + ".."
        print(
            "%-30s %9s %9s %9s %9s %9s"
            % (
                label,
                f"{session['cache_read_input_tokens']:,}",
                f"{session['cache_creation_input_tokens']:,}",
                f"{session['input_tokens']:,}",
                f"{session['output_tokens']:,}",
                "$%.2" % session["net_saved_usd"],
            )
        )


def print_breakpoints(sessions: list[dict[str, Any]]) -> None:
    for session in sessions:
        print(f"[{session['session']}] breakpoints={session['breakpoint_count']}")
        if not session["breakpoints"]:
            print("  (none)")
            continue
        for hit in session["breakpoints"]:
            print(
                "  line %d | role=%s | path=%s"
                % (hit["line"], hit["role"], hit["path"])
            )


def main() -> int:
    args = parse_args()
    transcripts_dir = Path(args.transcripts).expanduser()
    sessions_files = collect_sessions(transcripts_dir, args.last)

    if not transcripts_dir.exists() or not transcripts_dir.is_dir():
        message = {
            "status": "missing_transcripts_dir",
            "transcripts_dir": str(transcripts_dir),
            "sessions_analyzed": 0,
        }
        if args.json:
            print(json.dumps(message, indent=2))
        else:
            print("Transcript directory not found: %s" % transcripts_dir)
        return 0

    sessions = [analyze_session(path) for path in sessions_files]
    summary = summarize(sessions, transcripts_dir, args.last)
    payload = {"summary": summary, "sessions": sessions}

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    if not sessions:
        print("=== CACHE AUDIT (last 0 sessions) ===")
        print()
        print("0 cache events")
        return 0

    selected_view = any([args.breakpoints, args.hit_rate, args.breakdown])
    if not selected_view:
        print_summary_table(sessions, summary)
        return 0

    if args.hit_rate:
        print_hit_rate(summary)
        print()
    if args.breakdown:
        print_breakdown(sessions)
        print()
    if args.breakpoints:
        print_breakpoints(sessions)
    return 0


if __name__ == "__main__":
    sys.exit(main())
