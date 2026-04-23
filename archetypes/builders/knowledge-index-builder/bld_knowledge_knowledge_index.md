---
kind: knowledge_card
id: bld_knowledge_card_knowledge_index
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for knowledge_index production — semantic search index configuration
sources: FAISS (Meta), BM25/Okapi (Robertson), Elasticsearch, Vespa hybrid search
quality: 9.1
title: "Knowledge Card Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - knowledge-index-builder
  - p01_kc_knowledge_index
  - bld_examples_knowledge_index
  - p03_sp_knowledge_index_builder
  - p04_plug_brain_search
  - bld_collaboration_knowledge_index
  - p10_bi_intelligence_outputs
  - p10_bi_organization_brain
  - p10_lr_knowledge-index-builder
  - bld_examples_component_map
---

# Domain Knowledge: knowledge_index
## Executive Summary
Brain indexes configure search retrieval by combining BM25 (keyword scoring), FAISS (vector similarity), and hybrid ranking. They define what content to index, how to rank results, and when to rebuild. Brain indexes differ from embedding configs (model selection), knowledge cards (content being indexed), and RAG sources (external data pipes).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory/runtime) |
| Algorithms | BM25 (keyword), FAISS (vector), hybrid (weighted merge) |
| BM25 params | k1=1.2-2.0 (term freq saturation), b=0.75 (length norm) |
| FAISS params | nprobe (search breadth), nlist (cluster count) |
| Hybrid formula | score = alpha * BM25 + (1-alpha) * cosine_similarity |
| Rebuild trigger | time-based (>24h) or content-change-based |
| Accuracy | ~88% hybrid, ~50% BM25-only fallback |
## Patterns
- **Hybrid search**: combine BM25 precision (exact keywords) with FAISS recall (semantic similarity) — neither alone is sufficient
- **Alpha tuning**: alpha=0.4 (favor semantic) for exploratory queries; alpha=0.7 (favor keyword) for exact-term lookups
- **Scope boundaries**: index only specified directories and file types — indexing everything creates noise and degrades search
- **Freshness policies**: rebuild schedule (daily) + staleness threshold (24h) — stale indexes return outdated results
- **Fallback chain**: if embedding service is down, degrade to BM25-only rather than total search failure
- **Pre-filtering**: filter by pillar, kind, or tags before ranking — reduces search space, improves relevance and speed
| Source | Concept | Application |
|--------|---------|-------------|
| BM25 (Okapi) | Term frequency + doc length normalization | Keyword precision scoring |
| FAISS (Meta) | Approximate nearest neighbor search | Semantic similarity retrieval |
| Reciprocal Rank Fusion | Merging ranked lists from multiple sources | Hybrid weight combining |
| Elasticsearch | Full-text search with filters and boosts | Filter + ranking configuration |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vector-only search | Misses exact keyword matches; "BM25" query misses "BM25" |
| BM25-only search | Misses semantic similarity; "search engine" misses "retrieval system" |
| No rebuild schedule | Index drifts from content; new files invisible to search |
| Index everything | Noise drowns signal; large indexes are slow |
| Fixed alpha for all queries | Exploratory vs exact queries need different weights |
| No fallback when embedding down | Total failure instead of degraded results |
## Application
1. Define scope: directories, file types, pillars to index
2. Select algorithm: BM25, FAISS, or hybrid for the use case
3. Configure parameters: k1, b for BM25; nprobe, nlist for FAISS; alpha for hybrid
4. Set rebuild: cron schedule, staleness threshold, manual trigger
5. Define fallback: BM25-only when embedding service unavailable
6. Monitor: track latency, zero-result rate, and index freshness
## References
- FAISS: Facebook AI Similarity Search documentation
- Robertson et al.: BM25/Okapi probabilistic information retrieval
- Elasticsearch: hybrid search and filter configuration
- Vespa: configurable hybrid ranking and indexing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-index-builder]] | downstream | 0.59 |
| [[p01_kc_knowledge_index]] | sibling | 0.52 |
| [[bld_examples_knowledge_index]] | downstream | 0.51 |
| [[p03_sp_knowledge_index_builder]] | downstream | 0.51 |
| [[p04_plug_brain_search]] | downstream | 0.48 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.46 |
| [[p10_bi_intelligence_outputs]] | downstream | 0.45 |
| [[p10_bi_organization_brain]] | downstream | 0.45 |
| [[p10_lr_knowledge-index-builder]] | downstream | 0.41 |
| [[bld_examples_component_map]] | related | 0.39 |
