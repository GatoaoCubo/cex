---
id: p06_vs_signal_completion
kind: validation_schema
8f: F1_constrain
pillar: P06
description: "Output schema for agent_group completion signals"
format: json
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [output-schema, signal, completion, json]
updated: "2026-04-07"
domain: "schema"
title: "Validator Signal Completion"
density_score: 0.92
tldr: "Defines validation schema for validator signal completion, with validation gates and integration points."
related:
  - p12_sig_agent_group_complete
  - bld_schema_model_registry
  - p12_sig_admin_orchestration
  - bld_schema_tagline
  - bld_schema_experiment_tracker
  - bld_examples_signal
  - n06_schema_brand_config
  - bld_schema_signal
  - bld_schema_action_paradigm
  - bld_schema_landing_page
---

# Output Schema: signal_completion

## Schema
```json
{
  "agent_group": "string (edison|shaka|lily|pytha|atlas|york)",
  "status": "string (complete|error|progress)",
  "quality_score": "number (0.0-10.0)",
  "timestamp": "string (ISO 8601)",
  "task_summary": "string (what was done)",
  "artifacts": ["string (file paths created/modified)"],
  "commit_hash": "string (git commit if applicable)"
}
```

## Example
```json
{
  "agent_group": "edison",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-24T20:00:00Z",
  "task_summary": "8 P04 examples from real artifacts",
  "artifacts": ["P04_tools/examples/p04_mcp_organization_brain.md"],
  "commit_hash": "e8dd58b"
}
```

## Consumers
1. spawn_monitor.ps1: polls `.claude/signals/` for completion
2. orchestrator: reads signals to determine wave completion
3. spawn_grid.ps1 continuous mode: triggers next batch dispatch

## Properties

| Property | Value |
|----------|-------|
| Kind | `validation_schema` |
| Pillar | P06 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_sig_agent_group_complete]] | downstream | 0.39 |
| [[bld_schema_model_registry]] | related | 0.36 |
| [[p12_sig_admin_orchestration]] | downstream | 0.34 |
| [[bld_schema_tagline]] | related | 0.32 |
| [[bld_schema_experiment_tracker]] | related | 0.32 |
| [[bld_examples_signal]] | downstream | 0.30 |
| [[n06_schema_brand_config]] | related | 0.29 |
| [[bld_schema_signal]] | related | 0.28 |
| [[bld_schema_action_paradigm]] | related | 0.27 |
| [[bld_schema_landing_page]] | related | 0.26 |
