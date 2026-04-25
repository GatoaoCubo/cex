---
id: p01_kc_bm25_search
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "BM25 Search — Keyword Retrieval for Local Knowledge Bases"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [bm25, keyword-search, retrieval, offline-search, knowledge-base]
tldr: "BM25 keyword-based search in local CSVs/docs: ~10ms, offline, no embeddings — ideal for structured data"
when_to_use: "Implement fast search in local knowledge bases without dependency on embeddings or server"
keywords: [bm25, okapi-bm25, keyword-retrieval, text-search]
long_tails:
  - "How to implement BM25 search in Python for local knowledge base"
  - "When to use BM25 instead of embeddings for search"
axioms:
  - "ALWAYS cache fitted BM25 instance in production"
  - "NEVER use BM25 for semantic search — does not understand synonyms"
linked_artifacts:
  primary: null
  related: [p01_kc_csv_as_knowledge]
density_score: null
data_source: "https://en.wikipedia.org/wiki/Okapi_BM25"
related:
  - p01_kc_csv_as_knowledge
  - p01_rc_hybrid_rag
  - bld_knowledge_card_knowledge_index
  - p04_plug_brain_search
  - leverage_map_v2_n04_verify_legacy_2026_04_15
  - p10_bi_organization_brain
  - leverage_map_v2_n04_verify
  - p10_lr_knowledge-index-builder
  - p10_bi_intelligence_outputs
  - leverage_map_v2_verify_n04
---

## TL;DR

BM25 (Okapi Best Match 25) is a ranking algorithm based on term frequency that searches local documents without embeddings, without server, without GPU. Processes 161 rows in ~10ms and 1000 rows in ~50ms using only Python stdlib.

## Core Concept

BM25 calculates relevance using probabilistic TF-IDF: rare terms in a document that are rare in the corpus receive high scores. Two parameters control behavior: k1 (frequency saturation, typically 1.2-2.0) and b (length normalization, typically 0.75). The algorithm tokenizes queries and documents, builds an inverted index, and ranks by score.

BM25's strength is simplicity: no external dependencies, works offline, deterministic and interpretable results. The weakness is that it operates exclusively on keywords — "car" does not find "vehicle". For conceptual searches, embeddings are needed. BM25 is ideal as a first retrieval stage or as the only stage for structured data with well-defined keywords.

In hybrid systems (BM25 + embeddings), BM25 serves as fast recall and embeddings as semantic reranker. This combines speed with conceptual understanding.

## Architecture/Patterns

| Aspect | Value | Note |
|--------|-------|------|
| Complexity | O(n) per query | n = documents in corpus |
| Latency 161 docs | ~10ms | No cache, rebuild per query |
| Latency 1000 docs | ~50ms | No cache, rebuild per query |
| Dependencies | Zero | Python stdlib only |
| Parameter k1 | 1.2-2.0 | Frequency saturation |
| Parameter b | 0.75 | Length normalization |

Implementation pattern:

```python
from rank_bm25 import BM25Okapi

corpus = [doc.split() for doc in documents]
bm25 = BM25Okapi(corpus)  # fit once, query many
scores = bm25.get_scores(query.split())
top_n = sorted(range(len(scores)),
    key=lambda i: scores[i], reverse=True)[:5]
```

For production: instantiate BM25 once at startup and reuse. Rebuild only when corpus changes. Separate search_cols (indexed) from output_cols (returned) for precision.

Hybrid BM25 + embeddings (reranking pipeline):
```
Query -> BM25 recall (top 20, ~10ms)
  -> embedding rerank (top 5, ~200ms)
  -> LLM context injection
```

BM25 as first stage ensures speed. Embeddings as second stage add semantic understanding. Total cost: ~210ms vs ~500ms with pure embeddings. Fallback: if embedding service goes down, BM25 alone still works.

## Practical Examples

| Scenario | search_cols | Result |
|----------|------------|--------|
| Product by type | keywords, category | Top 3 matches with score |
| UX guideline | rule_name, description | Applicable rules |
| Font pairing | style, mood, use_case | Typographic pairs |
| Skill discovery | name, description | Relevant skills |

Typical flow:
1. Load CSV with pandas
2. Concatenate search_cols into single field
3. Tokenize and build BM25 index
4. Query returns top-N with score > threshold
5. Filter output_cols from results

Recommended threshold: discard results with score < 1.0 (too generic). Limit to 3-5 results for LLM context.

## Anti-Patterns

- Searching across too many verbose columns (degrades precision)
- Returning all results without score threshold
- Assuming BM25 understands synonyms or concepts
- Rebuilding index per query in production (cache it!)
- One giant multi-domain CSV instead of focused CSVs
- Using BM25 as the only search for open-ended questions

## References

- source: https://en.wikipedia.org/wiki/Okapi_BM25
- related: p01_kc_csv_as_knowledge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_csv_as_knowledge]] | sibling | 0.36 |
| [[p01_rc_hybrid_rag]] | related | 0.34 |
| [[bld_knowledge_card_knowledge_index]] | sibling | 0.34 |
| [[p04_plug_brain_search]] | downstream | 0.29 |
| [[leverage_map_v2_n04_verify_legacy_2026_04_15]] | related | 0.29 |
| [[p10_bi_organization_brain]] | downstream | 0.29 |
| [[leverage_map_v2_n04_verify]] | related | 0.26 |
| [[p10_lr_knowledge-index-builder]] | downstream | 0.25 |
| [[p10_bi_intelligence_outputs]] | downstream | 0.24 |
| [[leverage_map_v2_verify_n04]] | sibling | 0.24 |
