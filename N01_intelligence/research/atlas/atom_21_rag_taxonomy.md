---
id: atom_21_rag_taxonomy
kind: knowledge_card
pillar: P01
quality: 8.8
title: "RAG Taxonomy Surveys"
tags: [rag, retrieval, chunking, framework-atlas]
date: 2026-04-13
---
```

# Comprehensive RAG Configuration Guide with CEX Kind Mapping

## 1. Introduction

This document provides a structured technical reference for implementing Retrieval-Augmented Generation (RAG) systems, with a focus on configuration strategies and their alignment with CEX (Configuration Exchange) kinds. It covers all pillars of RAG architecture, including data indexing, retrieval strategies, generation pipelines, and evaluation frameworks.

---

## 2. Retrieval Strategies

### 2.1 Dense Vector Retrieval
| Strategy | Description | CEX Kind |
|---------|-------------|----------|
| FAISS | High-performance similarity search | `knowledge_index` (store_type: FAISS) |
| HNSW | Approximate nearest neighbor search | `knowledge_index` (index_algo: HNSW) |
| IVF-PQ | Quantized indexing for large-scale data | `knowledge_index` (index_algo: IVF-PQ) |

### 2.2 Sparse Text Retrieval
| Backend | Use Case | CEX Kind |
|--------|----------|----------|
| Elasticsearch | BM25 ranking | `knowledge_index` (sparse_backend: Elasticsearch) |
| Tantivy | Fast inverted index | `knowledge_index` (sparse_backend: Tantivy) |

### 2.3 Hybrid Retrieval
```yaml
retriever_config:
  hybrid: true
  top_k: 10
  fusion_method: "rrf"  # Reciprocal Rank Fusion
```

---

## 3. Chunking Strategies

### 3.1 Text Chunking
| Method | Parameters | CEX Kind |
|--------|------------|----------|
| Token-based | `size=512`, `overlap=64` | `chunk_strategy` (method: token) |
| Sentence-based | `separator_hierarchy: [".", "!", "?"]` | `chunk_strategy` (method: sentence) |

### 3.2 Graph Chunking
```yaml
chunk_strategy:
  type: "graph"
  method: "community_detection"
  graph_endpoint: "https://graphdb.example.com"
```

---

## 4. Embedding Models

### 4.1 Model Selection
| Model | Dimensions | Metric | CEX Kind |
|-------|------------|--------|----------|
| BGE | 768 | Cosine | `embedding_config` (model: BGE) |
| E5 | 1024 | Dot Product | `embedding_config` (model: E5) |
| Arctic | 3072 | L2 | `embedding_config` (model: Arctic) |

### 4.2 Normalization
```yaml
embedding_config:
  normalize: true
  metric: "cosine"
```

---

## 5. RAG Pipeline Components

### 5.1 Knowledge Indexing
```yaml
knowledge_index:
  store_type: "Pinecone"
  index_algo: "HNSW"
  backend: "https://api.pinecone.io"
```

### 5.2 Query Rewriting
```yaml
prompt_template:
  rewrite_strategy: "HyDE"
  multi_query: true
  num_queries: 3
```

### 5.3 Reranking
```yaml
retriever_config:
  reranker: "cross-encoder"
  reranker_model: "cross-encoder/ms-marco-MiniLM-12-v1"
  reranker_top_k: 5
```

---

## 6. Context Compression

### 6.1 Compression Strategies
| Method | Target Ratio | CEX Kind |
|--------|--------------|----------|
| LLMLingua | 0.3 | `context_window_config` (method: llmlingua) |
| FILCO | 0.5 | `context_window_config` (method: filco) |

### 6.2 Configuration
```yaml
context_window_config:
  compression_method: "llmlingua"
  target_ratio: 0.4
```

---

## 7. Evaluation Metrics

### 7.1 Retrieval Metrics
| Metric | Formula | CEX Kind |
|--------|---------|----------|
| Precision@k | TP / (TP + FP) | `scoring_rubric` (metric: precision) |
| nDCG | Discounted cumulative gain | `scoring_rubric` (metric: ndcg) |

### 7.2 Generation Metrics
| Metric | Evaluation Method | CEX Kind |
|--------|-------------------|----------|
| Faithfulness | LLM-as-judge | `scoring_rubric` (metric: faithfulness) |
| Hallucination Rate | Claim-source matching | `scoring_rubric` (metric: hallucination) |

---

## 8. CEX Kind Mapping Table

| RAG Component | CEX Kind | Pillar | Key Fields |
|---------------|----------|--------|------------|
| External data source | `rag_source` | P01 | url, format, crawl_schedule |
| Embedding model | `embedding_config` | P01 | model, dimensions, metric |
| Retrieval parameters | `retriever_config` | P04 | hybrid, reranker, top_k |
| Vector index | `knowledge_index` | P10 | store_type, index_algo |
| Query rewriting | `prompt_template` | P03 | rewrite_strategy, multi_query |
| Quality evaluation | `scoring_rubric` | P07 | metrics, thresholds |
| Graph knowledge base | `rag_source` | P01 | type: graph, endpoint |

---

## 9. Production RAG Pipeline Architecture

```
[Data Ingestion]
  └── [Chunker] (chunk_strategy)
      └── [Embedder] (embedding_config)
          └── [Vector Store] (knowledge_index)
              └── [Graph Store] (rag_source)

[Query Processing]
  └── [Query Rewriter] (prompt_template)
      └── [Retriever] (retriever_config)
          └── [Reranker] (retriever_config)
              └── [Compressor] (context_window_config)
                  └── [Generator LLM] (agent)
                      └── [Self-Evaluator] (scoring_rubric)
```

---

## 10. Gap Analysis and Recommendations

| Concept | Current Handling | Recommended CEX Kind |
|--------|------------------|----------------------|
| Reranker (standalone) | Subfield of `retriever_config` | `reranker_config` |
| Multi-modal indexing | Not supported | `knowledge_index` (type: multimodal) |
| Real-time updates | Not specified | `knowledge_index` (sync: real_time) |

---

## 11. Sources

- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Elasticsearch BM25](https://www.elastic.co/what-is/bm25)
- [LLMLingua Paper](https://arxiv.org/abs/2305.06625)
- [RAG Evaluation Metrics](https://arxiv.org/abs/2302.05332)
- [Firecrawl Chunking Strategies](https://firecrawl.com/docs)

---

## 12. Appendix: CEX Kind Definitions

### P01: Data Indexing
- `rag_source`: External data source configuration
- `embedding_config`: Embedding model parameters
- `chunk_strategy`: Text/graph chunking rules

### P04: Retrieval
- `retriever_config`: Hybrid search parameters

### P10: Knowledge Store
- `knowledge_index`: Vector/indexing backend configuration

### P03: Query Processing
- `prompt_template`: Query rewriting rules

### P07: Evaluation
- `scoring_rubric`: Metric definitions and thresholds

---

This document serves as a living reference, with updates to be made as new RAG paradigms and CEX standards evolve.