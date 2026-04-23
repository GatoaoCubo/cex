---
quality: 8.4
id: bld_memory_lineage_record
kind: knowledge_card
pillar: P10
title: "Memory: lineage_record Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-22"
author: builder
domain: lineage_record
quality: 8.3
tags: [memory, lineage_record, P10]
llm_function: INJECT
tldr: "Recalled patterns and corrections for lineage_record builder sessions."
density_score: 0.87
related:
  - bld_knowledge_lineage_record
  - bld_schema_lineage_record
  - bld_architecture_lineage_record
  - bld_model_lineage_record
  - bld_prompt_lineage_record
  - bld_tools_lineage_record
  - bld_output_lineage_record
  - bld_eval_lineage_record
  - bld_feedback_lineage_record
  - bld_config_lineage_record
---

# Memory: lineage_record Builder

## Persistent Patterns

| Pattern | Frequency | Gate | Notes |
|---------|-----------|------|-------|
| At least 1 source entity required | HIGH | H06 | Block if missing |
| ISO 8601 timestamps on all entities and activities | HIGH | H07 | Strict format |
| PROV-O vocabulary in derivation relations | HIGH | Domain | W3C standard |
| Agent identified for each activity | HIGH | H08 | Role field required |
| `derived_from` chain must be traceable | MEDIUM | H09 | No orphan nodes |
| Activity type declared (synthesis/curation/validation) | MEDIUM | H10 | From controlled list |

## Common Corrections

| Mistake | Correction | Teach? |
|---------|-----------|--------|
| User conflates with audit_log | Redirect: audit_log is compliance events; lineage_record is knowledge provenance | YES |
| User conflates with citation | Teach: citation is in-text ref; lineage_record is full derivation chain | YES |
| User omits timestamps | Block: add timestamps or mark as unknown with explicit note | YES |
| User lists agents without roles | Add role field: synthesizer, curator, validator | YES |
| `sources_count` mismatch | Recount and correct frontmatter field | NO |
| Missing derivation relation type | Add: derived_from / quoted_from / transformed_from / aggregated_from | YES |

## PROV-O Vocabulary Reference

| PROV-O Term | CEX Mapping | Required? |
|-------------|-------------|-----------|
| `prov:Entity` | source or derived artifact | YES |
| `prov:Activity` | transformation step | YES |
| `prov:Agent` | nucleus or human actor | YES |
| `prov:wasDerivedFrom` | entity-to-entity relation | YES |
| `prov:wasGeneratedBy` | entity-to-activity relation | RECOMMENDED |
| `prov:wasAssociatedWith` | activity-to-agent relation | RECOMMENDED |
| `prov:used` | activity consumed input | OPTIONAL |

## Session-Invariant Rules

- Every lineage_record has exactly one terminal entity (the artifact being tracked).
- Derivation chains must be acyclic (DAG shape).
- Agent `nucleus` field must match a valid N00-N07 identifier or `human`.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_lineage_record]] | sibling | 0.46 |
| [[bld_schema_lineage_record]] | sibling | 0.44 |
| [[bld_architecture_lineage_record]] | sibling | 0.42 |
| [[bld_model_lineage_record]] | sibling | 0.40 |
| [[bld_prompt_lineage_record]] | sibling | 0.38 |
| [[bld_tools_lineage_record]] | sibling | 0.36 |
| [[bld_output_lineage_record]] | sibling | 0.34 |
| [[bld_eval_lineage_record]] | sibling | 0.32 |
| [[bld_feedback_lineage_record]] | sibling | 0.30 |
| [[bld_config_lineage_record]] | sibling | 0.28 |
