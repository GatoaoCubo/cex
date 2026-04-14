---
id: p11_qg_daemon
kind: quality_gate
pillar: P11
title: "Gate: daemon"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "daemon — persistent background processes with lifecycle management"
quality: 9.0
tags: [quality-gate, daemon, background-process, lifecycle, P11]
tldr: "Gates for daemon artifacts: validates lifecycle completeness, signal handling, health checks, and restart policy correctness."
density_score: 0.91
llm_function: GOVERN
---
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
