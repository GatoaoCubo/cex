---
id: p09_bc_n05_ops
kind: batch_config
8f: F1_constrain
pillar: P09
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "batch-config-builder"
provider: "custom"
model: "n/a"
endpoint: "local_cli"
max_requests: 500
completion_window: "4h"
cost_cap_usd: 0.00
concurrency: 3
retry_policy: "max 2 retries, fixed backoff 5s, continue on partial failure"
input_format: "jsonl"
output_format: "jsonl"
quality: 9.0
tags: [batch_config, N05, operations, P09, mass-ops]
tldr: "N05 bulk ops: compile_all/doctor_all/sanitize_all/evolve_batch/score_batch -- local CLI, 4h window, retry 2x, progress every 10 items"
description: "Batch execution config for N05 operations nucleus mass ops: compile, health check, sanitize, evolve, and score."
density_score: 1.0
related:
  - bld_output_template_batch_config
  - bld_examples_batch_config
  - bld_knowledge_card_batch_config
  - bld_instruction_batch_config
  - bld_schema_batch_config
  - p03_sp_batch_config_builder
  - p10_lr_batch_config_builder
  - p01_kc_batch_config
  - bld_architecture_batch_config
  - bld_collaboration_batch_config
---

## Overview

Five bulk operation modes for N05 against the CEX local toolchain.
Triggered by: overnight scripts or N07 orchestrator dispatch.
Credential env var: `n/a` -- local tools only, no external API credentials required.

## Job Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| provider | custom | Local CEX CLI toolchain |
| endpoint | local_cli | Python _tools/ entry points |
| max_requests | 500 | Max artifacts per batch run |
| completion_window | 4h | Overnight batch SLA |

### Mode Table

| Mode | Command | Concurrency | Timeout/item |
|------|---------|-------------|--------------|
| compile_all | `cex_compile.py --all` | 1 | 60s |
| doctor_all | `cex_doctor.py` | 1 | 120s |
| sanitize_all | `cex_sanitize.py --check --scope N05_operations/` | 1 | 30s |
| evolve_batch | `cex_evolve.py --target N05_operations/ --threshold 9.0` | 2 | 300s |
| score_batch | `cex_score.py --dir N05_operations/` | 3 | 60s |

## Cost Controls

| Control | Value | Notes |
|---------|-------|-------|
| cost_cap_usd | $0.00 | Local tools, no API spend |
| alert_threshold | 500 items | Halt if batch exceeds max_requests |

## Retry and Error Policy

| Setting | Value | Description |
|---------|-------|-------------|
| max_retries | 2 | Per failed item |
| backoff | fixed 5s | Wait before retry |
| partial_failure | continue | Process remaining on per-item failure |
| dead_letter | `.cex/runtime/batch_errors/n05_ops.jsonl` | Permanent failures logged here |
| progress_signal | every 10 items | Emit progress to stdout + signal file |

## Input/Output Format

- Input: JSONL -- `{"item_id": "...", "mode": "compile_all", "path": "N05_operations/..."}`
- Output: JSONL -- `{"item_id": "...", "status": "ok|fail", "error": null}`
- Input path: `.cex/runtime/batch_jobs/n05_ops_input.jsonl`
- Output path: `.cex/runtime/batch_jobs/n05_ops_output.jsonl`

## References

- `N05_operations/P09_config/con_rate_limit_config_n05.md`
- `_tools/cex_compile.py` -- `cex_doctor.py` -- `cex_sanitize.py`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_batch_config]] | upstream | 0.39 |
| [[bld_examples_batch_config]] | upstream | 0.35 |
| [[bld_knowledge_card_batch_config]] | upstream | 0.30 |
| [[bld_instruction_batch_config]] | upstream | 0.29 |
| [[bld_schema_batch_config]] | upstream | 0.28 |
| [[p03_sp_batch_config_builder]] | upstream | 0.27 |
| [[p10_lr_batch_config_builder]] | downstream | 0.27 |
| [[p01_kc_batch_config]] | related | 0.26 |
| [[bld_architecture_batch_config]] | upstream | 0.24 |
| [[bld_collaboration_batch_config]] | downstream | 0.22 |
