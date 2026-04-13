---
id: atom_21_rag_taxonomy
kind: knowledge_card
pillar: P01
quality: 9.0
title: "RAG Taxonomy Surveys"
tags: [rag, retrieval, chunking, framework-atlas]
date: 2026-04-13
---
```

# Comprehensive RAG Configuration Guide with CEX Kind Mapping

## Boundary
This artifact is a technical reference for RAG configuration strategies and their alignment with CEX kinds. It is not a product specification, implementation guide, or performance benchmark. It focuses on structural taxonomy and configuration patterns rather than deployment specifics or vendor comparisons.

## Related Kinds
- **knowledge_index**: Stores vector embeddings and manages retrieval backends for RAG systems.
- **embedding_config**: Defines parameters for embedding models used in document representation.
- **scoring_rubric**: Provides evaluation metrics and thresholds for assessing RAG pipeline performance.
- **prompt_template**: Encapsulates query rewriting strategies to enhance retrieval effectiveness.
- **rag_source**: Manages external data sources and their integration into the RAG pipeline.

---

## 1. Introduction

This document provides a structured technical reference for implementing Retrieval-Augmented Generation (RAG) systems, with a focus on configuration strategies and their alignment with CEX (Configuration Exchange) kinds. It covers all pillars of RAG architecture, including data indexing, retrieval strategies, generation pipelines, and evaluation frameworks.

---

## 2. Retrieval Strategies

### 2.1 Dense Vector Retrieval
| Strategy | Description | CEX Kind | Use Case |
|---------|-------------|----------|----------|
| FAISS | High-performance similarity search | `knowledge_index` (store_type: FAISS) | Large-scale similarity search |
| HNSW | Approximate nearest neighbor search | `knowledge_index` (index_algo: HNSW) | Real-time retrieval with high recall |
| IVF-PQ | Quantized indexing for large-scale data | `knowledge_index` (index_algo: IVF-PQ) | Memory-constrained environments |
| Annoy | Tree-based indexing for fast queries | `knowledge_index` (index_algo: Annoy) | Low-latency applications |
| Milvus | Distributed vector database | `knowledge_index` (store_type: Milvus) | Multi-node clustering scenarios |

### 2.2 Sparse Text Retrieval
| Backend | Use Case | CEX Kind | Query Type |
|--------|----------|----------|------------|
| Elasticsearch | BM25 ranking | `knowledge_index` (sparse_backend: Elasticsearch) | Full-text search |
| Tantivy | Fast inverted index | `knowledge_index` (sparse_backend: Tantivy) | Lightweight applications |
| Meilisearch | Relevance ranking | `knowledge_index` (sparse_backend: Meilisearch) | E-commerce search |
| Whoosh | Python-native index | `knowledge_index` (sparse_backend: Whoosh) | Development environments |
| Solr | Enterprise search | `knowledge_index` (sparse_backend: Solr) | Large-scale deployments |

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
| Method | Parameters | CEX Kind | Example Use Case |
|--------|------------|----------|------------------|
| Token-based | `size=512`, `overlap=64` | `chunk_strategy` (method: token) | Legal document summarization |
| Sentence-based | `separator_hierarchy: [".", "!", "?"]` | `chunk_strategy` (method: sentence) | News article indexing |
| Paragraph-based | `max_length=1024` | `chunk_strategy` (method: paragraph) | Technical documentation |
| Semantic-based | `model: BERT`, `threshold=0.8` | `chunk_strategy` (method: semantic) | Scientific paper indexing |
| Line-based | `split_by: "\n"` | `chunk_strategy` (method: line) | Codebase indexing |

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
| Model | Dimensions | Metric | CEX Kind | Training Data |
|-------|------------|--------|----------|----------------|
| BGE | 768 | Cosine | `embedding_config` (model: BGE) | Multilingual corpus |
| E5 | 1024 | Dot Product | `embedding_config` (model: E5) | Wikipedia + Common Crawl |
| Arctic | 3072 | L2 | `embedding_config` (model: Arctic) | Code + technical documents |
| Sentence-BERT | 768 | Cosine | `embedding_config` (model: SBERT) | Sentiment analysis |
| MiniLM | 384 | Cosine | `embedding_config` (model: MiniLM) | Low-resource languages |

### 4.2 Model Configuration
```yaml
embedding_config:
  model: "BGE"
  batch_size: 32
  device: "cuda"
  normalize: true
