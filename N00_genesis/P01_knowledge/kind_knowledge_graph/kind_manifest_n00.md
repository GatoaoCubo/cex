---
id: n00_knowledge_graph_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Knowledge Graph -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, knowledge_graph, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_collaboration_knowledge_graph
  - knowledge-graph-builder
  - bld_schema_knowledge_graph
  - bld_schema_graph_rag_config
  - bld_architecture_knowledge_graph
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_integration_guide
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Knowledge Graph defines a graph-based knowledge schema for GraphRAG architectures. It specifies entity types, relationship types, property schemas, and the population strategy for building a structured knowledge representation from unstructured sources. Used as the schema contract between entity extraction pipelines and graph database backends.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `knowledge_graph` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Graph name and domain |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| entity_types | list | yes | Node types (Person, Company, Product, etc.) |
| relationship_types | list | yes | Edge types (WORKS_AT, COMPETES_WITH, etc.) |
| graph_backend | enum | yes | neo4j\|falkordb\|tigergraph\|networkx |
| population_method | enum | yes | llm_extraction\|rule_based\|hybrid |
| node_count_estimate | int | no | Expected number of nodes |

## When to use
- When designing a GraphRAG pipeline from scratch
- When formalizing entity relationships for a knowledge domain
- When migrating from flat document RAG to structured graph RAG

## Builder
`archetypes/builders/knowledge_graph-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind knowledge_graph --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- knowledge engineers, ML engineers
- `{{DOMAIN_CONTEXT}}` -- domain with rich entity-relationship structure

## Example (minimal)
```yaml
---
id: knowledge_graph_cex_ecosystem
kind: knowledge_graph
pillar: P01
nucleus: n04
title: "CEX Ecosystem Knowledge Graph"
version: 1.0
quality: null
---
entity_types: [Nucleus, Kind, Pillar, Builder, Artifact]
relationship_types: [OWNS, PRODUCES, REFERENCES, EXTENDS]
graph_backend: falkordb
population_method: llm_extraction
node_count_estimate: 5000
```

## Related kinds
- `ontology` (P01) -- formal taxonomy that seeds the graph schema
- `graph_rag_config` (P01) -- runtime config for querying this graph
- `rag_source` (P01) -- source documents used to populate the graph

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_graph]] | downstream | 0.47 |
| [[knowledge-graph-builder]] | related | 0.44 |
| [[bld_schema_knowledge_graph]] | downstream | 0.42 |
| [[bld_schema_graph_rag_config]] | downstream | 0.41 |
| [[bld_architecture_knowledge_graph]] | downstream | 0.40 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
