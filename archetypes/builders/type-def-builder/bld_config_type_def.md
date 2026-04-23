---
id: bld_config_type_def
kind: config
pillar: P09
llm_function: CONSTRAIN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [config, type-def, P09, naming, constraints]
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Type Def"
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
density_score: 0.90
related:
  - bld_schema_type_def
  - bld_schema_validation_schema
  - p03_ins_type_def
  - bld_knowledge_card_type_def
  - n06_schema_brand_config
  - p03_ch_kc_to_notebooklm
  - bld_schema_model_registry
  - bld_schema_agent_grounding_record
  - bld_schema_experiment_tracker
  - bld_schema_enum_def
---
## Naming Convention
| Element | Rule | Example |
|---|---|---|
| File name | `p06_td_{type_slug}.yaml` | `p06_td_agent_score.yaml` |
| `id` field | `p06_td_{type_slug}` | `p06_td_agent_score` |
| `type_slug` | PascalCase → snake_case → lowercase | `AgentScore` → `agent_score` |
| `type_name` | PascalCase, no spaces | `AgentScore` |
| Acronyms in slug | Expand or lowercase fully | `HTTPStatus` → `http_status` |
| Multi-word | Underscore separator | `p06_td_user_profile_id` |
## File Paths
| Context | Path |
|---|---|
| Canonical store | `archetypes/spec/type_defs/p06_td_{type_slug}.yaml` |
| Builder home | `archetypes/builders/type-def-builder/` |
| Domain subfolder (optional) | `archetypes/spec/type_defs/{domain}/p06_td_{type_slug}.yaml` |
## Size Limits
| Constraint | Value |
|---|---|
| `max_bytes` | 3072 |
| Recommended body prose | <= 200 chars per section |
| `tldr` max length | 120 chars |
| `tags` minimum | 2 entries |
| `examples` minimum | 1 entry |
## Base Type Enum (Controlled Vocabulary)
| Value | Represents |
|---|---|
| `string` | UTF-8 text |
| `integer` | Whole number (no fractional part) |
| `number` | Floating-point or decimal |
| `boolean` | `true` / `false` |
| `array` | Ordered sequence of items |
| `object` | Key-value map / struct |
| `enum` | Fixed set of allowed string values |
| `union` | One of multiple types (anyOf) |
| `intersection` | All of multiple types (allOf) |
| `tuple` | Fixed-length ordered sequence with per-position types |
| `record` | Map with typed keys and typed values |
## Constraint Types
| Constraint Key | Applicable base_types | Value type |
|---|---|---|
| `min_length` | string | integer |
| `max_length` | string | integer |
| `pattern` | string | regex string |
| `format` | string | string (uuid, email, uri, date-time, etc.) |
| `minimum` | integer, number | number |
| `maximum` | integer, number | number |
| `exclusive_minimum` | integer, number | number |
| `exclusive_maximum` | integer, number | number |
| `precision` | number | integer (decimal places) |
| `min_items` | array, tuple | integer |
| `max_items` | array, tuple | integer |
| `unique_items` | array | boolean |
| `allowed_values` | enum | array[string] |
| `required_keys` | object, record | array[string] |
| `key_type` | record | base_type string |
| `value_type` | record | base_type string or type_ref |
## Composition Mode Enum
| Value | Semantics |
|---|---|
| `union` | Exactly one member type must match |
| `intersection` | All member types must match simultaneously |
| `tuple` | Positional — each position has its own type |
| `discriminated_union` | Union with a shared discriminant field |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_type_def]] | upstream | 0.54 |
| [[bld_schema_validation_schema]] | upstream | 0.42 |
| [[p03_ins_type_def]] | upstream | 0.39 |
| [[bld_knowledge_card_type_def]] | upstream | 0.39 |
| [[n06_schema_brand_config]] | upstream | 0.37 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.32 |
| [[bld_schema_model_registry]] | upstream | 0.31 |
| [[bld_schema_agent_grounding_record]] | upstream | 0.30 |
| [[bld_schema_experiment_tracker]] | upstream | 0.29 |
| [[bld_schema_enum_def]] | upstream | 0.28 |
