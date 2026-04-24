---
id: n00_memory_architecture_manifest
kind: knowledge_card
8f: F3_inject
pillar: P10
nucleus: n00
title: "Memory Architecture -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, memory_architecture, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_memory_architecture
  - bld_schema_memory_scope
  - bld_schema_sandbox_spec
  - bld_schema_reranker_config
  - bld_schema_memory_type
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A memory_architecture document designs the complete memory system for a nucleus or enterprise brain, specifying which memory types are used, how they interact, what storage backends serve each layer, and how data flows between short-term (session) and long-term (persistent) memory. It is the blueprint that all other P10 kinds instantiate from.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `memory_architecture` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| scope | enum | yes | nucleus \| enterprise \| global |
| memory_layers | array | yes | List of memory types with storage backend and TTL |
| retrieval_strategy | enum | yes | bm25 \| faiss \| hybrid \| exact |
| consolidation_ref | string | no | ID of associated consolidation_policy |
| persistence_backend | enum | yes | filesystem \| redis \| sqlite \| vector_db |
| max_working_set | integer | yes | Maximum tokens held in active memory |

## When to use
- When designing the memory system for a new nucleus (N08+)
- When auditing or refactoring how a nucleus handles long-term knowledge
- When selecting storage backends and retrieval strategies for a new deployment

## Builder
`archetypes/builders/memory_architecture-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind memory_architecture --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ma_n04_knowledge_nucleus
kind: memory_architecture
pillar: P10
nucleus: n04
title: "Example Memory Architecture"
version: 1.0
quality: null
---
# N04 Memory Architecture
scope: nucleus
retrieval_strategy: hybrid
persistence_backend: filesystem
max_working_set: 50000
memory_layers:
  - type: entity_memory, backend: filesystem, ttl: permanent
  - type: session_state, backend: redis, ttl: 3600
```

## Related kinds
- `consolidation_policy` (P10) -- lifecycle rules this architecture depends on
- `session_backend` (P10) -- backend configuration for session-layer memory
- `memory_type` (P10) -- taxonomy of memory types this architecture uses

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_memory_architecture]] | upstream | 0.47 |
| [[bld_schema_memory_scope]] | upstream | 0.42 |
| [[bld_schema_sandbox_spec]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_memory_type]] | related | 0.39 |
| [[bld_schema_sandbox_config]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_integration_guide]] | upstream | 0.38 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.38 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
