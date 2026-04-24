---
id: p10_memory_deploy_history
kind: runtime_state
8f: F8_collaborate
pillar: P10
title: Deploy History Memory
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: deployment-operations
quality: 8.9
tags: [runtime_state, memory, operations, N05, deploy, history]
tldr: "Persistent deploy history tracking every deployment with evidence, timing, health status, rollback events, and incident correlation."
density_score: 0.95
related:
  - p03_sp_deploy_ops
  - p02_agent_deploy_ops
  - bld_schema_experiment_tracker
  - bld_schema_model_registry
  - p10_ck_railway_deploy_checkpoint
  - p05_output_deploy_checklist
  - p08_adr_001_railway_topology
  - bld_schema_validation_schema
  - bld_schema_nps_survey
  - p05_output_rollback_plan
---

# Deploy History Memory

## Purpose

This memory artifact tracks the history of all deployments to Railway.
Every deploy, rollback, and incident is recorded with evidence.
This memory enables pattern detection (recurring failures), trend
analysis (deploy frequency, success rate), and incident correlation.

## Schema

```yaml
deploy_entry:
  id: "deploy_{YYYYMMDD}_{HHMMSS}_{service}"
  timestamp: ISO-8601
  service: "api | frontend | dashboard | gateway"
  trigger: "git_push | manual | workflow_dispatch | rollback"
  branch: string
  commit_sha: string (short)
  status: "success | failed | rolled_back"
  duration_s: number
  health_check:
    endpoint: "/health"
    response_code: number
    response_time_ms: number
    healthy: boolean
  smoke_eval:
    passed: boolean
    checks_passed: number
    checks_total: number
  evidence:
    logs_hash: string
    health_json_hash: string
    env_vars_validated: number
  rollback:
    triggered: boolean
    reason: string | null
    rollback_duration_s: number | null
    recovery_verified: boolean | null
  incident_id: string | null
  notes: string | null
```

## Deploy Log

| date | service | status | duration | health_ms | smoke | notes |
|------|---------|--------|----------|-----------|-------|-------|
| 2026-04-07 | api | — | — | — | — | Memory initialized, no deploys recorded yet |

## Metrics

| metric | value | updated |
|--------|-------|---------|
| total_deploys | 0 | 2026-04-07 |
| success_rate | N/A | 2026-04-07 |
| avg_duration_s | N/A | 2026-04-07 |
| rollback_count | 0 | 2026-04-07 |
| last_deploy | N/A | 2026-04-07 |
| last_incident | N/A | 2026-04-07 |

## Pattern Detection

After 10+ deploys, analyze for:

- **Recurring failure services**: Which service fails most?
- **Time-of-day correlation**: Do deploys at certain hours fail more?
- **Commit size correlation**: Do large diffs correlate with failures?
- **Health check latency trends**: Is health response time degrading?
- **Rollback frequency**: Is rollback rate increasing?

## Retention

| field | value |
|-------|-------|
| entries_kept | Last 100 deploys |
| archive | Monthly archive to `.cex/runtime/archive/deploys/` |
| cleanup | Auto-purge entries older than 365 days |

## Boundary

Estado mental variavel acumulado em runtime. NAO eh mental_model P02 (identidade fixa do agente, imutavel) nem session_state (efemero, snapshot).


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_deploy_ops]] | upstream | 0.28 |
| [[p02_agent_deploy_ops]] | upstream | 0.27 |
| [[bld_schema_experiment_tracker]] | upstream | 0.27 |
| [[bld_schema_model_registry]] | upstream | 0.26 |
| [[p10_ck_railway_deploy_checkpoint]] | related | 0.26 |
| [[p05_output_deploy_checklist]] | upstream | 0.25 |
| [[p08_adr_001_railway_topology]] | upstream | 0.25 |
| [[bld_schema_validation_schema]] | upstream | 0.25 |
| [[bld_schema_nps_survey]] | upstream | 0.24 |
| [[p05_output_rollback_plan]] | upstream | 0.24 |
