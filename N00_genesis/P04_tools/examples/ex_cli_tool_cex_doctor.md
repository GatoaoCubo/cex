---
id: p04_ct_cex_doctor
kind: cli_tool
pillar: P04
title: "CEX Doctor — Naming, density, and 13-file completeness checker"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, governance, doctor, validation, health]
cli_command: "python _tools/cex_doctor.py"
cli_args:
  - name: "--fix"
    type: boolean
    required: false
    description: "Auto-fix naming issues (default: diagnose only)"
inputs: ["archetypes/builders/ directory (auto-scanned)"]
outputs: ["diagnostic report: naming violations, density scores, completeness per builder"]
dependencies: ["pyyaml"]
category: governance
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_fix_frontmatter
  - bld_tools_kind
  - p04_ct_validate_schema
  - p04_ct_validate_builder
  - n01_hybrid_review_wave1
  - bld_knowledge_card_kind
  - bld_config_builder
  - validate
  - bld_collaboration_naming_rule
  - doctor
---

## Purpose
Scans all builders in archetypes/builders/ for three health dimensions: bld_* naming convention compliance, information density (>= 0.78), and 13-file completeness (all ISO kinds present). Optionally auto-fixes naming violations.

## Usage
```bash
# Diagnose only (default)
python _tools/cex_doctor.py

# Diagnose and auto-fix naming issues
python _tools/cex_doctor.py --fix
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--fix` | flag | no | Auto-fix naming violations |

No arguments required — scans entire builders directory automatically.

## Pipeline Position
**8F Function**: GOVERN (F7) — quality governance and health monitoring.
**Stage**: Post-build validation. Run after creating or modifying builders. Upstream of cex_feedback (which tracks quality over time).

## Dependencies
1. `archetypes/builders/` directory with builder subdirectories
2. Expected 13 kinds: architecture, collaboration, config, examples, instruction, knowledge_card, manifest, memory, output_template, quality_gate, schema, system_prompt, tools
3. Naming regex: `^bld_[a-z][a-z0-9_]+_[a-z][a-z0-9_]+\.md$`

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
| [[p04_ct_fix_frontmatter]] | sibling | 0.39 |
| [[bld_tools_kind]] | related | 0.34 |
| [[p04_ct_validate_schema]] | sibling | 0.34 |
| [[p04_ct_validate_builder]] | sibling | 0.33 |
| [[n01_hybrid_review_wave1]] | upstream | 0.26 |
| [[bld_knowledge_card_kind]] | upstream | 0.26 |
| [[bld_config_builder]] | downstream | 0.25 |
| [[validate]] | downstream | 0.24 |
| [[bld_collaboration_naming_rule]] | downstream | 0.24 |
| [[doctor]] | downstream | 0.24 |
