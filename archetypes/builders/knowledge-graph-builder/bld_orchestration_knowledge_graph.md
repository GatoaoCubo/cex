---
kind: collaboration
id: bld_collaboration_knowledge_graph
pillar: P12
llm_function: COLLABORATE
purpose: How knowledge-graph-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration: knowledge-graph-builder"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, collaboration, P12]
tldr: "knowledge-graph-builder is a schema specialist: receives domain + entity seeds, produces graph schema, feeds retriever-config and entity-memory builders."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - knowledge-graph-builder
  - bld_architecture_knowledge_graph
  - bld_collaboration_knowledge_card
  - bld_collaboration_vector_store
  - graph-rag-config-builder
  - bld_collaboration_retriever_config
  - p01_kc_knowledge_graph
  - bld_collaboration_builder
  - bld_collaboration_knowledge_index
  - bld_collaboration_embedding_config
---

# Collaboration: knowledge-graph-builder

## My Role in Crews
I am a SCHEMA SPECIALIST. I answer ONE question: "what entity types and relation types does
this domain need, with what extraction logic, storage backend, and traversal strategy?"

I do not store entity instances (entity-memory-builder handles that).
I do not configure vector indices (knowledge-index-builder handles that).
I do not point to external sources (rag-source-builder handles that).
I define the relational schema that makes graph-based knowledge retrieval possible.

## Crew Compositions

### Crew: "Full GraphRAG Pipeline"
```
  1. rag-source-builder      -> "external document sources to index"
  2. chunk-strategy-builder  -> "how to split documents before extraction"
  3. embedding-config-builder -> "vector model for hybrid retrieval"
  4. knowledge-graph-builder  -> "graph schema: entities, relations, traversal"
  5. retriever-config-builder -> "hybrid retrieval config combining graph + vector"
```

### Crew: "Agent Knowledge Base"
```
  1. knowledge-card-builder   -> "domain knowledge cards for agent injection"
  2. knowledge-graph-builder  -> "relational graph schema for multi-hop reasoning"
  3. entity-memory-builder    -> "per-entity state storage using graph schema"
  4. agent-builder            -> "agent that uses graph for reasoning"
```

### Crew: "Domain Intelligence"
```
  1. knowledge-graph-builder  -> "graph schema for competitive/domain intel"
  2. knowledge-index-builder  -> "vector index of graph nodes"
  3. knowledge-card-builder   -> "key facts and summaries from graph communities"
```

## Handoff Protocol

### I Receive
- seeds: domain name, initial entity type ideas, sample text or documents
- optional: target storage backend, query patterns needed, downstream consumers
- optional: framework preference (GraphRAG, LlamaIndex, LightRAG, Neo4j)

### I Produce
- knowledge_graph artifact (.md + .yaml frontmatter)
- committed to: `P01_knowledge/examples/p01_kg_{domain}.md`

### I Signal
- signal: complete (with quality score from quality gate)
- if quality < 8.0: signal retry with failure reasons from HARD gate checks

## Builders I Depend On
| Builder | Why |
|---------|-----|
| chunk-strategy-builder | Chunked text is input to extraction pipeline |
| embedding-config-builder | Vector model reference for hybrid retrieval integration |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| retriever-config-builder | References knowledge_graph as retrieval backend |
| entity-memory-builder | Uses entity types from graph schema for state structure |
| knowledge-index-builder | Indexes graph nodes for vector similarity queries |
| agent-builder | Agents traverse graph schema during multi-hop reasoning |

## Signal Format

```yaml
nucleus: n03
kind: knowledge_graph
artifact: P01_knowledge/examples/p01_kg_{domain}.md
status: complete
quality_gate: pass
score: null
gates_passed: 12/12
timestamp: "{{ISO8601}}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-graph-builder]] | upstream | 0.47 |
| [[bld_architecture_knowledge_graph]] | upstream | 0.43 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.42 |
| [[bld_collaboration_vector_store]] | sibling | 0.41 |
| [[graph-rag-config-builder]] | upstream | 0.39 |
| [[bld_collaboration_retriever_config]] | sibling | 0.38 |
| [[p01_kc_knowledge_graph]] | upstream | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_collaboration_knowledge_index]] | sibling | 0.37 |
| [[bld_collaboration_embedding_config]] | sibling | 0.36 |
