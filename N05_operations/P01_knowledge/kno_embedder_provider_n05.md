---
id: kno_embedder_provider_n05
kind: embedder_provider
pillar: P02
nucleus: N05
title: "N05 Operations Embedder Provider"
version: "1.0.0"
quality: 9.0
tags: [n05, operations, embedder_provider, gating_wrath, retrieval, ci_cd, evidence]
density_score: 0.96
related:
  - p01_emb_openai_text_embedding_3_small
  - p01_kc_embedder_provider
  - bld_collaboration_model_provider
  - bld_collaboration_embedder_provider
  - bld_memory_embedder_provider
  - bld_examples_embedder_provider
  - bld_memory_model_provider
  - p03_ins_embedder_provider
  - embedder-provider-builder
  - bld_config_embedder_provider
---
<!-- 8F: F1=embedder_provider/P01 F2=embedder-provider-builder F3=nucleus_def_n05+P01_schema+kc_embedder_provider+examples+W1 contracts F4=managed primary with strict fallback gates
     F5=shell+apply_patch+cex_compile F6=approx-6KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/P01_knowledge/kno_embedder_provider_n05.md -->

# N05 Operations Embedder Provider

## Intent

N05 needs embeddings that survive the language mix of code review comments, CI logs, traceback text, deploy notes, shell commands, YAML keys, and short policy fragments.

The provider choice must optimize for:

- reliable semantic search on operational evidence
- predictable dimension contracts for the vector store
- low enough cost to reindex after config or schema changes
- strict handling of failures instead of silent degraded writes

## Properties

| Property | Value |
|----------|-------|
| Kind | `embedder_provider` |
| Pillar | `P01` |
| Nucleus | `N05` |
| Provider | `openai` |
| Model | `text-embedding-3-small` |
| Dimensions | `1536` |
| Normalization | `true` |
| Batch size | `96` |
| Failure stance | `fail_closed_on_mismatch` |

## Primary Decision

Use `text-embedding-3-small` as the primary embedder for N05 knowledge and memory retrieval.

Why this fits the Gating Wrath lens:

- high enough semantic quality for terse operational text
- low enough cost to support rebuilds after major ingest fixes
- explicit dimension control that makes validation simple
- mature API behavior suitable for CI environments

N05 does not need the most expensive model. It needs a provider that can be audited, pinned, and rejected on mismatch.

## Configuration Table

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| provider | `openai` | stable hosted API with clear model IDs |
| model | `text-embedding-3-small` | strong quality per cost for mixed operational text |
| dimensions | `1536` | keeps fidelity for logs plus policy text |
| max_tokens | `8191` | safely exceeds N05 chunk targets |
| batch_size | `96` | conservative for CI rate control |
| normalize | `true` | cosine search requires consistent vector scale |
| api_key_env | `OPENAI_API_KEY` | no inline secrets |
| timeout_seconds | `20` | avoids hung indexing workers |
| retry_policy | `2 tries, jittered backoff` | enough for transient API hiccups, not enough to hide systemic outage |

## Input Profile

The embedder must handle these text classes:

- code review rationale with short sentences and filenames
- stack traces with repeated module paths
- test assertions with exact expected and actual text
- deploy phase descriptions
- runbook prose and checklist bullets
- config snippets and env keys

Dense retrieval works only if the provider can cluster semantically related failures without erasing exact terms like service names, gate IDs, and command strings.

## Gating Wrath Guards

Hard rules for N05 indexing:

1. Reject writes when the returned dimension is not exactly `1536`.
2. Reject writes when the provider omits vectors for any input row.
3. Reject writes when normalization fails or produces NaN values.
4. Reject a batch if more than `2%` of rows error.
5. Stop reindex if rate limiting persists beyond the defined retry budget.

N05 prefers a delayed rebuild over a corrupted index.

## Fallback Policy

Fallback exists, but it is controlled:

- fallback model: `nomic-embed-text` via local Ollama
- fallback trigger: explicit operator override or documented OpenAI outage
- fallback scope: temporary query path or emergency rebuild, not silent production switch
- fallback warning: all mixed-model collections must be rebuilt from zero before normal service resumes

This is a critical gate. Mixing vectors from different models in the same collection is treated as index corruption.

## Cost and Rebuild Posture

| Scenario | Expected behavior |
|----------|-------------------|
| minor content delta | batch incremental upserts |
| schema change affecting chunk shape | full re-embed of affected namespace |
| dimension or model change | destroy and rebuild namespace |
| provider outage | pause dense writes, use sparse retrieval only if approved |

N05 should not optimize away rebuilds that preserve correctness. Operational evidence must stay trustworthy.

## Quality Notes

`text-embedding-3-small` is favored here because N05 queries are not mostly literary. They are short, sharp, and operational:

- "why did release gate fail after migration"
- "deploy health check loops on startup"
- "pytest import cycle after container refactor"
- "which runbook matches this rollback symptom"

These are semantic enough to benefit from dense retrieval, but concrete enough that a cheaper model still performs well when chunking and hybrid retrieval are done correctly.

## Failure Modes

| Failure mode | Symptom | Gate |
|--------------|---------|------|
| dimension drift | vector store rejects inserts later | validate dimension before write |
| silent partial batch | missing evidence in retrieval | require row-count parity |
| mixed model collection | strange nearest neighbors | hard namespace rebuild |
| overaggressive retries | CI timeouts and hidden outage | cap retries and surface error |
| no normalization | cosine ranking unstable | normalize every vector |

## Operational Validation

Before promoting a rebuild:

- embed a fixed probe set of N05 documents
- confirm all vectors share the same dimension
- verify nearest neighbors for known probe queries
- compare recall on incident, test, and deploy samples
- log model id and rebuild timestamp into index metadata

The probe set should include:

- one traceback chunk
- one deploy checklist chunk
- one health gate chunk
- one rollback lesson
- one CI failure summary

## Integration Contract

This embedder provider assumes:

- chunking from `kno_chunk_strategy_n05.md`
- `pgvector` storage from `kno_vector_store_n05.md`
- hybrid ranking from `kno_retriever_config_n05.md`
- freshness and rebuild rules from `mem_knowledge_index_n05.md`

The provider is not a free-floating preference. It is part of a gated retrieval chain.

## Decision Summary

Primary provider:

- `openai/text-embedding-3-small`

Acceptable emergency fallback:

- `ollama/nomic-embed-text`

Non-negotiable rule:

- any model swap requires an explicit rebuild boundary and index metadata update

That rule is the N05 expression of Gating Wrath: no silent drift, no mixed evidence, no optimistic corruption.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_emb_openai_text_embedding_3_small]] | sibling | 0.39 |
| [[p01_kc_embedder_provider]] | upstream | 0.37 |
| [[bld_collaboration_model_provider]] | related | 0.33 |
| [[bld_collaboration_embedder_provider]] | related | 0.33 |
| [[bld_memory_embedder_provider]] | downstream | 0.32 |
| [[bld_examples_embedder_provider]] | downstream | 0.31 |
| [[bld_memory_model_provider]] | downstream | 0.30 |
| [[p03_ins_embedder_provider]] | downstream | 0.30 |
| [[embedder-provider-builder]] | related | 0.30 |
| [[bld_config_embedder_provider]] | downstream | 0.29 |
