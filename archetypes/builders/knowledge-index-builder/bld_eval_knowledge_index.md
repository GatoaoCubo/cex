---
kind: quality_gate
id: p11_qg_knowledge_index
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_index artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: knowledge_index"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, knowledge-index, P11, P10, governance, search, retrieval, hybrid-search]
tldr: "Gates for knowledge_index artifacts — search index configs combining BM25, FAISS, or hybrid retrieval."
domain: knowledge_index
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.87
related:
  - bld_examples_knowledge_index
  - p03_sp_knowledge_index_builder
  - knowledge-index-builder
  - bld_instruction_knowledge_index
  - bld_collaboration_knowledge_index
  - bld_output_template_knowledge_index
  - bld_schema_knowledge_index
  - bld_architecture_knowledge_index
  - p11_qg_builder
  - p01_kc_knowledge_index
---

## Quality Gate

# Gate: knowledge_index
## Definition
| Field     | Value                                                  |
|-----------|--------------------------------------------------------|
| metric    | algorithm completeness + freshness policy coverage     |
| threshold | 8.0                                                    |
| operator  | >=                                                     |
| scope     | all knowledge_index artifacts (P10)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = index unreachable at query time |
| H02 | id matches `^p10_bi_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "knowledge_index" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, algorithm, scope, corpus_type, rebuild_schedule, freshness_max_days, quality, tags, tldr | Completeness |
| H07 | algorithm in [bm25, faiss, hybrid] | Only supported retrieval algorithms |
| H08 | corpus_type in [text, vector, structured] | Valid corpus classification |
| H09 | rebuild_schedule in [on_change, hourly, daily, weekly, manual] | Valid schedule value |
| H10 | freshness_max_days is non-negative integer | Freshness policy must be numeric |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "knowledge-index" | 0.5 |
| S03 | Algorithm Config section has parameters specific to chosen algorithm | 1.0 |
| S04 | Filters section has >= 2 entries with type and condition | 1.0 |
| S05 | Ranking section has >= 2 factors with explicit weights | 1.0 |
| S06 | Rebuild section specifies both schedule and trigger event | 1.0 |
| S07 | Monitoring section has >= 2 metrics with alert thresholds | 0.5 |
| S08 | scope boundary is specific (names included/excluded paths) | 1.0 |
| S09 | density_score >= 0.80 | 1.0 |
| S10 | No generic retrieval advice (content must be config, not tutorial) | 1.0 |
Weights sum: 9.0. Normalize: divide each by 9.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference search index configuration |
| >= 8.0 | PUBLISH — active retrieval index |
| >= 7.0 | REVIEW — complete ranking weights or monitoring thresholds |
| < 7.0  | REJECT — algorithm config missing or scope undefined |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical search gap requiring temporary index before full spec |
| approver | p10-chief |
| audit_trail | Log in records/audits/ with retrieval gap description and timestamp |
| expiry | 72h — full algorithm config required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

# Examples: knowledge-index-builder
## Golden Example
INPUT: "Create knowledge_index para search hibrida no pool de knowledge cards do CEX"
OUTPUT:
```yaml
id: p10_bi_knowledge_pool
kind: knowledge_index
pillar: P10
title: "Brain Index: Knowledge Pool"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
scope: "CEX knowledge card pool (P01, ~2000 cards)"
algorithm: "hybrid"
corpus_type: "text"
domain: "knowledge retrieval"
quality: null
tags: [knowledge-index, knowledge-pool, hybrid-search, bm25, faiss]
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
- kind: knowledge_index (H04 pass)
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
kind: knowledge_index
title: "Search"
quality: 9.0
algorithm: elasticsearch
## Config
- Use BM25 for search

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
