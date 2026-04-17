"""Auto-count repo stats so README badges stop drifting from reality.

Usage:
    python _tools/cex_stats.py            # print table
    python _tools/cex_stats.py --json     # machine-readable

Counts: builders, ISOs, kinds, KCs, sub-agents, CLI tools, pillars, nuclei.
Source of truth for any doc claiming numbers about the repo.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def count_builders() -> int:
    """Directories under archetypes/builders/ ending in -builder."""
    return sum(1 for d in (ROOT / "archetypes" / "builders").iterdir()
               if d.is_dir() and d.name.endswith("-builder"))


def count_isos() -> int:
    """bld_*.md files across all builders (excluding compiled mirrors)."""
    return sum(1 for p in (ROOT / "archetypes" / "builders").rglob("bld_*.md")
               if "compiled" not in p.parts)


def count_kinds() -> int:
    """Entries in .cex/kinds_meta.json."""
    meta = ROOT / ".cex" / "kinds_meta.json"
    if not meta.exists():
        return 0
    return len(json.loads(meta.read_text(encoding="utf-8")))


def count_kcs() -> int:
    """kc_*.md files in P01_knowledge."""
    return sum(1 for _ in (ROOT / "P01_knowledge").rglob("kc_*.md"))


def count_subagents() -> int:
    """.md files under .claude/P02_model/."""
    agents = ROOT / ".claude" / "agents"
    if not agents.exists():
        return 0
    return sum(1 for _ in agents.glob("*.md"))


def count_tools() -> int:
    """cex_*.py files in _tools/ (top-level only)."""
    return sum(1 for _ in (ROOT / "_tools").glob("cex_*.py"))


def count_pillars() -> int:
    return sum(1 for d in ROOT.iterdir()
               if d.is_dir() and d.name.startswith("P") and "_" in d.name)


def count_nuclei() -> int:
    return sum(1 for d in ROOT.iterdir()
               if d.is_dir() and d.name.startswith("N") and "_" in d.name)


def collect() -> dict:
    return {
        "builders": count_builders(),
        "isos": count_isos(),
        "kinds": count_kinds(),
        "knowledge_cards": count_kcs(),
        "sub_agents": count_subagents(),
        "cli_tools": count_tools(),
        "pillars": count_pillars(),
        "nuclei": count_nuclei(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()
    stats = collect()
    if args.json:
        print(json.dumps(stats, indent=2))
        return 0
    width = max(len(k) for k in stats)
    print("CEX repo stats (auto-counted):")
    for k, v in stats.items():
        print(f"  {k:<{width}}  {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
