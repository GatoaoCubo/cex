---
kind: schema
id: bld_schema_schedule
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for schedule
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Schedule"
version: "1.0.1"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-18"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_schema_handoff_protocol
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_prompt_version
  - bld_schema_chunk_strategy
  - bld_schema_golden_test
  - bld_schema_workflow
  - bld_schema_smoke_eval
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
| nl_spec | string | NO | null | Natural-language spec (HERMES pattern, e.g. "every weekday at 9am") |
| nl_parser | string | NO | null | Parser used to convert nl_spec -> cron (e.g. "chrono", "supabase-wrappers") |
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_handoff_protocol]] | sibling | 0.67 |
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_constraint_spec]] | sibling | 0.64 |
| [[bld_schema_prompt_version]] | sibling | 0.63 |
| [[bld_schema_chunk_strategy]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.62 |
| [[bld_schema_workflow]] | sibling | 0.61 |
| [[bld_schema_smoke_eval]] | sibling | 0.61 |
