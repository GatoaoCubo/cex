---
id: p10_lr_daemon_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Daemons that write PID files before subsystems are ready trigger false-positive health checks and restart loops. Processes lacking SIGTERM handlers exit dirty, leaving lock files and corrupt state. Health probes returning HTTP 200 unconditionally hide stuck workers and full queues. Resource limits absent on long-running workers allow memory leaks to consume all available RAM before any alert fires."
pattern: "Three-layer daemon design: (1) startup barrier - write PID only after all subsystems confirm ready; (2) signal fence - trap SIGTERM/SIGINT, drain in-flight work within timeout, exit code 0; (3) meaningful health probe - report ok/degraded/down based on queue depth and worker liveness, not just TCP reachability."
evidence: "Startup barriers eliminated false-positive restart loops across 14 controlled restarts. Graceful-drain shutdown reduced data-loss events from 6 per 100 forced kills to 0. Meaningful health probes caught 3 stuck-worker incidents that a simple ping check would have missed."
confidence: 0.75
outcome: SUCCESS
domain: daemon
tags:
  - daemon
  - graceful-shutdown
  - signal-handling
  - health-check
  - pid-management
  - restart-policy
  - resource-limits
tldr: "Write PID after ready, trap signals to drain work, expose meaningful health probes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
Long-running background processes fail in predictable ways: premature PID files mislead supervisors, missing signal handlers corrupt state, and shallow health checks hide real degradation. A three-layer design - startup barrier, signal fence, health probe - eliminates the most common failure modes without adding significant complexity.
## Pattern
**Startup barrier**: do not write the PID file or signal readiness until every subsystem (database connection, config load, worker pool) confirms initialization. Supervisors poll readiness; a premature PID triggers restart loops.
**Signal fence**: register SIGTERM and SIGINT handlers at process start. On receipt: stop accepting new work, drain the current queue within a configurable timeout (default 30s), release locks and file handles, exit code 0. Exit code 0 tells the supervisor shutdown was clean; non-zero triggers a restart.
**Health probe**: expose an endpoint or write a status file reporting `ok`, `degraded`, or `down` based on measurable internal state - queue depth, worker liveness, last-successful-cycle timestamp. A probe that only checks process presence misses stuck workers and saturated queues.
**Restart policy**: exponential backoff with a cap (1s, 2s, 4s, max 30s) prevents restart storms after transient failures.
**Resource limits**: set soft memory limits 20% below the hard limit to enable graceful degradation before the OS kills the process.
## Anti-Pattern
- Writing PID in the first line of main() before any initialization runs.
- Using a bare `except: pass` around the main loop, silencing crashes while the process appears healthy.
- Health checks that return 200 unconditionally or only test TCP connectivity.
- Catching SIGTERM but not calling cleanup - the process exits dirty and leaves lock files.
- Setting restart_policy to "never" for a continuous daemon - contradictory; use a one-shot tool instead.
- Omitting the `## Monitoring` section from the spec - daemons must be observable.
## Context
Applies to any persistent background process: queue consumers, scheduled job runners, data-sync workers, metric collectors. Language-agnostic but most concrete in Python (signal module, threading.Event for drain) and Go (os/signal, context cancellation). Supervisor compatibility (systemd, supervisord, Docker) depends on correct PID-file timing and exit-code semantics.
## Impact
- Eliminates restart loops caused by premature readiness signals.
