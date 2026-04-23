---
kind: schema
id: bld_schema_supervisor
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for supervisor
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_smoke_eval
  - bld_schema_action_prompt
  - bld_schema_input_schema
  - bld_schema_unit_eval
  - bld_schema_workflow
  - bld_schema_golden_test
---

# Schema: supervisor
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (ex_director_{topic}) | YES | - | Namespace compliance |
| kind | literal "supervisor" | YES | - | Type integrity |
| pillar | literal "P08" | YES | - | Pillar assignment |
| title | string | YES | - | Human-readable supervisor name |
| version | semver string | YES | "1.0.0" | Versioning |
| topic | string | YES | - | Mission domain scope |
| builders | list[string], len >= 2 | YES | - | Named builders dispatched |
| dispatch_mode | enum: sequential/parallel/conditional | YES | "sequential" | Execution strategy |
| signal_check | bool | YES | true | Wait for builder completion signals |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "supervisor" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| created | date YYYY-MM-DD | REC | - | Creation date |
| updated | date YYYY-MM-DD | REC | - | Last update |
| author | string | REC | - | Producer identity |
| llm_function | literal "ORCHESTRATE" | REC | "ORCHESTRATE" | Always ORCHESTRATE for directors |
| wave_topology | list[object] | REC | - | Wave sequence with builders per wave |
| fallback_per_builder | map[string, string] | REC | - | Fallback action per builder name |
| domain | string | REC | - | Primary domain of orchestration |
| density_score | float 0.85-1.00 | OPT | - | Content density |
## ID Pattern
Regex: `^ex_director_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Identity` — mission scope, domain, coordination strategy
2. `## Builders` — named list with roles and nucleus assignments
3. `## Wave Topology` — ordered waves, builders per wave, signal gates
4. `## Dispatch Config` — mode, signal_check, timeout, fallback_per_builder
5. `## Routing` — triggers, keywords, NOT-when exclusions
6. `## Crew Role` — coordination question answered, explicit exclusions
## Constraints
- max_bytes: 2048 (body only)
- naming: ex_director_{topic}.md + ex_director_{topic}.yaml
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- builders list min 2 entries required
- llm_function: ORCHESTRATE (never BECOME, REASON, CALL, or PRODUCE)
- dispatch_mode: required — no implicit defaults
- signal_check: required — no unmonitored dispatch
- Supervisor MUST NOT contain task execution logic

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.61 |
| [[bld_schema_memory_scope]] | sibling | 0.60 |
| [[bld_schema_handoff_protocol]] | sibling | 0.60 |
| [[bld_schema_output_validator]] | sibling | 0.60 |
| [[bld_schema_smoke_eval]] | sibling | 0.59 |
| [[bld_schema_action_prompt]] | sibling | 0.59 |
| [[bld_schema_input_schema]] | sibling | 0.59 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
| [[bld_schema_workflow]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.59 |
