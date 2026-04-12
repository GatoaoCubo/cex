---
id: bench_d
kind: knowledge_card
title: RAG Optimization
version: 1.0.0
quality: null
---

# RAG Pipeline Optimization

**RAG (Retrieval-Augmented Generation)** combines document retrieval with LLM generation to enhance factual accuracy.

## 4 Optimization Techniques

1. **Chunking**  
   - Splits documents into manageable segments  
   - Pros: Reduces context overload, improves relevance  
   - Cons: May lose cross-chunk context

2. **Reranking**  
   - Prioritizes retrieval results using semantic scoring  
   - Pros: Enhances precision, handles ambiguous queries  
   - Cons: Increases computational overhead

3. **Hybrid Search**  
   - Combines vector similarity + keyword matching  
   - Pros: Balances speed and accuracy  
   - Cons: Complex to tune parameters

4. **Query Expansion**  
   - Augments queries with synonyms/related terms  
   - Pros: Captures implicit user intent  
   - Cons: Risks introducing irrelevant information

## Comparison Table

| Technique     | Description                | Pros                     | Cons                   |
|---------------|----------------------------|--------------------------|------------------------|
| Chunking      | Document segmentation      | Reduces context overload | May lose cross-chunk context |
| Reranking     | Semantic result prioritization | Enhances precision       | Higher computational cost |
| Hybrid Search | Combines vector + keyword  | Balances speed/accuracy  | Complex parameter tuning |
| Query Expansion | Query term augmentation   | Captures implicit intent | Risks irrelevant info  |
