---
id: kno_retriever_config_n03
kind: retriever_config
pillar: P01
nucleus: N03
title: "N03 Retriever Config"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering retrieval architecture
quality: null
tags: [retriever_config, p01, n03, hybrid_search, reranking, inventive_pride]
---
<!-- 8F: F1=retriever_config/P01 F2=retriever-config-builder F3=nucleus_def_n03+kc_retriever_config+P01_schema F4=hybrid retrieval tuned for builder precision
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:6085 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/P01_knowledge/kno_retriever_config_n03.md -->

# N03 Retriever Config

## Properties

| Property | Value |
|----------|-------|
| Kind | `retriever_config` |
| Pillar | `P01` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Store type | hybrid lexical plus vector |
| Default top_k | `10` |
| Candidate pool | `24` |
| Reranker | lightweight cross-encoder or rule rerank |
| Metadata filters | pillar, kind, nucleus, path_role |
| Query goal | return reusable construction context |

## Mission Fit

N03 retrieves for build execution, not for casual answer generation.
The configuration must surface the most reusable artifacts first.
Inventive Pride raises the bar:
retrieval should return the sharpest precedent, not the most generic similarity.

## Default Retrieval Path

1. Parse query for kind, pillar, and nucleus hints.
2. Apply metadata filters before expensive ranking when hints are available.
3. Run lexical retrieval and vector retrieval in parallel.
4. Fuse both result sets into a candidate pool of `24`.
5. Rerank down to `10`.
6. Promote exact-kind hits when confidence is high.
7. Prefer source markdown over compiled derivatives when both match.

## Search Profile

| Parameter | Value | Purpose |
|----------|-------|---------|
| search_type | `hybrid` | preserve exact terminology and semantic recall |
| top_k | `10` | enough breadth without overwhelming prompt budget |
| lexical_k | `12` | protect against schema and filename queries |
| vector_k | `12` | surface conceptual neighbors |
| candidate_pool | `24` | enough room for reranking to matter |
| min_score_gate | medium | drop obvious noise before assembly |
| reranker | enabled | sharpen final top set |

## Why Hybrid

Engineering retrieval is full of exact tokens:
- `quality_gate`
- `runtime_state`
- `chunk_strategy`
- `P01`
- `N03`
Pure dense retrieval blurs these edges.
Pure lexical retrieval misses semantic siblings.
Hybrid search is the proud compromise because it respects literal structure and conceptual intent.

## Query Interpretation Rules

- If query names a kind, boost exact `kind`.
- If query names a pillar, filter to that pillar first.
- If query names N03, boost local nucleus artifacts over global references.
- If query contains `builder`, favor manifests, architecture notes, and kind KCs.
- If query contains `memory`, include P10 but demote unrelated learning records.
- If query is procedural, boost sections tagged as `procedure` or `quality`.

## Reranking Policy

| Signal | Weight direction | Reason |
|-------|------------------|--------|
| exact kind match | strong positive | kind correctness dominates |
| same nucleus | positive | local operating context matters |
| markdown source | positive | human-authored source is richer |
| compiled duplicate | negative | avoid redundant payload |
| stale artifact | mild negative | recent rules are safer |
| low-density chunk | negative | weak chunks waste context |

## Prompt Assembly Rules

1. Never inject more than two near-duplicate artifacts.
2. Prefer one kind KC plus one local artifact over five semantically similar notes.
3. Preserve provenance for every retrieved chunk.
4. Keep builder instructions ahead of examples when both are present.
5. Reserve final slots for contrasting references, not repetitive confirmations.

## Failure Modes

| Failure | Symptom | Fix |
|--------|---------|-----|
| over-recall | too many broad neighbors | tighten metadata filters |
| lexical tunnel vision | exact name matches but poor substance | raise vector contribution |
| semantic drift | related but wrong kind | strengthen reranker exact-kind boost |
| prompt waste | redundant compiled files | dedupe by source path family |
| stale authority | outdated artifact dominates | add freshness prior |

## Runtime Targets

- median retrieval latency should stay operationally small
- candidate fusion should be deterministic enough for debugging
- reranking should be optional under degraded mode
- top-3 precision matters more than recall at 50
- returned context should fit build-phase prompt budgets cleanly

## Evaluation Queries

Use canonical checks such as:
- `N03 8F enforcement`
- `chunk strategy for engineering corpus`
- `knowledge index memory boundary`
- `runtime state versus mental model`
- `builder manifest retriever config`

The proud config is the one that returns the right family without apology.

## Degraded Mode

If vector search is unavailable:
- keep lexical retrieval active
- reduce `top_k` to `6`
- flag degraded mode in runtime state
- favor exact path and kind signals
If lexical index is unavailable:
- keep vector retrieval active
- require reranker or stricter metadata filtering

## Integration Contract

This config assumes:
- `1024`-dimension normalized embeddings
- header-aware chunking
- vector store metadata filters
- an optional reranker with low operational cost
- compiled artifacts indexed, but demoted behind source markdown

## Inventive Pride Standard

Retrieval is part of authorship.
If the retriever feeds weak precedent, the build begins compromised.
N03 therefore values precision, provenance, and reusable context over maximal search exhaust.
The config should make excellent context the default, not a lucky accident.

## Final Position

N03 should run a hybrid retriever with `top_k=10`, a `24`-item candidate pool, and reranking enabled.
That is the smallest serious configuration that protects build quality under real corpus noise.
