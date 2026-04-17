---
id: p11_qg_schedule
kind: quality_gate
pillar: P11
title: "Gate: schedule"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "workflow scheduling — temporal trigger definitions that start workflows at declared times"
quality: 9.0
tags: [quality-gate, schedule, P12, cron, temporal-trigger, workflow-ref]
tldr: "Pass/fail gate for schedule artifacts: cron validity, timezone declaration, workflow_ref resolution, and policy completeness."
density_score: 0.90
llm_function: GOVERN
---
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
