---
kind: schema
id: bld_schema_schedule
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for schedule
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: schedule
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_sc_{slug}) | YES | - | Namespace compliance |
| kind | literal "schedule" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable schedule name |
| trigger_type | enum: cron, interval, event, manual, one_shot | YES | - | Trigger mechanism |
| cron | string (cron expression) | YES | - | e.g. "0 9 * * MON-FRI" |
| workflow_ref | string | YES | - | ID of workflow to trigger |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "schedule" |
| tldr | string <= 160ch | YES | - | Dense summary |
| timezone | string | REC | "UTC" | e.g. "America/Sao_Paulo" |
| enabled | boolean | REC | true | Active or paused |
| start_date | date YYYY-MM-DD | REC | - | Earliest trigger date |
| end_date | date or null | REC | null | Latest trigger date |
| max_concurrent | integer | REC | 1 | Max parallel runs |
| catch_up | boolean | REC | false | Run missed schedules on restart |
| jitter | string | REC | - | Random delay e.g. "0-30s" |
| description | string <= 200ch | REC | - | What this schedule triggers |
## ID Pattern
Regex: `^p12_sc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this schedule triggers, frequency, purpose
2. `## Trigger` — cron expression explained, timezone, enabled status
3. `## Workflow` — which workflow runs, expected duration, dependencies
4. `## Policy` — catch-up, max concurrent, jitter, failure handling
## Constraints
- max_bytes: 1024 (body only — compact schedule spec)
- naming: p12_sched_{name}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- cron field MUST be valid 5-field or 6-field cron expression
- workflow_ref MUST reference an existing workflow id
- quality: null always
- NO implementation code in body — spec only
