---
quality: 8.9
quality: 8.2
kind: schema
id: bld_schema_state_machine
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for state_machine
pattern: TEMPLATE derives from this. CONFIG restricts this.
title: "Schema State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, schema]
tldr: "Schema for state_machine: entity, initial/final states, transitions table (from/event/to/guard/action)."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_lifecycle_rule
  - bld_schema_sandbox_config
---

# Schema: state_machine

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_sm_{slug}) | YES | - | Namespace compliance |
| kind | literal "state_machine" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact version |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| entity | string | YES | - | Entity whose lifecycle is modeled |
| initial_state | string | YES | - | Starting state name |
| final_states | list[string] | YES | - | Terminal state names |
| states_count | integer | YES | - | Total number of states |
| transitions_count | integer | YES | - | Total number of transitions |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "state_machine" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p12_sm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)

1. `## States` -- table of all states with type and description
2. `## Transitions` -- table with from_state, event, to_state, guard, action
3. `## Guards` -- definition of guard conditions
4. `## Actions` -- definition of entry/exit/transition actions

## Transition Table Fields

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| from_state | string | YES | Must exist in states |
| event | string | YES | Trigger event name |
| to_state | string | YES | Must exist in states |
| guard | string | OPT | Boolean condition expression |
| action | string | OPT | Side-effect to execute |

## Constraints

- max_bytes: 4096 (body only)
- initial_state must appear in states list
- final_states must all appear in states list
- No two transitions from same (from_state, event) pair -- deterministic FSM
- states_count and transitions_count must match body
- quality: null always
- NOT workflow (no DAG), NOT process_manager (no event orchestration)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
| [[bld_schema_reranker_config]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_search_strategy]] | sibling | 0.65 |
| [[bld_schema_pitch_deck]] | sibling | 0.65 |
| [[bld_schema_integration_guide]] | sibling | 0.64 |
| [[bld_schema_benchmark_suite]] | sibling | 0.64 |
| [[bld_schema_lifecycle_rule]] | sibling | 0.64 |
| [[bld_schema_sandbox_config]] | sibling | 0.63 |
