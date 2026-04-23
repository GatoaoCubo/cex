---
kind: schema
id: bld_schema_handoff_protocol
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for handoff_protocol
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Handoff Protocol"
version: "1.0.0"
author: n03_builder
tags: [handoff_protocol, builder, examples]
tldr: "Golden and anti-examples for handoff protocol construction, demonstrating ideal structure and common pitfalls."
domain: "handoff protocol construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_prompt_version
  - bld_schema_effort_profile
  - bld_schema_hook_config
  - bld_schema_golden_test
  - bld_schema_unit_eval
---

# Schema: handoff_protocol
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_handoff_{slug}) | YES | - | Namespace compliance |
| kind | literal "handoff_protocol" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| trigger | string | YES | - | Trigger |
| context_passed | string | YES | - | Context passed |
| return_contract | string | YES | - | Return contract |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "handoff_protocol" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| source_agent | string | REC | - | Source agent |
| target_agent | string | REC | - | Target agent |
| timeout | string | REC | - | Timeout |
| retry_policy | string | REC | - | Retry policy |
| escalation | string | REC | - | Escalation |
## ID Pattern
Regex: `^p02_handoff_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Trigger` — trigger specification
3. `## Context Transfer` — context transfer specification
4. `## Return Contract` — return contract specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p02_handoff_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.77 |
| [[bld_schema_output_validator]] | sibling | 0.76 |
| [[bld_schema_memory_scope]] | sibling | 0.75 |
| [[bld_schema_constraint_spec]] | sibling | 0.74 |
| [[bld_schema_chunk_strategy]] | sibling | 0.73 |
| [[bld_schema_prompt_version]] | sibling | 0.73 |
| [[bld_schema_effort_profile]] | sibling | 0.71 |
| [[bld_schema_hook_config]] | sibling | 0.67 |
| [[bld_schema_golden_test]] | sibling | 0.66 |
| [[bld_schema_unit_eval]] | sibling | 0.66 |
