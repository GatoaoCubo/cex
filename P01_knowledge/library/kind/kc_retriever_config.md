---
id: p01_kc_retriever_config
kind: knowledge_card
type: kind
pillar: P01
title: "Retriever Config — Deep Knowledge for retriever_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: retriever_config
quality: null
tags: [retriever_config, p01, CONSTRAIN, kind-kc]
tldr: "Search-time parameters governing how chunks are retrieved — top_k, search type, reranking, and hybrid weights"
when_to_use: "Building, reviewing, or reasoning about retriever_config artifacts"
keywords: [retrieval, top-k, hybrid-search, reranker, bm25]
feeds_kinds: [retriever_config]
density_score: null
---

# Retriever Config

## Spec
```yaml
kind: retriever_config
pillar: P01
llm_function: CONSTRAIN
max_bytes: 2048
naming: p01_retr_cfg.md
core: true
```

## What It Is
A retriever_config defines how the system searches for relevant chunks at query time. It controls top_k, search type (vector/keyword/hybrid), reranking strategy, and filtering rules. It is NOT an embedding_config (which defines the vector model used to encode) nor a chunk_strategy (which defines how documents are split). Retriever config operates at search time; the others operate at index time.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BaseRetriever` / `VectorStoreRetriever` | `search_type`, `search_kwargs` (k, score_threshold, filter) |
| LlamaIndex | `RetrieverQueryEngine` / `VectorIndexRetriever` | `similarity_top_k`, `node_postprocessors` for reranking |
| CrewAI | RAG tool configuration | `n_results`, search params in tool setup |
| DSPy | `dspy.Retrieve(k=...)` | Declarative; optimizer can tune k |
| Haystack | `InMemoryBM25Retriever` / `EmbeddingRetriever` | Pipeline nodes with `top_k` parameter |
| OpenAI | Assistants `file_search` tool | `max_num_results` (default 20), `ranking_options` with `ranker` and `score_threshold` |
| Anthropic | No native retrieval | External retriever feeds context window |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| top_k | int | 5 | Higher = more recall but more noise and tokens |
| search_type | enum | similarity | Hybrid (vector+BM25) = best recall; vector = fastest |
| reranker | string | none | Reranking boosts precision 10-30% but adds latency |
| score_threshold | float | 0.0 | Higher = fewer but more relevant results |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Hybrid search | Best general-purpose retrieval | BM25 (0.3 weight) + vector (0.7 weight), top_k=10 |
| Two-stage retrieval | Large corpus, precision critical | Retrieve top_k=50, rerank to top_k=5 with Cohere reranker |
| Filtered retrieval | Multi-tenant or multi-domain | Filter by domain metadata before vector search |
| MMR (Maximal Marginal Relevance) | Diverse results needed | Reduces redundancy in retrieved chunks |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| top_k=1 | Single point of failure; misses context | Use top_k >= 3 for robustness |
| No reranking on large k | Noise overwhelms the generator | Add reranker when top_k > 10 |
| Vector-only on keyword-heavy queries | Misses exact matches (product codes, IDs) | Use hybrid search with BM25 component |

## Integration Graph
```
[embedding_config] --> [retriever_config] --> [template (P03)]
                            |
                     [chunk_strategy, brain_index (P10)]
```

## Decision Tree
- IF small corpus (<1000 chunks) THEN vector search, top_k=5, no reranker
- IF large corpus with exact-match queries THEN hybrid search (BM25+vector)
- IF precision critical (legal, medical) THEN two-stage with reranker
- IF results feel repetitive THEN enable MMR with lambda_mult=0.7
- DEFAULT: hybrid search, top_k=5, score_threshold=0.3

## Quality Criteria
- GOOD: top_k and search_type specified; tested on representative queries
- GREAT: Hybrid weights tuned on eval set; reranker benchmarked; score_threshold justified
- FAIL: top_k chosen arbitrarily; no search_type specified; vector-only on keyword-heavy domain
