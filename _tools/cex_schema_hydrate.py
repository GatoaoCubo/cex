#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_schema_hydrate.py -- Hydrate builder specs with universal schema fields.

Adds 8 universal patterns to all builders:
  - bld_model: keywords, triggers, capabilities (frontmatter)
  - bld_memory: memory_scope, observation_types (frontmatter)
  - bld_config: effort, max_turns, disallowed_tools, fork_context, hooks, permission_scope
  - bld_tools: ## Tool Permissions section

Usage:
    python _tools/cex_schema_hydrate.py --dry-run --stats
    python _tools/cex_schema_hydrate.py --apply --stats
    python _tools/cex_schema_hydrate.py --apply --builders agent-builder signal-builder
    python _tools/cex_schema_hydrate.py --apply --iso manifest
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# ---------------------------------------------------------------------------
# Overrides (15 builders with non-default values)
# ---------------------------------------------------------------------------

OVERRIDES: dict[str, dict] = {
    "_builder-builder": {"effort": "high", "disallowed_tools": [], "fork_context": None, "permission_scope": "global"},
    "research-pipeline-builder": {"effort": "high", "disallowed_tools": ["Write", "Edit"], "fork_context": "fork", "permission_scope": "nucleus"},
    "system-prompt-builder": {"effort": "medium", "disallowed_tools": ["BashTool"], "fork_context": "inline", "permission_scope": "pillar"},
    "output-validator-builder": {"effort": "low", "disallowed_tools": ["Write", "BashTool"], "fork_context": "inline", "permission_scope": "restricted"},
    "agent-builder": {"effort": "high", "disallowed_tools": [], "fork_context": None, "permission_scope": "pillar"},
    "knowledge-card-builder": {"effort": "medium", "disallowed_tools": [], "fork_context": "fork", "permission_scope": "nucleus"},
    "model-card-builder": {"effort": "low", "disallowed_tools": [], "fork_context": "inline", "permission_scope": "nucleus"},
    "benchmark-builder": {"effort": "high", "disallowed_tools": [], "fork_context": "fork", "permission_scope": "nucleus"},
    "content-monetization-builder": {"effort": "high", "disallowed_tools": [], "fork_context": None, "permission_scope": "nucleus"},
    "supabase-data-layer-builder": {"effort": "high", "disallowed_tools": [], "fork_context": None, "permission_scope": "nucleus"},
    "social-publisher-builder": {"effort": "medium", "disallowed_tools": [], "fork_context": None, "permission_scope": "nucleus"},
    "workflow-builder": {"effort": "high", "disallowed_tools": [], "fork_context": None, "permission_scope": "pillar"},
    "chain-builder": {"effort": "medium", "disallowed_tools": [], "fork_context": "inline", "permission_scope": "pillar"},
    "knowledge-index-builder": {"effort": "high", "disallowed_tools": [], "fork_context": "fork", "permission_scope": "global"},
    "bugloop-builder": {"effort": "medium", "disallowed_tools": [], "fork_context": "fork", "permission_scope": "nucleus"},
}

DEFAULTS = {
    "effort": "medium",
    "max_turns": 25,
    "disallowed_tools": [],
    "fork_context": None,
    "hooks": {"pre_build": None, "post_build": None, "on_error": None, "on_quality_fail": None},
    "permission_scope": "nucleus",
}

# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def split_fm(content: str) -> tuple[dict, str, str]:
    """Split into (frontmatter_dict, raw_fm_string, body).
    Returns ({}, '', content) if no frontmatter found."""
    m = FM_RE.match(content)
    if not m:
        return {}, "", content
    raw = m.group(1)
    body = content[m.end():]
    try:
        fm = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return {}, raw, body
    return fm, raw, body


