#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Memory Manager -- persistent build context + entity memory.

Tracks builder performance per kind, aggregates learning records,
provides build-time memory injection, and maintains entity memory
for recurring patterns and decisions.

Usage:
    python cex_memory.py --status                  # Overview
    python cex_memory.py --kind agent              # Kind-specific memory
    python cex_memory.py --aggregate               # Aggregate learning records
    python cex_memory.py --inject agent            # Get injection context for a kind
    python cex_memory.py --prune --before 2026-03  # Prune old records
"""

import argparse
import json
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter

CEX_ROOT = Path(__file__).resolve().parent.parent
LEARNING_DIR = CEX_ROOT / ".cex" / "learning_records"
MEMORY_DIR = CEX_ROOT / ".cex" / "memory"
ENTITY_DB = MEMORY_DIR / "entity_memory.json"
SUMMARY_DB = MEMORY_DIR / "build_summary.json"
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"


# ---------------------------------------------------------------------------
# Data Types
# ---------------------------------------------------------------------------


@dataclass
class MemoryHeader:
    """Lightweight reference to a single observation in a builder memory file."""

    path: str
    builder_id: str
    observation_preview: str
    type: str  # user | feedback | project | reference
    confidence: float
    outcome: str
    date: str


# ---------------------------------------------------------------------------
# Builder Memory Scanner (Phase 1A -- Runtime Evolution)
# ---------------------------------------------------------------------------


def _parse_memory_observations(content: str, path: str, builder_id: str) -> list[MemoryHeader]:
    """Parse a bld_memory file into individual MemoryHeader entries.

    bld_memory files have frontmatter with observation/pattern/evidence/confidence/outcome
    fields. Some may also have structured body sections with multiple observations.
    """
    fm = parse_frontmatter(content)
    if not fm:
        return []

    headers = []

    # Primary observation from frontmatter
    obs = fm.get("observation", "")
    conf = float(fm.get("confidence", 0.0))
    outcome = str(fm.get("outcome", "UNKNOWN"))
    obs_type = str(fm.get("memory_scope", "project"))
    date = str(fm.get("updated", fm.get("created", "")))

    if obs and conf >= 0.3:
        preview = obs[:120] + "..." if len(obs) > 120 else obs
        headers.append(MemoryHeader(
            path=path,
            builder_id=builder_id,
            observation_preview=preview,
            type=obs_type,
            confidence=conf,
            outcome=outcome,
            date=date,
        ))

    # Scan body for additional structured observations (## Observation N patterns)
    body_match = re.match(r'^---\n.*?\n---\s*', content, re.DOTALL)
    if body_match:
        body = content[body_match.end():]
        # Look for pattern/anti-pattern sections as additional observations
        for section_match in re.finditer(
            r'##\s+(Pattern|Anti-Pattern|Context|Impact)\s*\n(.*?)(?=\n##|\Z)',
            body, re.DOTALL
        ):
            section_type = section_match.group(1).lower().replace("-", "")
            section_text = section_match.group(2).strip()
            if len(section_text) > 30:
                preview = section_text[:120] + "..." if len(section_text) > 120 else section_text
                # Derived observations get slightly lower confidence
                derived_conf = max(conf * 0.8, 0.3)
                headers.append(MemoryHeader(
                    path=path,
                    builder_id=builder_id,
                    observation_preview=f"[{section_type}] {preview}",
                    type=obs_type,
                    confidence=derived_conf,
                    outcome=outcome,
                    date=date,
                ))

    return headers


def scan_builder_memories(builder_id: str) -> list[MemoryHeader]:
    """Scan a single builder's bld_memory file and return observation headers.

    Args:
        builder_id: e.g. "agent-builder"

    Returns:
        List of MemoryHeader sorted by confidence DESC. Only conf >= 0.3.
    """
    builder_path = BUILDER_DIR / builder_id
    if not builder_path.exists():
        return []

    # Find bld_memory file
    memory_files = list(builder_path.glob("bld_memory_*.md"))
    if not memory_files:
        return []

    headers = []
    for mf in memory_files:
        try:
            content = mf.read_text(encoding="utf-8")
            rel_path = str(mf.relative_to(CEX_ROOT))
            headers.extend(_parse_memory_observations(content, rel_path, builder_id))
        except (OSError, UnicodeDecodeError):
            continue

    # Sort by confidence DESC
    headers.sort(key=lambda h: -h.confidence)
    return headers


def scan_all_memories() -> list[MemoryHeader]:
    """Scan ALL builder memory files across all 104 builders.

    Returns:
        Merged list of MemoryHeader sorted by confidence DESC.
    """
    if not BUILDER_DIR.exists():
        return []

    all_headers = []
    for builder_dir in sorted(BUILDER_DIR.iterdir()):
        if not builder_dir.is_dir() or builder_dir.name.startswith("."):
            continue
        builder_id = builder_dir.name
        all_headers.extend(scan_builder_memories(builder_id))

    all_headers.sort(key=lambda h: -h.confidence)
    return all_headers


# ---------------------------------------------------------------------------
# Learning Record Loading
# ---------------------------------------------------------------------------


def load_learning_records() -> list[dict]:
    """Load all learning record JSON files."""
    if not LEARNING_DIR.exists():
        return []
    records = []
    for f in sorted(LEARNING_DIR.glob("*.json")):
        try:
            records.append(json.loads(f.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
    return records


# ---------------------------------------------------------------------------
# Entity Memory (per-kind performance tracking)
# ---------------------------------------------------------------------------


def build_entity_memory(records: list[dict]) -> dict:
    """Build entity memory from learning records.

    Tracks per-kind: success rate, common failures, avg retries,
    best/worst builds, timing trends.
    """
    entities: dict[str, dict] = defaultdict(lambda: {
        "builds": 0, "passed": 0, "failed": 0,
        "retries_total": 0, "times_ms": [],
        "gate_failures": Counter(),
        "last_build": "",
        "best_score": 0.0,
    })

    for rec in records:
        kind = rec.get("kind", "unknown")
        e = entities[kind]
        e["builds"] += 1

        verdict = rec.get("verdict", {})
        if verdict.get("passed"):
            e["passed"] += 1
        else:
            e["failed"] += 1
            for issue in verdict.get("issues", []):
                # Extract gate code (H01, H02, etc.)
                gate = issue[:3] if issue[:1] == "H" else issue[:20]
                e["gate_failures"][gate] += 1

        e["retries_total"] += verdict.get("retries", 0)

        total_ms = sum(rec.get("timings", {}).values())
        if total_ms > 0:
            e["times_ms"].append(total_ms)

        ts = rec.get("timestamp", "")
        if ts > e["last_build"]:
            e["last_build"] = ts

    # Finalize
    result = {}
    for kind, e in entities.items():
        avg_retries = e["retries_total"] / e["builds"] if e["builds"] else 0
        avg_time = sum(e["times_ms"]) / len(e["times_ms"]) if e["times_ms"] else 0
        pass_rate = e["passed"] / e["builds"] if e["builds"] else 0

        result[kind] = {
            "builds": e["builds"],
            "pass_rate": round(pass_rate, 3),
            "avg_retries": round(avg_retries, 2),
            "avg_time_ms": round(avg_time, 0),
            "top_failures": dict(e["gate_failures"].most_common(3)),
            "last_build": e["last_build"],
        }

    return result


def save_entity_memory(entities: dict):
    """Persist entity memory to disk."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    ENTITY_DB.write_text(
        json.dumps(entities, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def load_entity_memory() -> dict:
    """Load entity memory from disk."""
    if ENTITY_DB.exists():
        try:
            return json.loads(ENTITY_DB.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


# ---------------------------------------------------------------------------
# Build Summary (aggregate metrics)
# ---------------------------------------------------------------------------


def build_summary(records: list[dict]) -> dict:
    """Generate aggregate build summary."""
    if not records:
        return {"total": 0}

    total = len(records)
    passed = sum(1 for r in records if r.get("verdict", {}).get("passed"))
    kinds_seen = set(r.get("kind", "") for r in records)

    # Timing stats
    times = []
    for r in records:
        t = sum(r.get("timings", {}).values())
        if t > 0:
            times.append(t)

    avg_time = sum(times) / len(times) if times else 0
    retries = sum(r.get("verdict", {}).get("retries", 0) for r in records)

    # Recent trend (last 20 builds)
    recent = records[-20:]
    recent_pass = sum(1 for r in recent if r.get("verdict", {}).get("passed"))

    return {
        "total": total,
        "passed": passed,
        "failed": total - passed,
        "pass_rate": round(passed / total, 3) if total else 0,
        "kinds_seen": len(kinds_seen),
        "avg_time_ms": round(avg_time, 0),
        "total_retries": retries,
        "avg_retries": round(retries / total, 2) if total else 0,
        "recent_pass_rate": round(recent_pass / len(recent), 3) if recent else 0,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }


def save_summary(summary: dict):
    """Persist build summary."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_DB.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Memory Injection (for F3 INJECT)
# ---------------------------------------------------------------------------


def get_injection_context(kind: str) -> str:
    """Generate memory injection context for a specific kind build.

    Returns a structured text block that can be injected into F3.
    Contains: pass rate, common failures, retry patterns, timing hints.
    """
    entities = load_entity_memory()
    entity = entities.get(kind)

    if not entity:
        return f"No build history for kind '{kind}'. First build -- follow instruction closely."

    parts = [f"## Build Memory: {kind}"]
    parts.append(f"- Builds: {entity['builds']} total, {entity['pass_rate']:.0%} pass rate")
    parts.append(f"- Avg retries: {entity['avg_retries']:.1f}, Avg time: {entity['avg_time_ms']:.0f}ms")

    if entity.get("top_failures"):
        parts.append("- Top failure patterns:")
        for gate, count in entity["top_failures"].items():
            parts.append(f"  - {gate}: {count}x")

    # Actionable advice based on patterns
    if entity["pass_rate"] < 0.5:
        parts.append("- WARNING: Low pass rate. Pay extra attention to frontmatter structure.")
    if entity["avg_retries"] > 1.0:
        parts.append("- NOTE: High retry rate. Check H01 (YAML parse) and H03 (kind match) first.")
    if entity["pass_rate"] >= 0.9:
        parts.append("- This kind has high success rate. Standard procedure applies.")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Pruning
# ---------------------------------------------------------------------------


def prune_records(before: str, dry_run: bool = False) -> int:
    """Remove learning records older than the given date prefix."""
    if not LEARNING_DIR.exists():
        return 0

    count = 0
    for f in sorted(LEARNING_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            ts = data.get("timestamp", "")
            if ts < before:
                if not dry_run:
                    f.unlink()
                count += 1
        except (json.JSONDecodeError, OSError):
            continue
    return count


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Memory Manager -- persistent build context")
    parser.add_argument("--status", action="store_true", help="Show memory overview")
    parser.add_argument("--kind", "-k", help="Show memory for specific kind")
    parser.add_argument("--aggregate", action="store_true", help="Aggregate learning records -> entity memory")
    parser.add_argument("--inject", help="Get injection context for a kind")
    parser.add_argument("--scan", help="Scan builder memories (builder-id or 'all')")
    parser.add_argument("--prune", action="store_true", help="Prune old learning records")
    parser.add_argument("--before", help="Prune records before this date (e.g. 2026-03)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without modifying")
    args = parser.parse_args()

    if args.aggregate:
        records = load_learning_records()
        entities = build_entity_memory(records)
        save_entity_memory(entities)
        summary = build_summary(records)
        save_summary(summary)
        print(f"  Aggregated {len(records)} records -> {len(entities)} entity memories")
        print(f"  Pass rate: {summary.get('pass_rate', 0):.0%}")
        print(f"  Saved to: {MEMORY_DIR}")
        return

    if args.status:
        records = load_learning_records()
        summary = build_summary(records)
        entities = load_entity_memory()

        print("\n=== CEX Memory Status ===")
        print(f"  Learning records: {summary['total']}")
        print(f"  Pass rate:        {summary.get('pass_rate', 0):.0%}")
        print(f"  Kinds tracked:    {summary.get('kinds_seen', 0)}")
        print(f"  Entity memories:  {len(entities)}")
        print(f"  Avg time:         {summary.get('avg_time_ms', 0):.0f}ms")
        print(f"  Total retries:    {summary.get('total_retries', 0)}")

        if entities:
            print("\n  Top entities (by builds):")
            sorted_e = sorted(entities.items(), key=lambda x: -x[1].get("builds", 0))
            for kind, e in sorted_e[:10]:
                print(f"    {kind:25s} {e['builds']:>4d} builds  {e['pass_rate']:.0%} pass")
        return

    if args.kind:
        entities = load_entity_memory()
        entity = entities.get(args.kind)
        if not entity:
            print(f"No memory for kind '{args.kind}'")
            # Try to build from records
            records = load_learning_records()
            kind_records = [r for r in records if r.get("kind") == args.kind]
            if kind_records:
                print(f"  Found {len(kind_records)} learning record(s). Run --aggregate first.")
            sys.exit(1)

        print(f"\n=== Entity Memory: {args.kind} ===")
        print(f"  Builds:       {entity['builds']}")
        print(f"  Pass rate:    {entity['pass_rate']:.0%}")
        print(f"  Avg retries:  {entity['avg_retries']:.1f}")
        print(f"  Avg time:     {entity['avg_time_ms']:.0f}ms")
        print(f"  Last build:   {entity.get('last_build', '?')}")
        if entity.get("top_failures"):
            print("  Top failures:")
            for gate, count in entity["top_failures"].items():
                print(f"    {gate}: {count}x")
        return

    if args.inject:
        print(get_injection_context(args.inject))
        return

    if args.scan:
        if args.scan == "all":
            headers = scan_all_memories()
            print(f"\n=== All Builder Memories ({len(headers)} observations) ===")
        else:
            headers = scan_builder_memories(args.scan)
            print(f"\n=== Builder Memories: {args.scan} ({len(headers)} observations) ===")
        for h in headers[:20]:  # Show top 20
            print(f"  [{h.type:10s} conf={h.confidence:.2f} {h.outcome:7s}] {h.observation_preview}")
        if len(headers) > 20:
            print(f"  ... and {len(headers) - 20} more")
        return

    if args.prune:
        if not args.before:
            print("Specify --before DATE (e.g. --before 2026-03)")
            sys.exit(1)
        count = prune_records(args.before, dry_run=args.dry_run)
        mode = "DRY-RUN" if args.dry_run else "PRUNED"
        print(f"  {mode}: {count} record(s) before {args.before}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
