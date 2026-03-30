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
- `archetypes/builders/` directory with builder subdirectories
- Expected 13 kinds: architecture, collaboration, config, examples, instruction, knowledge_card, manifest, memory, output_template, quality_gate, schema, system_prompt, tools
- Naming regex: `^bld_[a-z][a-z0-9_]+_[a-z][a-z0-9_]+\.md$`
