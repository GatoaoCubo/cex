---
kind: knowledge_card
id: bld_knowledge_card_schedule
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for schedule production — temporal workflow trigger specification
sources: Airflow timetables, Dagster ScheduleDefinition, Temporal schedule, POSIX cron
quality: 9.1
title: "Knowledge Card Schedule"
version: "1.0.0"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_schedule_builder
  - schedule-builder
  - bld_examples_schedule
  - bld_instruction_schedule
  - bld_collaboration_schedule
  - p11_qg_schedule
  - p01_kc_schedule
  - bld_config_schedule
  - bld_architecture_schedule
  - bld_output_template_schedule
---

# Domain Knowledge: schedule
## Executive Summary
Schedules are temporal trigger definitions that determine WHEN a workflow starts. They are not the workflow itself (what runs), not a routing rule (which workflow handles a message), and not a hook (event-driven side effect). A schedule fires at a declared time, passes control to workflow_ref, and exits. All execution logic lives in the workflow.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (Orchestration) |
| llm_function | GOVERN (controls timing of workflow execution) |
| layer | runtime |
| core | false |
| machine_format | yaml |
| naming | p12_sched_{name}.md |
| max_bytes | 1024 |
| id_prefix | p12_sc |
## Trigger Types
| Type | Mechanism | When to use |
|------|-----------|-------------|
| cron | POSIX 5-field or 6-field expression | Fixed-clock recurrence (daily, weekly) |
| interval | Every N time units from last run | Polling, heartbeat, rate-based |
| event | External signal fires trigger | File arrival, webhook, queue message |
| manual | No automatic firing | On-demand by human or API call |
| one_shot | Single future execution, then disabled | Migration, one-time batch |
## Cron Expression Reference
| Expression | Meaning |
|-----------|---------|
| `0 9 * * MON-FRI` | 9:00 AM weekdays |
| `0 0 * * *` | Midnight daily |
| `0 */6 * * *` | Every 6 hours |
| `0 9 1 * *` | 9:00 AM first of each month |
| `*/15 * * * *` | Every 15 minutes |
## Patterns
- **Timezone-first**: always declare IANA timezone; UTC is a valid choice but must be explicit
- **Catch-up semantics**: Airflow `catchup=True` backfills all missed intervals on restart — dangerous for large gaps; default false
- **Dagster partition-aware**: ScheduleDefinition maps cron ticks to partition keys; schedule = WHEN, partition = WHAT DATA
- **Temporal durable timer**: schedule creates durable workflow starts; overlap_policy controls concurrent runs
- **Jitter pattern**: add random 0-Ns delay to stagger concurrent schedule starts across instances
| Pattern | Example | When to use |
|---------|---------|-------------|
| Fixed clock | `0 9 * * MON-FRI` | Business-hours report generation |
| Interval | every 5m | Polling, health-check workflows |
| Event-driven | on file arrival | ETL pipelines triggered by upstream data |
| One-shot | 2026-04-01 00:00 UTC | Migration, launch-day batch |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No timezone declared | DST transitions shift schedule by 1h silently |
| catch_up: true on daily schedules | Restart after 30-day outage fires 30 runs simultaneously |
| max_concurrent omitted | Slow workflow + fast schedule = unbounded parallelism |
| No jitter on shared infra | All shards hit DB at same second — thundering herd |
| Workflow logic in schedule | Coupling WHEN and WHAT makes both unmaintainable |
| Cron without explanation | `0 0 */2 * *` is ambiguous — always annotate |
## Application
1. Identify cadence: fixed-clock, interval, event, or one-shot?
2. Write cron expression, then annotate in plain English
3. Declare IANA timezone explicit — never rely on server default
4. Set catch_up: false unless backfill is explicitly required
5. Set max_concurrent: 1 unless workflow is proven idempotent and stateless
6. Add jitter if multiple schedule instances share infrastructure
7. Declare on-failure behavior: retry, alert, or skip
## References
- Airflow: `schedule_interval`, `catchup`, `max_active_runs`, `timetable`
- Dagster: `ScheduleDefinition`, `@schedule`, `cron_schedule`, `execution_timezone`
- Temporal: `ScheduleSpec`, `SchedulePolicy`, `overlap_policy`, `jitter`
- crontab.guru: interactive cron expression validator

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_schedule_builder]] | downstream | 0.55 |
| [[schedule-builder]] | downstream | 0.53 |
| [[bld_examples_schedule]] | downstream | 0.51 |
| [[bld_instruction_schedule]] | downstream | 0.51 |
| [[bld_collaboration_schedule]] | downstream | 0.49 |
| [[p11_qg_schedule]] | downstream | 0.47 |
| [[p01_kc_schedule]] | sibling | 0.47 |
| [[bld_config_schedule]] | downstream | 0.46 |
| [[bld_architecture_schedule]] | downstream | 0.46 |
| [[bld_output_template_schedule]] | downstream | 0.44 |
