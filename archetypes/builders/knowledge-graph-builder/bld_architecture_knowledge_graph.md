---
kind: architecture
id: bld_architecture_knowledge_graph
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of knowledge_graph -- inventory, dependencies, and architectural position in P01
quality: 9.1
title: "Architecture: knowledge_graph"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, architecture, P01, P08]
tldr: "Component map for knowledge_graph: entity+relation schema, extraction config, storage backend, traversal strategy, embedding integration, and downstream consumers."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_collaboration_knowledge_graph
  - knowledge-graph-builder
  - p01_kc_knowledge_graph
  - graph-rag-config-builder
  - p03_sp_knowledge_graph_builder
  - bld_examples_knowledge_graph
  - bld_schema_knowledge_graph
  - kc_graph_rag_config
  - bld_examples_graph_rag_config
  - p11_qg_knowledge_graph
---
# Architecture: knowledge_graph

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| entity_types | Constrained whitelist of node types with extraction hints | knowledge-graph-builder | required |
| relation_types | Annotated edge types with source, target, and directionality | knowledge-graph-builder | required |
| extraction_config | LLM prompt and extraction strategy for populating the graph | knowledge-graph-builder | required |
| storage_backend | Physical storage engine (neo4j, falkordb, in_memory, json) | knowledge-graph-builder | required |
| traversal_strategy | Query mode: local (entity-centric), global (community), or hybrid | knowledge-graph-builder | required |
| max_depth | Traversal depth limit for graph walks | knowledge-graph-builder | required |
| dedup_strategy | Entity resolution method: exact, fuzzy, or llm | knowledge-graph-builder | required |
| embedding_integration | Whether vector similarity augments graph traversal | knowledge-graph-builder | recommended |
| community_detection | Algorithm for grouping related entities (leiden, louvain) | knowledge-graph-builder | recommended |
| metadata | id, version, pillar, domain, author, created | knowledge-graph-builder | required |

## Dependency Graph

```
document_loader (P04) --feeds--> knowledge_graph (extraction populates graph)
chunk_strategy (P01) --feeds--> knowledge_graph (chunked text fed to extraction)
embedding_config (P01) --configures--> knowledge_graph (vector model for hybrid retrieval)
knowledge_graph --consumed_by--> retriever_config (P01) (graph used in hybrid retrieval)
knowledge_graph --consumed_by--> entity_memory (P10) (graph schema defines entity structure)
knowledge_graph --consumed_by--> knowledge_index (P10) (graph nodes indexed for vector search)
knowledge_graph --consumed_by--> agent (P02) (agents traverse graph during reasoning)
guardrail (P11) --constrains--> knowledge_graph (data governance rules for graph content)
```

| From | To | Type | Data |
|------|----|------|------|
| document_loader | knowledge_graph | feeds | Source text for triplet extraction |
| chunk_strategy | knowledge_graph | feeds | Text chunks input to extraction pipeline |
| embedding_config | knowledge_graph | configures | Vector model for hybrid node similarity |
| knowledge_graph | retriever_config | consumed_by | Graph schema used in hybrid retrieval config |
| knowledge_graph | entity_memory | consumed_by | Graph entity type definitions used for state storage |
| knowledge_graph | knowledge_index | consumed_by | Graph nodes ingested into vector index |
| knowledge_graph | agent | consumed_by | Agents traverse graph for multi-hop reasoning |
| guardrail | knowledge_graph | constrains | Data governance rules for graph content |

## Boundary Table

| knowledge_graph IS | knowledge_graph IS NOT |
|-------------------|----------------------|
| A schema for relational knowledge: entity types, relation types, traversal config | entity_memory (P10) -- stores per-entity state and recall, not schema |
| A specification for extraction, storage, and traversal of knowledge relationships | knowledge_index (P10) -- flat vector index config, no graph structure |
| A GraphRAG pipeline configuration artifact | rag_source (P01) -- external URL pointer, not a graph schema |
| A multi-hop reasoning enabler for agents | chunk_strategy (P01) -- text splitting, not relational structure |
| A community-detection-enabled summary structure | embedding_config (P01) -- vector model config, not graph schema |
| A hybrid retrieval schema (vector + graph) | knowledge_card (P01) -- distilled facts, not relational schema |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Schema | entity_types, relation_types | Define the typed structure of graph nodes and edges |
| Extraction | extraction_config, dedup_strategy | Populate the graph from unstructured text |
| Storage | storage_backend | Physical persistence and query engine |
| Traversal | traversal_strategy, max_depth | Query execution and context retrieval |
| Integration | embedding_integration, community_detection | Hybrid retrieval and summary capabilities |
| Safety | guardrail constraints | Data governance and quality enforcement |

## P01 Position

| P01 Kind | Relation to knowledge_graph |
|----------|---------------------------|
| knowledge_card | Provides domain knowledge about entities that appear in the graph |
| rag_source | External sources that feed the document_loader which feeds extraction |
| chunk_strategy | Splits source documents before graph extraction |
| embedding_config | Configures the vector model used for hybrid node similarity |
| retriever_config | Uses knowledge_graph as one of its retrieval backends |
| context_doc | Can be enriched with graph-retrieved context at query time |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_graph]] | downstream | 0.70 |
| [[knowledge-graph-builder]] | upstream | 0.68 |
| [[p01_kc_knowledge_graph]] | upstream | 0.53 |
| [[graph-rag-config-builder]] | upstream | 0.47 |
| [[p03_sp_knowledge_graph_builder]] | upstream | 0.44 |
| [[bld_examples_knowledge_graph]] | upstream | 0.41 |
| [[bld_schema_knowledge_graph]] | upstream | 0.41 |
| [[kc_graph_rag_config]] | upstream | 0.37 |
| [[bld_examples_graph_rag_config]] | upstream | 0.37 |
| [[p11_qg_knowledge_graph]] | downstream | 0.36 |
