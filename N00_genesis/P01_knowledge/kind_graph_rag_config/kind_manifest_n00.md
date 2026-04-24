---
id: n00_graph_rag_config_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Graph RAG Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, graph_rag_config, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_collaboration_knowledge_graph
  - bld_schema_graph_rag_config
  - graph-rag-config-builder
  - knowledge-graph-builder
  - bld_architecture_knowledge_graph
  - bld_schema_reranker_config
  - bld_schema_knowledge_graph
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Graph RAG Config defines the architecture and parameters for a graph-based retrieval augmented generation system. Unlike vector-only RAG, GraphRAG traverses knowledge graph edges to retrieve semantically related nodes, enabling multi-hop reasoning. It configures the graph backend, entity extraction method, traversal strategy, and integration with the LLM generation layer.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `graph_rag_config` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Config name and target graph |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| graph_backend | enum | yes | neo4j\|tigergraph\|falkordb\|networkx |
| entity_extraction | enum | yes | llm\|spacy\|regex\|hybrid |
| traversal_depth | int | yes | Maximum graph hops during retrieval |
| community_detection | bool | yes | Whether to use community clustering |
| vector_fallback | bool | yes | Fall back to vector search if graph misses |

## When to use
- When knowledge has rich relational structure (entities + relationships)
- When multi-hop reasoning across connected facts is required
- When semantic similarity alone produces low recall

## Builder
`archetypes/builders/graph_rag_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind graph_rag_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers building knowledge graph pipelines
- `{{DOMAIN_CONTEXT}}` -- domain with rich entity relationships

## Example (minimal)
```yaml
---
id: graph_rag_config_cex_knowledge
kind: graph_rag_config
pillar: P01
nucleus: n04
title: "CEX Knowledge Graph RAG"
version: 1.0
quality: null
---
graph_backend: falkordb
entity_extraction: hybrid
traversal_depth: 3
community_detection: true
vector_fallback: true
```

## Related kinds
- `knowledge_graph` (P01) -- the graph schema this config queries
- `retriever_config` (P01) -- vector retrieval fallback config
- `agentic_rag` (P01) -- agent-driven orchestration of graph retrieval
- `ontology` (P01) -- entity taxonomy used for entity extraction

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_graph]] | downstream | 0.51 |
| [[bld_schema_graph_rag_config]] | downstream | 0.47 |
| [[graph-rag-config-builder]] | related | 0.42 |
| [[knowledge-graph-builder]] | related | 0.41 |
| [[bld_architecture_knowledge_graph]] | downstream | 0.40 |
| [[bld_schema_reranker_config]] | downstream | 0.40 |
| [[bld_schema_knowledge_graph]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
