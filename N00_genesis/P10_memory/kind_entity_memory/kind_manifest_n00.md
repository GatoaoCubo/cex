---
id: n00_entity_memory_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Entity Memory -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, entity_memory, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_entity_memory
  - bld_schema_reranker_config
  - entity-memory-builder
  - bld_schema_search_strategy
  - bld_collaboration_entity_memory
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An entity_memory stores structured, persistent knowledge about a named entity (person, company, product, concept) across sessions. It enables agents to remember facts, preferences, and relationships about entities without re-discovering them each time, reducing token consumption and improving response quality.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `entity_memory` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| entity_name | string | yes | Canonical name of the entity |
| entity_type | enum | yes | person \| company \| product \| concept \| place |
| attributes | object | yes | Key-value map of known facts about the entity |
| relationships | array | no | Links to other entity_memory IDs with relationship type |
| last_updated | datetime | yes | Timestamp of most recent attribute update |
| confidence | float | yes | Confidence score 0.0-1.0 for stored facts |

## When to use
- When the agent repeatedly encounters the same named entity across sessions
- When building customer-facing agents that must remember user preferences and history
- When compiling competitive intelligence on companies or products

## Builder
`archetypes/builders/entity_memory-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind entity_memory --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: em_company_acme_corp
kind: entity_memory
pillar: P10
nucleus: n01
title: "Example Entity Memory"
version: 1.0
quality: null
---
# Entity: Acme Corp
entity_type: company
attributes: {founded: 2010, sector: SaaS, hq: "Austin TX"}
confidence: 0.92
```

## Related kinds
- `knowledge_index` (P10) -- search index that makes entity memories retrievable
- `knowledge_card` (P01) -- deeper knowledge about a domain; entities are the nodes
- `memory_type` (P10) -- classifies this as long-term factual memory

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_entity_memory]] | related | 0.55 |
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[entity-memory-builder]] | related | 0.45 |
| [[bld_schema_search_strategy]] | upstream | 0.43 |
| [[bld_collaboration_entity_memory]] | downstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.42 |
| [[bld_schema_usage_report]] | upstream | 0.42 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
