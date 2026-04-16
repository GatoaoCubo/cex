---
id: mem_entity_memory_n05
kind: entity_memory
pillar: P10
nucleus: N05
title: "N05 Operations Entity Memory"
version: "1.0.0"
quality: null
tags: [n05, operations, entity_memory, gating_wrath, memory, release_gate, retrieval]
---
<!-- 8F: F1=entity_memory/P10 F2=entity-memory-builder F3=nucleus_def_n05+P10_schema+kc_entity_memory+examples+N05 context F4=project entity for ops retrieval surface
     F5=shell+apply_patch+cex_compile F6=approx-6KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/memory/mem_entity_memory_n05.md -->

# N05 Operations Entity Memory

## Intent

This entity memory stores the current operational facts about the N05 retrieval and gating surface as a named project entity.

It is not an event log.

It is the current state snapshot that future sessions need in order to reason consistently about release gates, incident lookup, and retrieval infrastructure.

## Properties

| Property | Value |
|----------|-------|
| Kind | `entity_memory` |
| Pillar | `P10` |
| Nucleus | `N05` |
| Name | `n05_ops_retrieval_surface` |
| Entity type | `project` |
| Update policy | `merge_with_validation` |
| Volatility | `medium` |
| TTL | `45 days` |

## Entity Definition

The entity represented here is the operational retrieval surface used by N05 to support:

- code review verdicts
- CI failure lookup
- deploy gate decisions
- rollback runbook retrieval
- memory-backed incident pattern detection

## Current Attributes

| Attribute | Value | Confidence |
|-----------|-------|------------|
| primary_vector_backend | `pgvector` | high |
| primary_embedder | `openai/text-embedding-3-small` | high |
| retrieval_mode | `hybrid dense+sparse+rereank` | high |
| primary_dense_dimensions | `1536` | high |
| top_k_default | `6` | high |
| candidate_pool | `24` | high |
| dominant_corpus | `runbooks, ci logs, deploy logs, schema, memory` | high |
| gate_posture | `fail_closed_on_low_signal` | high |
| fallback_dense_provider | `ollama/nomic-embed-text` | medium |
| sparse_engine | `bm25` | high |

## Relationships

| Related entity | Relation | Why it matters |
|----------------|----------|----------------|
| `N05` | `owned_by` | nucleus ownership and domain scope |
| `kno_chunk_strategy_n05` | `depends_on` | chunk boundaries define searchable evidence |
| `kno_retriever_config_n05` | `executed_by` | query behavior for this entity |
| `kno_vector_store_n05` | `stored_in` | vector backend for dense branch |
| `mem_knowledge_index_n05` | `indexed_by` | sparse and dense refresh policy |
| `mem_learning_record_n05` | `improved_by` | recurring lessons tune the surface |

## Gating Wrath Facts

Persistent facts that should survive sessions:

- manual spot checks do not override failing automated release gates
- model swaps require namespace rebuilds
- low-signal retrieval must surface insufficiency, not confidence
- evidence chunks outrank polished summaries during first-pass triage
- environment and service filters are mandatory for deploy-sensitive queries

These are not abstract values. They are operating constraints.

## Update Policy

`merge_with_validation` means:

1. merge only if the new fact includes evidence or a direct config change
2. overwrite numeric settings only when the source version is newer
3. append related entities if they are unique
4. reject updates that conflict with known contract rules without explanation

Examples:

- changing `top_k_default` from `6` to `8` requires a retrieval benchmark note
- changing `primary_embedder` requires a rebuild statement
- adding a new namespace requires a documented document class

## Facts to Exclude

Do not store these here:

- one-off incidents
- per-session blockers
- raw benchmark outputs
- temporary experiment branches
- credentials or secret names with values

Those belong in learning records, session memory, or config artifacts.

## Refresh Triggers

Refresh this entity when any of the following change:

- embedder provider
- vector backend
- retrieval mode
- top_k or score floor
- corpus composition
- gate posture

If none of those changed, the entity should stay stable across sessions.

## Failure Modes

| Failure mode | Result | Response |
|--------------|--------|----------|
| entity used as timeline | bloated memory and stale facts | move event detail to learning record |
| no TTL | old retrieval posture stays forever | keep 45-day review |
| unvalidated overwrite | hidden config drift | require evidence-backed merge |
| missing relations | hard to trace dependencies | keep relation table current |

## Retrieval Use

This entity memory should be injected when N05 needs fast context on:

- what retrieval stack is currently authoritative
- which gates are hard rules
- what fallback paths exist
- which artifacts form the operational retrieval chain

It should not dominate context. It should supply the stable facts that prevent re-discovery.

## Validation Checklist

- entity has one clear name
- facts are current-state only
- attributes are decision-relevant
- update policy is explicit
- TTL is present
- relationships point to actual artifacts

## Decision Summary

`n05_ops_retrieval_surface` is the right entity to persist because it captures the stable shape of the N05 search and gate system without mixing in transient incident noise.
