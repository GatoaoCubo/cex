---
id: p04_ct_fix_frontmatter
kind: cli_tool
pillar: P04
title: "Fix Frontmatter — Batch add kind+id to builder files"
version: 1.0.0
created: 2026-03-28
author: builder_agent
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
quality: 9.1
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_cex_doctor
  - tpl_validation_schema
  - skill
  - research_then_build
  - bld_tools_kind
  - p04_ct_validate_schema
  - kind-builder
  - p04_ct_cex_pipeline
  - doctor
  - validate
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
1. `archetypes/builders/` directory
2. Filename convention: `bld_{kind}_{topic}.md`

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `cli_tool` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_cex_doctor]] | sibling | 0.38 |
| [[tpl_validation_schema]] | downstream | 0.35 |
| [[skill]] | downstream | 0.35 |
| [[research_then_build]] | downstream | 0.32 |
| [[bld_tools_kind]] | related | 0.30 |
| [[p04_ct_validate_schema]] | sibling | 0.29 |
| [[kind-builder]] | downstream | 0.27 |
| [[p04_ct_cex_pipeline]] | sibling | 0.27 |
| [[doctor]] | downstream | 0.26 |
| [[validate]] | downstream | 0.26 |
