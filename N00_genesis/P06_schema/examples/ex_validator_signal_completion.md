---
id: p06_vs_signal_completion
kind: validation_schema
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
