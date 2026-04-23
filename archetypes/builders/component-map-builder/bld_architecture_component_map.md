---
kind: architecture
id: bld_architecture_component_map
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of component_map — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Component Map"
version: "1.0.0"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - component-map-builder
  - p03_sp_component_map_builder
  - p11_qg_component_map
  - bld_collaboration_component_map
  - bld_instruction_component_map
  - bld_architecture_diagram
  - bld_schema_component_map
  - bld_knowledge_card_component_map
  - diagram-builder
  - p10_lr_component_map_builder
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
| agent_card | Detailed spec for a single component found in the map | P08 | consumer |
| pattern | Solution template that may reference component inventory | P08 | consumer |
| knowledge_index | Search index that stores maps for retrieval | runtime | consumer |
## Dependency Graph
```
scope_definition   --produces-->  component_entry
component_entry    --produces-->  connection
component_entry    --produces-->  layer_assignment
ownership_field    --depends-->   component_entry
status_field       --depends-->   component_entry
component_map      --produces-->  diagram
component_map      --produces-->  agent_card
component_map      --produces-->  pattern
component_map      --produces-->  knowledge_index
```
| From | To | Type | Data |
|------|----|------|------|
| scope_definition | component_entry | produces | bounded list of components to inventory |
| component_entry | connection | produces | source component for a typed relationship |
| component_entry | layer_assignment | produces | component placed into architectural layer |
| ownership_field | component_entry | depends | owner metadata attached to each entry |
| status_field | component_entry | depends | health/lifecycle metadata attached to entry |
| component_map | diagram | produces | structured data consumed by visual renderer |
| component_map | agent_card | produces | inventory that informs single-component spec |
| component_map | pattern | produces | inventory referenced by solution templates |
| component_map | knowledge_index | produces | searchable artifact stored for retrieval |
## Boundary Table
| component_map IS | component_map IS NOT |
|-----------------|---------------------|
| Structured tabular inventory of system parts and connections | A visual graph or diagram (that is diagram) |
| Covers many components across a system boundary | A detailed spec for one component (that is agent_card) |
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
| consumers | diagram, agent_card, pattern, knowledge_index | Downstream artifacts that consume the map data |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[component-map-builder]] | related | 0.58 |
| [[p03_sp_component_map_builder]] | related | 0.51 |
| [[p11_qg_component_map]] | downstream | 0.47 |
| [[bld_collaboration_component_map]] | downstream | 0.40 |
| [[bld_instruction_component_map]] | upstream | 0.38 |
| [[bld_architecture_diagram]] | sibling | 0.35 |
| [[bld_schema_component_map]] | related | 0.34 |
| [[bld_knowledge_card_component_map]] | upstream | 0.31 |
| [[diagram-builder]] | related | 0.31 |
| [[p10_lr_component_map_builder]] | downstream | 0.29 |
