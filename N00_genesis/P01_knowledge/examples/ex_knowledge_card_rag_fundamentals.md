---
id: ex_knowledge_card_rag_fundamentals
kind: knowledge_card
pillar: P01
title: RAG Fundamentals
tags: [rag, retrieval, embedding, search]
references:
  - tpl_knowledge_card
  - bld_knowledge_card_knowledge_card
  - ex_knowledge_card_prompt_caching
quality: 9.1
updated: "2026-04-07"
domain: "knowledge management"
version: "1.0.0"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.95
tldr: "Defines the knowledge card specification for rag fundamentals, with structural rules, validation gates, and integration points."
---
tldr: "Knowledge card covering RAG fundamentals: retrieval, augmentation, generation, and evaluation patterns."
quality: 8.5
tldr: "Knowledge card covering RAG fundamentals: retrieval, augmentation, generation, and evaluation patterns."
quality: 8.5
---

# RAG Fundamentals

> Skeleton: illustrates ideal naming `ex_{kind}_{topic}.md`

## Key Concepts

| Concept | Description |
|---------|------------|
| Chunking | Split docs into retrievable segments |
| Embedding | Vector representation for semantic search |
| Retrieval | Find relevant chunks via similarity |
| Augmentation | Inject retrieved context into prompt |

## Links

- Template: [[tpl_knowledge_card]]
- Builder: [[bld_knowledge_card_knowledge_card]]
- Related: [[ex_knowledge_card_prompt_caching]]
- Function: INJECT (what the AI knows)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `ex_knowledge_card_rag_fundamentals`
- **Tags**: [rag, retrieval, embedding, search]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `ex_knowledge_card_rag_fundamentals`
- **Tags**: [rag, retrieval, embedding, search]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "RAG Fundamentals"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "RAG Fundamentals" --top 5
```
