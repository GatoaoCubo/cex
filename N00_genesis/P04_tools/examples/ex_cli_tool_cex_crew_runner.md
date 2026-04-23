---
id: p04_ct_cex_crew_runner
kind: cli_tool
pillar: P04
title: "Crew Runner — Lightweight DAG executor for builder plans"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, core, crew, dag, execution]
cli_command: "python _tools/cex_crew_runner.py"
cli_args:
  - name: "--plan"
    type: string
    required: true
    description: "Path to Motor 8F plan JSON"
  - name: "--output-dir"
    type: string
    required: false
    description: "Output directory for prompts/outputs"
  - name: "--step"
    type: integer
    required: false
    description: "Execute only this step (by 8F position 1-8)"
  - name: "--dry-run"
    type: boolean
    required: false
    description: "Generate prompts only, no LLM calls (default)"
  - name: "--execute"
    type: boolean
    required: false
    description: "Real execution — calls LLM via anthropic SDK"
inputs: ["Motor 8F plan JSON", "optional step filter"]
outputs: ["generated prompts per builder step", "LLM outputs (--execute mode)", "run state JSON"]
dependencies: ["pyyaml", "anthropic (optional, for --execute)"]
category: core
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_cex_8f_motor
  - p03_ch_builder_pipeline
  - ctx_cex_new_dev_guide
  - p04_ct_cex_pipeline
  - p04_ct_cex_forge
  - p01_kc_cex_tooling_master
  - p12_wf_builder_8f_pipeline
  - p03_ch_brief_to_multiformat
  - tpl_instruction
  - p04_ct_validate_builder
---

## Purpose
LangGraph-inspired state machine that executes CEX builder plans produced by Motor 8F. In dry-run mode (default), generates prompts and saves to files. In execute mode, calls Claude via anthropic SDK with quality gates (>= 7.0 advance, < 7.0 retry, exhausted degrade).

## Usage
```bash
# Dry-run: generate prompts only
python _tools/cex_crew_runner.py --plan plan.json --output-dir out/

# Execute single step
python _tools/cex_crew_runner.py --plan plan.json --step 2 --output-dir out/

# Full execution with LLM
python _tools/cex_crew_runner.py --plan plan.json --execute --output-dir out/

# Full pipeline (Motor 8F -> Crew Runner)
python _tools/cex_8f_motor.py --intent "cria agente de vendas" --output /tmp/plan.json
python _tools/cex_crew_runner.py --plan /tmp/plan.json --output-dir /tmp/crew_out/
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--plan` | string | yes | Path to Motor 8F plan JSON |
| `--output-dir` | string | no | Output directory for results |
| `--step` | int | no | Execute only this 8F step (1-8) |
| `--dry-run` | flag | no | Prompt generation only (default: true) |
| `--execute` | flag | no | Real LLM execution via anthropic SDK |

## Pipeline Position
**8F Function**: Executes all functions in sequence per the plan DAG.
**Stage**: Third stage. Consumes Motor 8F plan, produces artifact files. Quality gate: >= 7.0 advance, < 7.0 retry (max 2), then degrade.

## Dependencies
- Motor 8F plan JSON (from `cex_8f_motor.py`)
- `archetypes/builders/` for builder ISO injection (30KB budget)
- `anthropic` SDK (only for `--execute` mode, model: claude-sonnet-4-6)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_cex_8f_motor]] | sibling | 0.40 |
| [[p03_ch_builder_pipeline]] | upstream | 0.27 |
| [[ctx_cex_new_dev_guide]] | related | 0.22 |
| [[p04_ct_cex_pipeline]] | sibling | 0.22 |
| [[p04_ct_cex_forge]] | sibling | 0.22 |
| [[p01_kc_cex_tooling_master]] | upstream | 0.22 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.21 |
| [[p03_ch_brief_to_multiformat]] | upstream | 0.21 |
| [[tpl_instruction]] | upstream | 0.21 |
| [[p04_ct_validate_builder]] | sibling | 0.20 |
