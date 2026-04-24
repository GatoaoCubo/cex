---
id: mem_knowledge_index_n03
kind: knowledge_index
8f: F3_inject
pillar: P10
nucleus: N03
title: "N03 Knowledge Index"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering operational memory
quality: 9.1
tags: [knowledge_index, p10, n03, bm25, faiss, hybrid, inventive_pride]
density_score: 0.99
related:
  - knowledge-index-builder
  - bld_collaboration_knowledge_index
  - p01_kc_knowledge_index
  - bld_knowledge_card_knowledge_index
  - bld_examples_knowledge_index
  - bld_instruction_knowledge_index
  - p03_sp_knowledge_index_builder
  - bld_collaboration_memory_scope
  - n04_knowledge_memory_index
  - p10_bi_bm25_knowledge
---
<!-- 8F: F1=knowledge_index/P10 F2=knowledge-index-builder F3=nucleus_def_n03+kc_knowledge_index+P10_schema F4=hybrid index memory tuned for builder corpus
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:5452 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/P10_memory/mem_knowledge_index_n03.md -->

# N03 Knowledge Index

## Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_index` |
| Pillar | `P10` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Index mode | hybrid BM25 plus vector |
| Sparse engine | BM25 |
| Dense engine | FAISS-compatible embeddings or pgvector-backed ANN |
| Default alpha | `0.62` dense weight |
| Rebuild trigger | content hash drift or model change |
| Scope rule | separate source, memory, and compiled strata |

## Purpose

This artifact defines how N03 remembers searchable knowledge at index level.
The index is not just a search utility.
It is the memory spine that decides which precedent becomes available during construction.
Inventive Pride means the index must reward exactness without becoming brittle.

## Index Topology

| Stratum | Contents | Reason |
|--------|----------|--------|
| source | authoring markdown | highest-quality retrieval target |
| memory | summaries and entity facts | cross-session recall |
| compiled | machine renderings | fallback and validation support |
| holdout | evaluation queries and gold pairs | measure drift |

## Default Scoring Blend

- BM25 contribution: `0.38`
- dense contribution: `0.62`
- rerank after fusion: yes
- exact kind boost: yes
- same nucleus boost: yes
- duplicate family penalty: yes

This blend acknowledges that N03 search is full of exact tokens but still benefits from semantic adjacency.

## Why Not Pure BM25

Pure lexical search fails when users ask by concept:
- `memory versus runtime`
- `builder identity`
- `construction laws`
- `retrieval dignity`
Those ideas often live across varied phrasing.

## Why Not Pure Dense

Pure dense search blurs exact CEX terms:
- `P01`
- `P10`
- `runtime_state`
- `knowledge_index`
- `chunk_strategy`
These are not optional details.
They are operational anchors.

## Corpus Admission Rules

1. Index source markdown first.
2. Admit memory artifacts with explicit pillar and kind metadata.
3. Admit compiled outputs only as shadow entries.
4. Exclude logs, archives, and low-signal generated noise by default.
5. Keep deleted-source tombstones until reindex completes.

## Freshness Policy

| Trigger | Action |
|--------|--------|
| content hash changed | incremental reindex |
| embedder changed | full dense rebuild |
| chunk strategy changed materially | rebuild affected collections |
| metadata schema changed | reindex with migration pass |
| evaluation precision drop | diagnose before further ingest |

## Inventive Pride Lens

A proud index is selective.
It does not swallow every file and then brag about coverage.
It curates a search surface that honors signal, provenance, and reuse.
N03 should be remembered through its best source artifacts, not through accidental noise.

## Ranking Priorities

| Priority | Ranking signal |
|---------|----------------|
| 1 | exact kind and nucleus alignment |
| 2 | source markdown over compiled derivative |
| 3 | freshness of updated artifact |
| 4 | density and section usefulness |
| 5 | semantic similarity among remaining candidates |

## Failure Modes

| Failure | Effect | Countermeasure |
|--------|--------|----------------|
| global undifferentiated index | precision collapse | stratify collections |
| no freshness tracking | stale context | hash and timestamp policies |
| duplicate source and compiled entries | prompt waste | family dedupe |
| over-indexing archives | ranking pollution | admission filter |
| alpha drift without evaluation | silent regressions | holdout benchmarks |

## Evaluation Set

Maintain a small stable query suite:
- `N03 compile step`
- `8F constrain versus govern`
- `runtime state memory boundary`
- `builder manifest identity`
- `vector store metadata filters`

Each query should have expected top references.
The index is trusted only if it repeatedly returns them.

## Operational Notes

- sparse index can refresh cheaply and frequently
- dense index should rebuild on planned cycles
- memory strata should tolerate higher freshness pressure
- holdout set must remain isolated from production ranking
- every document family needs stable IDs for dedupe and audit

## Integration Contract

This knowledge index assumes:
- header-aware chunking
- normalized dense embeddings
- metadata-rich vector store support
- hybrid retriever fusion
- runtime state capable of flagging degraded search mode

## Scale Philosophy

N03 should scale the index only when retrieval quality or latency demands it.
Premature complexity is not pride.
Pride is controlled performance with clear reasons.

## Final Position

N03 should maintain a stratified hybrid knowledge index with BM25 and dense retrieval, weighted slightly toward dense search but governed by exact metadata and evaluation checks.
That is how memory stays sharp as the corpus grows.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-index-builder]] | related | 0.43 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.38 |
| [[p01_kc_knowledge_index]] | related | 0.36 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.34 |
| [[bld_examples_knowledge_index]] | upstream | 0.31 |
| [[bld_instruction_knowledge_index]] | upstream | 0.30 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.30 |
| [[bld_collaboration_memory_scope]] | downstream | 0.30 |
| [[n04_knowledge_memory_index]] | related | 0.29 |
| [[p10_bi_bm25_knowledge]] | sibling | 0.29 |
