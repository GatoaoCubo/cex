---
id: p12_sig_agent_group_complete
kind: signal
pillar: P12
description: "Completion signal emitted by agent_group after task execution"
event: agent_group_complete
format: json
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.1
tags: [signal, completion, agent_group, orchestration]
updated: "2026-04-07"
domain: "orchestration"
title: "Signal Supervisor Complete"
density_score: 0.92
tldr: "Defines signal for signal supervisor complete, with validation gates and integration points."
---

# Signal: agent_group_complete

## Purpose
Emitted by agent_group after task completion. Consumed by spawn_monitor.ps1 and orchestrator for wave tracking.

## Schema
```json
{
  "agent_group": "edison",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-24T20:00:00Z",
  "task": "8 P04 examples from real artifacts",
  "artifacts_count": 8,
  "commit": "e8dd58b"
}
```

## Emit
```python
from records.core.python.signal_writer import write_signal
write_signal("edison", "complete", 9.0)
# Writes to .claude/signals/edison_complete_9.0.json
```

## Consume
```powershell
# spawn_monitor.ps1 polls every 30s
Get-ChildItem .claude/signals/*.json | ForEach-Object {
    $sig = Get-Content $_ | ConvertFrom-Json
    if ($sig.status -eq "complete") { "Done: $($sig.agent_group)" }
}
```

## Status Values
| Status | Meaning | Action |
|--------|---------|--------|
| complete | Task done, quality passed | Collect + next batch |
| error | Task failed | Log + retry or escalate |
| progress | Still working (heartbeat) | Wait, check stuck timer |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `signal` |
| Pillar | P12 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
