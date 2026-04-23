"""cex_capability_index.py -- build the capability_registry for composable crews.

Scans the full CEX agent pool (3 sources) and emits a single registry JSON
that any nucleus can query to assemble a crew:

  1. .claude/P02_model/*.md            Claude Code-spawnable sub-agents (builders)
  2. N0{1..7}_*/P02_model/*.md         Nucleus domain agents (non-builder)
  3. N0{1..7}_*/agent_card_*.md     Nucleus-level agent cards (A2A)

Output: .cex/P09_config/capability_registry.json

Fields per entry:
  - id: canonical ID
  - name: display name
  - source: "builder_subagent" | "domain_agent" | "nucleus_card"
  - path: relative path from repo root
  - nucleus: owning nucleus (n01..n07) or null
  - kind: artifact kind (for builders: the kind they build)
  - domain: capability domain
  - capabilities: list[str] (from frontmatter or body)
  - tools_allowed: list[str]
  - model_tier: "opus" | "sonnet" | "haiku" | "local" | null
  - description: one-liner

Usage:
  python _tools/cex_capability_index.py            # build + write
  python _tools/cex_capability_index.py --dry-run  # print counts
  python _tools/cex_capability_index.py --query kw # filter by keyword
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / ".cex" / "config" / "capability_registry.json"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_fm(text: str) -> dict:
    """Minimal YAML frontmatter parser (no external dep)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm: dict = {}
    key = None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and key:
            val = line[4:].strip().strip('"').strip("'")
            fm.setdefault(key, []).append(val) if isinstance(
                fm.get(key), list
            ) else fm.update({key: [val]})
        elif ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            key = k
            if not v:
                fm[k] = []
            else:
                fm[k] = v.strip('"').strip("'")
    return fm


