---
id: mem_knowledge_index_n05
kind: knowledge_index
pillar: P10
nucleus: N05
title: "N05 Operations Knowledge Index"
version: "1.0.0"
quality: null
tags: [n05, operations, knowledge_index, gating_wrath, bm25, pgvector, hybrid]
---
<!-- 8F: F1=knowledge_index/P10 F2=knowledge-index-builder F3=nucleus_def_n05+P10_schema+kc_knowledge_index+examples+N05 W1 contracts F4=hybrid index policy for ops corpus
     F5=shell+apply_patch+cex_compile F6=approx-7KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/memory/mem_knowledge_index_n05.md -->

# N05 Operations Knowledge Index

## Intent

This memory artifact defines how N05 indexes and refreshes its operational corpus across sparse and dense retrieval paths.

The index is a memory concern because it captures persistent search behavior, rebuild posture, freshness rules, and fallback routing across sessions.

## Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_index` |
| Pillar | `P10` |
| Nucleus | `N05` |
| Name | `n05_ops_hybrid_index` |
| Backend mode | `bm25 + pgvector` |
| Dense dimensions | `1536` |
| Hybrid alpha | `0.62 semantic / 0.38 lexical` |
| Rebuild threshold | `24h or source_hash drift` |
| Failure stance | `degrade_to_sparse_only_explicitly` |

## Corpus Scope

Indexed material:

- N05 knowledge artifacts
- N05 memory artifacts
- N05 schemas and config from Wave 1
- curated operational examples relevant to deploy, CI, tests, and rollback

Excluded by default:

- raw vendor docs with no local operational relevance
- generated compiled outputs as primary retrieval targets
- long transient logs after incident close unless converted into summaries

The index is for N05 judgment, not archival hoarding.

## Dense Branch

| Field | Value |
|-------|-------|
| vector backend | `pgvector` |
| embedder | `openai/text-embedding-3-small` |
| normalization | `required` |
| namespace split | `ops_runbook, ops_ci, ops_deploy, ops_schema, ops_memory` |
| ANN index | `hnsw` |
| freshness key | `source_hash` |

Dense retrieval is responsible for semantic matching across paraphrased symptoms and repeated patterns.

## Sparse Branch

| Field | Value |
|-------|-------|
| algorithm | `bm25` |
| token policy | `preserve code tokens and path segments` |
| boost fields | `title, tags, test_id, service, endpoint, env_key` |
| rebuild speed target | `< 2 minutes` |
| fallback role | `authoritative exact-match path when dense unavailable` |

Sparse search is critical for:

- exact test names
- filenames
- environment variables
- endpoint names
- commands
- release IDs

## Hybrid Policy

Fusion policy:

1. retrieve top candidates from both branches
2. fuse with reciprocal rank fusion
3. apply freshness decay
4. rerank toward evidence utility
5. emit only the strongest `6` results

N05 does not use a naive blended score because operational queries often have one exact needle and one semantic symptom. Rank fusion handles that mix more robustly.

## Freshness Rules

| Content class | Freshness posture |
|---------------|-------------------|
| schema/config | stable, low decay |
| runbook/checklist | stable, medium decay |
| deploy log | high decay |
| CI/test output | high decay |
| learning record | medium decay |
| memory summary | medium-high decay |

Freshness matters more in operations than in generic knowledge work. An old rollback note can be actively harmful.

## Rebuild Triggers

Trigger a rebuild when:

- any source hash changes in indexed artifacts
- chunk strategy changes
- embedder model changes
- vector dimension changes
- namespace mapping changes
- sparse tokenizer rules change

Rebuild scope:

- per-namespace if the change is local
- full index if the embedder or dimension changes

## Gating Wrath Controls

Hard controls for this index:

1. dense branch may not silently switch models
2. sparse-only degradation must be recorded in index state
3. stale namespaces may not remain queryable after a failed rebuild without warning
4. rebuild completion requires audit metadata
5. query responses should expose the active search mode when degraded

These controls prevent "it kind of worked" from becoming an accepted ops state.

## Audit Record

The index should persist:

- last rebuild time
- rebuild scope
- embedder model id
- vector dimension
- sparse tokenizer version
- source hashes covered
- degraded mode flag

Without these facts, future sessions cannot trust what the index represents.

## Failure Modes

| Failure mode | Symptom | Mitigation |
|--------------|---------|------------|
| stale dense namespace | old incidents retrieved | source_hash drift detection |
| sparse token collapse | filenames stop matching | token preservation tests |
| silent degraded mode | operators think hybrid is active | explicit mode flag |
| overwide corpus | noisy retrieval | strict corpus scope |
| no rebuild audit | unknown provenance | mandatory audit row |

## Validation Checklist

- dense dimensions match vector store contract
- sparse tokenizer preserves code and path tokens
- rebuild trigger paths are documented
- degraded mode is explicit
- freshness policy differs by content class
- top_k stays compact for gate decisions

## Integration

This index works with:

- `kno_chunk_strategy_n05.md`
- `kno_embedder_provider_n05.md`
- `kno_retriever_config_n05.md`
- `kno_vector_store_n05.md`
- `mem_entity_memory_n05.md`

The index is the memory of how search is supposed to behave, not just where data happens to live.

## Decision Summary

Use a hybrid `bm25 + pgvector` index with explicit rebuild audits, class-aware freshness, and visible degraded mode.

That is the correct N05 posture because operations memory must remain inspectable under pressure.
