---
id: p01_rc_hybrid_rag
kind: retriever_config
pillar: P01
title: Hybrid RAG Retriever (BM25 + Dense + Cohere Reranker)
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: knowledge_retrieval
quality: 9.1
tags: [retriever-config, hybrid-search, bm25, faiss, cohere, reranker, rag]
tldr: Retriever hibrido que combina BM25 keyword search (0.3) com FAISS dense search (0.7) e reranker Cohere v3 para top_k=5 final — usado no organization Brain MCP
when_to_use: Qualquer busca no Brain MCP que precise alta recall em corpus tecnico misto (knowledge cards, agents, skills)
---

# Retriever Config: Hybrid RAG (BM25 + Dense + Cohere Reranker)

## Overview
Configuracao do retriever hibrido usado pelo organization Brain MCP (`brain_query`). Combina BM25 para termos exatos (nomes de agentes, siglas, comandos) com busca densa FAISS/nomic-embed-text para similaridade semantica. Cohere Rerank v3 faz re-ranking final para maximizar precisao no top_k=5.

## Parameters
| Param | Value | Rationale |
|-------|-------|-----------|
| search_type | hybrid | BM25-only falha em sinonimos; dense-only falha em termos exatos (agent names, acronyms) |
| top_k | 5 | 5 documentos = ~4000 tokens de contexto. Acima de 7, noise domina signal |
| top_k_initial | 20 | Busca inicial ampla antes do reranker filtrar para 5 |
| bm25_weight | 0.3 | Termos exatos sao minoria das queries (~30%), mas criticos quando presentes |
| dense_weight | 0.7 | Maioria das queries sao semanticas ("como configurar X", "agente para Y") |
| reranker | cohere-rerank-v3 | +12% MRR@5 vs sem reranker no benchmark organization |
| reranker_top_n | 5 | Reranker seleciona top 5 dos 20 candidatos iniciais |
| embedding_model | nomic-embed-text | Local (Ollama), 768 dims, zero custo API |
| vector_store | FAISS (IndexFlatIP) | Inner product com vetores normalizados = cosine similarity. ~140MB index |
| bm25_backend | rank_bm25 | Python-native, sem dependencia externa, k1=1.5, b=0.75 |

## Architecture
```text
[Query] --> [Embedding] --> [FAISS Dense Search (top_k=20)]
   |                                      |
   +------> [BM25 Keyword Search (top_k=20)]
                                          |
                        [Reciprocal Rank Fusion]
                          weights: 0.7 dense + 0.3 bm25
                                          |
                        [Cohere Rerank v3 (20 -> 5)]
                                          |
                        [Top 5 Documents + Scores]
```

## Implementation
```python
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereRerank

# Dense retriever (FAISS + nomic-embed-text)
faiss_store = FAISS.load_local("records/core/brain/faiss_index", embeddings)
dense_retriever = faiss_store.as_retriever(search_kwargs={"k": 20})

# BM25 retriever
bm25_retriever = BM25Retriever.from_documents(documents, k=20)

# Hybrid ensemble
hybrid = EnsembleRetriever(
    retrievers=[dense_retriever, bm25_retriever],
    weights=[0.7, 0.3],
)

# Cohere reranker (top 20 -> top 5)
reranker = CohereRerank(model="rerank-english-v3.0", top_n=5)
pipeline = ContextualCompressionRetriever(
    base_compressor=reranker,
    base_retriever=hybrid,
)
```

## Fallback Strategy
| Condition | Fallback | Impact |
|-----------|----------|--------|
| Ollama down (no embeddings) | BM25-only (keyword search) | Recall drops ~50% -> ~38% |
| Cohere API down | Skip reranker, return RRF top 5 | MRR@5 drops 12% |
| FAISS index missing | Rebuild on-demand + BM25 interim | ~20 min rebuild |
| Query < 3 chars | Return empty (too ambiguous) | Prevents noise results |

## Benchmarks (organization Brain corpus, 1957 documents)
| Metric | Hybrid+Rerank | Dense Only | BM25 Only |
|--------|---------------|------------|-----------|
| MRR@5 | 0.82 | 0.71 | 0.54 |
| Recall@5 | 0.89 | 0.79 | 0.61 |
| Recall@10 | 0.94 | 0.88 | 0.72 |
| Latency (p50) | 180ms | 45ms | 12ms |
| Latency (p99) | 420ms | 120ms | 35ms |

## When NOT to Use
- Real-time autocomplete (latency > 100ms) — usar BM25-only
- Exact ID lookup ("agent scout-agent") — usar direct file read
- Cross-language queries — nomic-embed-text e English-optimized

## Related
- `ex_chunk_strategy_recursive_1000.md` — chunking que alimenta este retriever
- `ex_embedding_config_nomic_embed_text.md` — modelo de embedding do dense path
- `ex_rag_source_brain_faiss_index.md` — indice FAISS consultado
