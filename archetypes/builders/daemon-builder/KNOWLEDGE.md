---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for daemon production
sources: systemd conventions, process management patterns, Unix daemon standards
---

# Domain Knowledge: daemon

## Foundational Concept
A daemon artifact defines the LIFECYCLE SPECIFICATION for a persistent background process.
It specifies when the process runs (schedule), how it recovers (restart_policy), how it
responds to signals (signal_handling), and how operators monitor it (health_check). Daemons
are PERSISTENT: they run continuously or on a recurring schedule, unlike hooks (fire once)
or cli_tools (execute and exit).

## Schedule Patterns

| Pattern | Format | Use Case |
|---------|--------|----------|
| continuous | "continuous" | Always-running watchers, queue consumers |
| cron | "*/5 * * * *" | Periodic tasks (cleanup, sync, index rebuild) |
| interval | "every 30s" | Polling loops with fixed intervals |
| event-driven | "on:{event}" | Triggered by external event but stays alive |

Rule: every daemon MUST declare schedule — ambiguous lifecycle is a spec failure.

## Restart Policies

| Policy | Behavior | Use Case |
|--------|----------|----------|
| always | Restart regardless of exit code | Critical services that must run |
| on_failure | Restart only on non-zero exit | Tasks that may complete normally |
| never | Do not restart | One-shot scheduled tasks (prefer cli_tool) |

## Signal Handling Conventions

| Signal | Standard Behavior | Daemon Response |
|--------|-------------------|-----------------|
| SIGTERM | Graceful shutdown | Finish current work, flush buffers, exit 0 |
| SIGINT | Interrupt | Same as SIGTERM for daemons |
| SIGHUP | Reload config | Re-read config file without restart |
| SIGUSR1 | Custom | Dump status/metrics to log |

## Resource Limit Patterns
- memory_max: hard ceiling (OOM-kill if exceeded)
- cpu_shares: relative CPU allocation (not hard limit)
- max_open_files: file descriptor limit
- max_restarts: circuit breaker (stop restarting after N failures in window)

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT daemon |
|------|------------|---------------------|
| hook | Pre/post event trigger code | Hook fires once per event; daemon runs continuously |
| cli_tool | One-shot command-line execution | CLI tool exits after task; daemon persists |
| skill | Reusable invocable with phases | Skill is called on-demand; daemon runs independently |
| workflow | Orchestration of multiple steps | Workflow coordinates; daemon executes a single concern |
| connector | Bidirectional service bridge | Connector defines integration spec; daemon is process lifecycle |

## References
- systemd.service(5) — systemd unit file conventions
- daemon(7) — Linux daemon conventions
- Twelve-Factor App — Process management (factor VI)
