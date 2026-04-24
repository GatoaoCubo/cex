---
id: n00_component_map_manifest
kind: knowledge_card
8f: F3_inject
pillar: P08
nucleus: n00
title: "Component Map -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, component_map, p08, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_component_map
  - bld_schema_benchmark_suite
  - bld_schema_diagram
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_diff_strategy
  - bld_schema_rl_algorithm
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A component_map documents what connects to what within a system: services, APIs, databases, agents, and external integrations with their dependency edges. It is injected into the reasoning context (F3 INJECT) to give builders a clear picture of the architecture before they modify or extend it, preventing integration regressions.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `component_map` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable map name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| system | string | yes | Name of the system being mapped |
| components | list | yes | List of named components |
| components[].name | string | yes | Component identifier |
| components[].type | enum | yes | service \| agent \| database \| api \| tool \| ui |
| components[].dependencies | list | no | Names of components this one calls |
| components[].nucleus | string | no | Owning nucleus if applicable |
| format | enum | no | table \| mermaid \| ascii \| json |

## When to use
- Onboarding a new nucleus that needs to understand existing integrations
- Planning a new feature that touches multiple components
- Injecting context before refactoring cross-cutting concerns

## Builder
`archetypes/builders/component_map-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind component_map --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: component_map_cex_core
kind: component_map
pillar: P08
nucleus: n07
title: "CEX Core Component Map"
version: 1.0
quality: null
---
system: cex
components:
  - name: n07_orchestrator
    type: agent
    dependencies: [dispatch_sh, signal_writer, cex_doctor]
  - name: dispatch_sh
    type: tool
    dependencies: [spawn_grid_ps1, spawn_solo_ps1]
format: table
```

## Related kinds
- `diagram` (P08) -- visual representation of the same component topology
- `interface` (P06) -- data contracts between connected components
- `decision_record` (P08) -- records why a connection or component was chosen

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_reranker_config]] | upstream | 0.43 |
| [[bld_schema_component_map]] | related | 0.42 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_diagram]] | related | 0.41 |
| [[bld_schema_dataset_card]] | upstream | 0.41 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
| [[bld_schema_search_strategy]] | upstream | 0.41 |
| [[bld_schema_diff_strategy]] | upstream | 0.40 |
| [[bld_schema_rl_algorithm]] | upstream | 0.40 |