def scan_builder_subagents() -> list[dict]:
    """Parse .claude/P02_model/*.md (builder sub-agents)."""
    entries: list[dict] = []
    for p in sorted((ROOT / ".claude" / "agents").glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_fm(text)
        name = fm.get("name", p.stem)
        kind = name.replace("-builder", "").replace("-", "_") if name.endswith(
            "-builder"
        ) else None
        tools = fm.get("tools", "")
        tools_list = [t.strip() for t in tools.split(",")] if isinstance(
            tools, str
        ) else tools if isinstance(tools, list) else []
        entries.append({
            "id": p.stem,
            "name": name,
            "source": "builder_subagent",
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "nucleus": None,
            "kind": kind,
            "domain": "artifact-generation",
            "capabilities": [f"builds {kind}"] if kind else [],
            "tools_allowed": tools_list,
            "model_tier": fm.get("model", "sonnet"),
            "description": fm.get("description", ""),
        })
    return entries


def scan_domain_agents() -> list[dict]:
    """Parse N0x/P02_model/agent_*.md (nucleus domain agents)."""
    entries: list[dict] = []
    for nuc_dir in sorted(ROOT.glob("N0*_*")):
        agents_dir = nuc_dir / "agents"
        if not agents_dir.is_dir():
            continue
        nucleus = nuc_dir.name[:3].lower()  # n01..n07
        for p in sorted(agents_dir.glob("agent_*.md")):
            text = p.read_text(encoding="utf-8", errors="replace")
            fm = parse_fm(text)
            caps = fm.get("capabilities", [])
            if isinstance(caps, str):
                caps = [caps]
            tools = fm.get("tools", [])
            if isinstance(tools, str):
                tools = [t.strip() for t in tools.split(",")]
            entries.append({
                "id": fm.get("id", p.stem),
                "name": fm.get("title", p.stem),
                "source": "domain_agent",
                "path": str(p.relative_to(ROOT)).replace("\\", "/"),
                "nucleus": nucleus,
                "kind": fm.get("kind", "agent"),
                "domain": fm.get("domain", "unknown"),
                "capabilities": caps,
                "tools_allowed": tools,
                "model_tier": fm.get("model_tier", None),
                "description": fm.get("title", ""),
            })
    return entries


def scan_nucleus_cards() -> list[dict]:
    """Parse N0x/agent_card_*.md (nucleus-level agent cards)."""
    entries: list[dict] = []
    seen: set[str] = set()
    for p in sorted(ROOT.glob("N0*_*/agent_card_n*.md")):
        # Prefer canonical agent_card_n0X over architecture duplicates
        key = p.name
        if key in seen:
            continue
        seen.add(key)
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_fm(text)
        nuc_match = re.search(r"agent_card_(n0\d)", p.stem)
        nucleus = nuc_match.group(1) if nuc_match else None
        caps = fm.get("capabilities", [])
        if isinstance(caps, str):
            caps = [caps]
        entries.append({
            "id": fm.get("id", p.stem),
            "name": fm.get("title", p.stem),
            "source": "nucleus_card",
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "nucleus": nucleus,
            "kind": "agent_card",
            "domain": fm.get("domain", nucleus or "unknown"),
            "capabilities": caps,
            "tools_allowed": [],
            "model_tier": fm.get("model_tier", None),
            "description": fm.get("tldr", fm.get("title", "")),
        })
    return entries


def scan_role_assignments() -> list[dict]:
    """Parse N0*/P12_orchestration/p02_ra_*.md (role_assignment bindings for composable crews)."""
    entries: list[dict] = []
    for p in sorted(ROOT.glob("N0*_*/P12_orchestration/p02_ra_*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_fm(text)
        nucleus = p.parents[1].name[:3].lower()
        entries.append({
            "id": fm.get("id", p.stem),
            "name": fm.get("title", p.stem),
            "source": "role_assignment",
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "nucleus": nucleus,
            "kind": "role_assignment",
            "domain": fm.get("role_name", "unknown"),
            "capabilities": [fm.get("goal", "")],
            "tools_allowed": fm.get("tools", []) if isinstance(fm.get("tools"), list) else [],
            "agent_id": fm.get("agent_id", ""),
            "description": fm.get("goal", fm.get("title", "")),
        })
    return entries


def scan_crew_templates() -> list[dict]:
    """Parse N0*/P12_orchestration/p12_ct_*.md (crew_template recipes)."""
    entries: list[dict] = []
    for p in sorted(ROOT.glob("N0*_*/P12_orchestration/p12_ct_*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_fm(text)
        nucleus = p.parents[1].name[:3].lower()
        entries.append({
            "id": fm.get("id", p.stem),
            "name": fm.get("title", p.stem),
            "source": "crew_template",
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "nucleus": nucleus,
            "kind": "crew_template",
            "domain": fm.get("crew_name", p.stem),
            "capabilities": [fm.get("purpose", "")],
            "tools_allowed": [],
            "process": fm.get("process", "sequential"),
            "description": fm.get("purpose", fm.get("tldr", "")),
        })
    return entries


def scan_nucleus_defs() -> list[dict]:
    """Parse N0*/P08_architecture/nucleus_def_*.md (machine-readable nucleus identities)."""
    entries: list[dict] = []
    for p in sorted(ROOT.glob("N0*_*/P08_architecture/nucleus_def_*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_fm(text)
        nucleus_id = fm.get("nucleus_id", "").lower() or p.stem[-3:].lower()
        entries.append({
            "id": fm.get("id", p.stem),
            "name": fm.get("title", p.stem),
            "source": "nucleus_de",
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "nucleus": nucleus_id,
            "kind": "nucleus_de",
            "domain": fm.get("role", "unknown"),
            "capabilities": fm.get("crew_templates_exposed", []),
            "tools_allowed": [],
            "model_tier": fm.get("model_tier"),
            "sin_lens": fm.get("sin_lens", ""),
            "description": fm.get("tldr", fm.get("title", "")),
        })
    return entries


def build_registry() -> dict:
    builders = scan_builder_subagents()
    domains = scan_domain_agents()
    cards = scan_nucleus_cards()
    roles = scan_role_assignments()
    crews = scan_crew_templates()
    defs_ = scan_nucleus_defs()
    all_entries = builders + domains + cards + roles + crews + defs_
    # Indexes for fast lookup
    by_kind: dict[str, list[str]] = {}
    by_nucleus: dict[str, list[str]] = {}
    by_domain: dict[str, list[str]] = {}
    for e in all_entries:
        if e.get("kind"):
            by_kind.setdefault(e["kind"], []).append(e["id"])
        if e.get("nucleus"):
            by_nucleus.setdefault(e["nucleus"], []).append(e["id"])
        if e.get("domain"):
            by_domain.setdefault(e["domain"], []).append(e["id"])
    return {
        "version": "1.0",
        "generated": "cex_capability_index.py",
        "counts": {
            "total": len(all_entries),
            "builder_subagent": len(builders),
            "domain_agent": len(domains),
            "nucleus_card": len(cards),
            "role_assignment": len(roles),
            "crew_template": len(crews),
            "nucleus_def": len(defs_),
        },
        "indexes": {
            "by_kind": by_kind,
            "by_nucleus": by_nucleus,
            "by_domain": by_domain,
        },
        "agents": all_entries,
    }


def query(reg: dict, keyword: str) -> list[dict]:
    kw = keyword.lower()
    matches = []
    for a in reg["agents"]:
        hay = " ".join([
            a.get("id", ""),
            a.get("name", ""),
            a.get("domain", ""),
            str(a.get("capabilities", "")),
            a.get("description", ""),
        ]).lower()
        if kw in hay:
            matches.append(a)
    return matches


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Print counts, no write")
    ap.add_argument("--query", help="Filter by keyword across all fields")
    args = ap.parse_args()

    reg = build_registry()

    if args.query:
        matches = query(reg, args.query)
        print(f"[QUERY '{args.query}'] {len(matches)} match(es):")
        for m in matches[:20]:
            print(f"  [{m['source']}] {m['id']:40s} nucleus={m['nucleus'] or '-':4s} tier={m.get('model_tier') or '-'}")
        return 0

    print(f"[INDEX] total={reg['counts']['total']} "
          f"builders={reg['counts']['builder_subagent']} "
          f"domains={reg['counts']['domain_agent']} "
          f"cards={reg['counts']['nucleus_card']} "
          f"roles={reg['counts'].get('role_assignment', 0)} "
          f"crews={reg['counts'].get('crew_template', 0)} "
          f"defs={reg['counts'].get('nucleus_def', 0)}")
    print(f"[INDEX] kinds indexed: {len(reg['indexes']['by_kind'])}")
    print(f"[INDEX] nuclei indexed: {len(reg['indexes']['by_nucleus'])}")

    if args.dry_run:
        return 0

    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(
        json.dumps(reg, ensure_ascii=True, indent=2), encoding="utf-8"
    )
    print(f"[OK] wrote {REGISTRY_PATH.relative_to(ROOT)} ({REGISTRY_PATH.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
