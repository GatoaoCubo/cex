---
id: n00_learning_record_manifest
kind: knowledge_card
8f: F3_inject
pillar: P10
nucleus: n00
title: "Learning Record -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, learning_record, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_pitch_deck
  - bld_schema_action_paradigm
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A learning_record captures what worked and what failed during a build or inference session so that future runs can avoid repeating mistakes and amplify successes. It is the primary mechanism by which CEX accumulates operational intelligence, feeding the self-improvement loop and quality feedback flywheel.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `learning_record` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| session_id | string | yes | Session or wave that produced this learning |
| nucleus | string | yes | Nucleus that learned this |
| outcome | enum | yes | success \| failure \| partial |
| pattern | string | yes | What pattern was discovered (the insight) |
| evidence | string | yes | Concrete evidence supporting the pattern |
| applies_to | array | no | Kinds or tasks this learning applies to |
| decay_rate | float | no | Learning decay rate (0.0 = permanent, 1.0 = session-only) |

## When to use
- After any 8F pipeline run that produced notable successes or failures
- When a quality gate fails -- record why before retrying
- During /consolidate to capture wave-level learnings before archiving

## Builder
`archetypes/builders/learning_record-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind learning_record --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: lr_n05_2026_04_17_001
kind: learning_record
pillar: P10
nucleus: n05
title: "Example Learning Record"
version: 1.0
quality: null
---
# Learning: BM25 index rebuild required after new pillar
outcome: failure
pattern: Knowledge index misses new P10 artifacts if rebuild not triggered
evidence: cex_retriever returned 0 results for compression_config kind
applies_to: [knowledge_index, cex_retriever.py]
```

## Related kinds
- `reward_signal` (P11) -- quality signal that triggers learning record creation
- `agent_grounding_record` (P10) -- provenance record that learning records may reference
- `self_improvement_loop` (P11) -- consumes learning records to drive evolution

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.44 |
| [[bld_schema_dataset_card]] | upstream | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.43 |
| [[bld_schema_search_strategy]] | upstream | 0.43 |
| [[bld_schema_pitch_deck]] | upstream | 0.42 |
| [[bld_schema_action_paradigm]] | upstream | 0.42 |
| [[bld_schema_sandbox_spec]] | upstream | 0.42 |
