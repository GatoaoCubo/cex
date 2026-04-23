---
quality: 8.4
quality: 7.9
quality: 7.9
id: monitor
kind: instruction
pillar: P12
description: "Autonomous dispatch monitoring. Usage: /monitor"
quality: 7.9
title: "Monitor"
version: "1.0.0"
author: n07
tags: [monitor, dispatch, orchestration, lifecycle]
tldr: "Track nucleus health, detect stuck/crashed processes, trigger consolidation."
domain: "CEX system"
created: "2026-04-20"
updated: "2026-04-20"
density_score: 0.90
related:
  - skill_n07
  - ex_director_ops_health_monitor
  - skill_catalog_cex
  - p01_kc_orchestration_best_practices
  - p01_kc_orchestration
  - p02_agent_admin_orchestrator
  - p03_sp_admin_orchestrator
  - spec_multi_runtime_features
  - bld_collaboration_skill
  - dispatch
---

# /monitor -- Autonomous Dispatch Monitoring

Invoke the monitor skill for dispatch health checking.

See: `.claude/skills/monitor.md`

## Usage

1. `/monitor` -- run a single health check cycle (process liveness + git log + signals)
2. Auto-invoked by N07 after every `dispatch.sh solo|grid|crew|swarm`
3. Interleaved during active dispatch: N07 polls every 60-90s between own tasks

## What It Checks

| Check | Command | Detects |
|-------|---------|---------|
| Process liveness | `Get-Process claude, codex, node -EA SilentlyContinue` | RUNNING / CRASHED / ORPHAN |
| Recent commits | `git log --oneline --since="5 minutes ago"` | Progress from nuclei |
| Completion signals | `ls .cex/runtime/signals/` | Nucleus done notifications |
| Task file consumption | `ls .cex/runtime/handoffs/n0*_task.md` | Boot failures |

## Invocation

When the user types `/monitor`, invoke the skill:

```
Skill(skill="monitor")
```

## Cross-runtime

- **Claude Code**: native skill + this command
- **Codex/Gemini/Ollama**: boot wrapper loads `.cex/skills/monitor.md` as context

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill_n07]] | upstream | 0.43 |
| [[ex_director_ops_health_monitor]] | upstream | 0.38 |
| [[skill_catalog_cex]] | upstream | 0.36 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.35 |
| [[p01_kc_orchestration]] | upstream | 0.29 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.29 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.29 |
| [[spec_multi_runtime_features]] | upstream | 0.29 |
| [[bld_collaboration_skill]] | related | 0.29 |
| [[dispatch]] | sibling | 0.29 |
