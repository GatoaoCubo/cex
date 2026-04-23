---
id: p04_daemon_n05
kind: daemon
pillar: P04
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: daemon-builder
name: "N05 Operations Maintenance Daemon"
schedule: "continuous; heartbeat 60s, orphan-cleanup 5m/30m, PID-hygiene 10m, compile-verify 15m, lock-rotate 1h, temp-cleanup 24h"
restart_policy: on_failure
signal_handling: "SIGTERM: complete active task, flush heartbeat, delete PID, exit 0"
quality: 8.9
tags: [daemon, n05, operations, P04, system-health]
tldr: "N05 ops daemon: orphan reap, signal archival, PID hygiene, compile-verify, lock rotation, heartbeat 60s -- Windows PowerShell task"
description: "Persistent background daemon maintaining .cex/runtime/ health: 7 staggered tasks keep processes reaped and .md/.yaml pairs in sync."
health_check: "n05_heartbeat.json every 60s; stale >3min = alert"
pid_file: ".cex/runtime/pids/n05_daemon.pid"
resource_limits: "memory_max: 128MB, cpu_percent: 5, max_open_files: 256"
monitoring: "heartbeat JSON; alert if stale >3min or error_count >3 per 10min"
logging: structured
graceful_shutdown: "finish active task, write heartbeat status=stopping, delete PID, exit 0"
max_restarts: "5 in 30min"
density_score: 1.0
related:
  - bld_instruction_daemon
  - bld_examples_daemon
  - bld_knowledge_card_daemon
  - p04_daemon_{{NAME_SLUG}}
  - p10_lr_daemon_builder
  - report_bootstrap_preflight
  - p04_daemon_autonomous
  - p11_qg_daemon
  - bld_architecture_daemon
  - daemon-builder
---

## Overview
N05 maintenance daemon (Windows PowerShell). 7 staggered tasks keep
.cex/runtime/ clean: orphan reap, signal archival, PID hygiene,
temp cleanup, compile verify, lock rotation, heartbeat.

## Lifecycle
Schedule: heartbeat 60s; orphan 5m/30m; PID-hygiene 10m;
compile-verify 15m; lock-rotate 1h; temp-cleanup 24h.
Startup: verify dirs, write PID, enter loop.
Restart: on_failure; backoff 1->4s cap 30s; max 5 in 30min.
Shutdown: complete cycle, flush heartbeat, delete PID, exit 0.

## Signal Handling
| Signal | Response |
|--------|----------|
| SIGTERM | Flush heartbeat, delete PID, exit 0 |
| SIGINT | Same as SIGTERM |
| SIGHUP | Reload interval config, no restart |
| STOP_DAEMON file | Graceful exit next cycle |

## Monitoring
Health: n05_heartbeat.json every 60s -- timestamp, last_task, error_count;
stale >3min = N07 alert. Metrics: orphans_reaped, signals_archived,
compile_flags, locks_released. Alert: error_count >3 per 10min.
Logging: structured JSON, .cex/runtime/logs/n05_daemon.jsonl, 7d.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_daemon]] | upstream | 0.35 |
| [[bld_examples_daemon]] | downstream | 0.35 |
| [[bld_knowledge_card_daemon]] | upstream | 0.33 |
| [[p04_daemon_{{NAME_SLUG}}]] | sibling | 0.32 |
| [[p10_lr_daemon_builder]] | downstream | 0.31 |
| [[report_bootstrap_preflight]] | downstream | 0.26 |
| [[p04_daemon_autonomous]] | sibling | 0.25 |
| [[p11_qg_daemon]] | downstream | 0.23 |
| [[bld_architecture_daemon]] | downstream | 0.21 |
| [[daemon-builder]] | related | 0.21 |
