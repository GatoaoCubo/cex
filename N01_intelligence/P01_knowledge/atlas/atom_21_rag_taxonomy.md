---
id: atom_21_rag_taxonomy
kind: knowledge_card
pillar: P01
quality: 8.8
title: "RAG Taxonomy Surveys"
tags: [rag, retrieval, chunking, reranking, agentic-rag, graph-rag, late-chunking, framework-atlas]
date: 2026-04-13
---

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

---

## 11. Agentic RAG (2025-2026)

### 11.1 Definition and Taxonomy

Agentic RAG embeds autonomous AI agents into the RAG pipeline, transcending the limitations of static retrieve-then-generate patterns. Source: [arXiv 2501.09136 -- Agentic RAG Survey, updated Apr 2026](https://arxiv.org/abs/2501.09136)

| Dimension | Naive RAG | Agentic RAG |
|-----------|-----------|-------------|
| Retrieval | Single-shot, fixed query | Iterative, adaptive, multi-step |
| Control | Linear pipeline | Agentic loop with reflection |
| Memory | Context window only | Long-term + episodic memory |
| Tools | Embedder + LLM | Planner + Retriever + Executor + Critic |
| Error handling | None | Self-correction via reflection |
| Multi-source | Manual config | Dynamic source selection |

### 11.2 Agentic RAG Architectures

| Architecture | Cardinality | Control | Description | Best For |
|---|---|---|---|---|
| Single-agent RAG | 1 agent | Linear | One agent manages plan + retrieve + generate | Simple QA |
| Multi-agent RAG | N agents | Parallel | Specialized agents (planner, retriever, critic) run concurrently | Complex research |
| Hierarchical RAG | N agents | Tree | Supervisor dispatches to specialist retriever agents | Enterprise Q&A |
| Reflexion RAG | 1 agent + critic | Loop | Agent self-evaluates and re-queries until confidence threshold met | High-accuracy tasks |
| FLARE | 1 agent | Forward-looking | Generates tentatively, triggers retrieval when uncertain | Long-form generation |

### 11.3 Agentic RAG Design Patterns

| Pattern | Industry Term | Description |
|---------|--------------|-------------|
| Reflection | Self-critique | Agent evaluates its own output and re-retrieves if quality below threshold |
| Planning | Task decomposition | Agent breaks complex query into sub-queries before retrieval |
| Tool use | Function calling | Agent selects retrieval backends dynamically (web, vector DB, SQL) |
| Memory | Episodic + semantic | Agent maintains short-term working memory + long-term knowledge store |
| Multi-agent coordination | Orchestration | Supervisor agent dispatches retrieval subtasks to specialist agents |

### 11.4 Open Research Challenges (2026)

| Challenge | Current Gap | Active Work |
|-----------|------------|-------------|
| Evaluation | No unified benchmark for agentic retrieval quality | RAGAS 2.0, AgentBench RAG track |
| Coordination overhead | Multi-agent latency 3-5x naive RAG | Async retrieval + speculative generation |
| Memory management | Context saturation in long sessions | Hierarchical compression + selective eviction |
| Governance | Agentic loops can escape guardrails | Structured output constraints + kill-switch |
| Efficiency | Reflection loops consume 10x tokens | Confidence-gated retrieval triggers |

---

## 12. Graph RAG (v2 and LazyGraphRAG)

### 12.1 Evolution from v1 to v2

Microsoft's GraphRAG project (2024-2026) constructs a knowledge graph from the corpus and uses community detection to answer global queries. Source: [Microsoft Research -- GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/) | [GitHub microsoft/graphrag](https://github.com/microsoft/graphrag)

| Version | Release | Indexing Cost | Key Feature |
|---------|---------|--------------|-------------|
| GraphRAG v1 | 2024-Q2 | ~$33K per large dataset | Global + local search via community summaries |
| GraphRAG v1.2 | 2024-Q4 | ~$33K | +10-20% quality on global queries via mixed community reports |
| LazyGraphRAG | 2025-Q2 | ~$330 (99% reduction) | Community summarization deferred to query time |
| GraphRAG v2 | 2025-Q4 | Optimized | Developer-experience overhaul, modular pipeline |

### 12.2 GraphRAG vs Naive RAG vs Agentic RAG

| Dimension | Naive RAG | GraphRAG | Agentic RAG |
|-----------|-----------|---------|-------------|
| Query type | Local (factoid) | Global (thematic, cross-doc) | Both + multi-step |
| Indexing cost | Low | High (v1) / Low (Lazy) | Low |
| Relationship reasoning | No | Yes (graph traversal) | Partial (tool use) |
| Latency | Low (50-200ms) | High (2-10s) | High (seconds-minutes) |
| Best for | Factoid QA | Cross-document synthesis | Complex research |

### 12.3 LazyGraphRAG Implementation

```yaml
# LazyGraphRAG defers community summarization to query time
graph_rag_config:
  mode: lazy                         # deferred summarization
  community_detection: leiden        # Leiden algorithm for graph partitioning
  summary_depth: on_demand           # generate summaries only when queried
  embedding_backend: text-embedding-3-small
  graph_store: networkx              # or neo4j for production
  cost_vs_quality: balanced          # quality < eager but cost 99% lower
```

### 12.4 When to Use Graph RAG

| Signal | Use GraphRAG? |
|--------|-------------|
| Query spans multiple documents | YES |
| Query is thematic ("what are the themes in...") | YES |
| Query is a factoid ("what is X") | NO -- use naive RAG |
| Corpus has clear entity relationships | YES |
| Cost is primary constraint | Use LazyGraphRAG |
| Low latency required (<500ms) | NO |

Source: [Graph Praxis -- Graph RAG in 2026](https://medium.com/graph-praxis/graph-rag-in-2026-a-practitioners-guide-to-what-actually-works-dca4962e7517)

---

## 13. Late Chunking (Jina 2024-2025)

### 13.1 Technique Overview

Late chunking inverts the traditional chunk-then-embed pipeline. The full document is embedded first using a long-context model; only after full-document attention is applied are the token vectors pooled per chunk. This preserves inter-chunk context in each chunk's embedding. Source: [arXiv 2409.04701 -- Late Chunking](https://arxiv.org/pdf/2409.04701) | [Jina AI Blog](https://jina.ai/news/late-chunking-in-long-context-embedding-models/)

```
TRADITIONAL:     split document -> embed each chunk -> retrieve
LATE CHUNKING:   embed full document -> pool per-chunk spans -> retrieve
```

### 13.2 Performance Results

| Benchmark | Traditional Chunking | Late Chunking | Delta |
|-----------|---------------------|--------------|-------|
| Average (512-token chunks) | baseline | +24.47% relative | +24.47% |
| Pronoun resolution accuracy | Low (no cross-chunk context) | High (full-doc attention) | Significant |
| "the city" -> "Berlin" mapping | Fails across chunk boundaries | Resolves correctly | Fixed |

### 13.3 Implementation

```python
# Late chunking with Jina Embeddings v3
from jina_embeddings import JinaEmbeddingsV3

model = JinaEmbeddingsV3(max_tokens=8192)  # long-context required

# Step 1: embed the full document
doc_tokens = model.tokenize(full_document)         # up to 8192 tokens
full_embedding_matrix = model.encode(doc_tokens)   # shape: [seq_len, dim]

# Step 2: define chunk spans (character offsets -> token indices)
chunk_spans = [(0, 512), (448, 960), (896, 1408)]  # with overlap

# Step 3: mean-pool per span (late pooling)
chunk_embeddings = [
    full_embedding_matrix[start:end].mean(axis=0)
    for start, end in chunk_spans
]
# Result: each chunk embedding carries full-document context
```

### 13.4 Constraints and Requirements

| Requirement | Value | Why |
|---|---|---|
| Model context window | >= 8192 tokens | Must fit full document |
| Compatible models | jina-embeddings-v2, v3 | Must expose token-level embeddings |
| Document length limit | Model max_tokens | Longer docs need sliding window |
| Memory overhead | O(seq_len * dim) | Stores full embedding matrix before pooling |
| Incompatible with | OpenAI text-embedding-3-* | API returns only [CLS] vector, not per-token |

Sources: [GitHub jina-ai/late-chunking](https://github.com/jina-ai/late-chunking) | [Elasticsearch + Jina Late Chunking](https://www.elastic.co/search-labs/blog/late-chunking-elasticsearch-jina-embeddings) | [Milvus + Late Chunking](https://milvus.io/blog/smarter-retrieval-for-rag-late-chunking-with-jina-embeddings-v2-and-milvus.md)

---

## 14. Chunking Benchmarks (NVIDIA 2024 + 2026 State)

### 14.1 NVIDIA 2024 Benchmark Results

NVIDIA tested 7 chunking strategies across 5 datasets including DigitalCorpora767 (767 PDFs, 991 annotated questions), Earnings (512 PDFs), and FinanceBench. Source: [NVIDIA Technical Blog -- Best Chunking Strategy](https://developer.nvidia.com/blog/finding-the-best-chunking-strategy-for-accurate-ai-responses/)

| Strategy | Financial Docs | Knowledge Graphs | Legal Docs | Winner |
|----------|---------------|-----------------|-----------|--------|
| Page-level | 0.60 | 0.52 (best) | 0.58 | Knowledge graphs |
| 1024-token | 0.579 (best) | 0.45 | 0.54 | Financial |
| 512-token | 0.54 | 0.48 | 0.56 | Balanced |
| 256-token | 0.51 | 0.44 | 0.52 | Factoid queries |
| Semantic | 0.55 | 0.49 | 0.57 | Mixed corpora |
| Sentence | 0.49 | 0.42 | 0.55 | Conversational |
| Paragraph | 0.53 | 0.47 | 0.58 | Legal |

Key NVIDIA finding: Page-level chunking highest accuracy (0.648) with lowest variance (0.107). Optimal chunk size varies by content type AND query pattern.

### 14.2 Query-Type vs Chunk Size Matrix

| Query Type | Optimal Chunk Size | Reasoning |
|-----------|-------------------|-----------|
| Factoid ("Who is...") | 256-512 tokens | Precise, localized answer |
| Analytical ("Summarize the...") | 1024+ tokens | Needs broader context |
| Comparison ("How does X differ from Y") | 512-1024 tokens | Needs enough detail per concept |
| Global ("What are the themes in...") | Page-level or GraphRAG | Cross-document synthesis |

### 14.3 2026 Benchmark Update

Source: [Prem AI -- RAG Chunking 2026 Benchmark Guide](https://blog.premai.io/rag-chunking-strategies-the-2026-benchmark-guide/)

| Strategy | Accuracy (real-doc test) | Cost | Verdict |
|----------|------------------------|------|---------|
| Recursive splitting 512 tokens | 69% | Zero model calls | Best overall cost/quality |
| Semantic chunking | 65% | 1 embedding call/chunk | Good for mixed corpora |
| Late chunking (Jina) | 72% | 1 full-doc embedding | Best quality, higher memory |
| Agentic re-chunking | 70% | LLM call per doc | Best for PDFs/tables |
| Fixed 256 tokens | 58% | Zero model calls | Fast baseline |

### 14.4 Chunking Strategy Selection Guide

```
Is the document structured (PDF with tables, headers)?
  YES --> Agentic re-chunking or page-level
  NO  --> Does the doc exceed 8192 tokens total?
            YES --> Recursive splitting (512, overlap=64)
            NO  --> Late chunking (preserves cross-chunk context, +24% recall)
                    Requires: jina-embeddings-v2/v3 or similar long-ctx model
```

---

## 15. Reranker Taxonomy and Performance Comparison

### 15.1 Reranker Types

| Type | Mechanism | Latency | Accuracy | Example Models |
|------|-----------|---------|----------|---------------|
| Cross-encoder | Full attention over (query, doc) pair | High (150-400ms) | Highest | MonoT5, ms-marco-MiniLM, BGE-Reranker |
| Bi-encoder reranker | Dot-product over pre-encoded vecs | Low (5-20ms) | Medium | ColBERT-v2 |
| LLM-based reranker | LLM generates relevance score | Very High (500ms+) | Very High | RankLLM, Cohere Rerank |
| Lightweight reranker | Distilled cross-encoder | Low (10-30ms) | Medium-High | FlashRank (MiniLM-L-12-v2) |
| API reranker | Managed cloud endpoint | Medium (100-300ms) | High | Cohere Rerank, Voyage Rerank |

Sources: [Analytics Vidhya -- Top 7 Rerankers for RAG](https://www.analyticsvidhya.com/blog/2025/06/top-rerankers-for-rag/) | [Medium -- Reranking in RAG 2026](https://medium.com/@vaibhav-p-dixit/reranking-in-rag-cross-encoders-cohere-rerank-flashrank-c7d40c685f6a)

### 15.2 BEIR Benchmark Performance (2025)

Source: [arXiv -- How Good are LLM-based Rerankers](https://arxiv.org/html/2508.16757v1) | [Oreate AI -- Best Reranker Models 2025](https://www.oreateai.com/blog/beyond-keywords-unpacking-the-best-reranker-models-for-smarter-ai-search-in-2025/18feff9cf157109e65e799c8a60291b5)

| Model | NDCG@10 (BEIR avg) | Latency | Open Source |
|-------|-------------------|---------|-------------|
| MonoT5-3B-10k | 60.75 | 400ms | YES |
| Twolar-xl | 60.03 | 350ms | YES |
| mxbai-rerank-large | 57.49 | 200ms | YES |
| Cohere Rerank v3 | 57.2 | 150ms | NO |
| mxbai-rerank-base | 55.57 | 80ms | YES |
| FlashRank MiniLM-L-12-v2 | 55.43 | 15ms | YES |
| ColBERT-v2 | 54.20 | 20ms | YES |
| Voyage Rerank | 54.0 | 120ms | NO |
| BGE-Reranker-large | 53.5 | 180ms | YES |
| No reranker (BM25 baseline) | 47.3 | 0ms | -- |

### 15.3 Reranker Selection Matrix

| Constraint | Recommended | Why |
|-----------|-------------|-----|
| Real-time (<30ms) | FlashRank or ColBERT-v2 | Fastest open-source options |
| Maximum accuracy | MonoT5-3B or Cohere Rerank | Top BEIR scores |
| Zero infrastructure | Cohere Rerank API or Voyage | One API call, no hosting |
| On-premise high accuracy | mxbai-rerank-large | Best open-source BEIR score |
| Multilingual | Cohere Rerank v3 | Native multilingual support |
| Code retrieval | BGE-Reranker + fine-tune | Domain-specific training |

### 15.4 Reranker CEX Integration

```yaml
retriever_config:
  initial_retrieval:
    method: hybrid        # dense + sparse fusion
    top_k: 50             # retrieve more, rerank down
  reranker:
    type: cross_encoder   # or: llm_based, lightweight, api
    model: mxbai-rerank-large
    top_k_after_rerank: 5
    score_threshold: 0.4  # discard low-confidence results
    budget_ms: 200        # latency cap per request
```

---

## 16. RAG Architecture Decision Tree

```
START: What is your primary use case?
|
+-- [A] Factoid QA (single-doc, specific facts)
|       --> Naive RAG (dense retrieval + 512-token chunks)
|       --> Reranker: FlashRank (low latency)
|       --> Embedding: BGE or E5
|
+-- [B] Multi-document synthesis (themes, summaries)
|       --> GraphRAG or LazyGraphRAG
|       --> Reranker: MonoT5 or Cohere (accuracy priority)
|
+-- [C] Complex multi-step research (reason + retrieve)
|       --> Agentic RAG (reflexion or multi-agent)
|       --> Reranker: LLM-based (RankLLM)
|       --> Memory: entity_memory + memory_summary kinds
|
+-- [D] Real-time chat (< 500ms SLA)
|       --> Naive RAG + FlashRank reranker
|       --> Chunking: 256-512 fixed tokens
|       --> Pre-warmed vector index (HNSW)
|
+-- [E] High-accuracy (compliance, medical, legal)
        --> Agentic RAG with reflexion pattern
        --> Reranker: MonoT5-3B or Cohere Rerank
        --> Chunking: late chunking (Jina, +24% recall)
        --> Guardrail: citation enforcement (every claim sourced)

SECONDARY: What is your chunk size constraint?
|
+-- Document fits in 8192 tokens AND Jina model available
|       --> Use late chunking (best recall, context-preserving)
+-- Mixed document types (PDFs, tables, HTML)
|       --> Agentic re-chunking (LLM identifies boundaries)
+-- Cost-first, any document type
        --> Recursive splitting 512 tokens (69% accuracy, zero model calls)

SECONDARY: What is your latency budget?
|
+-- <30ms reranking budget    --> FlashRank or ColBERT-v2
+-- <200ms reranking budget   --> mxbai-rerank-large or Cohere Nimble
+-- No latency constraint     --> MonoT5-3B-10k (highest NDCG)
```

### 16.1 CEX Kind Mapping for Full RAG Stack

| Component | CEX Kind | Config Key |
|-----------|---------|------------|
| Chunking strategy | `chunk_strategy` | method, size, overlap |
| Embedding model | `embedding_config` | model, dimensions, normalize |
| Vector index | `knowledge_index` | store_type, index_algo |
| Sparse retrieval | `knowledge_index` | sparse_backend, bm25_k1 |
| Hybrid fusion | `retriever_config` | hybrid: true, fusion_method |
| Reranker | `retriever_config` | reranker.type, reranker.model |
| Data sources | `rag_source` | type, endpoint, auth |
| Evaluation | `scoring_rubric` | metrics, thresholds |
| Agentic loop | `workflow` | steps, reflection_gate |
| Graph index | `knowledge_index` | store_type: graph, graph_endpoint |
| Memory | `entity_memory` + `memory_summary` | ttl, scope, decay |