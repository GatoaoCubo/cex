---
id: bench_d
kind: knowledge_card
title: RAG Optimization
version: 1.0.0
quality: null
---

# RAG Optimization

**RAG (Retrieval-Augmented Generation)** combines document retrieval with generative models to enhance accuracy and relevance.

## 4 Optimization Techniques

1. **Chunking**  
   Splits documents into manageable parts.  
   *Pros*: Improves context relevance. *Cons*: May lose document coherence.

2. **Reranking**  
   Uses models to prioritize relevant snippets.  
   *Pros*: Enhances retrieval precision. *Cons*: Increases computational cost.

3. **Hybrid Search**  
   Combines keyword + semantic search methods.  
   *Pros*: Balances speed and accuracy. *Cons*: Complex implementation.

4. **Query Expansion**  
   Enhances queries with related terms.  
   *Pros*: Captures implicit user intent. *Cons*: Risks introducing irrelevant results.

## Comparison Table

| Technique     | Description               | Pros                     | Cons                     |
|---------------|---------------------------|--------------------------|--------------------------|
| Chunking      | Document segmentation     | Context relevance        | Coherence loss          |
| Reranking     | Prioritizes relevant snippets | Precision improvement   | Higher resource use     |
| Hybrid Search | Combines search methods   | Balanced accuracy/speed | Implementation complexity |
| Query Expansion | Expands search terms     | Captures implicit intent | Risk of irrelevant results |
