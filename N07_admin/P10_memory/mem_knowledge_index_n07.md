---
id: p10_bi_n07_orchestration
kind: knowledge_index
pillar: P10
nucleus: N07
title: "Brain Index: N07 Orchestration"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "knowledge-index-builder"
scope: "N07 orchestration knowledge: 257-kind taxonomy, KC library, handoff archive, signal archive, decision manifests, mission plans, nucleus capability registry"
algorithm: "hybrid"
corpus_type: "text"
domain: "orchestration intent resolution"
quality: 8.4
tags: [knowledge-index, n07, orchestration, hybrid-search, intent-resolution, bm25, faiss]
tldr: "Hybrid BM25+FAISS index over N07 orchestration corpus enabling instant intent resolution: vague user input -> {kind, pillar, nucleus} tuple"
rebuild_schedule: "on_change"
freshness_max_days: 1
embedding_model: "nomic-embed-text"
density_score: 0.88
corpus_size_estimate: "~3500 documents, ~15MB text (257 kinds + 424 KCs + handoffs + signals + manifests)"
linked_artifacts:
  primary: "p01_ec_nomic_embed"
  related: [p03_pc_cex_universal, p10_bi_knowledge_pool]
---
<!-- 8F TRACE
F1 CONSTRAIN: kind=knowledge_index, pillar=P10, max_bytes=3072, naming=p10_bi_{index}.md
F2 BECOME: knowledge-index-builder (13 ISOs). Identity: search index architect for BM25/FAISS hybrid
F3 INJECT: schema + template + examples + memory loaded. N07 domain: orchestration taxonomy.
     Query profile: 65% exact-match (kind names, pillar IDs, nucleus IDs) + 35% paraphrase (intent phrases).
     Memory lesson: exact-match-heavy -> BM25=0.60, FAISS=0.40 (memory bld_memory_knowledge_index.md).
F4 REASON: 6 sections. on_change rebuild (orchestration corpus updates on every artifact save).
     Sloth lens: index once, retrieve in <50ms, never scan raw files at query time.
F5 CALL: tools ready. golden example match ~90%.
F6 PRODUCE: 108 lines, 6 required sections, dual-algorithm config.
F7 GOVERN: quality=null, id=p10_bi_n07_orchestration, kind=knowledge_index, algorithm=hybrid,
     scope has include paths, rebuild_schedule=on_change. All HARD gates pass.
F8 COLLABORATE: written to N07_admin/P10_memory/mem_knowledge_index_n07.md + compile
-->

## Scope

The N07 orchestration index covers all knowledge required for intent resolution:
mapping vague user input to the canonical `{kind, pillar, nucleus, verb}` tuple.

**Included document sources:**

| Source | Path | Document count | Update frequency |
|--------|------|----------------|-----------------|
| Kind taxonomy | `.cex/kinds_meta.json` | 257 entries | On kind addition |
| KC library | `N00_genesis/P01_knowledge/library/kind/kc_*.md` | 424 files | On KC update |
| Prompt compiler | `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md` | 1 file (257 patterns) | On kind addition |
| Handoff archive | `.cex/runtime/handoffs/*.md` | Variable (~50-200) | Per dispatch |
| Signal archive | `.cex/runtime/signals/*.json` | Variable | Per nucleus completion |
| Decision manifests | `.cex/runtime/decisions/*.yaml` | Variable | Per GDP session |
| Mission plans | `.cex/runtime/plans/*.md` | Variable | Per mission |
| Nucleus definitions | `N0[0-7]_*/P08_architecture/nucleus_def_*.md` | 8 files | Rare |
| Builder manifests | `archetypes/builders/*/bld_manifest_*.md` | 257 files | On builder update |

**Excluded:** binary files, `.cex/index/` (index storage itself), `.git/`, compiled `.yaml` outputs,
test fixtures, brand config secrets.

**Index path:** `.cex/index/n07/` (BM25 pickle at `bm25.pkl` + FAISS binary at `faiss.index`)

## Algorithm Config

N07 query profile: 65% exact-match (kind names, pillar codes, nucleus IDs, CLI flags) +
35% paraphrase (intent phrases in PT/EN). Memory-derived optimal split: BM25=0.60, FAISS=0.40.

### BM25 Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| k1 | 1.5 | Raised saturation for short documents (KC entries avg ~400 tokens) |
| b | 0.65 | Reduced length norm: short and long docs equally valid |
| tokenizer | whitespace + lowercase + underscore-split | Split `kind_name` tokens: `kind`, `name` both indexed |
| field_weights | kind_name:3.0, nucleus:2.0, pillar:2.0, title:1.5, body:1.0 | Taxonomy fields outrank prose |

