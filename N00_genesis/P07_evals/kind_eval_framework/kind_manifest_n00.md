---
id: n00_eval_framework_manifest
kind: knowledge_card
8f: F3_inject
pillar: P07
nucleus: n00
title: "Eval Framework -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, eval_framework, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_integration_guide
  - bld_schema_eval_framework
  - bld_schema_benchmark_suite
  - bld_schema_eval_metric
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_scoring_rubric
  - bld_schema_search_strategy
  - bld_schema_nps_survey
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Eval framework defines an end-to-end evaluation framework integration configuration specifying how CEX connects to external evaluation platforms (HELM, EleutherAI lm-evaluation-harness, OpenAI Evals, Braintrust) or runs custom internal evaluations. It covers adapter configuration, metric collection, result storage, and reporting pipeline. The framework artifact is the integration layer that makes individual evals composable and automated.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `eval_framework` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Framework name + "Integration" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| framework_name | string | yes | External framework name (HELM, lm-eval, Braintrust, etc.) |
| adapter_type | enum | yes | native / api / cli / custom |
| supported_eval_kinds | list | yes | CEX eval kinds this framework can run |
| result_format | enum | yes | json / csv / wandb / mlflow |
| ci_integration | bool | yes | Whether results are checked in CI |

## When to use
- Integrating CEX evals with a standardized external framework for reproducibility
- Setting up automated eval runs in CI/CD for continuous quality monitoring
- Connecting benchmark results to an experiment tracking platform

## Builder
`archetypes/builders/eval_framework-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind eval_framework --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations integrates; N01 intelligence configures
- `{{SIN_LENS}}` -- Gating Wrath: automated quality enforcement at every commit
- `{{TARGET_AUDIENCE}}` -- ML engineers and CI/CD pipeline consuming eval results
- `{{DOMAIN_CONTEXT}}` -- framework ecosystem, eval scope, CI integration requirements

## Example (minimal)
```yaml
---
id: eval_framework_cex_braintrust
kind: eval_framework
pillar: P07
nucleus: n05
title: "CEX -- Braintrust Eval Framework Integration"
version: 1.0
quality: null
---
framework_name: Braintrust
adapter_type: api
result_format: json
ci_integration: true
supported_eval_kinds: [benchmark, unit_eval, smoke_eval, llm_judge]
```

## Related kinds
- `benchmark_suite` (P07) -- suite executed via this framework
- `experiment_tracker` (P07) -- stores results produced by the framework
- `trace_config` (P07) -- observability for framework execution

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | upstream | 0.41 |
| [[bld_schema_eval_framework]] | upstream | 0.40 |
| [[bld_schema_benchmark_suite]] | upstream | 0.39 |
| [[bld_schema_eval_metric]] | upstream | 0.39 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_scoring_rubric]] | upstream | 0.36 |
| [[bld_schema_search_strategy]] | upstream | 0.36 |
| [[bld_schema_nps_survey]] | upstream | 0.36 |
| [[bld_schema_dataset_card]] | upstream | 0.36 |
