---
id: p07_bm_agent_group_boot_time
kind: benchmark
pillar: P07
description: "Benchmark for agent_group boot times across all providers"
metric: boot_time_seconds
version: 1.0.0
created: 2026-03-24
author: operations_agent
quality: 9.0
tags: [benchmark, performance, boot, agent_group]
updated: "2026-04-07"
domain: "evaluation"
title: "Benchmark Supervisor Boot Time"
density_score: 0.92
tldr: "Defines benchmark for benchmark supervisor boot time, with validation gates and integration points."
related:
  - p12_dr_keyword_agent_group
  - bld_examples_boot_config
  - p02_boot_edison_claude
  - p01_kc_iterative_refinement_skill
  - p07_gt_stripe_pipeline
  - bld_config_spawn_config
  - tpl_validation_schema
  - p01_kc_claude_model_capabilities_2026
  - p01_kc_refinement
  - p08_diag_agent_group_grid
---

# Benchmark: Agent_group Boot Time

## Metric
Time from `Start-Process` to first Claude API response (seconds).

## Baselines (measured 2026-03-05)
| Agent_group | Model | Boot Time | Status |
|-----------|-------|-----------|--------|
| edison | opus | 5s | PASS |
| shaka | sonnet | 12s | PASS |
| lily | sonnet | 10s | PASS |
| pytha | sonnet | 5s | PASS |
| atlas | opus | 15s | WARN (MCP heavy) |
| york | sonnet | 5s | PASS |
| chrome | sonnet | 10s | PASS |
| minimal | haiku | 2s | PASS |

## Thresholds
| Tier | Max Boot | Action |
|------|----------|--------|
| Fast | < 5s | Ideal for interactive |
| Normal | 5-15s | Acceptable for grid |
| Slow | > 15s | Investigate MCP load |

## How to Run
```bash
powershell -Command "Measure-Command { Start-Process boot\edison.cmd -Wait }"
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_keyword_agent_group]] | downstream | 0.33 |
| [[bld_examples_boot_config]] | related | 0.29 |
| [[p02_boot_edison_claude]] | upstream | 0.28 |
| [[p01_kc_iterative_refinement_skill]] | upstream | 0.27 |
| [[p07_gt_stripe_pipeline]] | related | 0.27 |
| [[bld_config_spawn_config]] | downstream | 0.26 |
| [[tpl_validation_schema]] | upstream | 0.25 |
| [[p01_kc_claude_model_capabilities_2026]] | upstream | 0.24 |
| [[p01_kc_refinement]] | upstream | 0.24 |
| [[p08_diag_agent_group_grid]] | downstream | 0.24 |