```

---

## 5. Generation Pipelines

### 5.1 LLM Integration
| Model | Parameters | CEX Kind | Use Case |
|-------|------------|----------|----------|
| GPT-3 | 175B | `generation_config` (model: GPT-3) | Open-ended tasks |
| LLaMA | 65B | `generation_config` (model: LLaMA) | Private deployment |
| BLOOM | 176B | `generation_config` (model: BLOOM) | Multilingual tasks |
| Falcon | 180B | `generation_config` (model: Falcon) | Code generation |
| Mistral | 24B | `generation_config` (model: Mistral) | Dialogue systems |

### 5.2 Prompt Engineering
```yaml
prompt_template:
  system: "You are a helpful assistant"
  user: "Answer the following question: {question}"
  format: "chat"
```

---

## 6. Evaluation Metrics

### 6.1 Scoring Rubrics
| Metric | Description | CEX Kind | Threshold |
|--------|-------------|----------|-----------|
| Recall@K | Proportion of relevant documents retrieved | `scoring_rubric` (metric: recall) | ≥0.85 |
| Precision@K | Proportion of retrieved documents that are relevant | `scoring_rubric` (metric: precision) | ≥0.75 |
| MRR | Mean Reciprocal Rank | `scoring_rubric` (metric: mrr) | ≥0.65 |
| NDCG | Normalized Discounted Cumulative Gain | `scoring_rubric` (metric: ndcg) | ≥0.70 |
| F1 Score | Harmonic mean of precision and recall | `scoring_rubric` (metric: f1) | ≥0.80 |

### 6.2 Threshold Configuration
```yaml
scoring_rubric:
  metrics:
    recall: 0.85
    precision: 0.75
    mrr: 0.65
    ndcg: 0.70
    f1: 0.80
```

---

## 7. Data Sources

### 7.1 External Integration
| Source | Format | CEX Kind | Access Method |
|--------|--------|----------|---------------|
| Wikipedia | Text | `rag_source` (type: wikipedia) | API |
| Common Crawl | Text | `rag_source` (type: common_crawl) | S3 |
| PubMed | PDF/Text | `rag_source` (type: pubmed) | OAI |
| arXiv | PDF/Text | `rag_source` (type: arxiv) | API |
| GitHub | Code | `rag_source` (type: github) | Webhook |

### 7.2 Source Configuration
```yaml
rag_source:
  type: "wikipedia"
  language: "en"
  endpoint: "https://en.wikipedia.org/w/api.php"
```

---

## 8. Deployment Patterns

### 8.1 Infrastructure
| Pattern | Description | CEX Kind | Use Case |
|--------|-------------|----------|----------|
| Single-node | All components on one server | `deployment_config` (pattern: single_node) | Development |
| Multi-node | Distributed architecture | `deployment_config` (pattern: multi_node) | Production |
| Serverless | Cloud-based FaaS | `deployment_config` (pattern: serverless) | Scalable workloads |
| Edge | On-device processing | `deployment_config` (pattern: edge) | IoT applications |
| Hybrid | Combination of cloud and edge | `deployment_config` (pattern: hybrid) | Real-time analytics |

### 8.2 Configuration Example
```yaml
deployment_config:
  pattern: "multi_node"
  nodes: 3
  autoscaling: true
  region: "us-east-1"
```

---

## 9. Gap Analysis and Recommendations

| Concept | Current State | Recommendation |
|--------|---------------|----------------|
| Multimodal Retrieval | Limited support | Integrate CLIP and BLIP models |
| Real-time Updates | Batch processing only | Implement streaming pipelines |
| Security | No encryption | Add TLS and access controls |
| Cost Optimization | No budgeting | Introduce cost tracking metrics |
| Model Versioning | Manual process | Automate with MLflow |

---

## 10. Appendices

### 10.1 CEX Kind Mapping
| CEX Kind | Description | Example |
|----------|-------------|---------|
| knowledge_index | Vector storage and retrieval | FAISS, Milvus |
| embedding_config | Model parameters | BGE, E5 |
| scoring_rubric | Evaluation metrics | Recall@K, NDCG |
| prompt_template | Query formatting | Chat templates |
| rag_source | Data integration | Wikipedia, GitHub |

### 10.2 Glossary
- **RAG**: Retrieval-Augmented Generation
- **CEX**: Configuration Exchange
- **LLM**: Large Language Model
- **MRR**: Mean Reciprocal Rank
- **NDCG**: Normalized Discounted Cumulative Gain

This document serves as a living reference, with updates to be made as new RAG paradigms and CEX standards evolve.