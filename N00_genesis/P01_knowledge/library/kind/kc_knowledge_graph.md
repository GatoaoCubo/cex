---
id: p01_kc_knowledge_graph
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "knowledge_graph: Relational Knowledge Structure"
version: 1.0.0
created: 2026-04-12
updated: 2026-04-12
author: n03_builder
domain: knowledge_graph
quality: 9.1
tags: [knowledge_graph, p01, INJECT, kind-kc]
tldr: "Defines entity types, relation types, extraction logic, storage backend, and traversal strategies for graph-based knowledge"
when_to_use: "Building, reviewing, or reasoning about knowledge_graph artifacts"
keywords: [knowledge-graph, GraphRAG, entity-extraction, neo4j, relations, traversal]
feeds_kinds: [knowledge_graph]
density_score: null
related:
  - knowledge-graph-builder
  - bld_collaboration_knowledge_graph
  - bld_knowledge_card_knowledge_graph
  - p03_sp_knowledge_graph_builder
  - bld_architecture_knowledge_graph
  - bld_knowledge_card_graph_rag_config
  - p10_lr_knowledge_graph_builder
  - bld_instruction_knowledge_graph
  - bld_schema_knowledge_graph
  - bld_examples_knowledge_graph
---

# Knowledge Graph

## Spec
```yaml
kind: knowledge_graph
pillar: P01
llm_function: INJECT
max_bytes: 2048
naming: p01_kg_{{domain}}.yaml
core: false
```

## What It Is
A knowledge_graph defines the relational structure for domain knowledge: entity types, relation types, extraction prompts, storage backend, traversal strategies, and embedding integration. It is NOT an entity_memory (P10, which stores and recalls individual entity state) nor a knowledge_index (P10, which is flat vector search). The knowledge_graph captures RELATIONSHIPS between entities -- the "graph" in GraphRAG.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| Microsoft GraphRAG | `GraphRAGIndexer` | LLM extracts entities+relations from docs, builds community summaries |
| LlamaIndex KG | `KnowledgeGraphIndex` | Triplet extraction (subject, predicate, object) from documents |
| Neo4j + LangChain | `Neo4jGraph` + `GraphCypherQAChain` | Cypher query generation from natural language |
| LightRAG | Local + global search | Dual-level: entity-centric (local) + community (global) retrieval |
| Haystack | `KnowledgeGraph` component | RDF/SPARQL integration; entity linking pipeline |
| Amazon Neptune | Managed graph DB | Property graph (Gremlin) or RDF (SPARQL) |
| FalkorDB | In-memory graph | Redis-compatible, Cypher queries, vector+graph hybrid |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| entity_types | list[string] | required | More types = richer graph but noisier extraction |
| relation_types | list[string] | required | Constrained set prevents hallucinated relations |
| extraction_prompt | string | required | LLM prompt for entity+relation extraction from text |
| storage_backend | enum(neo4j/falkordb/in_memory/json) | in_memory | Neo4j for production; in_memory for prototyping |
| traversal_strategy | enum(local/global/hybrid) | hybrid | Local = entity-centric; global = community summaries |
| max_depth | int | 3 | Deeper traversal = richer context but slower queries |
| embedding_integration | bool | true | Combine vector similarity + graph traversal |
| community_detection | enum(leiden/louvain/none) | leiden | Groups related entities; enables global search |
| dedup_strategy | enum(exact/fuzzy/llm) | fuzzy | Entity resolution: "OpenAI" = "Open AI" = same node |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| GraphRAG (MS) | Large corpus, need global summaries | Index 1000 docs, answer "what are the main themes?" |
| Triplet extraction | Structured knowledge from unstructured text | Extract (Company, acquired, Startup) from news articles |
| Hybrid retrieval | Need both semantic + relational answers | Vector search for similar docs + graph walk for relations |
| Schema-constrained | Known domain ontology | Medical: (Drug, treats, Disease), (Gene, encodes, Protein) |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Unconstrained entity types | Exploding node count, noisy graph | Define explicit entity type whitelist |
| No deduplication | Same entity appears as 5 different nodes | Implement fuzzy or LLM-based entity resolution |
| Flat traversal (depth=1) | Misses multi-hop relationships | Use depth 2-3 with relevance pruning |
| Graph without embeddings | Can't do semantic similarity on nodes | Embed entity descriptions, enable hybrid search |

## Integration Graph
```
[document_loader] --> [knowledge_graph] --> [retriever_config]
                           |                      |
                    [entity_memory (P10)]   [embedding_config]
                           |
                    [storage backend]
```

## Decision Tree
- IF flat Q&A over documents THEN vector search only (skip graph)
- IF "what are the themes/trends" questions THEN GraphRAG with community detection
- IF known ontology (medical, legal, financial) THEN schema-constrained graph
- IF need to combine "similar to X" + "related to Y" THEN hybrid retrieval
- DEFAULT: LlamaIndex KG with triplet extraction, in-memory, hybrid traversal

## Quality Criteria
- GOOD: Entity types + relation types + extraction prompt + storage backend defined
- GREAT: Community detection; dedup strategy; embedding integration; traversal depth justified
- FAIL: No entity types defined; unconstrained extraction; no dedup; graph without retrieval strategy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-graph-builder]] | related | 0.67 |
| [[bld_collaboration_knowledge_graph]] | downstream | 0.60 |
| [[bld_knowledge_card_knowledge_graph]] | sibling | 0.57 |
| [[p03_sp_knowledge_graph_builder]] | downstream | 0.57 |
| [[bld_architecture_knowledge_graph]] | downstream | 0.54 |
| [[bld_knowledge_card_graph_rag_config]] | sibling | 0.54 |
| [[p10_lr_knowledge_graph_builder]] | downstream | 0.51 |
| [[bld_instruction_knowledge_graph]] | downstream | 0.51 |
| [[bld_schema_knowledge_graph]] | downstream | 0.48 |
| [[bld_examples_knowledge_graph]] | downstream | 0.43 |
