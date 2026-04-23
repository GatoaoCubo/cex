---
id: p04_ct_validate_builder
kind: cli_tool
pillar: P04
title: "Validate Builder — 13-file checklist validator for builders"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, governance, validation, builder, checklist]
cli_command: "python _tools/validate_builder.py"
cli_args:
  - name: "builder"
    type: string
    required: false
    description: "Path to builder directory to validate"
  - name: "--json"
    type: boolean
    required: false
    description: "Print JSON output only"
  - name: "--summary"
    type: boolean
    required: false
    description: "Print compact summary table"
  - name: "--all"
    type: boolean
    required: false
    description: "Validate all builders in archetypes/builders/"
  - name: "--changed"
    type: boolean
    required: false
    description: "Validate only git-staged builders"
inputs: ["builder directory path(s)"]
outputs: ["validation report: pass/fail per kind, density scores, size checks"]
dependencies: ["pyyaml"]
category: governance
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_kind
  - bld_examples_handoff
  - p04_ct_cex_doctor
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_builder
  - bld_collaboration_kind
  - p04_ct_cex_forge
  - p04_ct_compare_builders
  - validate
---

## Purpose
Validates a CEX builder directory against the archetype checklist: bld_* naming, 13 required ISO kinds, density >= 0.8 per file, size <= 4096B (6144B for instruction), and correct frontmatter (kind, pillar, 8F function mapping).

## Usage
```bash
# Validate single builder
python _tools/validate_builder.py archetypes/builders/agent-builder

# Validate with JSON output
python _tools/validate_builder.py archetypes/builders/agent-builder --json

# Validate all builders
python _tools/validate_builder.py --all

# Compact summary
python _tools/validate_builder.py --all --summary

# Only staged builders (pre-commit hook)
python _tools/validate_builder.py --changed
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `builder` | positional | no | Path to builder directory |
| `--json` | flag | no | JSON-only output |
| `--summary` | flag | no | Compact summary table |
| `--all` | flag | no | Validate all builders |
| `--changed` | flag | no | Only git-staged builders |

One of `builder`, `--all`, or `--changed` required.

## Pipeline Position
**8F Function**: GOVERN (F7) — validates builder completeness and quality.
**Stage**: Pre-commit / post-build validation. Gate before builders are used by cex_forge or cex_crew_runner.

## Dependencies
- 13 expected kinds with LP+8F mapping (KIND_SPECS)
- `archetypes/builders/` directory structure
- Git (for `--changed` mode: `git diff --cached --name-only`)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | related | 0.38 |
| [[bld_examples_handoff]] | downstream | 0.34 |
| [[p04_ct_cex_doctor]] | sibling | 0.34 |
| [[bld_architecture_kind]] | downstream | 0.33 |
| [[kind-builder]] | downstream | 0.32 |
| [[bld_collaboration_builder]] | downstream | 0.31 |
| [[bld_collaboration_kind]] | downstream | 0.30 |
| [[p04_ct_cex_forge]] | sibling | 0.30 |
| [[p04_ct_compare_builders]] | sibling | 0.29 |
| [[validate]] | downstream | 0.29 |
