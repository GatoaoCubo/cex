---
id: p04_ct_compare_builders
kind: cli_tool
8f: F5_call
pillar: P04
title: "Compare Builders — 5-metric diff for original vs reconstructed"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, qa, compare, diff, metrics]
cli_command: "python _tools/compare_builders.py"
cli_args:
  - name: "--original"
    type: string
    required: true
    description: "Directory with original builder files"
  - name: "--generated"
    type: string
    required: true
    description: "Directory with reconstructed builder files"
  - name: "--output"
    type: string
    required: false
    description: "JSON output file path"
  - name: "--format"
    type: string
    required: false
    description: "Output format: json or table (default: json)"
  - name: "--strict"
    type: boolean
    required: false
    description: "Exit code 1 if any file FAILs"
  - name: "--skip-quality"
    type: boolean
    required: false
    description: "Skip quality 5D scoring (default: true)"
  - name: "--quality-file"
    type: string
    required: false
    description: "JSON file with pre-scored quality values"
inputs: ["original builder directory", "generated builder directory"]
outputs: ["comparison report with 5 metrics per file: structural, field coverage, Jaccard, size delta, quality 5D"]
dependencies: ["pyyaml (optional)"]
category: qa
quality: 9.1
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_builder
  - bld_architecture_kind
  - bld_collaboration_validation_schema
  - p04_ct_validate_builder
  - bld_tools_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_collaboration_response_format
  - p04_ct_cex_forge
  - bld_collaboration_golden_test
---

## Purpose
Compares original vs reconstructed builder files across 5 metrics: structural similarity, field coverage, content similarity (Jaccard with stopword removal), size delta, and quality 5D scoring. Used to validate LLM-generated builders against reference implementations.

## Usage
```bash
# Compare two builder directories
python _tools/compare_builders.py --original archetypes/builders/signal-builder/ --generated /tmp/signal-builder/

# Table format output
python _tools/compare_builders.py --original archetypes/builders/signal-builder/ --generated /tmp/signal-builder/ --format table

# Strict mode (CI/CD gate)
python _tools/compare_builders.py --original archetypes/builders/signal-builder/ --generated /tmp/signal-builder/ --strict
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--original` | string | yes | Original builder directory |
| `--generated` | string | yes | Reconstructed builder directory |
| `--output` | string | no | JSON output file |
| `--format` | string | no | json or table (default: json) |
| `--strict` | flag | no | Exit 1 on any FAIL |
| `--skip-quality` | flag | no | Skip 5D scoring (default: true) |
| `--quality-file` | string | no | Pre-scored quality JSON |

## Pipeline Position
**8F Function**: GOVERN (F7) — quality assurance for LLM-generated content.
**Stage**: Post-generation validation. Compares cex_crew_runner output against reference builders. Used in eval loops.

## Dependencies
- Both directories must contain bld_*.md files with YAML frontmatter
- Stopword filtering (PT + EN) for Jaccard similarity

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_builder]] | downstream | 0.33 |
| [[bld_architecture_kind]] | downstream | 0.31 |
| [[bld_collaboration_validation_schema]] | downstream | 0.31 |
| [[p04_ct_validate_builder]] | sibling | 0.30 |
| [[bld_tools_kind]] | related | 0.30 |
| [[kind-builder]] | downstream | 0.29 |
| [[bld_collaboration_kind]] | downstream | 0.29 |
| [[bld_collaboration_response_format]] | downstream | 0.27 |
| [[p04_ct_cex_forge]] | sibling | 0.27 |
| [[bld_collaboration_golden_test]] | downstream | 0.26 |
