---
id: p04_ct_distill
kind: cli_tool
pillar: P04
title: "CEX Distill — Template-driven knowledge extraction from raw input"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, qa, distill, extraction, template]
cli_command: "python _tools/distill.py"
cli_args:
  - name: "--input"
    type: string
    required: false
    description: "Path to raw input file"
  - name: "--type"
    type: string
    required: false
    description: "Artifact type (default: knowledge_card)"
  - name: "--output"
    type: string
    required: false
    description: "Output path (default: stdout)"
  - name: "--dry-run"
    type: boolean
    required: false
    description: "Show prompt without executing"
  - name: "--list-types"
    type: boolean
    required: false
    description: "List available distillation types"
  - name: "--validate"
    type: string
    required: false
    description: "Validate existing file against template"
inputs: ["raw input file (PDF, markdown, text)"]
outputs: ["LLM prompt for template-compliant artifact extraction"]
dependencies: []
category: qa
quality: 9.1
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
---

## Purpose
Transforms raw input into template-compliant artifacts. The template IS the prompt — it forces LLM to fill every {{PLACEHOLDER}} with knowledge extracted and expanded from the input. Enforces density >= 0.85, actionable axioms, anti-patterns, and concrete application sections.

## Usage
```bash
# Distill from raw file
python _tools/distill.py --input raw_file.pdf --type knowledge_card

# Dry-run (show prompt only)
python _tools/distill.py --input raw_file.pdf --type knowledge_card --dry-run

# List available types
python _tools/distill.py --list-types

# Validate existing artifact against template
python _tools/distill.py --validate existing_kc.md
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--input` | string | yes* | Raw input file path |
| `--type` | string | no | Artifact type (default: knowledge_card) |
| `--output` | string | no | Output file (default: stdout) |
| `--dry-run` | flag | no | Show prompt without executing |
| `--list-types` | flag | no | List available types |
| `--validate` | string | no | Validate file against template |

*Required unless `--list-types` is used.

## Pipeline Position
**8F Function**: INJECT (F3) + PRODUCE (F6) — extracts knowledge and produces artifacts.
**Stage**: Input processing. Converts raw sources into CEX-compliant artifacts via template enforcement. Upstream of cex_compile.

## Dependencies
- Templates in `P01_knowledge/templates/` (tpl_knowledge_card_*.md)
- TYPE_TO_TEMPLATE mapping for type resolution
