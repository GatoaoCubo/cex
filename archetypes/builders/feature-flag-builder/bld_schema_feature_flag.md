---
kind: schema
id: bld_schema_feature_flag
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for feature_flag
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_golden_test
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_unit_eval
  - bld_schema_search_strategy
  - bld_schema_effort_profile
---

# Schema: feature_flag
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_ff_{feature_slug}) | YES | - | Namespace compliance |
| kind | literal "feature_flag" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| flag_name | string | YES | - | Human-readable flag name |
| default_state | enum: on, off | YES | off | Default state when no targeting matches |
| category | enum: release, experiment, ops, permission | YES | - | Flag category per Fowler |
| rollout_percentage | integer 0-100 | YES | 0 | Current rollout percentage |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "feature_flag" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this flag controls |
| owner | string | REC | - | Team or person responsible |
| expires | date YYYY-MM-DD | REC | - | Stale flag cleanup date |
| targeting | string | REC | - | Targeting strategy summary |
## ID Pattern
Regex: `^p09_ff_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Flag Specification` — what feature, current state, rollout %, kill switch behavior
2. `## Rollout Strategy` — how to ramp: stages, percentage, timeline, cohorts
3. `## Lifecycle` — created, test, ramp, full rollout, retire/cleanup plan
## Constraints
- max_bytes: 1536 (body only — feature_flag is compact)
- naming: p09_ff_{feature_slug}.yaml
- machine_format: json (compiled artifact)
- id == filename stem
- default_state MUST be "on" or "off" (no "maybe", "partial")
- rollout_percentage MUST be integer 0-100
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_handoff_protocol]] | sibling | 0.64 |
| [[bld_schema_golden_test]] | sibling | 0.64 |
| [[bld_schema_constraint_spec]] | sibling | 0.63 |
| [[bld_schema_chunk_strategy]] | sibling | 0.63 |
| [[bld_schema_unit_eval]] | sibling | 0.63 |
| [[bld_schema_search_strategy]] | sibling | 0.62 |
| [[bld_schema_effort_profile]] | sibling | 0.62 |
