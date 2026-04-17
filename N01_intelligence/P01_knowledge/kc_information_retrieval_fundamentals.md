---
id: kc_information_retrieval_fundamentals
kind: knowledge_card
pillar: P01
nucleus: n01
title: "Information Retrieval Fundamentals for N01"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: information-retrieval
quality: 9.1
tags: [information_retrieval, BM25, dense_retrieval, NDCG, precision_recall, RAG, n01]
tldr: "Core IR concepts applied to N01 research: BM25 vs. dense retrieval, NDCG metric, precision/recall trade-off, hybrid search. Grounds the retriever_n01 and knowledge_index_n01 design decisions in IR fundamentals."
density_score: 0.90
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P01/knowledge_card F2 become=knowledge-card-builder F3 inject=retriever_n01+knowledge_index_n01+search_strategy_n01 F4 reason=N01 must understand WHY its retrieval architecture works in order to debug when it doesn't -- fundamentals ground the tools F5 call=cex_compile F6 produce=kc_information_retrieval_fundamentals.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P01_knowledge/ -->

## Core IR Concepts

### Retrieval Models

| Model | Algorithm | Strengths | Weaknesses | N01 Use |
|-------|-----------|-----------|-----------|---------|
| BM25 | probabilistic keyword | exact match, fast, no GPU | misses synonyms | L1 sparse retrieval |
| TF-IDF | term frequency weighting | interpretable | outdated vs BM25 | legacy, not primary |
| Dense (bi-encoder) | cosine similarity on embeddings | semantic matching | no exact match, GPU | L1 semantic retrieval |
| Cross-encoder | full attention over query+doc | best re-ranking | slow (O(n) per query) | top-10 re-ranking |
| Hybrid (BM25 + dense) | RRF fusion | best of both | complexity | primary for retriever_n01 |

### BM25 Formula

```
BM25(D, Q) = sum over qi in Q:
  IDF(qi) * (f(qi, D) * (k1 + 1)) / (f(qi, D) + k1 * (1 - b + b * |D| / avgdl))

where:
  k1 = 1.2 to 2.0 (term saturation)
  b = 0.75 (length normalization)
  f(qi, D) = frequency of term qi in document D
  avgdl = average document length in corpus
```

Key behavior: adding more occurrences of a term has diminishing returns (saturation via k1).

### Reciprocal Rank Fusion (RRF)

Combines BM25 and dense rankings:

```
RRF(d, rankings) = sum over r in rankings:
  1 / (k + rank(d, r))

k = 60 (typical)
```

Documents appearing high in multiple rankings get the highest fused score.

## Evaluation Metrics

| Metric | Formula | What It Measures | Target for N01 |
|--------|---------|-----------------|---------------|
| Precision@k | relevant_in_top_k / k | fraction of top-k that is relevant | > 0.70 at k=5 |
| Recall@k | relevant_in_top_k / total_relevant | fraction of all relevant in top-k | > 0.80 at k=10 |
| MRR | avg(1/rank_of_first_relevant) | how quickly first relevant result appears | > 0.75 |
| NDCG@k | normalized discounted cumulative gain | rank-weighted relevance | > 0.70 at k=10 |
| MAP | mean average precision over queries | overall precision quality | > 0.65 |

### NDCG Calculation

```
DCG@k = sum over i from 1 to k:
  relevance_i / log2(i + 1)

NDCG@k = DCG@k / IDCG@k  # IDCG = ideal DCG (perfect ranking)
```

NDCG penalizes relevant documents appearing lower in ranking -- perfect for N01 where first result is most used.

## Query Processing

| Stage | Operation | N01 Application |
|-------|-----------|----------------|
| Tokenization | split text into tokens | BM25 preprocessing |
| Stop-word removal | remove "the", "and", etc. | reduces noise |
| Stemming / lemmatization | "running" -> "run" | improves recall |
| Query expansion | add synonyms / related terms | increases recall |
| Query rewriting | rephrase for better retrieval | N01 Step 1 comparative variant |

### Query Expansion for Research

N01 generates 3 query variants (from reasoning_strategy_n01.md):
- Direct: literal query
- Comparative: adds competitor context
- Signal: indirect evidence query

This is manual query expansion -- effective for research where the exact vocabulary may not match source terms.

## Precision-Recall Trade-off

| Scenario | Prefer | Why |
|----------|--------|-----|
| Quality-critical research | precision | fewer false positives |
| Discovery / exploration | recall | don't miss relevant sources |
| N01 standard research | balanced (F1) | triangulation needs recall; synthesis needs precision |

N01 strategy: high recall at retrieval (top-20), high precision at synthesis (top-5 after re-ranking).

## Chunking Strategy Impact on IR

| Chunk Size | Retrieval Quality | Synthesis Quality | N01 Recommendation |
|------------|------------------|------------------|-------------------|
| Full document | low precision | full context | only for short docs (< 1000 words) |
| 512 tokens | high precision | loses context | primary for web content |
| Semantic (by heading/section) | high precision | preserves context | primary for papers/reports |
| Sentence-level | very high precision | poor synthesis | avoid |

N01 uses semantic chunking (heading-based) for structured documents, 512-token for web content.

## Comparison: IR Systems

| System | BM25 | Dense | Hybrid | Rerank | N01 Fit |
|--------|------|-------|--------|--------|---------|
| Elasticsearch | yes | plugin | plugin | no | heavy for local |
| Weaviate | plugin | yes | yes | yes | cloud dependency |
| This (local) | rank_bm25 | sentence-transformers | RRF | cross-encoder | optimal for N01 |
| Pinecone | no | yes | no | no | no sparse |
