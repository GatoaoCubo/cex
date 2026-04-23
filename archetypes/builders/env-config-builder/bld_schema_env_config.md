---
kind: schema
id: bld_schema_env_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for env_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_smoke_eval
  - bld_schema_constraint_spec
  - bld_schema_enum_def
  - bld_schema_cli_tool
  - bld_schema_golden_test
  - bld_schema_chunk_strategy
---

# Schema: env_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_env_{scope_slug}) | YES | - | Namespace compliance |
| kind | literal "env_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | Config scope: global, agent_group name, or service name |
| variables | list[string], len >= 1 | YES | - | Variable names defined |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "env_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this config covers |
| environment | enum: development, staging, production, all | REC | all | Target environment |
| sensitive_count | integer | REC | - | Number of sensitive vars |
| override | string | REC | - | Override precedence summary |
| validation | string | REC | - | Validation strategy summary |
## ID Pattern
Regex: `^p09_env_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what scope, why these variables, who consumes them
2. `## Variable Catalog` — table: name, type, required, default, sensitive, validation
3. `## Override Precedence` — how values are resolved (env > file > default)
4. `## Sensitive Variables` — which vars are secrets, masking rules, storage guidance
## Constraints
- max_bytes: 4096 (body only — env configs can be larger)
- naming: p09_env_{scope_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- variables list MUST match variable names in ## Variable Catalog
- quality: null always
- NEVER include actual secret values — names and validation only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.62 |
| [[bld_schema_smoke_eval]] | sibling | 0.62 |
| [[bld_schema_constraint_spec]] | sibling | 0.62 |
| [[bld_schema_enum_def]] | sibling | 0.61 |
| [[bld_schema_cli_tool]] | sibling | 0.61 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
| [[bld_schema_chunk_strategy]] | sibling | 0.61 |
