---
kind: examples
id: bld_examples_daemon
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of daemon artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: daemon-builder
## Golden Example
INPUT: "Create daemon for a brain index rebuilder that runs every 6 hours"
OUTPUT:
```yaml
id: p04_daemon_brain_index_rebuilder
kind: daemon
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
name: "Brain Index Rebuilder"
schedule: "0 */6 * * *"
restart_policy: on_failure
signal_handling: "SIGTERM: finish current index batch, flush to disk, exit 0"
quality: null
tags: [daemon, brain, index, P04, background, scheduled]
tldr: "Brain index rebuilder: cron every 6h, on_failure restart, structured logging, 512MB limit"
description: "Periodic daemon that rebuilds BM25+FAISS brain indexes from pool artifacts every 6 hours"
health_check: "touch /tmp/brain_rebuild.heartbeat after each cycle; stale > 7h = alert"
pid_file: "/var/run/brain_rebuilder.pid"
resource_limits: "memory_max: 512MB, cpu_shares: 256, max_open_files: 1024"
monitoring: "prometheus metrics: rebuild_duration_seconds, artifacts_indexed_total, errors_total"
logging: structured
graceful_shutdown: "finish current file, write checkpoint, flush index, exit 0"
max_restarts: "3 in 30min"
```
## Overview
Rebuilds BM25 and FAISS brain search indexes from pool artifacts on a 6-hour cron schedule.
Used by brain_query consumers and all satellite agents that depend on search accuracy.
## Lifecycle
Schedule: cron `0 */6 * * *` (00:00, 06:00, 12:00, 18:00 UTC)
Startup: validate pool path exists, load checkpoint if present, begin indexing
Restart: on_failure — restart on non-zero exit; normal completion exits 0 (no restart)
Shutdown: finish current file, write checkpoint to resume next cycle, flush index to disk
## Signal Handling
| Signal | Response |
|--------|----------|
| SIGTERM | Finish current file, write checkpoint, flush, exit 0 |
| SIGINT | Same as SIGTERM |
| SIGHUP | Re-read config (pool path, index params) without restart |
| SIGUSR1 | Dump current progress (files indexed / total) to log |
## Monitoring
Health: heartbeat file `/tmp/brain_rebuild.heartbeat` touched after each cycle; stale > 7h triggers alert
Metrics: rebuild_duration_seconds, artifacts_indexed_total, index_size_bytes, errors_total
Alerting: PagerDuty if 2 consecutive cycles fail or heartbeat stale > 7h
Logging: structured JSON to stdout, rotated daily, 7-day retention
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_daemon_ pattern (H02 pass)
- kind: daemon (H04 pass)
- 21 required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Lifecycle, Signal Handling, Monitoring (H07 pass)
- schedule is concrete cron expression (H09 pass)
- signal_handling includes SIGTERM with clear behavior (S04 pass)
- restart_policy is valid enum: on_failure (S05 pass)
- tldr: 82 chars <= 160 (S01 pass)
- tags: 6 items, includes "daemon" (S02 pass)
## Anti-Example
INPUT: "Create daemon for log cleanup"
BAD OUTPUT:
```yaml
id: log-cleanup-daemon
kind: background_process
pillar: tools
name: Log Cleanup
schedule: periodically
restart_policy: "restart when it crashes"
quality: 8.0
tags: [cleanup]
```
Cleans up old log files.
## How it works
Deletes logs older than 7 days.
FAILURES:
1. id: "log-cleanup-daemon" uses hyphens and no `p04_daemon_` prefix -> H02 FAIL
2. kind: "background_process" not "daemon" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. schedule: "periodically" is vague, not concrete cron/interval -> H09 FAIL
6. restart_policy: free text, not valid enum -> S05 FAIL
7. Missing fields: version, created, updated, author, signal_handling, tldr -> H06 FAIL
8. tags: only 1 item, missing "daemon" -> S02 FAIL
9. Body missing ## Lifecycle, ## Signal Handling, ## Monitoring sections -> H07 FAIL
10. No signal_handling defined at all -> S04 FAIL
11. No health_check or monitoring strategy -> S08 FAIL
