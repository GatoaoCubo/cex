#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_materialize.py -- Materialize 99 Claude Code sub-agents from kinds_meta.json.

Reads .cex/kinds_meta.json and generates one .claude/P02_model/{kind}-builder.md
file per kind. Each sub-agent is a specialized builder that follows the 8F pipeline.

Preserves manually-authored agents (kind-builder.md, validator.md).

Usage:
  python _tools/cex_materialize.py              # generate all 99
  python _tools/cex_materialize.py --dry-run    # preview without writing
  python _tools/cex_materialize.py --kind agent  # generate one
  python _tools/cex_materialize.py --list        # list all kinds
"""

import argparse
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"
AGENTS_DIR = CEX_ROOT / ".claude" / "agents"

# Files that should NOT be overwritten (manually authored)
PROTECTED = {"kind-builder.md", "validator.md"}


def load_kinds() -> dict:
    """Load kinds_meta.json."""
    with open(KINDS_META, encoding="utf-8") as f:
        return json.load(f)


def kind_to_slug(kind: str) -> str:
    """Convert kind name to slug (underscores to hyphens)."""
    return kind.replace("_", "-")


def generate_agent_md(kind: str, meta: dict) -> str:
    """Generate the .md content for a kind-specific builder sub-agent."""
    slug = kind_to_slug(kind)
    pillar = meta.get("pillar", "P??")
    description = meta.get("description", "")
    llm_function = meta.get("llm_function", "")
    primary_8f = meta.get("primary_8f", "")
    max_bytes = meta.get("max_bytes", 4096)
    naming = meta.get("naming", "")
    boundary = meta.get("boundary", "")

    return '''---
name: {slug}-builder
description: "Builds ONE {kind} artifact via 8F pipeline. Loads {slug}-builder specs. Produces draft with frontmatter + body. Never self-scores quality."
model: sonnet
tools: Read, Write, Edit, Bash, Glob, Grep
---

# {slug}-builder Sub-Agent

You are a specialized builder for **{kind}** artifacts (pillar: {pillar}).

## Kind Definition

| Field | Value |
|-------|-------|
| Kind | `{kind}` |
| Pillar | `{pillar}` |
| LLM Function | `{llm_function}` |
| 8F | `{primary_8f}` |
| Max Bytes | {max_bytes} |
| Naming | `{naming}` |
| Description | {description} |
| Boundary | {boundary} |

## How You Work

1. You receive a **target name/topic** for the artifact
2. You load builder specs from `archetypes/builders/{slug}-builder/`
3. You read these specs in order:
   - `bld_schema_{kind}.md` -- CONSTRAINTS (what fields, what format)
   - `bld_model_{kind}.md` -- IDENTITY (who you become + persona)
   - `bld_prompt_{kind}.md` -- PROCESS (research > compose > validate)
   - `bld_output_{kind}.md` -- TEMPLATE (the shape to fill)
   - `bld_eval_{kind}.md` -- QUALITY + EXAMPLES (gates + what good looks like)
   - `bld_memory_{kind}.md` -- PATTERNS (learned from past builds)
4. You produce the artifact following the template
5. You compile: `python _tools/cex_compile.py {{path}}`

## Rules

- `quality: null` ALWAYS -- never self-score
- `8f:` field MUST be set in frontmatter (value: `{primary_8f}`)
- Frontmatter MUST parse as valid YAML
- Body MUST stay under {max_bytes} bytes
- Follow naming pattern: `{naming}`
- Read existing file first if it exists -- rebuild, don't start from zero
- ONE artifact per invocation -- stay focused

## 8F Trace (show this for every build)

```
F1 CONSTRAIN: kind={kind}, pillar={pillar}, 8f={primary_8f}
F2 BECOME: {slug}-builder specs loaded
F3 INJECT: schema + examples + memory loaded
F4 REASON: plan decided
F5 CALL: tools ready (Read, Write, compile)
F6 PRODUCE: artifact written to {{path}}
F7 GOVERN: gates checked (quality: null)
F8 COLLABORATE: compiled to YAML
```
'''


def materialize(kinds: dict, target_kind: str | None = None, dry_run: bool = False) -> int:
    """Generate sub-agent files. Returns count of files written."""
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    for kind, meta in sorted(kinds.items()):
        if target_kind and kind != target_kind:
            continue

        slug = kind_to_slug(kind)
        filename = f"{slug}-builder.md"

        if filename in PROTECTED:
            print(f"  SKIP {filename} (protected)")
            continue

        filepath = AGENTS_DIR / filename
        content = generate_agent_md(kind, meta)

        if dry_run:
            print(f"  DRY  {filename} ({len(content)} bytes)")
        else:
            filepath.write_text(content, encoding="utf-8")
            print(f"  WRITE {filename} ({len(content)} bytes)")

        count += 1

    return count


def main():
    parser = argparse.ArgumentParser(description="Materialize Claude Code sub-agents from kinds_meta.json")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--kind", type=str, help="Generate only this kind")
    parser.add_argument("--list", action="store_true", help="List all kinds and exit")
    args = parser.parse_args()

    kinds = load_kinds()

    if args.list:
        for k in sorted(kinds.keys()):
            slug = kind_to_slug(k)
            print(f"  {k:30s} -> {slug}-builder.md")
        print(f"\n  Total: {len(kinds)} kinds")
        return

    if args.kind and args.kind not in kinds:
        print(f"ERROR: kind '{args.kind}' not found in kinds_meta.json", file=sys.stderr)
        sys.exit(1)

    mode = "DRY RUN" if args.dry_run else "MATERIALIZE"
    scope = args.kind or "all 99 kinds"
    print(f"\n=== {mode}: {scope} ===\n")

    count = materialize(kinds, target_kind=args.kind, dry_run=args.dry_run)

    print(f"\n  {'Would generate' if args.dry_run else 'Generated'}: {count} sub-agent files")
    print(f"  Target: {AGENTS_DIR}/")
    print(f"  Protected (untouched): {', '.join(sorted(PROTECTED))}\n")


if __name__ == "__main__":
    main()
