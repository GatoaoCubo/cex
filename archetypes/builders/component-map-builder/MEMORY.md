---
id: component-map-builder-memory
kind: memory
parent: component-map-builder
version: 1.0.0
---

# Memory — component-map-builder

## Common Mistakes

1. Setting `quality` to a number instead of null (H05) — most frequent failure
2. Writing prose instead of tables ("the system has components...") — kills density (S08)
3. Missing connection direction (just "A relates to B") — S03 fail
4. Confusing with diagram — ask: "is this data or a picture?" data -> component_map
5. Orphan components (listed in Components table but no entry in Connections) — S05 fail
6. component_count doesn't match actual table rows — H06 fail
7. Missing owner for one or more components — S04 fail
8. Scope too vague ("the whole system") — use precise boundary with explicit exclusions
9. Using `.md` extension instead of `.yaml` — CONFIG constraint violation
10. id uses hyphens: `p08_cmap_brain-infra` — H02 fail, must use underscores

## Component Mapping Catalog

| Domain | Common maps | Key boundary |
|--------|------------|-------------|
| Infrastructure | Brain, API, deployment | vs diagram (visual) |
| Orchestration | Satellite network, signal bus | vs satellite_spec (one component) |
| Knowledge | Pool, indexes, embedding | vs dag (execution order) |
| Tools | MCP servers, hooks, plugins | vs interface (contract only) |
| Frontend | React components, routes, stores | vs diagram (visual graph) |

## Scope Scoping Heuristics

Too broad: "the entire CEX system" — split into domain maps
Too narrow: "just the BM25 index" — use satellite_spec instead
Right size: "Brain search infrastructure: indexing, embedding, retrieval"

Rule of thumb: 3-15 components per map. >15 = split scope.

## Connection Type Decision

| Situation | Use |
|-----------|-----|
| Data moves from A to B | data_flow |
| A cannot function without B | dependency |
| A sends event/trigger to B | signal |
| A creates B as output | produces |
| A reads/uses B | consumes |

## Production Counter

0 artifacts produced.

## Session Log

| Date | Scope | component_count | Score | Notes |
|------|-------|----------------|-------|-------|
| — | — | — | — | No productions yet |
