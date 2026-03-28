---
kind: architecture
id: bld_architecture_component_map
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of component_map — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| component_entry | Single row in the inventory — name, role, owner, status | component_map | required |
| connection | Typed directed relationship between two components | component_map | required |
| scope_definition | Boundary declaration — what the map covers and excludes | component_map | required |
| layer_assignment | Architectural layer each component belongs to | component_map | required |
| ownership_field | Who owns or maintains each component | component_map | required |
| status_field | Health or lifecycle state of each component (active, deprecated) | component_map | required |
| diagram | Visual rendering of the same component data | P08 | consumer |
| satellite_spec | Detailed spec for a single component found in the map | P08 | consumer |
| pattern | Solution template that may reference component inventory | P08 | consumer |
| brain_index | Search index that stores maps for retrieval | runtime | consumer |
## Dependency Graph
```
scope_definition   --produces-->  component_entry
component_entry    --produces-->  connection
component_entry    --produces-->  layer_assignment
ownership_field    --depends-->   component_entry
status_field       --depends-->   component_entry
component_map      --produces-->  diagram
component_map      --produces-->  satellite_spec
component_map      --produces-->  pattern
component_map      --produces-->  brain_index
```
| From | To | Type | Data |
|------|----|------|------|
| scope_definition | component_entry | produces | bounded list of components to inventory |
| component_entry | connection | produces | source component for a typed relationship |
| component_entry | layer_assignment | produces | component placed into architectural layer |
| ownership_field | component_entry | depends | owner metadata attached to each entry |
| status_field | component_entry | depends | health/lifecycle metadata attached to entry |
| component_map | diagram | produces | structured data consumed by visual renderer |
| component_map | satellite_spec | produces | inventory that informs single-component spec |
| component_map | pattern | produces | inventory referenced by solution templates |
| component_map | brain_index | produces | searchable artifact stored for retrieval |
## Boundary Table
| component_map IS | component_map IS NOT |
|-----------------|---------------------|
| Structured tabular inventory of system parts and connections | A visual graph or diagram (that is diagram) |
| Covers many components across a system boundary | A detailed spec for one component (that is satellite_spec) |
| Describes static structure — what exists and how it connects | Prescribes a solution to a recurring problem (that is pattern) |
| Data artifact — tables, typed connections, ownership, status | An execution dependency graph with ordering semantics (that is dag) |
| Defines scope boundary (what is in and out of the map) | A governance mandate for system behavior (that is law) |
| Feeds diagrams, specs, patterns, and search indexes | Implements or enforces anything at runtime |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| scoping | scope_definition | Declare what the map covers and excludes |
| inventory | component_entry, ownership_field, status_field | Enumerate each component with owner and health |
| structure | connection, layer_assignment | Define typed relationships and architectural placement |
| consumers | diagram, satellite_spec, pattern, brain_index | Downstream artifacts that consume the map data |
