---
kind: schema
id: bld_schema_effort_profile
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for effort_profile
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Effort Profile"
version: "1.0.0"
author: n03_builder
tags: [effort_profile, builder, examples]
tldr: "Golden and anti-examples for effort profile construction, demonstrating ideal structure and common pitfalls."
domain: "effort profile construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_constraint_spec
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_chunk_strategy
  - bld_schema_prompt_version
  - bld_schema_hook_config
  - bld_schema_golden_test
  - bld_schema_unit_eval
---

# Schema: effort_profile
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_effort_{slug}) | YES | - | Namespace compliance |
| kind | literal "effort_profile" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| model | string | YES | - | Target LLM model (haiku, sonnet, opus) |
| thinking_level | string | YES | - | Reasoning depth (low, medium, high, max) |
| target_builder | string | YES | - | Builder this profile applies to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "effort_profile" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| cost_tier | string | REC | - | Cost category (low, medium, high) |
| fallback_model | string | REC | - | Alternative model for failover |
| max_tokens | integer | REC | - | Token budget for this profile |
| temperature | float | REC | - | Temperature setting |
## ID Pattern
Regex: `^p09_effort_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Configuration` — configuration specification
3. `## Levels` — levels specification
4. `## Integration` — integration specification
## Constraints
- max_bytes: 4096 (body only)
- naming: p09_effort_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.76 |
| [[bld_schema_output_validator]] | sibling | 0.76 |
| [[bld_schema_constraint_spec]] | sibling | 0.75 |
| [[bld_schema_handoff_protocol]] | sibling | 0.74 |
| [[bld_schema_memory_scope]] | sibling | 0.74 |
| [[bld_schema_chunk_strategy]] | sibling | 0.73 |
| [[bld_schema_prompt_version]] | sibling | 0.72 |
| [[bld_schema_hook_config]] | sibling | 0.68 |
| [[bld_schema_golden_test]] | sibling | 0.67 |
| [[bld_schema_unit_eval]] | sibling | 0.66 |
