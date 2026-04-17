---
id: sch_type_def_n04
kind: type_def
pillar: P06
nucleus: n04
title: Knowledge Record Type
version: 1.0
quality: null
tags: [schema, type, knowledge, provenance, index]
---
<!-- 8F: F1 constrain=P06/type_def F2 become=type-def-builder F3 inject=n04-knowledge+kc_type_def+P06 examples+N04 schema contracts F4 reason=reusable typed record for provenance-heavy knowledge objects F5 call=shell,apply_patch F6 produce=6018 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P06_schema/sch_type_def_n04.md -->
# Knowledge Record Type
## Purpose
N04 needs a reusable object type for facts that survive beyond one prompt or one batch.
Under the Knowledge Gluttony lens, the type must preserve text, provenance, taxonomy, freshness, and ranking hints in one reusable shape so the system can keep learning from the same record over time.
This type is the durable vocabulary used by input contracts, validators, and downstream config.
## Schema
```yaml
name: knowledge_record
base_type: object
nullable: false
extends: null
serialization:
  primary: yaml
  secondary: json
required:
  - record_id
  - title
  - body
  - signal_state
  - provenance
  - taxonomy
  - freshness
fields:
  record_id: string
  title: string
  body: string
  summary: string?
  signal_state: enum<knowledge_signal_state>
  provenance: list<provenance_item>
  taxonomy: list<string>
  freshness: freshness_window
  embedding: embedding_ref?
  retrieval_score_hint: number?
  access_tier: string?
```
## Fields
| Field | Type | Required | Example | Why it exists |
|-------|------|----------|---------|---------------|
| record_id | string | yes | `kr_rag_rerank_001` | stable primary key |
| title | string | yes | `Hybrid Reranking Pattern` | human-readable retrieval anchor |
| body | string | yes | `Dense explanation of reranking...` | main evidence payload |
| summary | string | no | `Short abstract for previews` | cheaper recall surfaces |
| signal_state | enum | yes | `enriched` | lifecycle-aware retrieval |
| provenance | list<object> | yes | `[{source_id:..., confidence:...}]` | hungry memory needs source depth |
| taxonomy | list<string> | yes | `[rag, retrieval, ranking]` | categorization for route and search |
| freshness | object | yes | `{review_after_days: 30, stale_after_days: 90}` | explicit time decay |
| embedding | object | no | `{model: text-embedding-3-large, vector_ref: ...}` | decouples text from vector storage |
| retrieval_score_hint | number | no | `0.82` | precomputed ranking signal |
| access_tier | string | no | `internal_shared` | permission-aware serving |
## Nested Types
| Nested type | Shape | Constraint |
|-------------|-------|-----------|
| provenance_item | object | source_id, source_type, confidence, observed_at required |
| freshness_window | object | review_after_days <= stale_after_days |
| embedding_ref | object | model, dimension, vector_ref, generated_at |
## Constraints
| Constraint | Rule | Rationale |
|------------|------|-----------|
| `record_id` uniqueness | unique per active namespace | avoids duplicate evidence collisions |
| `title` size | 8-120 chars | enough signal without bloated headings |
| `body` size | 160+ chars | N04 avoids starving the index |
| `taxonomy` count | 1-8 labels | enough context without taxonomy spam |
| `confidence` range | 0.0-1.0 | machine-sortable trust |
| `retrieval_score_hint` | 0.0-1.0 if present | normalized ranking signal |
## Freshness Window Definition
```yaml
freshness_window:
  review_after_days: 30
  stale_after_days: 90
  last_reviewed_at: 2026-04-16
  freshness_basis: observed_at_max
```
## Embedding Reference Definition
```yaml
embedding_ref:
  model: text-embedding-3-large
  dimension: 3072
  vector_ref: vs://n04/knowledge/kr_rag_rerank_001
  generated_at: 2026-04-16T18:20:00Z
```
## Example
```yaml
knowledge_record:
  record_id: kr_taxonomy_conflict_017
  title: Taxonomy conflict between product and workflow labels
  body: "A retrieval gap appears when ecommerce docs use product_taxonomy while workflow docs use process_taxonomy..."
  summary: "Cross-domain taxonomy mismatch harms recall."
  signal_state: contested
  provenance:
    - source_id: src_framework_taxonomy
      source_type: doc
      confidence: 0.88
      observed_at: 2026-04-12
  taxonomy: [taxonomy, retrieval, drift]
  freshness:
    review_after_days: 14
    stale_after_days: 45
    last_reviewed_at: 2026-04-16
    freshness_basis: observed_at_max
  retrieval_score_hint: 0.74
  access_tier: internal_shared
```
## Rationale
| Decision | Knowledge Gluttony interpretation | Operational effect |
|----------|----------------------------------|--------------------|
| keep both body and summary | N04 hoards full evidence and compressed recall forms | supports cheap previews and deep audits |
| store freshness as object | hunger for facts must include hunger for recency context | stale detection becomes deterministic |
| embedding kept as ref not vector inline | gluttony for metadata should not bloat the type with heavy payloads | storage remains portable |
| taxonomy required | unlabeled knowledge is hard to retrieve and compare | better index partitioning |
| provenance list, not singleton | multiple witnesses beat one unchallenged claim | better confidence handling |
## Usage Surfaces
| Consumer | Usage |
|----------|-------|
| input schema | validates raw intake before becoming this type |
| validators | enforce invariants on confidence and freshness |
| config | path, permission, and secret layers decide where and how records live |
| retrieval layer | scores and filters by state, freshness, and taxonomy |
## Properties
| Property | Value |
|----------|-------|
| Type name | `knowledge_record` |
| Base type | object |
| Nullable | no |
| Required field count | 7 |
| Optional field count | 4 |
| Primary serialization | yaml |
| Secondary serialization | json |
| Reuse target | N04 ingestion, indexing, audit |
| Drift tolerance | low |
| Governance mode | validator enforced |
