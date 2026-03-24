---
id: p04_daemon_autonomous
name: autonomous_agent_daemon
description: "Background service orchestrating autonomous agent execution with start/stop/status lifecycle"
pid_file: records/core/python/autonomous/daemon.pid
restart_policy: on_failure
health_check: /status
max_retries: 3
check_interval: 60
lp: P04
type: daemon
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: orchestration
quality: 9.0
tags: [daemon, autonomous, background, agent, pipeline, orchestration]
---

# Autonomous Agent Daemon — Background Orchestration

## Purpose
Background service that orchestrates autonomous agent execution at system level. Manages the full agent pipeline with start/stop/status lifecycle, PID file tracking, and state persistence.

## Commands
```bash
python daemon.py start      # Start daemon (background)
python daemon.py stop       # Stop daemon (via PID file)
python daemon.py status     # Check running status
python daemon.py run-once   # Single execution (testing)
```

## Configuration
| Setting | Default | Env Var |
|---------|---------|---------|
| API URL | http://localhost:8000 | CODEXA_API_URL |
| API Key | (empty) | CODEXA_API_KEY |
| Model | claude-sonnet-4-20250514 | ANTHROPIC_API_KEY |
| Check interval | 60s | - |
| Max retries | 3 | - |

## Lifecycle
- **PID file**: `daemon.pid` — prevents duplicate instances
- **State file**: `daemon_state.json` — persists agent states across restarts
- **Log file**: `daemon.log` — structured logging with configurable level
- **Restart policy**: on_failure (auto-restart on crash, not on clean exit)

## Agent States
`IDLE` -> `RUNNING` -> `COMPLETED` or `FAILED`

Pipeline checks run every 60s. Failed agents retry up to 3x before escalation. Webhook notifications enabled for pipeline events.
