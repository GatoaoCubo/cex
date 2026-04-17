---
id: sch_input_schema_n04
kind: input_schema
pillar: P06
nucleus: n04
title: Knowledge Intake Schema
version: 1.0
quality: 8.8
tags: [schema, input, knowledge, ingestion, retrieval]
density_score: 1.0
---
<!-- 8F: F1 constrain=P06/input_schema F2 become=input-schema-builder F3 inject=n04-knowledge+kc_input_schema+P06 examples+N03/N05 contracts F4 reason=strict intake contract for evidence-hungry ingestion F5 call=shell,apply_patch F6 produce=7006 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P06_schema/sch_input_schema_n04.md -->
# Knowledge Intake Schema
## Purpose
N04 does not accept vague payloads. Under the Knowledge Gluttony lens, every intake should preserve enough context to support re-ranking, provenance tracing, freshness review, and taxonomy repair later.
This schema defines the unilateral contract for any caller that submits a knowledge unit, chunk batch, or indexing candidate into N04 workflows.
The contract is intentionally rich: it gathers source shape, traceability, and enrichment hints early so later stages do not need to infer missing facts.
## Schema
```yaml
name: knowledge_intake_input
type: object
strict: true
additionalProperties: false
required:
  - artifact_id
  - source_uri
  - content_kind
  - raw_text
  - target_signal_state
  - provenance
properties:
  artifact_id: {type: string, pattern: "^[a-z0-9_\\-]{6,80}$"}
  source_uri: {type: string, min_length: 8}
  content_kind: {type: string, enum_ref: sch_enum_def_n04.md}
  raw_text: {type: string, min_length: 80}
  target_signal_state: {type: string, enum_ref: sch_enum_def_n04.md}
  language: {type: string, default: "pt-BR"}
  taxonomy_candidates: {type: array, items: string, max_items: 12}
  provenance: {type: array, min_items: 1, items: provenance_record}
  freshness_days: {type: integer, minimum: 0, default: 30}
  embedding_required: {type: boolean, default: true}
  index_priority: {type: integer, minimum: 1, maximum: 5, default: 3}
```
## Fields
| Field | Type | Required | Default | Constraints | Why N04 wants it |
|-------|------|----------|---------|-------------|------------------|
| artifact_id | string | yes | none | stable slug, 6-80 chars | binds all later evidence to one key |
| source_uri | string | yes | none | absolute or repo-relative locator | provenance without location is weak |
| content_kind | string | yes | none | closed vocabulary only | keeps retrieval cohorts analyzable |
| raw_text | string | yes | none | min 80 chars | enough substance for chunking and embeddings |
| target_signal_state | string | yes | none | must be allowed enum | blocks ambiguous lifecycle entry |
| language | string | no | `pt-BR` | BCP47-ish token | improves tokenizer and search tuning |
| taxonomy_candidates | array[string] | no | `[]` | max 12 | greedy capture of hints before pruning |
| provenance | array[object] | yes | none | at least one record | gluttony for sources, not guesses |
| freshness_days | integer | no | `30` | zero or more | allows freshness gates to start immediately |
| embedding_required | boolean | no | `true` | strict bool | indexing path can skip only on purpose |
| index_priority | integer | no | `3` | 1-5 | lets queues favor high-value knowledge |
## Validation Rules
1. `artifact_id` must be unique within the active N04 index namespace.
2. `raw_text` must not be placeholder text such as `todo`, `tbd`, or repeated filler tokens.
3. `provenance` records must include at least one source classified as primary or directly observed.
4. `target_signal_state` cannot be `archived` or `rejected` at first submission unless `content_kind` is audit or tombstone.
5. If `embedding_required` is `false`, caller must provide a rationale in provenance notes.
6. `taxonomy_candidates` values must already be normalized to snake_case labels.
## Provenance Subschema
| Field | Type | Required | Constraints | N04 rationale |
|-------|------|----------|-------------|---------------|
| source_id | string | yes | stable slug | merge-friendly source identity |
| source_type | string | yes | doc, repo, api, human_note, crawl | preserves origin semantics |
| confidence | number | yes | 0.0-1.0 | greedy capture of trust signal |
| observed_at | string | yes | ISO date or datetime | freshness without timestamp is fantasy |
| notes | string | no | max 240 chars | concise context for later auditors |
## Example
```yaml
artifact_id: kc_rag_reweighting_patterns
source_uri: P01_knowledge/library/specs/CEX_SYSTEM_MAP.md
content_kind: normalized
raw_text: "Hybrid retrieval improves recall when taxonomy labels and embedding neighborhoods disagree..."
target_signal_state: enriched
language: pt-BR
taxonomy_candidates: [rag, retrieval, ranking, embeddings]
provenance:
  - source_id: cex_system_map
    source_type: doc
    confidence: 0.93
    observed_at: 2026-04-16
    notes: "Primary repo document with direct architectural claims"
freshness_days: 21
embedding_required: true
index_priority: 4
```
## Invalid Example
```yaml
artifact_id: temp
source_uri: unknown
content_kind: whatever
raw_text: "todo"
target_signal_state: done
provenance: []
```
## Invalid Example Reasons
| Field | Problem | Expected fix |
|-------|---------|--------------|
| artifact_id | too weak and non-descriptive | use stable domain slug |
| source_uri | not actionable | provide resolvable path or URL |
| content_kind | unconstrained label | map to approved vocabulary |
| raw_text | insufficient evidence | provide substantive content |
| target_signal_state | enum violation | choose valid lifecycle value |
| provenance | empty | include at least one record |
## Rationale
| Design choice | Knowledge Gluttony expression | Benefit |
|---------------|------------------------------|---------|
| provenance mandatory | hungry systems remember where claims came from | lowers hallucinated facts |
| taxonomy hints collected early | N04 prefers surplus metadata before pruning | faster downstream classification |
| strict schema | greedy collection must still be coherent | prevents sloppy caller contracts |
| freshness on intake | hunger without time-awareness creates stale indexes | supports automatic review |
| priority field | not all knowledge deserves equal queue share | protects high-value sources |
## Upstream And Downstream
| Direction | Component | Contract role |
|-----------|-----------|---------------|
| upstream | N01 research, N07 handoffs, import scripts | must satisfy this input |
| downstream | chunkers, embedders, validators | may rely on guaranteed fields |
| downstream | path and rate configs | tune storage and throughput by priority |
## Properties
| Property | Value |
|----------|-------|
| Schema name | `knowledge_intake_input` |
| Strict | yes |
| Additional properties | false |
| Required field count | 6 |
| Optional field count | 5 |
| Min text length | 80 |
| Provenance minimum | 1 record |
| Priority range | 1-5 |
| Intended scope | N04 ingestion and indexing |
| Enforcement layer | pre-ingest and pre-commit |
