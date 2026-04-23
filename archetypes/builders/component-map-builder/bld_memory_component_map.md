---
id: p10_lr_component_map_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Component maps that listed orphan components (present in the component table but absent from connections) provided false confidence about system boundaries. In 4 of 6 architecture reviews, orphan components concealed undocumented dependencies that caused production incidents."
pattern: "Every component in the map must appear in at least one connection. Use explicit direction annotations on all connections. Scope to 3-15 components per map; split at 15."
evidence: "6 architecture reviews: 4 had orphan components that concealed undocumented dependencies. After enfo..."
confidence: 0.7
outcome: SUCCESS
domain: component_map
tags: [component-map, architecture, orphan-detection, connection-direction, scope-boundary]
tldr: "No orphan components. Every component must appear in at least one connection. Explicit direction on all connections. Split scope at 15 components."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [component map, architecture mapping, orphan detection, connection direction, data flow, dependency, scope boundary, ownership]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Component Map"
density_score: 0.90
llm_function: INJECT
related:
  - bld_instruction_component_map
  - p11_qg_component_map
  - bld_config_component_map
  - component-map-builder
  - bld_collaboration_component_map
  - bld_schema_component_map
  - p03_sp_component_map_builder
  - bld_knowledge_card_component_map
  - bld_tools_component_map
  - bld_architecture_component_map
---
## Summary
A component map's value is making hidden dependencies visible. Orphan components — listed in the component table but absent from connections — destroy that value. Orphans signal either truly isolated components (rare, annotate explicitly) or omitted connections (common, dangerous).
The second most common failure is undirected connections ("A relates to B"): structural information without operational information. Direction is what makes a map reasoned from vs. merely looked at.
## Pattern
**No orphans. Explicit direction. Bounded scope.**
No-orphan rule: after writing both the component table and the connection table, verify every component_id in the component table appears at least once as source or target in the connection table. Any component with no connections must be annotated explicitly as `isolated: true` with a justification.
Connection direction types:
1. data_flow: data moves from source to target (A sends records to B)
2. dependency: source cannot function without target (A requires B to be running)
3. signal: source sends event/trigger to target (A emits events consumed by B)
4. produces: source creates target as output artifact (A generates B)
5. consumes: source reads or uses target (A reads from B)
Scope boundary rules:
1. 3-15 components per map. Fewer than 3: use a agent_group spec instead. More than 15: split by domain.
2. Scope statement must name what is explicitly excluded, not just what is included.
3. Right-size example: "Brain search infrastructure: indexing, embedding, retrieval. Excludes: UI layer, API routing, authentication."
Component table required columns: id, name, type, owner, description (one sentence). No prose beyond the table.
## Anti-Pattern
1. Orphan components without `isolated: true` annotation (conceals dependencies).
2. Undirected connections without type annotation (structurally present, operationally useless).
3. Scope too broad ("the whole system") — split by domain.
4. Scope too narrow ("just the BM25 index") — use a spec for single-component documentation.
5. Prose connections instead of a table (kills density; S08 fail).
6. Confusing component map (structured data) with diagram (visual rendering).
7. component_count not matching actual table rows (H06 fail).
## Context
Orphan detection emerged from maps where components were listed to signal existence without documenting connections — creating false completeness while hiding the actual dependency graph.
Ownership column is required for incident response: knowing who owns a component halves time-to-contact when it is implicated in a failure. Health status column (optional): current, degraded, deprecated, unknown — doubles as a live dashboard when kept current.

## Metadata

```yaml
id: p10_lr_component_map_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-component-map-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | component_map |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_component_map]] | upstream | 0.45 |
| [[p11_qg_component_map]] | downstream | 0.36 |
| [[bld_config_component_map]] | related | 0.35 |
| [[component-map-builder]] | upstream | 0.35 |
| [[bld_collaboration_component_map]] | downstream | 0.34 |
| [[bld_schema_component_map]] | related | 0.32 |
| [[p03_sp_component_map_builder]] | upstream | 0.32 |
| [[bld_knowledge_card_component_map]] | upstream | 0.32 |
| [[bld_tools_component_map]] | related | 0.28 |
| [[bld_architecture_component_map]] | upstream | 0.25 |