def insert_fm_fields(raw_fm: str, new_fields: dict) -> str:
    """Insert new YAML fields at end of raw frontmatter string.
    Only adds fields not already present."""
    lines = raw_fm.rstrip().split("\n")
    additions = []
    existing_keys = set()
    for line in lines:
        key_match = re.match(r"^(\w[\w_]*):", line)
        if key_match:
            existing_keys.add(key_match.group(1))

    for key, val in new_fields.items():
        if key in existing_keys:
            continue
        additions.append(yaml_field(key, val))

    if not additions:
        return raw_fm
    return raw_fm.rstrip() + "\n" + "\n".join(additions)


def yaml_field(key: str, val) -> str:
    """Serialize a single YAML field line (or block for dicts/lists)."""
    if val is None:
        return f"{key}: null"
    if isinstance(val, bool):
        return f"{key}: {'true' if val else 'false'}"
    if isinstance(val, int):
        return f"{key}: {val}"
    if isinstance(val, str):
        if "\n" in val or len(val) > 80:
            return f"{key}: >\n  {val.strip()}"
        return f"{key}: {val}"
    if isinstance(val, list):
        if not val:
            return f"{key}: []"
        items = ", ".join(_yaml_scalar(v) for v in val)
        return f"{key}: [{items}]"
    if isinstance(val, dict):
        sub = "\n".join(f"  {k}: {_yaml_scalar(v)}" for k, v in val.items())
        return f"{key}:\n{sub}"
    return f"{key}: {val}"


def _yaml_scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, str):
        # Quote if contains special chars or spaces (safer for triggers/keywords)
        if any(c in v for c in "[]{},:\"' "):
            escaped = v.replace('"', '\\"')
            return f'"{escaped}"'
        return v
    return str(v)


def reassemble(raw_fm: str, body: str) -> str:
    """Reassemble frontmatter + body into complete file."""
    return f"---\n{raw_fm.strip()}\n---\n{body}"


# ---------------------------------------------------------------------------
# Extraction from body
# ---------------------------------------------------------------------------

KW_RE = re.compile(r"keywords:\s*\[([^\]]*)\]", re.IGNORECASE)
TRIGGER_RE = re.compile(r'triggers?:\s*(.+)', re.IGNORECASE)


def extract_keywords_from_body(body: str) -> list[str]:
    """Extract keywords list from ## Routing section in body."""
    m = KW_RE.search(body)
    if not m:
        return []
    raw = m.group(1)
    items = [w.strip().strip("'\"") for w in raw.split(",") if w.strip()]
    return items[:10]


def extract_triggers_from_body(body: str) -> list[str]:
    """Extract trigger phrases from ## Routing section."""
    m = TRIGGER_RE.search(body)
    if not m:
        return []
    raw = m.group(1)
    parts = re.findall(r'"([^"]+)"', raw)
    if not parts:
        parts = [s.strip().strip("'\"") for s in raw.split(",") if s.strip()]
    return parts[:6]


def generate_capabilities(fm: dict, body: str) -> str:
    """Generate 3-layer capabilities from manifest content."""
    kind = fm.get("domain", fm.get("id", "unknown")).replace("-builder", "").replace("-", "_")
    identity = ""
    caps = ""
    for line in body.split("\n"):
        if line.startswith("## Identity"):
            identity = ""
        elif identity == "" and line.strip() and not line.startswith("#") and not line.startswith("<!--"):
            identity = line.strip()
        if line.startswith("## Capabilities"):
            caps = ""
        elif caps == "" and line.strip().startswith("- ") and not line.startswith("<!--"):
            caps = line.strip("- ").strip()

    l1 = identity if identity else f"Builds {kind} artifacts"
    l2 = caps if caps else "Via 8F pipeline with schema validation"
    l3 = f"When user needs to create, build, or scaffold {kind.replace('_', ' ')}"

    desc = f"L1: {l1[:80]}. L2: {l2[:80]}. L3: {l3[:80]}."
    return desc


# ---------------------------------------------------------------------------
# Hydrators (one per spec type)
# ---------------------------------------------------------------------------

class Stats:
    def __init__(self):
        self.manifests = 0
        self.memories = 0
        self.configs = 0
        self.tools = 0
        self.skipped = 0
        self.errors: list[str] = []

    def summary(self) -> str:
        return (
            f"Manifests: {self.manifests} | Memories: {self.memories} | "
            f"Configs: {self.configs} | Tools: {self.tools} | "
            f"Skipped: {self.skipped} | Errors: {len(self.errors)}"
        )


