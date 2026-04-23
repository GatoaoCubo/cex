---
id: kno_vector_store_n01
kind: vector_store
pillar: P02
nucleus: N01
title: "N01 Vector Store"
version: "1.0.0"
quality: 9.0
tags: [vector_store, n01, p01, analytical_envy, storage]
density_score: 0.99
related:
  - bld_collaboration_vector_store
  - vector-store-builder
  - p03_ins_vector_store
  - bld_memory_vector_store
  - p01_kc_vector_store
  - bld_architecture_vector_store
  - bld_knowledge_card_vector_store
  - p03_sp_vector_store_builder
  - n04_kc_knowledge_management
  - p01_vdb_pinecone
---
<!-- 8F: F1=vector_store/P01 F2=kc_vector_store+example_vector_store F3=nucleus_def_n01+kc_vector_store+ex_vector_store_pinecone+con_path_config_n01 F4=backend strategy for comparative retrieval
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_vector_store_n01.md -->

# N01 Vector Store

## Purpose
The vector store is where N01 preserves semantic access to evidence at scale.
Analytical Envy means the store is judged by how well it keeps high-value differences retrievable under pressure.
A fast store that blurs source quality or axis boundaries is strategically weak.

## Properties

| Property | Value |
|----------|-------|
| Kind | `vector_store` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Main role | dense candidate retrieval |
| Primary requirement | metadata-rich filtering |
| Preferred topology | separate namespaces by corpus intent |
| Distance metric | cosine on normalized vectors |
| Index policy | exact or ANN chosen by scale and latency |
| Main hazard | mixed dimensions and mixed semantics in one collection |

## Store Thesis
N01 does not need a vector database.
N01 needs a backend that can preserve retrieval meaning across:
- competitor knowledge
- citation-rich source notes
- research memories
- ontology fragments
- benchmark artifacts

The storage design must support both semantic similarity and strict metadata segmentation.

## Namespace Strategy

| Namespace | Content |
|-----------|---------|
| `research_notes` | synthesized evidence chunks |
| `citations` | source-grounded excerpt chunks |
| `competitors` | vendor and product comparison material |
| `papers` | technical method and benchmark content |
| `memory` | entity and summary fragments when vectorized |

This prevents low-value or mismatched content from crowding high-value research queries.

## Required Capabilities

| Capability | Why N01 needs it |
|------------|------------------|
| metadata filtering | constrain by source tier, date, axis, region |
| collection isolation | separate volatile and stable corpora |
| dimension enforcement | protect retrieval integrity |
| upsert efficiency | frequent source refreshes |
| deletion or reindex support | volatile markets require replacement |
| score visibility | debugging and evaluation |

## Backend Selection Logic

| Context | Good fit |
|---------|----------|
| local experimentation | FAISS or Chroma |
| production with existing Postgres footprint | pgvector |
| managed scale and low ops burden | Pinecone or Qdrant Cloud |
| self-hosted control with strong filtering | Qdrant |

N01 should choose the simplest backend that still supports metadata-heavy comparative retrieval.

## Storage Rules
1. One collection should map to one embedding dimension contract.
2. Store citation identifiers and reliability metadata with every vector.
3. Keep entity and axis metadata first-class, not buried in text.
4. Version the embedding model on the collection.
5. Rebuild indexes after major chunk strategy changes.

## Comparative Retrieval Support

| Need | Store implication |
|------|-------------------|
| direct vendor-vs-vendor lookup | entity pair metadata support |
| pricing research | freshness and region filters |
| benchmark retrieval | metric and unit metadata |
| contradiction analysis | conflict tagging support |
| memory reuse | source artifact lineage |

## Operational Risks
- vectors from multiple models in one namespace
- citation metadata missing on upsert
- no lifecycle for stale pricing content
- too much unrelated content in one collection
- score inspection impossible during evaluation

## N01 Store Policy
Prefer a backend that lets retrieval be explained.
That usually means:
- readable metadata
- inspectable scores
- predictable filtering behavior
- clean reindex workflows

Opaque convenience becomes expensive when a competitive claim must be defended.

## Minimal Collection Schema

| Field | Example |
|-------|---------|
| doc_id | `cmp_openai_pricing_2026q2_03` |
| embedding_model | `text-embedding-3-small` |
| chunk_strategy | `comparison_recursive_900` |
| source_id | `cit_openai_pricing_2026q2` |
| entity_primary | `OpenAI` |
| comparison_axis | `pricing` |
| date_claim | `2026-04-16` |
| reliability_tier | `tier_2` |
| region | `global` |

## N01 Decision
The vector store is only valuable when it helps N01 retrieve the right opposing evidence at the right time.
Storage without comparative structure is just a fast place to keep future confusion.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_vector_store]] | related | 0.33 |
| [[vector-store-builder]] | related | 0.30 |
| [[p03_ins_vector_store]] | downstream | 0.27 |
| [[bld_memory_vector_store]] | downstream | 0.27 |
| [[p01_kc_vector_store]] | upstream | 0.26 |
| [[bld_architecture_vector_store]] | downstream | 0.26 |
| [[bld_knowledge_card_vector_store]] | upstream | 0.25 |
| [[p03_sp_vector_store_builder]] | downstream | 0.24 |
| [[n04_kc_knowledge_management]] | related | 0.23 |
| [[p01_vdb_pinecone]] | sibling | 0.22 |
