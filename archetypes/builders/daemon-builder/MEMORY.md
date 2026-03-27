---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: daemon-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p04_daemon_brain_rebuilder not p04_daemon_brain-rebuilder)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. Vague schedule like "periodically" or "regularly" (must be concrete: cron, interval, or "continuous")
4. Missing signal_handling field (required — daemon MUST define SIGTERM behavior)
5. Confusing daemon with hook (daemon persists, hook fires once per event)
6. Including implementation code in body (this is a spec, not source)
7. restart_policy: "restart" instead of valid enum (always, on_failure, never)
8. Missing ## Monitoring section (required — daemons must be observable)
9. No graceful_shutdown procedure (just "exit" is insufficient — flush state first)
10. Setting restart_policy: never for continuous daemon (contradictory — use cli_tool instead)

### Daemon Archetypes
| Archetype | Schedule | Restart | Example |
|-----------|----------|---------|---------|
| Watcher | continuous | always | File watcher, queue consumer |
| Cron Job | cron expr | on_failure | Index rebuild, cleanup |
| Poller | interval | always | API polling, health monitor |
| Event Loop | continuous | always | Event processor, stream reader |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | vague schedule, missing signal handling, daemon vs hook confusion |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a daemon, update:
- New common mistake (if encountered)
- New daemon archetype (if discovered)
- Production counter increment
