---
id: n00_prompt_version_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Prompt Version -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, prompt_version, p03, n00, archetype, template]
density_score: 0.98
related:
  - prompt-version-builder
  - bld_schema_prompt_version
  - p03_sp_prompt_version_builder
  - bld_architecture_prompt_version
  - bld_schema_multimodal_prompt
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_examples_prompt_version
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prompt_version is an immutable versioned snapshot of a prompt artifact at a specific point in time, capturing the exact text, variables, quality score, and performance metrics that were active during a production run. It enables regression detection, A/B comparison, and rollback when prompt changes degrade quality. The output is a versioned prompt record that serves as the ground truth for that artifact's historical behavior.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prompt_version` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| parent_prompt_id | string | yes | ID of the prompt_template this version derives from |
| snapshot_date | date | yes | When this version was captured |
| quality_score | float | no | Quality score at time of snapshot |
| change_summary | string | no | What changed from prior version |

## When to use
- When committing a prompt_template or system_prompt to production after validation
- When running A/B tests between prompt variants that need isolated version records
- When the prompt_optimizer produces an improved version that must be tracked separately

## Builder
`archetypes/builders/prompt_version-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prompt_version --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: pv_cold_email_v2_20260415
kind: prompt_version
pillar: P03
nucleus: n02
title: "Cold Email Template v2 Snapshot"
version: 2.0
quality: 8.7
---
parent_prompt_id: tpl_cold_email_outreach
snapshot_date: "2026-04-15"
quality_score: 8.7
change_summary: "Added urgency hook, reduced length by 30%, improved CTA specificity"
```

## Related kinds
- `prompt_template` (P03) -- parent artifact that prompt_version snapshots
- `prompt_optimizer` (P03) -- tool that generates new versions from optimization runs
- `benchmark` (P07) -- performance measurement that justifies version promotion
- `regression_check` (P11) -- comparison that detects when a new version underperforms

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-version-builder]] | related | 0.49 |
| [[bld_schema_prompt_version]] | downstream | 0.44 |
| [[p03_sp_prompt_version_builder]] | related | 0.44 |
| [[bld_architecture_prompt_version]] | downstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.39 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_search_strategy]] | downstream | 0.38 |
| [[bld_examples_prompt_version]] | downstream | 0.38 |
