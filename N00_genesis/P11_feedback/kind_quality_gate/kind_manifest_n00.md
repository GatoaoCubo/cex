---
id: n00_quality_gate_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Quality Gate -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, quality_gate, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_bugloop
  - bld_schema_usage_report
  - bld_schema_scoring_rubric
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_voice_pipeline
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A quality_gate defines a pass/fail barrier with a numeric score threshold that an artifact must exceed before being published, committed, or passed to the next pipeline stage. It is the enforcement mechanism for the CEX 8.0 floor / 9.0 target quality standard, preventing low-quality artifacts from propagating through the pipeline.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `quality_gate` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| gate_name | string | yes | Short name for the gate (e.g. F7_govern) |
| applies_to | array | yes | Kinds or nuclei this gate applies to |
| min_score | float | yes | Minimum score to pass (floor: 8.0) |
| target_score | float | yes | Target score (standard: 9.0) |
| dimensions | array | yes | Quality dimensions scored (D1-D5 or custom) |
| on_fail | enum | yes | retry \| escalate \| block \| human_review |
| max_retries | integer | yes | Maximum retry attempts before escalation |

## When to use
- When enforcing quality standards at F7 GOVERN in the 8F pipeline
- When configuring automated quality enforcement for artifact publication
- When setting domain-specific quality thresholds for different kinds

## Builder
`archetypes/builders/quality_gate-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind quality_gate --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: qg_f7_standard_gate
kind: quality_gate
pillar: P11
nucleus: n00
title: "Example Quality Gate"
version: 1.0
quality: null
---
# Quality Gate: F7 Standard (8F Pipeline)
gate_name: F7_govern
applies_to: [all]
min_score: 8.0
target_score: 9.0
dimensions: [structural, rubric, semantic]
on_fail: retry
max_retries: 2
```

## Related kinds
- `reward_signal` (P11) -- signal emitted when gate passes or fails
- `bugloop` (P11) -- auto-fix loop activated when gate fails repeatedly
- `scoring_rubric` (P07) -- rubric that generates the score evaluated by this gate

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[bld_schema_bugloop]] | related | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_scoring_rubric]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_search_strategy]] | upstream | 0.42 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_quickstart_guide]] | upstream | 0.42 |
| [[bld_schema_voice_pipeline]] | upstream | 0.42 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.41 |
