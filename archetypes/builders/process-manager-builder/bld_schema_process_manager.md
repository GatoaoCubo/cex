---
id: bld_schema_process_manager
kind: schema
pillar: P12
title: "Process Manager Builder -- Schema"
version: 1.0.0
quality: 7.1
tags: [builder, process_manager, schema]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
---
# Schema: process_manager
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p12_pm_{slug}` | namespace + slug |
| kind | literal `process_manager` | type integrity |
| pillar | literal `P12` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| correlation_key | string | field that ties events to process instance |
| start_event | string | domain event that creates a new instance |
| terminal_states | list[string] | states that end the process (success + failure) |
| states | list[string] | all possible states including start and terminal |
| subscribed_events | list[string] | domain events this process manager listens to |
| commands_issued | list[string] | commands dispatched by this process manager |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| timeout_strategy | object | per_state timeouts + actions |
| compensation | list[string] | rollback commands per failure state |
| persistence | enum(in_memory, database, event_sourced) | how process state is stored |
| idempotency_key | string | ensures at-most-once processing |
## ID Pattern
Regex: `^p12_pm_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Correlation` -- key used to track process instances
2. `## States` -- state machine diagram/table with transitions
3. `## Event Routing` -- event -> transition + command table
4. `## Commands` -- each command issued with target and payload
5. `## Timeout` -- per-state timeouts and timeout actions
6. `## Compensation` -- failure rollback commands
## Constraints
- max_bytes: 4096
- naming: p12_pm_{slug}.md
- process manager holds state only, never domain data
- all commands target external services or aggregates
- quality: null always
