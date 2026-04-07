---
id: p04_ct_cex_8f_motor
kind: cli_tool
pillar: P04
title: "Motor 8F — Intent to execution plan decomposer"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, core, motor, 8f, planning]
cli_command: "python _tools/cex_8f_motor.py"
cli_args:
  - name: "--intent"
    type: string
    required: true
    description: "Natural language intent string (PT or EN)"
  - name: "--quality"
    type: float
    required: false
    description: "Quality target override (default from config)"
  - name: "--output"
    type: string
    required: false
    description: "Output file path (default: stdout)"
  - name: "--compact"
    type: boolean
    required: false
    description: "Compact JSON output (no indentation)"
  - name: "--test"
    type: boolean
    required: false
    description: "Run inline test suite"
inputs: ["natural language intent", "optional quality target"]
outputs: ["JSON execution plan with builder steps, dependencies, 8F positions"]
dependencies: ["pyyaml"]
category: core
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
---

## Purpose
Receives a natural language intent and produces a structured execution plan: which builders to activate, in what order, with what dependencies, following the 8F pipeline (CONSTRAIN > BECOME > INJECT > REASON > CALL > PRODUCE > GOVERN > COLLABORATE).

## Usage
```bash
# Simple intent
python _tools/cex_8f_motor.py --intent "cria agente de vendas para ML"

# With quality override
python _tools/cex_8f_motor.py --intent "reconstroi signal-builder" --quality 9.5

# Multi-artifact intent
python _tools/cex_8f_motor.py --intent "cria agente E workflow de pesquisa"

# Save plan to file
python _tools/cex_8f_motor.py --intent "cria agente" --output plan.json

# Run tests
python _tools/cex_8f_motor.py --test
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--intent` | string | yes* | Natural language intent |
| `--quality` | float | no | Quality target override |
| `--output` | string | no | Output file (default: stdout) |
| `--compact` | flag | no | Compact JSON output |
| `--test` | flag | no | Run inline tests (replaces --intent) |

*Required unless `--test` is used.

## Pipeline Position
**8F Function**: All 8 functions — the Motor maps intent to the full pipeline.
**Stage**: Second stage. Receives human intent, produces JSON plan consumed by cex_crew_runner.

## Dependencies
- `_docs/8F_BUILDER_MAP.yaml` for builder-to-function mapping
- Verb normalization table (PT imperative/infinitive to canonical actions)
- Output consumed by `cex_crew_runner.py`
