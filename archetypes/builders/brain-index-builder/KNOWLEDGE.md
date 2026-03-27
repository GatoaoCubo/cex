---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for brain_index production
sources: [BM25 Theory, FAISS, Hybrid Search, CEX Brain Architecture]
---

# Domain Knowledge: brain_index

## Foundational Concepts
Brain indexes make knowledge FINDABLE through search algorithms.
BM25: term-frequency scoring with document length normalization (keyword search).
FAISS: approximate nearest neighbor search over dense vectors (semantic search).
Hybrid: combines BM25 (precision) with FAISS (recall) using weighted fusion.
In CEX: declarative index configurations for the Brain MCP retrieval system.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| BM25 (Okapi) | Term frequency, inverse doc frequency, length norm | BM25 Parameters section |
| FAISS (Meta) | Vector indexing, approximate NN search | FAISS Parameters section |
| Reciprocal Rank Fusion | Merging ranked lists from multiple sources | Hybrid Weights section |
| Elasticsearch | Full-text search with filters and boosts | Filters + Ranking sections |
| Vespa | Hybrid search with configurable ranking | Algorithm Config section |

## Key Principles
- BM25 excels at exact keyword matching (high precision)
- FAISS excels at semantic similarity (high recall)
- Hybrid combines both for best F1 score
- k1 controls term frequency saturation (1.2-2.0 typical)
- b controls document length normalization (0.75 standard)
- nprobe controls FAISS search breadth (more = slower + more accurate)
- Rebuild schedule must balance freshness vs compute cost
- Monitoring latency and zero-result rate catches degradation early

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| rebuild_schedule | When to rebuild index | Elasticsearch refresh interval |
| freshness_max_days | Max acceptable staleness | TTL / cache expiry |
| corpus_type | Content type indexed | Elasticsearch mapping type |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| embedding_config (P01) | Defines EMBEDDING MODEL (dimensions, provider) | Does NOT configure search |
| rag_source (P01) | Defines DATA SOURCE (URL, crawl config) | Does NOT define index structure |
| knowledge_card (P01) | The CONTENT being indexed | Does NOT configure retrieval |
| runtime_state (P10) | Agent DECISION state | Does NOT manage search infrastructure |
