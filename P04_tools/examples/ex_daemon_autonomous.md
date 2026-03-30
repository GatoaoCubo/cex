---
id: p04_daemon_autonomous
kind: daemon
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
---

# Daemon: autonomous_agent_daemon

## Runtime
- Trigger: queue (watches .claude/inbox/ for new tasks)
- Interval: 60s poll cycle
- Owner: system-level (runs outside Claude session)

## Loop
1. Read task queue from `.claude/inbox/*.json`
2. Route task to agent_node via spawn_solo.ps1
3. Emit completion signal to `.claude/signals/`

## Safety
- Healthcheck: PID file exists + process responsive
- Restart policy: on_failure (max 3 retries, then alert)
- Stop condition: SIGTERM or `daemon.py stop` (reads PID)

## CLI
`daemon.py start|stop|status|run-once` — start backgrounds with PID, stop via SIGTERM, run-once for testing.
