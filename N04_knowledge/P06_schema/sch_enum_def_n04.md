---
id: sch_enum_def_n04
kind: enum_def
pillar: P06
nucleus: n04
title: Knowledge Signal Enum
version: 1.0
quality: 9.0
tags: [schema, enum, knowledge, taxonomy, governance]
name: knowledge_signal_state
values: [raw_capture, normalized, enriched, contested, stale, archived, rejected]
density_score: 1.0
related:
  - bld_examples_lifecycle_rule
  - p01_kc_schema_validation
  - bld_architecture_validator
  - agent_card_n04
  - bld_architecture_api_reference
  - bld_collaboration_knowledge_card
  - self_audit_n04_codex_2026_04_15
  - bld_architecture_legal_vertical
  - bld_architecture_healthcare_vertical
  - bld_knowledge_card_enum_def
---
<!-- 8F: F1 constrain=P06/enum_def F2 become=enum-def-builder F3 inject=n04-knowledge+kc_enum_def+P06 examples+P06 schema F4 reason=closed-set vocabulary for knowledge ingestion rigor F5 call=shell,apply_patch F6 produce=5908 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P06_schema/sch_enum_def_n04.md -->
# Knowledge Signal Enum
## Purpose
N04 works under the Knowledge Gluttony lens: capture more signal than the minimum, but capture it in a finite, auditable vocabulary so retrieval, indexing, and validator layers do not drown in synonyms.
This enum defines the canonical lifecycle labels for knowledge-bearing units handled by N04 pipelines such as ingestion, chunk enrichment, taxonomy alignment, freshness review, and publication.
The design favors gluttonous observation with controlled naming: we want many facts, but we want them compressed into a reusable closed set instead of free-text drift.
## Values
| Value | Meaning | Typical producer | Typical consumer | Status |
|-------|---------|------------------|------------------|--------|
| raw_capture | Source was collected with minimal normalization | crawler, importer, handoff reader | input_schema, validator | active |
| normalized | Core fields were normalized to canonical names and formats | parser, mapper | type_def, retriever | active |
| enriched | Added metadata such as taxonomy tags, embeddings, or provenance | enrichment worker | ranking, quality audit | active |
| contested | Conflicting facts or weak provenance detected | validator, auditor | human review, dispute queue | active |
| stale | Previously valid knowledge exceeded freshness policy | freshness checker | reingestion planner | active |
| archived | Kept for history, excluded from active retrieval by default | archive pipeline | analytics, audits | active |
| rejected | Failed structural or provenance checks and cannot enter index | validator | remediation queue | active |
## Schema
```yaml
name: knowledge_signal_state
type: string
default: raw_capture
case_sensitive: false
extensible: controlled
allowed_values:
  - raw_capture
  - normalized
  - enriched
  - contested
  - stale
  - archived
  - rejected
normalization_rule: lowercase_snake_case_exact_match
```
## Usage Map
| Surface | Field | Why this enum appears |
|---------|-------|-----------------------|
| knowledge card metadata | signal_state | lets retrievers filter on maturity |
| ingestion logs | target_state | records what stage a batch should reach |
| validator output | failing_state | blocks invalid promotion paths |
| freshness audit | current_state | separates stale from rejected facts |
| path and rate policies | index_priority | lets config tune treatment by state |
## Rationale
| Decision | Knowledge Gluttony reason | Control mechanism |
|----------|---------------------------|------------------|
| include `raw_capture` | N04 wants to remember unrefined intake, not just polished artifacts | downstream validators prevent direct promotion |
| include `contested` | gluttony for evidence means conflicting facts are stored, not discarded silently | retrieval can demote contested items |
| separate `stale` and `archived` | stale knowledge needs hunger-driven recheck; archived knowledge is intentionally cold | freshness policies target only stale |
| include `rejected` | failed evidence should still be learnable as a negative pattern | excluded from active index |
| forbid free-text states | too many labels destroy search precision | exact enum matching |
## Properties
| Property | Value |
|----------|-------|
| Enum name | `knowledge_signal_state` |
| Domain | N04 knowledge lifecycle |
| Default | `raw_capture` |
| Required | yes |
| Max values | 7 |
| Expansion policy | PR review plus validator update |
| Case policy | lowercase snake_case |
| Consumer pillars | P06, P09, P10 |
| Drift risk | medium if aliases are allowed |
| Drift mitigation | exact-match validator |
## Example
```yaml
artifact_id: kc_taxonomy_llm_ops
signal_state: enriched
provenance_count: 4
freshness_days: 12
taxonomy_alignment: high
```
## Example Interpretation
| Field | Value | Interpretation |
|-------|-------|----------------|
| artifact_id | kc_taxonomy_llm_ops | knowledge unit under review |
| signal_state | enriched | metadata and provenance are present |
| provenance_count | 4 | gluttonous capture preserved multiple sources |
| freshness_days | 12 | still within expected review window |
| taxonomy_alignment | high | retrieval should trust category placement |
## Integration Notes
| Neighbor artifact | Relationship |
|-------------------|--------------|
| `sch_input_schema_n04.md` | constrains intake field `target_signal_state` |
| `sch_type_def_n04.md` | embeds this enum in typed knowledge records |
| `sch_validator_n04.md` | rejects unknown or impossible transitions |
| `con_rate_limit_config_n04.md` | can prioritize enriched over raw batches |
## Anti-Patterns
| Anti-pattern | Why N04 rejects it |
|--------------|--------------------|
| `status: done` | semantically empty, no retrieval value |
| mixed case labels | causes duplicate buckets in analytics |
| overloading `archived` for low quality | hides whether a fact is old or bad |
| deleting contested states | destroys conflict memory that N04 should study |
## Change Policy
| Event | Required action |
|-------|-----------------|
| new lifecycle stage needed | add value here, update input schema and validator |
| state renamed | provide migration map and deprecation window |
| retrieval semantics changed | update rate, path, and freshness configs together |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_lifecycle_rule]] | related | 0.30 |
| [[p01_kc_schema_validation]] | upstream | 0.24 |
| [[bld_architecture_validator]] | downstream | 0.24 |
| [[agent_card_n04]] | upstream | 0.24 |
| [[bld_architecture_api_reference]] | downstream | 0.24 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.23 |
| [[self_audit_n04_codex_2026_04_15]] | downstream | 0.23 |
| [[bld_architecture_legal_vertical]] | downstream | 0.22 |
| [[bld_architecture_healthcare_vertical]] | downstream | 0.22 |
| [[bld_knowledge_card_enum_def]] | upstream | 0.22 |
