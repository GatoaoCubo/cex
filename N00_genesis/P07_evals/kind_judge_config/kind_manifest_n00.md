---
id: n00_judge_config_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Judge Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, judge_config, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_llm_judge
  - bld_collaboration_llm_judge
  - bld_schema_judge_config
  - llm-judge-builder
  - p01_kc_llm_judge
  - judge-config-builder
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_collaboration_judge_config
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Judge config defines the configuration for an LLM-as-Judge automated evaluation system, specifying which model acts as judge, the judging prompt template, scoring dimensions, calibration dataset, bias mitigation settings, and confidence thresholds. Judge configs enable consistent, scalable automated quality assessment across large artifact volumes without human reviewer bottlenecks.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `judge_config` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Judge name + "Config" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| judge_model | string | yes | Model used as judge (e.g., claude-opus-4-6) |
| judge_prompt_id | string | yes | ID of the prompt_template artifact used for judging |
| scoring_dimensions | list | yes | Dimensions judged with weights |
| calibration_dataset_id | string | yes | Eval dataset used to calibrate judge |
| confidence_threshold | float | yes | Min judge confidence to trust the score |
| position_bias_mitigation | bool | yes | Whether to randomize option order to reduce bias |

## When to use
- Setting up an automated quality review pipeline for high-volume artifact production
- Configuring a judge for a specific eval dimension (helpfulness, accuracy, safety)
- Calibrating a new judge model against human ratings before deployment

## Builder
`archetypes/builders/judge_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind judge_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence designs; N05 operations deploys
- `{{SIN_LENS}}` -- Analytical Envy: calibrated, unbiased, reproducible judgment
- `{{TARGET_AUDIENCE}}` -- automated eval pipelines running quality gates at scale
- `{{DOMAIN_CONTEXT}}` -- eval volume, judge model budget, acceptable error rate

## Example (minimal)
```yaml
---
id: judge_config_cex_quality_gate
kind: judge_config
pillar: P07
nucleus: n01
title: "CEX Quality Gate Judge Config"
version: 1.0
quality: null
---
judge_model: claude-opus-4-6
confidence_threshold: 0.85
position_bias_mitigation: true
scoring_dimensions:
  - {name: structural_completeness, weight: 0.30}
  - {name: semantic_accuracy, weight: 0.40}
  - {name: rubric_compliance, weight: 0.30}
```

## Related kinds
- `llm_judge` (P07) -- the executable artifact; judge_config is its configuration
- `scoring_rubric` (P07) -- defines the criteria that the judge evaluates against
- `golden_test` (P07) -- calibration data used to validate judge accuracy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_llm_judge]] | upstream | 0.49 |
| [[bld_collaboration_llm_judge]] | downstream | 0.47 |
| [[bld_schema_judge_config]] | upstream | 0.46 |
| [[llm-judge-builder]] | related | 0.44 |
| [[p01_kc_llm_judge]] | sibling | 0.44 |
| [[judge-config-builder]] | related | 0.42 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_benchmark_suite]] | upstream | 0.41 |
| [[bld_collaboration_judge_config]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | upstream | 0.40 |
