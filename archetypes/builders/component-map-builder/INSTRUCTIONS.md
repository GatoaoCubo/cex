---
id: component-map-builder-instructions
kind: instructions
parent: component-map-builder
version: 1.0.0
---

# Instructions — component-map-builder

## Phase 1: SURVEY

1. Define the scope boundary (what system/subsystem to map)
2. List all components within scope
3. Identify the owner of each component
4. Map connections between components (data_flow, dependency, signal)
5. brain_query [IF MCP]: search existing maps to avoid duplicates
6. Determine health/status of each component (active, deprecated, planned)
7. Identify interfaces at component boundaries

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 15 required + 4 extended fields (null OK for optional)
4. Set `quality: null` (NEVER self-score)
5. Write Scope section: what is and isn't included
6. Write Components table: name, role, owner, status, version
7. Write Connections table: from, to, type, data, direction
8. Write Interfaces section: boundary contracts between components
9. Write Dependencies section: critical path and failure impact
10. Write Boundaries section: where this map ends and other maps begin
11. Write References section: sources and related artifacts

## Phase 3: VALIDATE

1. Open QUALITY_GATES.md
2. Check all 9 HARD gates — any failure = reject and fix
3. Check all 10 SOFT gates — compute score
4. Cross-check: is output structured data, not a visual diagram or single-component spec?
5. Verify component_count matches actual rows in Components table
6. Verify connection_count matches actual rows in Connections table
7. Verify no orphan components (every component has >= 1 connection)
8. If score < 8.0: revise in same pass, do not deliver

## Phase 4: DELIVER

1. Write file to `cex/P08_architecture/examples/p08_cmap_{scope_slug}.yaml`
2. Confirm filename stem matches `id` field
3. Report: component_count, connection_count, HARD gates passed, SOFT score
