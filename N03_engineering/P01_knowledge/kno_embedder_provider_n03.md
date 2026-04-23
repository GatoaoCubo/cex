---
id: kno_embedder_provider_n03
kind: embedder_provider
pillar: P02
nucleus: N03
title: "N03 Embedder Provider"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering retrieval architecture
quality: 9.1
tags: [embedder_provider, p01, n03, embeddings, retrieval, inventive_pride]
density_score: 0.99
related:
  - bld_collaboration_embedder_provider
  - bld_memory_embedder_provider
  - bld_collaboration_model_provider
  - bld_config_embedder_provider
  - embedder-provider-builder
  - p01_kc_embedder_provider
  - p03_sp_embedder_provider_builder
  - p03_ins_embedder_provider
  - bld_knowledge_card_embedder_provider
  - bld_collaboration_vector_store
---
<!-- 8F: F1=embedder_provider/P01 F2=embedder-provider-builder F3=nucleus_def_n03+kc_embedder_provider+P01_schema F4=proud dense-retrieval default
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:6247 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/P01_knowledge/kno_embedder_provider_n03.md -->

# N03 Embedder Provider

## Properties

| Property | Value |
|----------|-------|
| Kind | `embedder_provider` |
| Pillar | `P01` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Provider class | hosted dense embedder with stable truncation |
| Preferred dimensions | `1024` |
| Query mode | symmetric text embeddings |
| Batch profile | medium throughput, high consistency |
| Normalization | mandatory |
| Upgrade posture | reindex on model family change |

## Role

The embedder provider turns N03 knowledge into a geometry of engineering meaning.
Inventive Pride rejects cheap embeddings that flatten nuanced build constraints.
The provider must reward precise terminology, structural similarity, and procedural intent.
It is selected for retrieval dignity, not novelty.

## Default Position

N03 should use a modern hosted embedding model with:
- native dimension control
- strong technical-text performance
- deterministic normalization expectations
- acceptable latency for batch indexing
- predictable long-term vendor support

The default shape is:
- provider family: enterprise hosted API
- model class: latest general-purpose text embedding family
- dimension target: `1024`
- vector normalization: `l2`
- batch size: `64`
- retry policy: exponential backoff with bounded retries

## Why `1024`

| Option | Strength | Weakness | Verdict |
|-------|----------|----------|---------|
| 256 | cheap and compact | loses structural nuance in technical docs | too compressed for N03 |
| 512 | reasonable balance | still trims distinction between adjacent builders | acceptable fallback |
| 1024 | strong semantic headroom | larger index footprint | preferred |
| 1536+ | maximal fidelity | unnecessary cost for current corpus scale | reserve for expansion |

## Text Scope

The provider must handle:
- builder manifests
- nucleus architecture notes
- schemas with mixed prose and keys
- markdown tables
- handoff instructions
- memory summaries and runtime state digests

It should not be optimized around conversational fluff.
Its center of gravity is technical instruction and architectural contrast.

## Configuration Contract

| Field | N03 stance | Rationale |
|------|-------------|-----------|
| provider | explicit and versioned | avoid hidden vendor drift |
| model | pinned | reindexing must be intentional |
| dimensions | pinned at index time | mixed dimensions are unacceptable |
| max_input_tokens | above chunk ceiling | prevents silent truncation |
| batch_size | moderate | keeps throughput stable under rate limits |
| normalize | true | cosine search assumes normalized vectors |
| api_key_env | dedicated secret | isolate operational failure domains |

## Operational Guardrails

1. Never mix vectors from different model families in one live collection.
2. Never change dimension without full reindex.
3. Never disable normalization when cosine ranking is used.
4. Never embed raw compiled noise if source markdown already exists.
5. Never optimize purely for cost if it degrades builder retrieval precision.

## Pride Lens

Inventive Pride means retrieval should recognize the difference between:
- a schema boundary and a runtime heuristic
- a builder identity and a deployment concern
- a quality gate and a casual checklist
The embedder must preserve these distinctions.
If adjacent artifact kinds collapse together, the provider is unworthy.

## Fallback Stack

| Tier | Use case | Expectation |
|------|----------|-------------|
| Tier 1 | hosted primary embedder | production indexing and query embeddings |
| Tier 2 | hosted smaller sibling | temporary budget relief with same family if possible |
| Tier 3 | local sentence transformer | offline recovery, lower recall accepted |

## Cost Discipline

N03 values quality first, but not theatrically.
The corpus is finite and engineering-dense.
That favors a mid-high dimension model over the largest available option.
The proud choice is the smallest model that still separates close technical concepts.

## Observability

- record embedding model in artifact metadata
- track reindex timestamp
- track vector count per collection
- track average chunk length
- sample nearest-neighbor quality on canonical queries
- compare retrieval precision after any provider change

## Failure Signals

| Signal | Interpretation | Action |
|-------|----------------|--------|
| frequent irrelevant neighbors | semantic compression too weak | increase dimensions or change family |
| high latency on batch ingest | provider throttling or batch too large | reduce batch size |
| empty or malformed vectors | provider contract changed | halt indexing |
| query and corpus mismatch | asymmetric embedding path broken | audit query mode |

## Compatibility Notes

The provider is paired with:
- chunk sizes around `720` tokens
- hybrid retrieval with lexical backup
- metadata-aware vector store filtering
- periodic evaluation against known N03 queries

It must support enough input length to encode section-rich engineering chunks.
It must also behave predictably under repeated nightly reindex cycles.

## Migration Rules

- minor model revision within same family: benchmark before switch
- dimension reduction: rebuild collection and compare top-10 query sets
- provider family change: dual-index trial before cutover
- offline fallback use: mark retrieval quality as degraded in runtime state

## Final Position

N03 should embed with a stable, modern, normalized, `1024`-dimension provider.
That choice respects cost, but it is ultimately a quality decision.
Retrieval should feel engineered, not approximate.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_embedder_provider]] | related | 0.41 |
| [[bld_memory_embedder_provider]] | downstream | 0.38 |
| [[bld_collaboration_model_provider]] | related | 0.37 |
| [[bld_config_embedder_provider]] | downstream | 0.36 |
| [[embedder-provider-builder]] | related | 0.34 |
| [[p01_kc_embedder_provider]] | upstream | 0.33 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.32 |
| [[p03_ins_embedder_provider]] | downstream | 0.32 |
| [[bld_knowledge_card_embedder_provider]] | upstream | 0.31 |
| [[bld_collaboration_vector_store]] | related | 0.31 |
