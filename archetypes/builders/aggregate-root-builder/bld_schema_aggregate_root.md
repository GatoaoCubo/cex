---
id: bld_schema_aggregate_root
kind: schema
pillar: P06
title: "Aggregate Root Builder -- Schema"
version: 1.0.0
quality: 6.6
tags: [builder, aggregate_root, schema]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
---
# Schema: aggregate_root
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p06_ar_{slug}` | namespace + slug |
| kind | literal `aggregate_root` | type integrity |
| pillar | literal `P06` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| bounded_context | string | which domain context owns this |
| invariants | list[string] | at least 2 concrete rules |
| commands | list[string] | allowed mutations |
| domain_events | list[string] | emitted facts |
| repository | string | persistence interface name |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| cluster_members | list[string] | entities + value_objects inside boundary |
| identity_type | string | UUID, natural key, surrogate |
| concurrency_strategy | enum(optimistic, pessimistic, none) | conflict resolution |
| linked_artifacts | object | cross-references |
## ID Pattern
Regex: `^p06_ar_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Identity` -- root entity, bounded context, cluster members
2. `## Invariants` -- numbered hard rules, each concrete and measurable
3. `## Commands` -- mutations with pre/postconditions
4. `## Domain Events` -- emitted facts with payloads
5. `## Repository` -- find_by_id + save interface only
6. `## Boundaries` -- inside vs outside the aggregate
## Constraints
- max_bytes: 4096
- naming: p06_ar_{slug}.md
- other aggregates referenced by ID only, never object
- at least 2 invariants required
- quality: null always
