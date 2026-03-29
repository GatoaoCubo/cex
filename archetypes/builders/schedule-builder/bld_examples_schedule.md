---
kind: examples
id: bld_examples_schedule
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of schedule artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
author: "EDISON"
name: "Daily Sales Report Schedule"
trigger_type: cron
cron: "0 9 * * MON-FRI"
workflow_ref: "p13_wf_daily_sales_report"
quality: null
tags: [schedule, sales, daily-report, P12]
tldr: "Triggers daily-sales-report workflow at 9 AM Sao Paulo time, Mon-Fri. max_concurrent 1, catch_up false."
timezone: "America/Sao_Paulo"
enabled: true
start_date: "2026-04-01"
end_date: null
max_concurrent: 1
catch_up: false
jitter: "0-60s"
description: "Weekday morning trigger for sales report consolidation workflow. Fires after overnight ETL completes."
```
## Overview
Triggers the daily sales report workflow each weekday morning in Sao Paulo business hours.
Designed to fire after overnight data pipeline completes (~8:30 AM) with 60s jitter buffer.
## Trigger
- Expression: `0 9 * * MON-FRI` — 9:00 AM Monday through Friday
- Timezone: America/Sao_Paulo (UTC-3, UTC-2 during summer time)
- Enabled: true
- Trigger type: cron
## Workflow
- Workflow: `p13_wf_daily_sales_report`
- Expected duration: 8-12 minutes
- Dependencies: overnight ETL must complete before 9 AM; upstream tables: orders, products, customers
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