def hydrate_manifest(path: Path, dry_run: bool, stats: Stats) -> bool:
    """Add keywords, triggers, capabilities to manifest frontmatter."""
    content = path.read_text(encoding="utf-8")
    fm, raw_fm, body = split_fm(content)
    if not fm:
        stats.errors.append(f"No frontmatter: {path.name}")
        return False

    keywords = fm.get("keywords")
    triggers = fm.get("triggers")
    geo = fm.get("capabilities")

    if keywords and triggers and geo:
        stats.skipped += 1
        return False

    new_fields = {}
    if not keywords:
        kw = extract_keywords_from_body(body)
        if len(kw) < 3:
            domain = fm.get("domain", "").replace("_", " ")
            tags = fm.get("tags", [])
            kw_set = set(kw)
            for t in tags:
                if t not in ("kind-builder", "specialist") and t not in kw_set:
                    kw_set.add(t)
            kw = list(kw_set)[:8]
            if domain and domain not in kw:
                kw.insert(0, domain)
        new_fields["keywords"] = kw[:8]

    if not triggers:
        tr = extract_triggers_from_body(body)
        if len(tr) < 2:
            domain = fm.get("domain", "").replace("_", " ")
            tr = [f"create {domain}", f"build {domain} artifact"]
        new_fields["triggers"] = tr[:4]

    if not geo:
        new_fields["capabilities"] = generate_capabilities(fm, body)

    if not new_fields:
        stats.skipped += 1
        return False

    updated_fm = insert_fm_fields(raw_fm, new_fields)
    result = reassemble(updated_fm, body)

    if not dry_run:
        path.write_text(result, encoding="utf-8")

    stats.manifests += 1
    return True


def hydrate_memory(path: Path, dry_run: bool, stats: Stats) -> bool:
    """Add memory_scope, observation_types to memory frontmatter."""
    content = path.read_text(encoding="utf-8")
    fm, raw_fm, body = split_fm(content)
    if not fm:
        stats.errors.append(f"No frontmatter: {path.name}")
        return False

    has_scope = "memory_scope" in fm
    has_obs = "observation_types" in fm

    if has_scope and has_obs:
        stats.skipped += 1
        return False

    new_fields = {}
    if not has_scope:
        new_fields["memory_scope"] = "project"
    if not has_obs:
        new_fields["observation_types"] = ["user", "feedback", "project", "reference"]

    updated_fm = insert_fm_fields(raw_fm, new_fields)
    result = reassemble(updated_fm, body)

    if not dry_run:
        path.write_text(result, encoding="utf-8")

    stats.memories += 1
    return True


def hydrate_config(path: Path, builder_name: str, dry_run: bool, stats: Stats) -> bool:
    """Add effort, max_turns, disallowed_tools, fork_context, hooks, permission_scope."""
    content = path.read_text(encoding="utf-8")
    fm, raw_fm, body = split_fm(content)
    if not fm:
        stats.errors.append(f"No frontmatter: {path.name}")
        return False

    overrides = OVERRIDES.get(builder_name, {})
    fields_to_add = {}

    for key in ("effort", "max_turns", "disallowed_tools", "fork_context", "hooks", "permission_scope"):
        if key not in fm:
            val = overrides.get(key, DEFAULTS[key])
            fields_to_add[key] = val

    if not fields_to_add:
        stats.skipped += 1
        return False

    updated_fm = insert_fm_fields(raw_fm, fields_to_add)
    result = reassemble(updated_fm, body)

    if not dry_run:
        path.write_text(result, encoding="utf-8")

    stats.configs += 1
    return True


TOOL_PERMISSIONS_SECTION = """
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | {denied} | Explicitly blocked |
| EFFECTIVE | {effective} | ALLOWED minus DENIED |
"""


