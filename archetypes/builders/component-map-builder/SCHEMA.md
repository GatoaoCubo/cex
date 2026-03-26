---
id: component-map-builder-schema
kind: schema
parent: component-map-builder
version: 1.0.0
---

# Schema — component-map-builder

SOURCE OF TRUTH. OUTPUT_TEMPLATE derives from this. CONFIG restricts from this.

## Required Fields (15)

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | YES | — | Pattern: `^p08_cmap_[a-z][a-z0-9_]+$` (H02, H03) |
| kind | literal "component_map" | YES | — | Exact string (H04) |
| pillar | literal "P08" | YES | — | Architecture pillar (H06) |
| version | semver X.Y.Z | YES | "1.0.0" | Quoted string |
| created | date YYYY-MM-DD | YES | — | Quoted string (H06) |
| updated | date YYYY-MM-DD | YES | — | Quoted string (H06) |
| author | string | YES | — | Satellite or human (H06) |
| domain | string | YES | — | Architecture domain |
| quality | null | YES | null | NEVER a number (H05) |
| tags | list[string], len >= 3 | YES | — | Searchability (H07) |
| tldr | string <= 160ch | YES | — | Dense summary (S01) |
| scope | string | YES | — | What is mapped (H08) |
| component_count | integer >= 2 | YES | — | Must match Components table (H09) |
| connection_count | integer >= 1 | YES | — | Must match Connections table |
| components | list[object] | YES | — | Each: {name, role, owner, status} |

## Extended Fields (4 — REC)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| connections | list[object] | REC | Each: {from, to, type} |
| interfaces | list[object] | REC | Each: {boundary, components, contract} |
| dependencies | list[object] | REC | Each: {component, depends_on, failure_impact} |
| keywords | list[string] | REC | len >= 2, for brain search (S10) |

## ID Pattern

```
^p08_cmap_[a-z][a-z0-9_]+$
```

Examples: `p08_cmap_brain_infrastructure`, `p08_cmap_satellite_network`, `p08_cmap_api_layer`

## Component Object Schema

```yaml
name: string        # component identifier
role: string        # what it does
owner: string       # satellite, team, or "system"
status: enum        # active | deprecated | planned
version: string     # optional, semver or descriptor
```

## Connection Object Schema

```yaml
from: string        # source component name
to: string          # target component name
type: enum          # data_flow | dependency | signal | produces | consumes
data: string        # optional, what flows
direction: enum     # unidirectional | bidirectional
```

## Body Structure (7 sections — S07)

1. `## Scope` — what is and isn't mapped
2. `## Components` — table: name, role, owner, status, version
3. `## Connections` — table: from, to, type, data, direction
4. `## Interfaces` — boundary contracts between components
5. `## Dependencies` — critical path and failure impact
6. `## Boundaries` — where map scope ends, what adjacent maps cover
7. `## References` — sources and related artifacts

## Constraints

| Constraint | Value |
|-----------|-------|
| max_bytes | 3072 |
| density_min | 0.80 |
| naming | p08_cmap_{scope_slug}.yaml |
| component_count | >= 2 |
| connection_count | >= 1 |
| connection direction | required per row |
| component owner | required per row |
| component status | required per row |
| orphan components | FORBIDDEN (each must have >= 1 connection) |
| quality field | ALWAYS null |

## Enum Values

| Field | Valid Values |
|-------|-------------|
| status | active, deprecated, planned |
| connection type | data_flow, dependency, signal, produces, consumes |
| direction | unidirectional, bidirectional |
| kind | component_map (exact literal) |
| pillar | P08 (exact literal) |
