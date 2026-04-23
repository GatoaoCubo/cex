---
id: "p04_daemon_{{NAME_SLUG}}"
kind: daemon
pillar: P04
version: 1.0.0
title: Template - Daemon
tags: [template, daemon, background, service, worker]
tldr: "Long-running background service: startup, shutdown, health check, signal handling, restart policy."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
related:
  - p04_daemon_autonomous
  - bld_instruction_daemon
  - bld_knowledge_card_daemon
  - daemon-builder
  - bld_collaboration_daemon
  - p11_qg_daemon
  - p10_lr_daemon_builder
  - bld_output_template_daemon
  - bld_architecture_daemon
  - bld_examples_daemon
---

# Daemon: [NAME]

## Purpose
[WHAT this daemon does]
## Configuration
```yaml
name: "[DAEMON_NAME]"
type: [worker | watcher | scheduler | server]
health_interval_s: [30]
pid_file: "[/var/run/daemon.pid]"
```
## Lifecycle
| Phase | Action | Signal |
|-------|--------|--------|
| Start | Init resources, begin loop | -- |
| Health | Verify connectivity | -- |
| Reload | Re-read config | SIGHUP |
| Stop | Finish task, cleanup | SIGTERM |
| Kill | Immediate stop | SIGKILL |
## Restart Policy
1. **Crash**: Auto-restart after 5s, max 3 retries
2. **OOM**: Restart + increase memory
3. **Unresponsive**: Kill after 60s no health
## Quality Gate
1. [ ] PID file prevents duplicates
2. [ ] Graceful SIGTERM handling
3. [ ] Health check endpoint
4. [ ] Max restart limit set

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `daemon` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_daemon_autonomous]] | sibling | 0.47 |
| [[bld_instruction_daemon]] | upstream | 0.43 |
| [[bld_knowledge_card_daemon]] | upstream | 0.42 |
| [[daemon-builder]] | related | 0.42 |
| [[bld_collaboration_daemon]] | downstream | 0.38 |
| [[p11_qg_daemon]] | downstream | 0.37 |
| [[p10_lr_daemon_builder]] | downstream | 0.36 |
| [[bld_output_template_daemon]] | downstream | 0.35 |
| [[bld_architecture_daemon]] | downstream | 0.35 |
| [[bld_examples_daemon]] | downstream | 0.34 |
