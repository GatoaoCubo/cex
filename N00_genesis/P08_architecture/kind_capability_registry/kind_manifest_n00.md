---
id: n00_capability_registry_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Capability Registry -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, capability_registry, p08, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_capability_registry
  - bld_schema_nucleus_def
  - bld_schema_reranker_config
  - bld_schema_action_paradigm
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_crew_template
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A capability_registry is a searchable catalog of all agents available to crews and orchestrators. It indexes agent_cards by domain, tool set, model tier, and nucleus ownership so that N07 and crew planners can discover, select, and compose agents without manual lookup. It is the central registry that makes composable crews possible.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `capability_registry` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable registry name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| agents | list | yes | List of registered agent entries |
| agents[].agent_id | string | yes | Unique agent identifier |
| agents[].nucleus | string | yes | Owning nucleus |
| agents[].domain | string | yes | Capability domain (e.g. research, build) |
| agents[].tools | list | yes | Tools this agent exposes |
| agents[].model_tier | enum | yes | opus \| sonnet \| haiku \| local |
| search_index | string | no | Path to TF-IDF index file |
| updated_at | date | no | Last registry refresh timestamp |

## When to use
- Planning a composable crew that requires discovering which agents are available
- Auditing the full set of spawnable agents across all nuclei
- Auto-selecting the best agent for a role based on domain and tool match

## Builder
`archetypes/builders/capability_registry-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind capability_registry --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: capability_registry_cex
kind: capability_registry
pillar: P08
nucleus: n07
title: "CEX Global Capability Registry"
version: 1.0
quality: null
---
agents:
  - agent_id: n03_builder
    nucleus: n03
    domain: build
    tools: [cex_compile, cex_8f_runner]
    model_tier: opus
search_index: .cex/cache/capability_index.json
```

## Related kinds
- `agent_card` (P08) -- each entry in the registry points to an agent_card
- `crew_template` (P12) -- crew planner queries the registry to resolve roles
- `role_assignment` (P02) -- binds registry entries to crew roles

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_capability_registry]] | upstream | 0.49 |
| [[bld_schema_nucleus_def]] | upstream | 0.47 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_action_paradigm]] | upstream | 0.44 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_schema_search_strategy]] | upstream | 0.43 |
| [[bld_schema_integration_guide]] | upstream | 0.43 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_crew_template]] | upstream | 0.42 |
