---
quality: 8.2
quality: 7.8
kind: schema
id: bld_schema_prospective_memory
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema for prospective_memory
title: "Schema Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, schema]
tldr: "Schema for prospective_memory: reminders array with trigger/payload/priority/expiry, owner, execution_mechanism."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_search_strategy
  - bld_schema_multimodal_prompt
---

# Schema: prospective_memory

## Frontmatter Fields
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string (p10_pm_{slug}) | YES | Namespace compliance |
| kind | literal "prospective_memory" | YES | Type integrity |
| pillar | literal "P10" | YES | |
| version | semver | YES | |
| created | date | YES | |
| updated | date | YES | |
| author | string | YES | |
| owner | string | YES | Agent/nucleus that executes reminders |
| reminders | list[Reminder] | YES | Array of future actions |
| execution_mechanism | enum: schedule_signal, polling, wake_notification | YES | How reminders are checked |
| quality | null | YES | Never self-score |
| tags | list[string], len >= 3 | YES | Must include "prospective_memory" |
| tldr | string <= 160ch | YES | |
| completion_policy | enum: mark_done, re_schedule | REC | Per-reminder or global |

## Reminder Object Schema
```yaml
- id: "{reminder_id}"
  trigger_type: time | event | condition
  trigger_value: "{datetime|signal_name|condition_expression}"
  action_payload: "{what_the_agent_should_do}"
  priority: int (1=highest)
  expiry: "YYYY-MM-DD or null"
  completion_policy: mark_done | re_schedule
  recurrence: "null or {cron_like_expression}"
```

## ID Pattern
Regex: `^p10_pm_[a-z][a-z0-9_]+$`

## Constraints
- max_bytes: 2048
- reminders array MUST have >= 1 entry
- Each reminder MUST have trigger_type and action_payload
- quality: null always
- owner MUST be declared

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_integration_guide]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
| [[bld_schema_benchmark_suite]] | sibling | 0.63 |
| [[bld_schema_sandbox_spec]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
| [[bld_schema_pitch_deck]] | sibling | 0.62 |
| [[bld_schema_search_strategy]] | sibling | 0.62 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.61 |
