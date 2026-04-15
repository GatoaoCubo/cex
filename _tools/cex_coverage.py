#!/usr/bin/env python3
"""cex_coverage.py: Artifact coverage by pillar/kind for N05 ops.

Measures what % of kinds in kinds_meta.json have at least one built artifact.
Reports gaps so N05 can drive backfill.

Usage:
    python _tools/cex_coverage.py
    python _tools/cex_coverage.py --pillar P03
    python _tools/cex_coverage.py --json
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS_META = ROOT / ".cex" / "kinds_meta.json"


def load_kinds() -> dict:
    if not KINDS_META.exists():
        return {}
    return json.loads(KINDS_META.read_text(encoding="utf-8"))


def find_artifacts_for_kind(kind: str, naming_pattern: str) -> list[Path]:
    prefix = naming_pattern.split("{")[0].rstrip("_") if naming_pattern else kind
    hits = []
    for p in ROOT.rglob(f"*{prefix}*.md"):
        if ".cex/runtime" in p.as_posix() or "/archetypes/" in p.as_posix():
            continue
        hits.append(p)
    return hits


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--pillar", help="filter by pillar (e.g. P03)")
    p.add_argument("--json", action="store_true")
    p.add_argument("--top-gaps", type=int, default=20)
    args = p.parse_args()

    kinds = load_kinds()
    if not kinds:
        print(f"ERROR: {KINDS_META} missing or empty", file=sys.stderr)
        return 1

    pillar_stats = defaultdict(lambda: {"total": 0, "covered": 0, "gaps": []})
    for kind, meta in kinds.items():
        pillar = meta.get("pillar", "?")
        if args.pillar and pillar != args.pillar:
            continue
        naming = meta.get("naming", "")
        artifacts = find_artifacts_for_kind(kind, naming)
        pillar_stats[pillar]["total"] += 1
        if artifacts:
            pillar_stats[pillar]["covered"] += 1
        else:
            pillar_stats[pillar]["gaps"].append(kind)

    result = {}
    for pillar, stats in sorted(pillar_stats.items()):
        pct = (stats["covered"] / stats["total"] * 100) if stats["total"] else 0
        result[pillar] = {
            "total_kinds": stats["total"],
            "covered": stats["covered"],
            "coverage_pct": round(pct, 1),
            "gap_count": len(stats["gaps"]),
            "gaps": stats["gaps"][:args.top_gaps],
        }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{'Pillar':<8} {'Kinds':<8} {'Covered':<10} {'Coverage':<10} {'Gaps':<8}")
        print("-" * 50)
        for pillar, r in result.items():
            print(f"{pillar:<8} {r['total_kinds']:<8} {r['covered']:<10} {r['coverage_pct']:<10.1f} {r['gap_count']:<8}")
        print()
        for pillar, r in result.items():
            if r["gaps"]:
                print(f"{pillar} gaps ({len(r['gaps'])}): {', '.join(r['gaps'][:10])}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
