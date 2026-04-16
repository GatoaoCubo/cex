---
id: kno_retriever_config_n05
kind: retriever_config
pillar: P01
nucleus: N05
title: "N05 Operations Retriever Config"
version: "1.0.0"
quality: null
tags: [n05, operations, retriever_config, gating_wrath, hybrid_search, ci_cd, deploy]
---
<!-- 8F: F1=retriever_config/P01 F2=retriever-config-builder F3=nucleus_def_n05+P01_schema+kc_retriever_config+ops examples+W1 config F4=hybrid retrieval with strict filters and rerank
     F5=shell+apply_patch+cex_compile F6=approx-7KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/knowledge/kno_retriever_config_n05.md -->

# N05 Operations Retriever Config

## Intent

The retriever for N05 must answer operational questions with evidence that is precise, recent, and gate-relevant.

The retrieval stance is not "show something related."

It is:

- surface the exact failing evidence first
- combine lexical and semantic matching
- filter by nucleus, pillar, and document class
- rerank toward decision utility, not narrative similarity

## Properties

| Property | Value |
|----------|-------|
| Kind | `retriever_config` |
| Pillar | `P01` |
| Nucleus | `N05` |
| Store type | `hybrid_pgvector_plus_bm25` |
| Search type | `hybrid` |
| top_k | `6` |
| candidate_k | `24` |
| Reranker | `enabled` |
| Failure stance | `block_on_low_signal` |

## Primary Query Classes

This retriever is tuned for:

- code review risk lookup
- failing test explanation lookup
- deploy runbook retrieval
- rollback criteria lookup
- incident pattern match
- config/schema boundary lookup

Each query class needs fast access to both exact strings and semantically related prior evidence.

## Core Parameters

| Parameter | Value | Why |
|-----------|-------|-----|
| top_k | `6` | enough for synthesis without flooding the gate |
| candidate_k_dense | `16` | semantic recall for short ops queries |
| candidate_k_sparse | `16` | exact term recovery for test names and env keys |
| fusion_method | `rrf` | stable merge across dense and sparse rankings |
| dense_weight | `0.62` | semantic edge for paraphrased incident questions |
| sparse_weight | `0.38` | preserve exact identifiers and commands |
| reranker_top_n | `6` | final evidence packet stays compact |
| score_floor | `0.18` | below this, respond with insufficient evidence |
| freshness_decay_days | `30` | older ops evidence is useful but should fade |

## Hard Filters

Every query applies these filters unless explicitly overridden:

- `nucleus = N05`
- `pillar in [P01, P10]`
- `document_class in [runbook, checklist, ci_log, test_output, deploy_log, schema, memory]`
- `archived = false`

Optional narrow filters:

- `kind`
- `service`
- `environment`
- `release_id`
- `incident_id`

Gating Wrath principle:

- do not let a broad semantic match outrank the wrong environment or stale release window

## Query Flow

1. normalize the query but preserve code tokens, filenames, test ids, and env keys
2. run sparse search for exact identifiers and failure strings
3. run dense search against the vector store
4. fuse with reciprocal rank fusion
5. rerank using gate utility features
6. discard below score floor
7. if fewer than 2 strong results remain, return an insufficiency warning instead of bluffing

## Rerank Policy

The reranker should prefer chunks with:

- explicit failure verdicts
- matching service or environment tags
- recent timestamps
- direct commands, tests, or endpoints named in the query
- one operational event per chunk

The reranker should demote:

- generic handbook prose
- stale incidents from incompatible environments
- chunks that mention the concept but lack evidence

## Special Handling

| Query type | Extra rule |
|------------|------------|
| release gate | prefer checklists, smoke evals, deploy logs, learning records |
| failing test | boost exact test id and traceback chunks |
| rollback | require deploy log or runbook evidence |
| config lookup | boost schema and config artifacts, demote memories |
| repeated incident | boost learning records and memory summaries after direct evidence |

## Fail-Closed Behavior

The retriever must not fabricate confidence.

Return `insufficient_evidence` when:

- only one weak chunk survives score threshold
- dense and sparse results disagree across environments
- freshness-critical queries retrieve only stale evidence
- filters remove all candidates

In those cases N05 should ask for:

- more scope
- the failing service name
- the environment
- the exact gate or test id

## Example Defaults

| Scenario | Retrieval mode |
|----------|----------------|
| "why did ready probe fail after migration" | dense+sparse+rereank, freshness boost |
| "tests/test_ready.py timeout" | sparse heavy, traceback boost |
| "rollback checklist for api deploy" | hybrid, checklist priority |
| "what do we remember about repeated secret loading failure" | hybrid, memory and learning boost |

## Operational Constraints

The retriever is designed for low-latency triage, not broad research.

Target posture:

- p50 under `220ms` for cached sparse plus warm vector index
- top_k no larger than `6`
- no query expansion unless explicitly requested
- no automatic cross-nucleus retrieval during gate decisions

That last rule is important. Gating decisions should stay local unless the operator chooses to widen scope.

## Failure Modes

| Failure mode | Result | Mitigation |
|--------------|--------|------------|
| dense-only bias | misses exact test or env names | retain sparse branch |
| sparse-only bias | misses semantically similar incident patterns | retain dense branch |
| no freshness control | stale deploy advice retrieved | apply decay and environment filter |
| too many hits | answer becomes noncommittal | cap final set at 6 |
| weak score floor | noisy evidence approved | block on low signal |

## Validation Checklist

- top result must match service or environment when query includes one
- exact test ids must appear in final candidate set if present in query
- deploy queries should surface a checklist or deploy log in top 3
- memory artifacts should not outrank direct evidence for first-pass triage
- empty or low-signal results should produce explicit insufficiency

## Integration

This retriever assumes:

- chunks produced by `kno_chunk_strategy_n05.md`
- vectors from `kno_embedder_provider_n05.md`
- storage from `kno_vector_store_n05.md`
- namespace and freshness policy from `mem_knowledge_index_n05.md`

It also expects N05 memories to stay compact and decision-oriented so that memory artifacts help only after direct evidence is found.

## Decision Summary

Default N05 retrieval mode:

- hybrid search
- strict filters
- top_k `6`
- candidate pool `24`
- reranker on
- low-signal block enabled

This is the right posture for an operations nucleus. A gatekeeper should return less, but better.
