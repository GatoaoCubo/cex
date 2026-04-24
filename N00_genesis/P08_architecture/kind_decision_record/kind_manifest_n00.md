---
id: n00_decision_record_manifest
kind: knowledge_card
8f: F3_inject
pillar: P08
nucleus: n00
title: "Decision Record -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, decision_record, p08, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_decision_record
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_schema_action_paradigm
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A decision_record (ADR -- Architecture Decision Record) captures the context, decision, and consequences of a significant architectural or operational choice. It makes the reasoning behind system design permanent and searchable so that future builders and nuclei do not re-litigate settled decisions or make changes that violate established constraints.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `decision_record` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable decision summary |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| status | enum | yes | proposed \| accepted \| deprecated \| superseded |
| context | string | yes | What forces led to this decision |
| decision | string | yes | The specific choice made |
| consequences | string | yes | Trade-offs and impacts of the decision |
| alternatives | list | no | Options considered and rejected |
| supersedes | string | no | ID of decision_record this replaces |
| date | date | no | When decision was made |

## When to use
- Recording why a specific model tier, routing strategy, or tool was selected
- Documenting why a simpler alternative was rejected
- Preserving institutional knowledge about architectural constraints

## Builder
`archetypes/builders/decision_record-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind decision_record --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: dr_opus_all_nuclei
kind: decision_record
pillar: P08
nucleus: n07
title: "Use Opus for all nuclei (not downgraded)"
version: 1.0
quality: null
---
status: accepted
context: Sensitive code generation; quality regressions observed with Sonnet
decision: All N01-N07 default to claude-opus-4-6 at 1M context
consequences: Higher cost per dispatch; quality ceiling raised
```

## Related kinds
- `invariant` (P08) -- operational laws that encode accepted decisions as constraints
- `naming_rule` (P08) -- naming decisions captured as enforceable rules
- `component_map` (P08) -- documents the architectural topology decisions produce

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_decision_record]] | upstream | 0.55 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_search_strategy]] | upstream | 0.44 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
| [[bld_schema_action_paradigm]] | upstream | 0.42 |
| [[bld_schema_quickstart_guide]] | upstream | 0.41 |
