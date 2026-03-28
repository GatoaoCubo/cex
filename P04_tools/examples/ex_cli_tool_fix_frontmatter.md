---
id: p04_ct_fix_frontmatter
kind: cli_tool
pillar: P04
title: "Fix Frontmatter — Batch add kind+id to builder files"
version: 1.0.0
created: 2026-03-28
author: edison
tags: [cli, tool, cex, qa, frontmatter, repair, batch]
cli_command: "python _tools/fix_frontmatter.py"
cli_args:
  - name: "--dry-run"
    type: boolean
    required: false
    description: "Report what would change without modifying files"
  - name: "--fix"
    type: boolean
    required: false
    description: "Apply frontmatter fixes"
inputs: ["archetypes/builders/ .md files"]
outputs: ["fixed .md files with kind+id in frontmatter", "dry-run report"]
dependencies: ["pyyaml (implicit via frontmatter parsing)"]
category: qa
---

## Purpose
Scans all builder .md files and adds missing `kind` and `id` fields to YAML frontmatter. Derives kind from filename pattern (bld_{kind}_{topic}.md) and id from the filename stem. Operates in dry-run (report) or fix (apply) mode.

## Usage
```bash
# Report what would change
python _tools/fix_frontmatter.py --dry-run

# Apply fixes
python _tools/fix_frontmatter.py --fix
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--dry-run` | flag | no | Report only |
| `--fix` | flag | no | Apply changes |

One of `--dry-run` or `--fix` should be used.

## Pipeline Position
**8F Function**: GOVERN (F7) — repair and normalization.
**Stage**: Repair tool. Run after bulk builder creation or migration to ensure all files have consistent frontmatter. Upstream of cex_doctor and validate_builder.

## Dependencies
- `archetypes/builders/` directory
- Filename convention: `bld_{kind}_{topic}.md`
