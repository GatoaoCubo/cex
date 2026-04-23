---
id: hibernation_policy_n05
kind: hibernation_policy
nucleus: n05
pillar: P09
mirrors: N00_genesis/P09_config/tpl_hibernation_policy.md
overrides:
  tone: strict, deterministic, gate-heavy
  voice: imperative, risk-averse
  sin_lens: IRA
  required_fields:
    - sla_target
    - failure_mode
    - rollback_procedure
  quality_threshold: 9.3
  density_target: 0.90
  example_corpus: 3+ examples with failure modes section
title: "N05 Operations -- Hibernation Policy (Idle Cost Guard)"
version: 1.0.0
quality: 8.2
tags: [mirror, n05, operations, hermes_assimilation, hibernation_policy]
tldr: "N05-owned idle-cost guard: per-backend hibernation triggers, wake SLA, state persistence, cost savings enforcement."
related:
  - enterprise-sla-builder
  - bld_tools_enterprise_sla
  - bld_collaboration_enterprise_sla
  - bld_knowledge_card_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - bld_collaboration_session_backend
  - p03_sp_cost_budget_builder
  - bld_memory_action_paradigm
  - p10_lr_cost_budget_builder
  - cost-budget-builder
---

## Ownership

N05 OWNS this kind. Operations controls hibernation behavior for all serverless
and hibernation-capable backends. IRA lens: idle resources are wasted money.

## Per-Backend Hibernation Matrix

| Backend | Idle Trigger | Threshold (s) | Wake Latency SLA | State Persist | Cost Savings Est |
|---------|-------------|---------------|------------------|---------------|------------------|
| daytona | no_activity | 600 | 8s | memory + disk | 75% |
| modal | no_requests | 300 | 5s | disk only | 80% |
| singularity | explicit_signal | 900 | 15s | disk snapshot | 60% |
| generic | no_activity | 900 | 10s | configurable | 70% |

## Idle Trigger Rules (IRA-Enforced)

| Trigger Type | Detection Method | Grace Period | Failure Mode |
|-------------|-----------------|-------------|--------------|
| no_activity_seconds | no tool calls, agent messages, or I/O | 0 (immediate after threshold) | hibernate + log |
| no_requests_seconds | no inbound HTTP/gRPC requests | 0 | hibernate + log |
| explicit_signal | N07 or orchestrator sends hibernate command | n/a | hibernate + log |

## Wake Conditions

| Condition | Priority | Max Latency | Failure Mode |
|-----------|----------|-------------|--------------|
| incoming_request | 1 (highest) | per SLA | queue request, wake, retry |
| scheduled_cron | 2 | SLA + 5s | alert if wake fails |
| explicit_signal | 3 | SLA + 10s | alert + fallback to fresh start |

## State Persistence (Per Backend)

| Backend | keep_memory | snapshot_disk | checkpoint_cadence (s) | Restore Verified |
|---------|------------|---------------|----------------------|-----------------|
| daytona | true | true | 60 | health check on wake |
| modal | false | true | 120 | function test on wake |
| singularity | false | true | 60 | bind mount verify |
| generic | true | true | 60 | configurable |

## Failure Modes

| Failure | Detection | Response | Escalation | SLA |
|---------|-----------|----------|------------|-----|
| Wake timeout | latency > SLA | retry 2x, then fresh start | oncall | SLA + 30s |
| State corruption | health check fail on wake | discard state, cold start | alert | 2min |
| Checkpoint failure | write error during snapshot | retry 1x, then skip | log + alert | 30s |
| Orphan hibernated instance | no wake in 24h | terminate + cleanup | log | 24h |
| Cost overshoot | billing > 2x estimate | force-hibernate + alert | N07 | 1h |

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Wake latency p99 | per backend SLA | warn at 80% SLA, page at 110% |
| Hibernation frequency | >20/hour/backend | warn (possible thrashing) |
| State restore failures | >0 | immediate alert |
| Cost savings actual vs estimate | <50% of estimate | weekly report |

## Rollback Procedure

| Step | Action | Gate |
|------|--------|------|
| 1 | Disable hibernation (set enabled: false) | config applied |
| 2 | Wake all hibernated instances | all instances healthy |
| 3 | Investigate root cause | cause identified |
| 4 | Re-enable with corrected thresholds | health check pass |

## Integration Points

- `terminal_backend` (P09): each hibernation policy pairs with a specific backend
- `sandbox_config` (P09): hibernated instances must respect sandbox on wake
- `schedule` (P12): pre-warm schedules prevent cold-start latency for known workloads
- `cost_budget` (P09): hibernation savings feed into budget tracking

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[enterprise-sla-builder]] | downstream | 0.24 |
| [[bld_tools_enterprise_sla]] | upstream | 0.23 |
| [[bld_collaboration_enterprise_sla]] | downstream | 0.20 |
| [[bld_knowledge_card_enterprise_sla]] | upstream | 0.18 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.18 |
| [[bld_collaboration_session_backend]] | downstream | 0.18 |
| [[p03_sp_cost_budget_builder]] | upstream | 0.17 |
| [[bld_memory_action_paradigm]] | downstream | 0.17 |
| [[p10_lr_cost_budget_builder]] | downstream | 0.17 |
| [[cost-budget-builder]] | related | 0.16 |
