---
kind: quality_gate
id: p11_qg_schedule
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of schedule artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: schedule"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, schedule, P12, cron, temporal-trigger, workflow-ref]
tldr: "Pass/fail gate for schedule artifacts: cron validity, timezone declaration, workflow_ref resolution, and policy completeness."
domain: "workflow scheduling — temporal trigger definitions that start workflows at declared times"
created: "2026-03-29"
updated: "2026-03-29"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_examples_schedule
  - bld_instruction_schedule
  - p03_sp_schedule_builder
  - schedule-builder
  - bld_schema_schedule
  - bld_output_template_schedule
  - bld_knowledge_card_schedule
  - bld_collaboration_schedule
  - bld_architecture_schedule
  - p01_kc_schedule
---

## Quality Gate

# Gate: schedule
## Definition
| Field | Value |
|---|---|
| metric | schedule artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: schedule` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p12_sc_[a-z][a-z0-9_]+$` | ID has hyphens, uppercase, or wrong prefix |
| H03 | ID equals filename stem | `id: p12_sc_daily` but file is `p12_sched_weekly.md` |
| H04 | Kind equals literal `schedule` | `kind: cron` or `kind: trigger` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `trigger_type`, `cron`, or `workflow_ref` |
| H07 | Cron is valid 5-field or 6-field expression | `cron: "every day"` or malformed expression |
| H08 | trigger_type is a recognized enum value | `trigger_type: scheduled` or unrecognized value |
| H09 | workflow_ref is non-empty string | `workflow_ref: ""` or field absent |
| H10 | Schedule is not a workflow definition | Body does not contain step execution logic — WHEN only, not WHAT |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Cron expression clarity | 1.0 | Plain-English explanation of the cron expression in ## Trigger section |
| Timezone declaration | 1.0 | Explicit IANA timezone; not defaulting silently to UTC |
| Workflow ref traceability | 1.0 | workflow_ref resolves to a known workflow id in the cex corpus |
| Policy completeness | 1.0 | catch_up, max_concurrent, jitter all declared with rationale |
| Enabled status documented | 0.5 | enabled field present; paused schedules explain why |
| Date range documented | 0.5 | start_date and end_date (or null) explicitly declared |
| Failure handling declared | 1.0 | On-failure behavior in ## Policy (retry/alert/skip with reason) |
| Jitter rationale | 0.5 | Jitter value explained — why this range prevents thundering herd |
| Concurrency rationale | 1.0 | max_concurrent value justified relative to workflow idempotency |
| Boundary clarity | 1.0 | Explicitly not a dispatch_rule, workflow, or hook — WHEN-only contract |
| Domain specificity | 1.0 | Schedule names, tags, and description specific to the declared domain |
| Catch-up semantics | 0.5 | catch_up false/true with explanation of backfill behavior |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Placeholder schedule created during workflow scaffolding, not yet wired to real workflow |
| approver | Author self-certification with comment noting workflow_ref is pending |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — placeholder schedules must be wired or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates corrupt metrics), H07 (invalid cron fires at wrong time) |

## Examples