def hydrate_tools(path: Path, builder_name: str, dry_run: bool, stats: Stats) -> bool:
    """Add ## Tool Permissions section to tools file."""
    content = path.read_text(encoding="utf-8")

    if "## Tool Permissions" in content:
        stats.skipped += 1
        return False

    overrides = OVERRIDES.get(builder_name, {})
    denied = overrides.get("disallowed_tools", [])
    denied_str = ", ".join(denied) if denied else "(none)"

    base_tools = {"Read", "Write", "Edit", "Bash", "Glob", "Grep"}
    effective = sorted(base_tools - set(denied))
    effective_str = ", ".join(effective)

    section = TOOL_PERMISSIONS_SECTION.format(denied=denied_str, effective=effective_str).strip()

    # Insert before ## Interim Validation if exists, else append
    if "## Interim Validation" in content:
        content = content.replace("## Interim Validation", f"{section}\n\n## Interim Validation")
    else:
        content = content.rstrip() + "\n\n" + section + "\n"

    if not dry_run:
        path.write_text(content, encoding="utf-8")

    stats.tools += 1
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def discover_builders(filter_list: list[str] | None = None) -> list[Path]:
    """Discover all builder directories."""
    dirs = []
    for d in sorted(BUILDER_DIR.iterdir()):
        if not d.is_dir():
            continue
        if d.name == "bld_norms.md":
            continue
        if filter_list and d.name not in filter_list:
            continue
        dirs.append(d)
    return dirs


def find_iso(builder_dir: Path, prefix: str) -> Path | None:
    """Find an builder spec by prefix in a builder directory."""
    candidates = list(builder_dir.glob(f"{prefix}_*.md"))
    # For _builder-builder, skip meta files
    if builder_dir.name == "_builder-builder":
        candidates = [c for c in candidates if "meta" not in c.name]
    return candidates[0] if candidates else None


def run(args: argparse.Namespace) -> int:
    builders = discover_builders(args.builders if args.builders else None)
    iso_filter = set(args.iso) if args.iso else {"manifest", "memory", "config", "tools"}

    stats = Stats()
    changes: list[str] = []

    for bdir in builders:
        name = bdir.name

        if "manifest" in iso_filter or "model" in iso_filter:
            mp = find_iso(bdir, "bld_model")
            if mp and hydrate_manifest(mp, args.dry_run, stats):
                changes.append(f"  manifest: {mp.name}")

        if "memory" in iso_filter:
            mp = find_iso(bdir, "bld_memory")
            if mp and hydrate_memory(mp, args.dry_run, stats):
                changes.append(f"  memory:   {mp.name}")

        if "config" in iso_filter:
            mp = find_iso(bdir, "bld_config")
            if mp and hydrate_config(mp, name, args.dry_run, stats):
                changes.append(f"  config:   {mp.name}")

        if "tools" in iso_filter:
            mp = find_iso(bdir, "bld_tools")
            if mp and hydrate_tools(mp, name, args.dry_run, stats):
                changes.append(f"  tools:    {mp.name}")

    mode = "DRY-RUN" if args.dry_run else "APPLIED"
    print(f"\n=== Schema Hydration [{mode}] ===")
    print(f"Builders scanned: {len(builders)}")
    print(f"Stats: {stats.summary()}")

    if args.stats and changes:
        print(f"\nChanges ({len(changes)}):")
        for c in changes:
            print(c)

    if stats.errors:
        print(f"\nErrors ({len(stats.errors)}):")
        for e in stats.errors:
            print(f"  {e}")

    return 0 if not stats.errors else 1


def main():
    p = argparse.ArgumentParser(description="Hydrate builders with universal schema fields")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    mode.add_argument("--apply", action="store_true", help="Apply changes to files")
    p.add_argument("--builders", nargs="+", help="Specific builder dirs to process")
    p.add_argument("--iso", nargs="+", choices=["manifest", "memory", "config", "tools"],
                   help="Specific spec types to process")
    p.add_argument("--stats", action="store_true", help="Show detailed change list")

    args = p.parse_args()
    sys.exit(run(args))


if __name__ == "__main__":
    main()
