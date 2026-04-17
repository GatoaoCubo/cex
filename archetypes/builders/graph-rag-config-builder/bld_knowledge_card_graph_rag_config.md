---
kind: knowledge_card
id: bld_knowledge_card_graph_rag_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for graph_rag_config production
quality: 9.2
title: "Knowledge Card Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, knowledge_card]
tldr: "Domain knowledge for graph_rag_config production"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
GraphRAG (Graph Retrieval-Augmented Generation) is a distinct architecture from traditional KG-QA (Knowledge Graph Question Answering). Traditional KG-QA executes SPARQL/Cypher queries against structured triples. GraphRAG (Edge et al., Microsoft 2024) instead builds a text-derived knowledge graph via LLM entity extraction, then performs community detection (Leiden algorithm) to create hierarchical summaries, enabling global sensemaking queries that flat vector RAG cannot answer.

The `graph_rag_config` artifact defines the pipeline parameters: entity extraction model, community detection settings, graph store backend, and query mode (local vs global). Local mode traverses entity neighborhoods; global mode synthesizes across community summaries. This distinction drives all key configuration decisions.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| GraphRAG (MS) | LLM-driven entity extraction + Leiden community detection + map-reduce summarization | Edge et al., Microsoft 2024 |
| Leiden Algorithm | Community detection that maximizes modularity; used by MS GraphRAG for hierarchical clustering | Traag et al. 2019 |
| Entity Extraction | LLM-driven extraction of named entities and relations from source docs into graph nodes/edges | Neo4j LLM Graph Builder |
| Local Query Mode | Traverses entity neighborhoods for specific entity-centric questions | MS GraphRAG docs |
| Global Query Mode | Map-reduce across community summaries for broad thematic questions | MS GraphRAG docs |
| Community Summaries | LLM-generated summaries for each detected graph community; the key RAG unit | Edge et al. 2024 |
| KG-QA (traditional) | Structured query execution over pre-defined ontology triples (SPARQL, Cypher) | W3C SPARQL 1.1 |
| Graph Store | Backend persistence for nodes/edges (Neo4j, Cosmos DB, NetworkX for dev) | MS GraphRAG config |

## Industry Standards
- Microsoft GraphRAG (github.com/microsoft/graphrag, Edge et al. 2024)
- Leiden community detection (Traag et al. 2019, scikit-network/graspologic)
- Neo4j LLM Graph Builder (entity extraction to property graph)
- LangChain GraphRAG chain (graph_chain.invoke with entity resolution)
- LlamaIndex KnowledgeGraphIndex (triplet extraction + graph store)
- W3C RDF/SPARQL (traditional KG-QA, distinct from GraphRAG)

## Common Patterns
1. **Local vs global query routing**: Route entity-specific queries to local mode, thematic queries to global mode.
2. **Entity extraction prompt tuning**: Customize extraction prompt per domain (legal, medical, technical).
3. **Community level selection**: Level 0 = fine-grained, Level 2 = coarse thematic; configure per query type.
4. **Hybrid GraphRAG + vector**: Use graph communities for global context, vector store for precise retrieval.
5. **Incremental graph update**: Re-run entity extraction only on changed documents, not full corpus.

## Pitfalls
- Conflating GraphRAG with traditional KG-QA: GraphRAG builds graph from unstructured text via LLM, not from pre-existing ontologies.
- Using global mode for entity-specific queries: global mode is expensive (map-reduce), wrong tool for lookup questions.
- Missing Leiden settings: default resolution parameter affects community granularity; must be tuned per corpus size.
- Skipping entity extraction validation: hallucinated entities degrade community quality; validate extraction samples.
- Treating community summaries as verbatim facts: they are LLM-generated summaries, require source attribution.
