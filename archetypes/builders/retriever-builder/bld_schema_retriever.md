---
kind: schema
id: bld_schema_retriever
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for retriever
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [schema, retriever, P04, P06, vector-search, RAG]
density_score: 1.0
title: Schema ISO - retriever
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_golden_test
  - bld_schema_prompt_version
  - bld_schema_action_prompt
  - bld_schema_enum_def
---
# Schema: retriever

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | YES | - | Pattern: `p04_retr_{store_slug}` |
| kind | literal "retriever" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable retriever name |
| store_type | enum (see below) | YES | - | Vector store backend |
| embedding_model | string | YES | - | e.g. text-embedding-3-small |
| similarity_metric | enum (see below) | YES | cosine | Distance function |
| top_k | int >= 1 | YES | 10 | Number of results returned |
| search_type | enum (see below) | REC | vector | Search strategy |
| reranker | string or null | REC | null | Optional reranking model |
| metadata_filters | list[string] | REC | - | Filterable metadata fields |
| namespace | string | REC | default | Collection/namespace scoping |
| quality | null | YES | null | Never self-score |
| tags | list[string] len >= 3 | YES | - | Must include "retriever" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the retriever does |

## ID Pattern
Regex: `^p04_retr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
Examples: `p04_retr_chroma`, `p04_retr_pinecone_hybrid`, `p04_retr_faiss_local`

## Enum: store_type
`chroma | pinecone | faiss | qdrant | weaviate | milvus | elasticsearch | costm`

## Enum: similarity_metric
`cosine | dot_product | euclidean | manhattan`

## Enum: search_type
`vector | keyword | hybrid`

## Body Structure (required sections)
1. `## Overview` — what store, embedding model, use case
2. `## Search Strategy` — vector/keyword/hybrid, metric, reranking pipeline
3. `## Configuration` — top_k, filters, namespace, score thresholds
4. `## Integration` — SDK/API, authentication, connection string pattern

## Constraints
- max_bytes: 2048 (body only, excludes frontmatter)
- naming: `p04_retr_{store_slug}.md` (single file, no companion .yaml required at authoring)
- machine_format: yaml (compiled artifact format)
- id == filename stem (enforced by quality gate H02)
- quality: null always (H04)
- NO implementation code in body — spec only
- NO raw embedding vectors in output spec

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.70 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_constraint_spec]] | sibling | 0.63 |
| [[bld_schema_chunk_strategy]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
| [[bld_schema_prompt_version]] | sibling | 0.61 |
| [[bld_schema_action_prompt]] | sibling | 0.61 |
| [[bld_schema_enum_def]] | sibling | 0.60 |
