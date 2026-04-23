---
kind: schema
id: bld_schema_context_map
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for context_map
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.9
title: "Schema Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, schema]
tldr: "Schema for context_map: contexts list, relationships with pattern/upstream/downstream, integration_type, team_coupling."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_retriever_config
  - bld_schema_benchmark_suite
  - bld_schema_rl_algorithm
---

# Schema: context_map

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p08_cm_{slug}) | YES | - | Namespace compliance |
| kind | literal "context_map" | YES | - | Type integrity |
| pillar | literal "P08" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact version |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| system_name | string | YES | - | Name of the system being mapped |
| contexts_count | integer | YES | - | Number of BCs in scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "context_map" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p08_cm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)

1. `## Bounded Contexts` -- table of all BCs in scope
2. `## Relationships` -- directed relationship table with patterns
3. `## Integration Details` -- translation layers and sync/async types
4. `## Team Coupling` -- organizational implications

## Relationship Entry Fields

| Field | Type | Required | Values |
|-------|------|----------|--------|
| upstream | string (BC name) | YES | - |
| downstream | string (BC name) | YES | - |
| pattern | enum | YES | ACL, OHS, Conformist, Partnership, Shared_Kernel, Customer_Supplier |
| integration_type | enum | REC | sync, async, batch |
| translation_layer | string | conditional | Required if pattern == ACL |
| published_language | string | conditional | Required if pattern == OHS |

## Constraints

- max_bytes: 4096 (body only)
- contexts_count MUST match actual contexts listed in body
- quality: null always
- NOT bounded_context (single BC), NOT component_map (deployment)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.68 |
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_search_strategy]] | sibling | 0.67 |
| [[bld_schema_integration_guide]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
| [[bld_schema_dataset_card]] | sibling | 0.66 |
| [[bld_schema_pitch_deck]] | sibling | 0.66 |
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_benchmark_suite]] | sibling | 0.65 |
| [[bld_schema_rl_algorithm]] | sibling | 0.65 |