### FAISS Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| index_type | HNSW32 | No IVF training needed; corpus < 10K docs; HNSW gives <10ms at 99% recall |
| ef_search | 64 | Search breadth: 64 neighbors explored per query node |
| metric | cosine | Normalized similarity; embedding magnitudes vary by doc length |
| dimensions | 768 | nomic-embed-text output |

### Hybrid Fusion (RRF)

| Component | Weight | Rationale |
|-----------|--------|-----------|
| BM25 | 0.60 | Exact-match dominant for kind/pillar/nucleus lookups |
| FAISS | 0.40 | Semantic coverage for PT/EN paraphrase intent phrases |
| Fusion strategy | RRF (k=60) | Reciprocal Rank Fusion; robust to score distribution differences |

## Filters

| Filter | Type | Condition | Applied |
|--------|------|-----------|---------|
| Quality floor | pre-search | quality >= 7.0 OR quality IS NULL | Always |
| Freshness cap | pre-search | updated within freshness_max_days=1 day | On stale index alert |
| Nucleus scope | pre-search | nucleus IN query_nucleus when specified | When nucleus filter active |
| Pillar scope | pre-search | pillar IN query_pillar when specified | When pillar filter active |
| Deduplication | post-search | Remove near-duplicates (cosine > 0.96) | Always |
| Kind boundary | post-search | Return kind+pillar+nucleus fields always | Always |

## Ranking

| Factor | Weight | Description |
|--------|--------|-------------|
| Hybrid score (RRF) | 0.65 | Combined BM25 + FAISS reciprocal rank fusion |
| Kind taxonomy match | 0.15 | Exact kind_name match in kinds_meta.json -> hard boost |
| Freshness | 0.10 | Handoffs/signals/manifests: recency matters; KCs: neutral |
| Authority | 0.10 | Pillar schema + KC library rank above handoff/signal docs |

**Tie-breaking:** pillar number ascending (P01 > P12 when equal score).

**Score output format:** `{score: float, kind: str, pillar: str, nucleus: str, path: str}`
This tuple is the canonical F1 CONSTRAIN output fed directly into 8F dispatch.

## Rebuild

**Rebuild command:** `python _tools/cex_index.py --nucleus n07`

| Trigger | Schedule | Estimated duration | Service impact |
|---------|-----------|--------------------|---------------|
| New artifact saved (F8 COLLABORATE) | Immediate incremental | < 5 sec | Zero (hot swap) |
| New handoff written | Immediate incremental | < 2 sec | Zero (hot swap) |
| New signal received | Immediate incremental | < 1 sec | Zero (hot swap) |
| Full rebuild (manual) | On demand | < 90 sec | Zero (read-only during rebuild) |
| Nightly integrity check | 02:00 local | < 90 sec | Zero |

**Incremental strategy:** hash each document path; rebuild only changed/new documents.
Full rebuild triggered when > 10% of corpus has changed since last full rebuild.

**Sloth lens applied:** index everything once on change; all subsequent queries read from
`.cex/index/n07/` -- zero file scanning at query time. The orchestrator never re-reads
`kinds_meta.json` on each intent resolution call; the index answer arrives in < 50ms.

## Monitoring

| Metric | Threshold | Alert action |
|--------|-----------|--------------|
| Query latency p95 | > 200ms | Log warning; check HNSW ef_search setting |
| Index staleness | > freshness_max_days (1 day) | Trigger full rebuild automatically |
| Zero-result rate | > 5% of queries | Review corpus coverage; re-check tokenizer |
| Recall@5 on golden queries | < 0.75 | Reweight BM25/FAISS split; rebuild HNSW |
| BM25 corpus size drift | > 10% change | Trigger full rebuild |
| FAISS index dimension mismatch | Any | HALT -- embedding model changed; full rebuild required |

**Golden query set:** 20 canonical intent phrases (10 EN + 10 PT) covering all 12 pillars.
Stored at `.cex/index/n07/golden_queries.json`. Run after every full rebuild.

## Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_index` |
| Pillar | P10 |
| Nucleus | N07 |
| Domain | orchestration intent resolution |
| Pipeline | 8F (F1-F8) |
| Algorithm | hybrid (BM25 k1=1.5 + HNSW32 + RRF k=60) |
| Corpus | ~3500 documents, ~15MB |
| Index path | `.cex/index/n07/` |
| Rebuild command | `python _tools/cex_index.py --nucleus n07` |
| Rebuild schedule | on_change (incremental) + nightly full |
| Query output | `{score, kind, pillar, nucleus, path}` |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