# Examples: schedule-builder
## Golden Example
INPUT: "Create a schedule that runs the daily sales report workflow every weekday at 9 AM Sao Paulo time"
OUTPUT:
```yaml
id: p12_sc_daily_sales_report
kind: schedule
pillar: P12
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Daily Sales Report Schedule"
trigger_type: cron
cron: "0 9 * * MON-FRI"
workflow_ref: "p13_wf_daily_sales_report"
quality: 8.9
tags: [schedule, sales, daily-report, P12]
tldr: "Triggers daily-sales-report workflow at 9 AM Sao Paulo time, Mon-Fri. max_concurrent 1, catch_up false."
timezone: "America/Sao_Paulo"
enabled: true
start_date: "2026-04-01"
end_date: null
max_concurrent: 1
catch_up: false
jitter: "0-60s"
description: "Weekday morning trigger for sales report consolidation workflow. Fires after overnight ETL complete."
```
## Overview
Triggers the daily sales report workflow each weekday morning in Sao Paulo business hours.
Designed to fire after overnight data pipeline complete (~8:30 AM) with 60s jitter buffer.
## Trigger
- Expression: `0 9 * * MON-FRI` — 9:00 AM Monday through Friday
- Timezone: America/Sao_Paulo (UTC-3, UTC-2 during summer time)
- Enabled: true
- Trigger type: cron
## Workflow
- Workflow: `p13_wf_daily_sales_report`
- Expected duration: 8-12 minutes
- Dependencies: overnight ETL must complete before 9 AM; upstream tables: orders, products, costmers
## Policy
- Catch-up: false — missed days are not backfilled; report is generated on next scheduled run
- Max concurrent: 1 — workflow writes to shared reporting tables; parallel runs would corrupt output
- Jitter: 0-60s — staggers start against other 9 AM schedules sharing the same DB cluster
- On failure: alert — notify #data-alerts Slack channel; do not auto-retry (data consistency risk)

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p12_sc_[a-z][a-z0-9_]+$` (H02 pass)
- kind: schedule (H04 pass)
- cron: valid 5-field expression (H07 pass)
- trigger_type: cron (recognized enum, H08 pass)
- workflow_ref non-empty (H09 pass)
- body has all 4 sections: Overview, Trigger, Workflow, Policy (H10 pass)
- timezone: explicit IANA name (SOFT pass)
- catch_up declared with rationale (SOFT pass)
- max_concurrent declared with rationale (SOFT pass)
- jitter declared with thundering-herd rationale (SOFT pass)
- on-failure declared in Policy (SOFT pass)
- cron annotated in plain English (SOFT pass)

## Anti-Example
INPUT: "Create a schedule for the report workflow"
BAD OUTPUT:
```yaml
id: report-schedule
kind: trigger
pillar: orchestration
cron: every day at 9
workflow_ref: report
quality: 8.5
tags: [schedule]
```
Runs the report every day.
FAILURES:
1. id: "report-schedule" has hyphens and no `p12_sc_` prefix -> H02 FAIL
2. kind: "trigger" not "schedule" -> H04 FAIL
3. pillar: "orchestration" not "P12" -> H06 FAIL
4. cron: "every day at 9" is not a valid cron expression -> H07 FAIL
5. quality: 8.5 (not null) -> H05 FAIL
6. Missing fields: trigger_type, version, created, updated, author, tldr -> H06 FAIL
7. tags: only 1 item, missing "schedule" (needs >= 3) -> SOFT FAIL
8. No timezone declared — DST will shift schedule silently -> SOFT FAIL
9. No Policy section — catch_up, max_concurrent, jitter all absent -> SOFT FAIL
10. workflow_ref: "report" is not a resolvable id -> SOFT FAIL
11. Body missing ## Trigger, ## Workflow, ## Policy sections -> H10 FAIL

## Golden Example 2 (HERMES — Natural Language Schedule)
INPUT: "Create a schedule that runs the overnight evolution loop every weekday at midnight; specify it in plain English"
OUTPUT:
```yaml
id: p12_sc_overnight_evolution
kind: schedule
pillar: P12
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n07_orchestrator"
name: "Overnight Evolution Loop Schedule"
trigger_type: cron
cron: "0 0 * * MON-FRI"
workflow_ref: "p12_wf_overnight_evolution"
quality: null
tags: [schedule, evolution, overnight, hermes, P12]
tldr: "Triggers overnight artifact evolution at midnight Mon-Fri; nl_spec parsed by chrono to cron"
timezone: "America/Sao_Paulo"
enabled: true
start_date: "2026-04-18"
end_date: null
max_concurrent: 1
catch_up: false
jitter: "0-120s"
description: "Midnight weekday trigger for autonomous artifact evolution loop (cex_evolve.py sweep)."
nl_spec: "every weekday at midnight Sao Paulo time"
nl_parser: "chrono"
```
## Overview
Triggers the overnight artifact evolution workflow each weekday midnight in Sao Paulo.
nl_spec provides the human-readable intent; chrono parser compiles it to the cron expression.
## Trigger
- Expression: `0 0 * * MON-FRI` -- midnight Monday through Friday
- nl_spec: "every weekday at midnight Sao Paulo time" (chrono-parsed)
- nl_parser: chrono (deterministic NL-to-cron converter)
- Timezone: America/Sao_Paulo
## Workflow
- Workflow: `p12_wf_overnight_evolution`
- Expected duration: 90-180 minutes
- Dependencies: None; evolution loop is self-contained
## Policy
- Catch-up: false -- missed overnight runs are not retried; next scheduled run takes over
- Max concurrent: 1 -- evolution writes to shared artifact store
- Jitter: 0-120s -- staggers against other midnight cron jobs

WHY THIS IS GOLDEN (HERMES nl_spec fields):
- `nl_spec`: captures the human intent verbatim for auditability and re-parsing
- `nl_parser: chrono`: explicit parser declaration enables deterministic reproduction
- cron field is the machine-executable form; nl_spec is the human-verifiable source-of-truth

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
