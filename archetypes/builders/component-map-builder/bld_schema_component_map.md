---
pillar: P00
id: bld_schema_component_map
kind: schema
parent: component-map-builder
version: 2.0.0
quality: 9.1
title: "Schema Component Map"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_schema_diagram
  - bld_schema_input_schema
  - bld_schema_retriever_config
  - bld_schema_dataset_card
  - bld_schema_enum_def
  - bld_schema_smoke_eval
  - bld_schema_usage_report
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_action_prompt
---
# Schema — component-map-builder
SOURCE OF TRUTH. OUTPUT_TEMPLATE derives from this. CONFIG restricts from this.
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P08` |
| Type | literal `component_map` |
| Machine format | `yaml` (frontmatter yaml + md body) |
| Naming | `p08_cmap_{scope_slug}.yaml` |
| Max bytes | 4096 |
## Required Fields (11)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string, matches `^p08_cmap_[a-z][a-z0-9_]+$` | YES | — | Namespace compliance |
| kind | literal "component_map" | YES | — | Type discriminator |
| pillar | literal "P08" | YES | — | Architecture pillar |
| version | semver X.Y.Z | YES | "1.0.0" | Quoted string |
| created | date YYYY-MM-DD | YES | — | Quoted string |
| updated | date YYYY-MM-DD | YES | — | Quoted string |
| author | string | YES | — | Agent_group or human |
| domain | string | YES | — | Architecture domain |
| quality | null | YES | null | NEVER a number |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
## Recommended Fields (5)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| scope | string | REC | What is mapped — one sentence |
| component_count | integer >= 2 | REC | Must match Components table |
| connection_count | integer >= 1 | REC | Must match Connections table |
| layers_count | integer >= 2 | REC | Number of architectural layers (layered decomposition) |
| keywords | list[string], len >= 2 | REC | For brain search |
## ID Pattern
```
^p08_cmap_[a-z][a-z0-9_]+$
```
Examples: `p08_cmap_brain_infrastructure`, `p08_cmap_agent_group_network`, `p08_cmap_api_layer`
## Component Object Schema
```yaml
name: string        # component identifier
role: string        # what it does
owner: string       # agent_group, team, or "system"
status: enum        # active | deprecated | planned
```
## Connection Object Schema
```yaml
from: string        # source component name
to: string          # target component name
type: enum          # data_flow | dependency | signal | produces | consumes
data: string        # optional, what flows
direction: enum     # unidirectional | bidirectional
```
## Dependency Notation
| Notation | Meaning | Example |
|----------|---------|---------|
| `A --> B` | Data flow | Parser --> Classifier |
| `A --depends--> B` | A requires B | Search --depends--> Embeddings |
| `A --signals--> B` | Event/notification | Worker --signals--> Monitor |
| `A --produces--> B` | A generates B | Indexer --produces--> VectorIndex |
| `A <--> B` | Bidirectional | Cache <--> Database |
Per component: document `receives_from` (whom, what data) and `produces_for` (whom, what data).
## Body Structure (4 sections)
1. `## Component Inventory` — table: name, role, owner, status; every component listed
2. `## Dependency Graph` — typed connections using notation above; ASCII topology diagram
3. `## Boundary Table` — IS / IS NOT table defining what the map covers and excludes
4. `## Layer Map` — architectural layers (top-down); which components belong to each layer
## Constraints
| Constraint | Value |
|-----------|-------|
| max_bytes | 4096 (body only) |
| naming | p08_cmap_{scope_slug}.yaml |
| component_count | >= 2 |
| connection_count | >= 1 |
| orphan components | FORBIDDEN (each must have >= 1 connection) |
| untyped connections | FORBIDDEN (every arrow must have a type) |
| quality field | ALWAYS null |
| scope | definable in one sentence; if not, split the map |
## Enum Values
| Field | Valid Values |
|-------|-------------|
| status | active, deprecated, planned |
| connection type | data_flow, dependency, signal, produces, consumes |
| direction | unidirectional, bidirectional |
| kind | component_map (exact literal) |
| pillar | P08 (exact literal) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_diagram]] | sibling | 0.53 |
| [[bld_schema_input_schema]] | sibling | 0.52 |
| [[bld_schema_retriever_config]] | sibling | 0.52 |
| [[bld_schema_dataset_card]] | sibling | 0.51 |
| [[bld_schema_enum_def]] | sibling | 0.51 |
| [[bld_schema_smoke_eval]] | sibling | 0.50 |
| [[bld_schema_usage_report]] | sibling | 0.50 |
| [[bld_schema_memory_scope]] | sibling | 0.50 |
| [[bld_schema_handoff_protocol]] | sibling | 0.50 |
| [[bld_schema_action_prompt]] | sibling | 0.50 |
