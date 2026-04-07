---
kind: knowledge_card
id: bld_knowledge_card_daemon
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for daemon production — persistent background process specification
sources: systemd.service(5), daemon(7) Linux conventions, 12-Factor App process model
quality: 9.1
title: "Knowledge Card Daemon"
version: "1.0.0"
author: n03_builder
tags: [daemon, builder, examples]
tldr: "Golden and anti-examples for daemon construction, demonstrating ideal structure and common pitfalls."
domain: "daemon construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: daemon
## Executive Summary
Daemons are persistent background processes that run continuously or on schedule. They define lifecycle (start/stop/restart), signal handling (SIGTERM, SIGHUP), health checks, resource limits, and monitoring. Daemons differ from hooks (single event trigger), CLI tools (execute and exit), skills (invocable on-demand), and workflows (multi-step orchestration).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | GOVERN (lifecycle management) |
| Frontmatter fields | 20+ |
| Quality gates | 9 HARD + 12 SOFT |
| Schedule types | continuous, cron, interval, event-driven |
| Restart policies | always, on_failure, never |
| Key sections | schedule, restart_policy, signal_handling, health_check, resources |
## Patterns
- **Schedule declaration**: every daemon MUST declare schedule type — ambiguous lifecycle is a spec failure
| Schedule | Format | Use case |
|----------|--------|----------|
| continuous | "continuous" | Always-running watchers, queue consumers |
| cron | "*/5 * * * *" | Periodic cleanup, sync, index rebuild |
| interval | "every 30s" | Polling loops with fixed intervals |
| event-driven | "on:{event}" | Triggered but stays alive between events |
- **Signal handling**: standard Unix signals with defined daemon responses
| Signal | Response |
|--------|----------|
| SIGTERM | Graceful shutdown: finish work, flush, exit 0 |
| SIGINT | Same as SIGTERM for daemons |
| SIGHUP | Reload config without restart |
| SIGUSR1 | Dump status/metrics to log |
- **Resource limits**: memory_max (hard ceiling), cpu_shares (relative), max_open_files, max_restarts (circuit breaker)
- **Health checks**: periodic probes confirming process is alive and functional, not just running
- **PID management**: write PID file on start, remove on graceful stop, check for stale PID on restart
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No schedule declared | Ambiguous lifecycle; operators cannot manage process |
| Missing SIGTERM handler | Process killed ungracefully; data loss, corruption |
| No max_restarts limit | Crash loop consumes resources indefinitely |
| restart: always for optional tasks | Non-critical tasks should use on_failure |
| No health check | Dead process detected only when users report failures |
| Missing resource limits | Runaway daemon consumes all system memory/CPU |
## Application
1. Define schedule: continuous, cron, interval, or event-driven
2. Set restart policy: always (critical), on_failure (standard), never (one-shot)
3. Implement signal handlers: SIGTERM (graceful), SIGHUP (reload), SIGUSR1 (status)
4. Configure health check: endpoint or command, interval, failure threshold
5. Set resource limits: memory, CPU, file descriptors, max restarts
6. Validate: schedule is explicit, signals handled, limits defined
## References
- systemd.service(5): unit file conventions and lifecycle management
- daemon(7): Linux daemon programming conventions
- 12-Factor App: process model and disposability (Factors VI, IX)
- Kubernetes: liveness/readiness probes for container health
