---
id: schedule_n05
kind: schedule
nucleus: n05
pillar: P12
mirrors: N00_genesis/P12_orchestration/templates/tpl_schedule.md
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
title: "N05 Operations -- Schedule (Maintenance Windows)"
version: 1.0.0
quality: 8.4
tags: [mirror, n05, operations, hermes_assimilation, schedule]
tldr: "N05 ops schedules: maintenance windows, backup cadence, cert rotation, health checks -- IRA-enforced cron with failure handling."
nl_spec: "Run maintenance tasks on schedule: daily health, weekly backup, monthly cert rotation"
related:
  - p12_schedule
  - p01_kc_schedule
  - bld_output_template_schedule
  - p03_sp_schedule_builder
  - p11_qg_schedule
  - bld_knowledge_card_schedule
  - p12_sched_daily_reindex
  - bld_instruction_schedule
  - bld_examples_schedule
  - bld_config_schedule
---

## Ops Schedule Matrix

N05 owns all operational schedules. IRA lens: missed schedules are incidents.
Every schedule has a failure mode and escalation path.

### Active Schedules

| Schedule | Cron | Timezone | SLA | Failure Mode | Rollback |
|----------|------|----------|-----|--------------|----------|
| health_check | `*/1 * * * *` | UTC | 2s | retry 3x, then alert | n/a |
| quality_sweep | `0 9 * * *` | America/Sao_Paulo | 30min | retry next day | n/a |
| backup_artifacts | `0 3 * * 0` | UTC | 2h | retry 1x, alert | n/a |
| cert_rotation | `0 9 1 * *` | UTC | 1h | alert at 75d age | block at 91d |
| log_rotation | `0 4 * * *` | UTC | 15min | alert | n/a |
| signal_cleanup | `0 5 * * *` | UTC | 10min | skip + log | n/a |
| orphan_process_scan | `*/5 * * * *` | UTC | 30s | log | n/a |
| mirror_audit | `0 10 * * 1` | America/Sao_Paulo | 1h | alert | n/a |

### Schedule Definition (Template)

```yaml
id: "sched_n05_{{name}}"
name: "{{human_readable}}"
cron: "{{CRON}}"
timezone: "{{TZ}}"
enabled: true
task:
  command: "{{COMMAND}}"
  working_dir: "."
  timeout_s: {{TIMEOUT}}
  env:
    CEX_NUCLEUS: "n05"
  on_success: log
  on_failure: retry
```

### Retry Policy (IRA-Enforced)

| Attempt | Delay | Action | Gate |
|---------|-------|--------|------|
| 1st failure | 60s | Retry automatically | same conditions |
| 2nd failure | 300s | Retry with alert | oncall notified |
| 3rd failure | -- | Skip + page oncall | incident created |

### Failure Modes

| Failure | Detection | Response | Escalation |
|---------|-----------|----------|------------|
| Cron daemon down | no execution at expected time | restart daemon | page oncall |
| Task timeout | duration > timeout_s | kill + retry | alert |
| Task crash | exit code != 0 | retry per policy | alert at 3rd |
| Overlapping runs | lock file exists | skip + log | warn |
| Timezone drift | clock skew >30s | alert | infra team |

### Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Missed schedules (24h) | 0 | alert on any miss |
| Success rate (7d) | >98% | warn at 95%, page at 90% |
| Avg execution time | <SLA | warn at 80% SLA |
| Consecutive failures | <2 | alert at 2, page at 3 |

### Maintenance Windows

| Window | When | Duration | Impact |
|--------|------|----------|--------|
| Weekly full backup | Sunday 03:00 UTC | 2h | read-only during backup |
| Monthly cert rotation | 1st of month 09:00 UTC | 1h | brief connection drops |
| Quarterly audit | 1st Mon of quarter | 4h | no impact (read-only) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_schedule]] | sibling | 0.50 |
| [[p01_kc_schedule]] | related | 0.28 |
| [[bld_output_template_schedule]] | upstream | 0.27 |
| [[p03_sp_schedule_builder]] | upstream | 0.27 |
| [[p11_qg_schedule]] | upstream | 0.24 |
| [[bld_knowledge_card_schedule]] | upstream | 0.24 |
| [[p12_sched_daily_reindex]] | sibling | 0.24 |
| [[bld_instruction_schedule]] | upstream | 0.24 |
| [[bld_examples_schedule]] | upstream | 0.23 |
| [[bld_config_schedule]] | upstream | 0.23 |
