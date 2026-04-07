---
id: n04_rag_pipeline_memory
kind: memory_scope  
nucleus: N04
pillar: P10
domain: rag_pipeline
quality: 9.1
created: 2026-04-02
type: technical_memory
scope: rag_components
density_score: 1.0
title: "Rag Pipeline Memory"
version: 1.0.0
author: N04
tags: [memory_scope, knowledge, memory-scope, cex, artifact]
tldr: "Persistent memory store for cross-session learning with decay and relevance scoring"
updated: 2026-04-07
---

# RAG Pipeline Technical Memory

## Current Architecture
- **Retriever**: TF-IDF based via cex_retriever.py
- **Index Size**: 9.5MB (.cex/retriever_index.json)  
- **Document Count**: ~2184 documents indexed
- **Query Performance**: 5 results typical, <1s response
- **Storage**: Local JSON file with vocabulary and TF-IDF matrix

## Component Status
| Component | Status | Notes |
|-----------|--------|-------|
| Document Loader | ✅ Functional | Processes .md files |
| Chunking Strategy | ✅ Basic | File-level chunks |
| Embedding Generator | ❌ Missing | Only TF-IDF available |
| Vector Store | ❌ Missing | JSON file storage only |
| Retriever | ✅ Functional | TF-IDF similarity |
| Memory Selector | ❌ Broken | cex_memory_select.py fails |

## Knowledge Sources
- Builder ISOs (13 per builder × 107 builders)
- Knowledge Cards (106 KCs)
- Nucleus artifacts (N01-N07 fractals)
- Compiled artifacts (.yaml versions)
- Example artifacts in various directories

## Retrieval Patterns
```python
# Functional pattern
python _tools/cex_retriever.py --query "knowledge card" --top-k 5

# Expected pattern (broken)  
python _tools/cex_memory_select.py --query "rag" --limit 3
```

## Performance Baseline
- Query: "knowledge card" → 5 results in ~0.36 relevance score
- Best match: bld_collaboration_knowledge_card (0.3596 score)
- Vocabulary size: Estimated ~12K terms
- Memory usage: 9.5MB for full index

## Improvement Roadmap
1. **Semantic Layer**: Add embedding-based retrieval
2. **Hybrid Search**: Combine TF-IDF + embeddings  
3. **Memory Injection**: Fix broken memory selection
4. **Chunking**: Implement section-level chunking
5. **Persistence**: Move from JSON to proper vector DB