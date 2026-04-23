---
id: n04_knowledge_memory_index
kind: memory_summary
nucleus: N04
pillar: P10
domain: knowledge_management
quality: 9.1
created: 2026-04-02
type: persistent_memory
scope: knowledge_nucleus
density_score: 1.0
title: "Knowledge Memory Index"
version: 1.0.0
author: N04
tags: [memory_summary, knowledge]
tldr: "1. Implement semantic embeddings alongside TF-IDF"
updated: 2026-04-07
related:
  - self_review_2026-04-02
  - n04_rag_pipeline_memory
  - agent_card_n04
  - bld_collaboration_memory_scope
  - bld_collaboration_memory_type
  - p01_kc_memory_scope
  - knowledge-index-builder
  - memory-scope-builder
  - bld_manifest_memory_type
  - bld_collaboration_knowledge_index
---

# N04 Knowledge Memory Index

## Domain Memory
- **RAG Pipeline**: TF-IDF retriever functional, 9.5MB index, ~2184 documents
- **KC Library**: 106 knowledge cards covering all major kinds
- **Taxonomy**: 114 kinds tracked across 12 pillars
- **Embeddings**: Status unclear - mainly TF-IDF based retrieval
- **Cross-References**: Naming convention drift (hyphens vs underscores)

## Recent Learning
- Unicode corruption affects critical system files (.cex/kinds_meta.json)
- N04 memory system was empty - now being populated
- Retriever works but memory selection tools broken
- Builders (107) vs KCs (106) - mainly naming convention issues

## Knowledge Gaps Identified
- Missing semantic search capabilities
- No persistent memory accumulation patterns
- Limited cross-nucleus knowledge sharing verification
- Taxonomy consistency automation missing

## Tools Status
- ✅ cex_retriever.py: functional
- ❌ cex_memory_select.py: broken  
- ✅ cex_compile.py: functional
- ⚠️ .cex/retriever_index.json: unicode issues

## Memory Injection Points
- F3 INJECT: KCs loaded into 8F pipeline
- Handoffs: Knowledge context in task specifications  
- Cross-nucleus: Domain expertise sharing
- Retrieval: Similarity search for relevant artifacts

## Improvement Opportunities
1. Implement semantic embeddings alongside TF-IDF
2. Create automated taxonomy consistency checks
3. Fix memory selection and injection tools
4. Establish memory decay and refresh protocols
5. Create knowledge graph relationships between KCs


## Memory Index Architecture

The knowledge memory index enables fast retrieval with these design decisions:

- **Inverted index**: tags map to document lists for O(1) lookup by keyword
- **Recency weighting**: entries decay linearly over 365 days unless explicitly refreshed
- **Type partitioning**: four memory types stored in separate index segments
- **Pruning schedule**: entries below 0.3 relevance threshold purged on weekly cycle

### Index Configuration

```yaml
# Memory index settings
index:
  backend: filesystem
  format: json
  max_entries: 10000
  prune_threshold: 0.3
  prune_schedule: weekly
  decay_model: linear_365d
  partitions: [correction, preference, convention, context]
```

| Metric | Value | Update Frequency |
|--------|-------|-----------------|
| Total entries | Tracked | Per-write |
| Average relevance | Computed | Per-query |
| Partition balance | Monitored | Weekly |
| Stale entry ratio | Alerting | Daily |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[self_review_2026-04-02]] | upstream | 0.50 |
| [[n04_rag_pipeline_memory]] | related | 0.46 |
| [[agent_card_n04]] | upstream | 0.39 |
| [[bld_collaboration_memory_scope]] | downstream | 0.37 |
| [[bld_collaboration_memory_type]] | downstream | 0.34 |
| [[p01_kc_memory_scope]] | upstream | 0.32 |
| [[knowledge-index-builder]] | related | 0.31 |
| [[memory-scope-builder]] | upstream | 0.31 |
| [[bld_manifest_memory_type]] | upstream | 0.31 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.30 |
