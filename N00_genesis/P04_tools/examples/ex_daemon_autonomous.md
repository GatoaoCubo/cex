---
id: p04_daemon_autonomous
kind: daemon
8f: F8_collaborate
name: autonomous_agent_daemon
pid_file: records/core/python/autonomous/daemon.pid
restart_policy: on_failure
health_check: /status
pillar: P04
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [daemon, autonomous, background, orchestration]
updated: "2026-04-07"
domain: "tool integration"
title: "Daemon Autonomous"
density_score: 0.92
tldr: "Defines daemon for daemon autonomous, with validation gates and integration points."
related:
  - p04_daemon_{{NAME_SLUG}}
  - daemon-builder
  - bld_architecture_daemon
  - bld_collaboration_daemon
  - bld_tools_daemon
  - bld_knowledge_card_daemon
  - bld_output_template_daemon
  - p10_lr_daemon_builder
  - p01_kc_daemon
  - bld_instruction_daemon
---

# Daemon: autonomous_agent_daemon

## Runtime
1. Trigger: queue (watches .claude/inbox/ for new tasks)
2. Interval: 60s poll cycle
3. Owner: system-level (runs outside Claude session)

## Loop
1. Read task queue from `.claude/inbox/*.json`
2. Route task to agent_group via spawn_solo.ps1
3. Emit completion signal to `.claude/signals/`

## Safety
1. Healthcheck: PID file exists + process responsive
2. Restart policy: on_failure (max 3 retries, then alert)
3. Stop condition: SIGTERM or `daemon.py stop` (reads PID)

## CLI
`daemon.py start|stop|status|run-once` — start backgrounds with PID, stop via SIGTERM, run-once for testing.

## Metadata

```yaml
id: p04_daemon_autonomous
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p04-daemon-autonomous.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `daemon` |
| Pillar | P04 |
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
| [[p04_daemon_{{NAME_SLUG}}]] | sibling | 0.43 |
| [[daemon-builder]] | related | 0.39 |
| [[bld_architecture_daemon]] | downstream | 0.39 |
| [[bld_collaboration_daemon]] | downstream | 0.35 |
| [[bld_tools_daemon]] | related | 0.32 |
| [[bld_knowledge_card_daemon]] | upstream | 0.32 |
| [[bld_output_template_daemon]] | downstream | 0.31 |
| [[p10_lr_daemon_builder]] | downstream | 0.31 |
| [[p01_kc_daemon]] | related | 0.30 |
| [[bld_instruction_daemon]] | upstream | 0.30 |
