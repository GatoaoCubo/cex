---
id: n00_ab_test_config_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "A/B Test Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, ab_test_config, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_benchmark_suite
  - bld_schema_nps_survey
  - bld_schema_dataset_card
  - bld_schema_experiment_config
  - bld_schema_integration_guide
  - bld_schema_eval_metric
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An ab_test_config defines an A/B experiment for conversion optimization, specifying variants, traffic allocation, success metrics, and statistical significance thresholds. It governs how CEX tests different prompt templates, landing pages, pricing tiers, or agent behaviors against each other to discover which variant maximizes the target metric.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `ab_test_config` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| experiment_name | string | yes | Short identifier for the experiment |
| variants | array | yes | List of variants with IDs and traffic weights |
| primary_metric | string | yes | Conversion metric being optimized |
| secondary_metrics | array | no | Supporting metrics to track |
| significance_threshold | float | yes | p-value required to declare winner (e.g. 0.05) |
| min_sample_size | integer | yes | Minimum observations per variant |
| duration_days | integer | yes | Maximum experiment run duration |

## When to use
- When testing prompt variants for conversion rate improvement
- When comparing pricing tier designs for revenue optimization
- When evaluating agent behavior changes against a baseline

## Builder
`archetypes/builders/ab_test_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind ab_test_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ab_landing_page_cta_001
kind: ab_test_config
pillar: P11
nucleus: n06
title: "Example A/B Test Config"
version: 1.0
quality: null
---
# A/B Test: CTA Button Copy
experiment_name: cta_copy_v1
variants: [{id: control, weight: 0.5}, {id: treatment, weight: 0.5}]
primary_metric: click_through_rate
significance_threshold: 0.05
min_sample_size: 500
duration_days: 14
```

## Related kinds
- `reward_signal` (P11) -- quality signal that ab_test data feeds into
- `content_monetization` (P11) -- monetization pipeline that may run A/B variants
- `nps_survey` (P11) -- survey that may measure qualitative response to variants

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.48 |
| [[bld_schema_usage_report]] | upstream | 0.46 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.46 |
| [[bld_schema_benchmark_suite]] | upstream | 0.46 |
| [[bld_schema_nps_survey]] | upstream | 0.45 |
| [[bld_schema_dataset_card]] | upstream | 0.45 |
| [[bld_schema_experiment_config]] | upstream | 0.45 |
| [[bld_schema_integration_guide]] | upstream | 0.45 |
| [[bld_schema_eval_metric]] | upstream | 0.45 |
| [[bld_schema_search_strategy]] | upstream | 0.44 |
