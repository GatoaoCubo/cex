---
kind: examples
id: bld_examples_brain_index
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of brain_index artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: brain-index-builder
## Golden Example
INPUT: "Cria brain_index para busca hibrida no pool de knowledge cards do CEX"
OUTPUT:
```yaml
id: p10_bi_knowledge_pool
kind: brain_index
pillar: P10
title: "Brain Index: Knowledge Pool"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
scope: "CEX knowledge card pool (P01 artifacts, ~2000 cards)"
algorithm: "hybrid"
corpus_type: "text"
domain: "knowledge retrieval"
quality: null
tags: [brain-index, knowledge-pool, hybrid-search, bm25, faiss]
tldr: "Hybrid BM25+FAISS index over ~2000 knowledge cards with daily rebuild and 7-day freshness"
rebuild_schedule: "daily"
freshness_max_days: 7
embedding_model: "nomic-embed-text"
density_score: 0.90
corpus_size_estimate: "~2000 cards, ~8MB text"
linked_artifacts:
  primary: "p01_ec_nomic_embed"
  related: [p01_rs_pool_crawler, p10_rs_researcher]
## Scope
Indexes all knowledge cards in the CEX pool for semantic and keyword
retrieval. Covers P01 through P12 artifacts with quality >= 7.0.
Excludes archived and rejected cards. Serves all agent queries.
## Algorithm Config
### BM25 Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| k1 | 1.2 | Standard saturation for mixed-length docs |
| b | 0.75 | Standard length normalization |
| tokenizer | whitespace + lowercase | Simple, fast tokenization |
### FAISS Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| index_type | IVF256,Flat | Inverted file with 256 centroids |
| nprobe | 16 | Search 16 of 256 clusters (6.25% scan) |
| metric | cosine | Normalized dot product similarity |
| dimensions | 768 | nomic-embed-text output dimensions |
### Hybrid Weights
| Component | Weight | Notes |
|-----------|--------|-------|
| BM25 | 0.40 | Keyword precision for exact matches |
| FAISS | 0.60 | Semantic recall for concept matching |
## Filters
| Filter | Type | Condition | Applied |
|--------|------|-----------|---------|
| Quality floor | pre-search | quality >= 7.0 | Always |
| Pillar scope | pre-search | pillar in query scope | When pillar specified |
| Freshness cap | post-search | updated within freshness_max_days | Always |
| Deduplication | post-search | Remove near-duplicate results (cosine > 0.95) | Always |
## Ranking
| Factor | Weight | Description |
|--------|--------|-------------|
| Hybrid score | 0.70 | Combined BM25 + FAISS score |
| Quality boost | 0.15 | Higher quality cards rank higher |
| Freshness boost | 0.10 | Recently updated cards get slight boost |
| Domain match | 0.05 | Cards in same domain as query rank higher |
## Rebuild
| Trigger | Schedule | Duration | Impact |
|---------|----------|----------|--------|
| Daily cron | 03:00 UTC daily | ~20 min | No downtime (hot swap) |
| Manual trigger | On demand | ~20 min | No downtime (hot swap) |
| Corpus change > 5% | On threshold | ~20 min | No downtime (hot swap) |
## Monitoring
| Metric | Threshold | Alert |
|--------|-----------|-------|
| Query latency p95 | > 500ms | Warn to operator |
| Index staleness | > freshness_max_days | Trigger rebuild |
| Zero-result rate | > 10% of queries | Review index coverage |
| Recall@10 | < 0.70 on golden queries | Index quality degraded |
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p10_bi_ pattern (H02 pass)
- kind: brain_index (H04 pass)
- 19 frontmatter fields present (H08 pass)
- algorithm: "hybrid" valid enum (H07 pass)
- corpus_type: "text" valid enum (H09 pass)
- rebuild_schedule: "daily" valid enum (H10 pass)
- BM25 + FAISS + Hybrid config all present (S03 pass)
- 4 filters with type and condition (S04 pass)
- 4 ranking factors with weights (S05 pass)
- 4 monitoring metrics with thresholds (S07 pass)
## Anti-Example
INPUT: "Set up search"
BAD OUTPUT:
```yaml
id: search_index
kind: brain_index
title: "Search"
quality: 9.0
algorithm: elasticsearch
## Config
- Use BM25 for search
