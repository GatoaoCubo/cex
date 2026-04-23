---
kind: schema
id: bld_schema_constraint_spec
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for constraint_spec
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_chunk_strategy
  - bld_schema_prompt_version
  - bld_schema_effort_profile
  - bld_schema_hook_config
  - bld_schema_golden_test
  - bld_schema_usage_report
---

# Schema: constraint_spec
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_constraint_{slug}) | YES | - | Namespace compliance |
| kind | literal "constraint_spec" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| constraint_type | string | YES | - | Constraint type |
| pattern | string | YES | - | Pattern |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "constraint_spec" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| provider_compat | string | REC | - | Provider compat |
| fallback | string | REC | - | Fallback |
| temperature_override | string | REC | - | Temperature override |
| max_tokens | string | REC | - | Max tokens |
## ID Pattern
Regex: `^p03_constraint_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Constraint Definition` — constraint definition specification
3. `## Provider Compatibility` — provider compatibility specification
4. `## Integration` — integration specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p03_constraint_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.85

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.77 |
| [[bld_schema_output_validator]] | sibling | 0.76 |
| [[bld_schema_handoff_protocol]] | sibling | 0.75 |
| [[bld_schema_memory_scope]] | sibling | 0.75 |
| [[bld_schema_chunk_strategy]] | sibling | 0.73 |
| [[bld_schema_prompt_version]] | sibling | 0.73 |
| [[bld_schema_effort_profile]] | sibling | 0.72 |
| [[bld_schema_hook_config]] | sibling | 0.67 |
| [[bld_schema_golden_test]] | sibling | 0.66 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
