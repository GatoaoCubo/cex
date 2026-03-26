---
id: p06_vs_signal_completion
kind: validation_schema
pillar: P06
description: "Output schema for satellite completion signals"
format: json
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [output-schema, signal, completion, json]
---

# Output Schema: signal_completion

## Schema
```json
{
  "satellite": "string (edison|shaka|lily|pytha|atlas|york)",
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
  "satellite": "edison",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-24T20:00:00Z",
  "task_summary": "8 P04 examples from real artifacts",
  "artifacts": ["P04_tools/examples/p04_mcp_codexa_brain.md"],
  "commit_hash": "e8dd58b"
}
```

## Consumers
- spawn_monitor.ps1: polls `.claude/signals/` for completion
- STELLA: reads signals to determine wave completion
- spawn_grid.ps1 continuous mode: triggers next batch dispatch
