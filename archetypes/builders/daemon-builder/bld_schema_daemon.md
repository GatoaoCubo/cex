---
kind: schema
id: bld_schema_daemon
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for daemon
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Daemon"
version: "1.0.0"
author: n03_builder
tags: [daemon, builder, examples]
tldr: "Golden and anti-examples for daemon construction, demonstrating ideal structure and common pitfalls."
domain: "daemon construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_constraint_spec
  - bld_schema_prompt_version
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
  - bld_schema_golden_test
  - bld_schema_agent_card
---

# Schema: daemon
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_daemon_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "daemon" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable daemon name |
| schedule | string | YES | - | "continuous", cron expr, or interval |
| restart_policy | enum: always, on_failure, never | YES | - | Restart behavior |
| signal_handling | string | YES | - | SIGTERM + other signals summary |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "daemon" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the daemon does |
| health_check | string | REC | - | Health check strategy |
| pid_file | string | REC | - | PID file path |
| resource_limits | string | REC | - | CPU, memory, fd limits summary |
| monitoring | string | REC | - | Metrics and alerting summary |
| logging | enum: structured, plaintext, syslog | REC | structured | Log format |
| graceful_shutdown | string | REC | - | Shutdown procedure summary |
| max_restarts | string | REC | - | Circuit breaker (N in window) |
## ID Pattern
Regex: `^p04_daemon_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the daemon does, why it runs in background, who depends on it
2. `## Lifecycle` — schedule, startup sequence, restart policy, graceful shutdown
3. `## Signal Handling` — response to SIGTERM, SIGINT, SIGHUP, costm signals
4. `## Monitoring` — health check, metrics, alerting, log rotation
## Constraints
- max_bytes: 1024 (body only — compact daemon spec)
- naming: p04_daemon_{name_slug}.md + .yaml (dual file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- schedule MUST be concrete (cron, interval, or "continuous")
- quality: null always
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.69 |
| [[bld_schema_memory_scope]] | sibling | 0.68 |
| [[bld_schema_handoff_protocol]] | sibling | 0.68 |
| [[bld_schema_output_validator]] | sibling | 0.68 |
| [[bld_schema_constraint_spec]] | sibling | 0.66 |
| [[bld_schema_prompt_version]] | sibling | 0.66 |
| [[bld_schema_chunk_strategy]] | sibling | 0.65 |
| [[bld_schema_smoke_eval]] | sibling | 0.65 |
| [[bld_schema_golden_test]] | sibling | 0.64 |
| [[bld_schema_agent_card]] | sibling | 0.63 |
