---
kind: quality_gate
id: p11_qg_daemon
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of daemon artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: daemon"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, daemon, background-process, lifecycle, P11]
tldr: "Gates for daemon artifacts: validates lifecycle completeness, signal handling, health checks, and restart policy correctness."
domain: "daemon — persistent background processes with lifecycle management"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - bld_examples_daemon
  - bld_knowledge_card_daemon
  - p03_sp_daemon_builder
  - bld_output_template_daemon
  - bld_instruction_daemon
  - daemon-builder
  - bld_architecture_daemon
  - p11_qg_chunk_strategy
  - p11_qg_cli_tool
  - p11_qg_schedule
---

## Quality Gate

# Gate: daemon
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: daemon` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p04_d_[a-z][a-z0-9_]+$` | "ID fails daemon namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"daemon"` | "Kind is not 'daemon'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, schedule, restart_policy, signal_handling, health_check, version, created, author, tags | "Missing required field(s)" |
| H07 | `restart_policy` is one of: `always`, `on-failure`, `unless-stopped`, `never` | "Invalid restart_policy value" |
| H08 | `signal_handling` contains at minimum `SIGTERM` entry with defined action | "SIGTERM handler not defined" |
| H09 | `health_check` includes `endpoint` or `command` plus `interval_seconds` | "Health check definition incomplete" |
| H10 | `schedule` is valid cron expression or literal `continuous` | "Schedule is not valid cron or 'continuous'" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Lifecycle completeness | 1.0 | start, stop, restart, and graceful shutdown all defined |
| Signal handling depth | 1.0 | SIGTERM + SIGINT + SIGHUP covered with distinct actions |
| Health check quality | 1.0 | interval, timeout, failure_threshold, and recovery action defined |
| Resource limits | 0.5 | CPU and memory limits specified (not just documented) |
| PID management | 0.5 | PID file path and cleanup on exit defined |
| Logging config | 1.0 | log level, rotation policy, and output destination specified |
| Monitoring strategy | 1.0 | metrics exported or alerting conditions documented |
| Boundary clarity | 0.5 | explicitly not hook/skill/workflow in scope comment |
| Restart policy rationale | 0.5 | reason for chosen restart_policy explained |
| Schedule precision | 1.0 | cron expression correct, timezone specified if relevant |
| Error handling | 1.0 | what happens on crash, max retries, backoff strategy |
| Documentation | 1.0 | tldr, purpose, and operational runbook link or inline |
Weight sum: 1.0+1.0+1.0+0.5+0.5+1.0+1.0+0.5+0.5+1.0+1.0+1.0 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Emergency production incident requiring immediate daemon deploy |
| approver | Senior architect sign-off required (written record) |
| audit_trail | Bypass event logged to `records/audits/daemon_bypass_{date}.md` |
| expiry | 48h; artifact must reach >= 7.0 within expiry or be pulled |
| never_bypass | H01 (invalid YAML breaks all tooling), H05 (null quality is a system invariant) |

## Examples

# Examples: daemon-builder
## Golden Example
INPUT: "Create daemon for a brain index rebuilder that runs every 6 hours"
OUTPUT:
```yaml
id: p04_daemon_knowledge_index_rebuilder
kind: daemon
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
name: "Brain Index Rebuilder"
schedule: "0 */6 * * *"
restart_policy: on_failure
signal_handling: "SIGTERM: finish current index batch, flush to disk, exit 0"
quality: 8.9
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
Used by brain_query consumers and all agent nodes that depend on search accuracy.
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
