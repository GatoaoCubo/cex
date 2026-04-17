---
id: n00_daemon_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Daemon -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, daemon, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A daemon is a long-running background process that monitors conditions, polls signals, or continuously processes incoming events without direct user interaction. In CEX, daemons implement the autonomous lifecycle loop: watching for nucleus completion signals, polling git log for commits, and triggering consolidation when wave gates pass. The output is a managed background service definition with health checks, restart policy, and observability hooks.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `daemon` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| trigger | string | yes | What activates daemon action: poll_interval, signal, event |
| poll_interval_seconds | integer | no | Polling frequency when trigger is poll_interval |
| health_check | string | no | Command or URL to verify daemon liveness |
| restart_policy | string | yes | never, on-failure, always |

## When to use
- When N07 needs a background monitor that watches for nucleus signal completion
- When building a continuous quality monitoring loop (cex_quality_monitor.py pattern)
- When the pipeline requires an event-driven trigger that does not block the main agent loop

## Builder
`archetypes/builders/daemon-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind daemon --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: daemon_signal_watcher
kind: daemon
pillar: P04
nucleus: n07
title: "Signal Watcher Daemon"
version: 1.0
quality: null
---
trigger: poll_interval
poll_interval_seconds: 60
restart_policy: on-failure
health_check: "ls .cex/runtime/signals/ | wc -l"
```

## Related kinds
- `hook` (P04) -- event hook triggered by daemon condition detection
- `schedule` (P12) -- cron-based alternative to poll-based daemon triggers
- `workflow` (P12) -- orchestration layer that a daemon monitors for completion
- `notifier` (P04) -- delivery channel for daemon alerts and status reports
