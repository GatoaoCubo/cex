---
id: n00_experiment_tracker_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Experiment Tracker -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, experiment_tracker, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_experiment_config
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_eval_metric
  - bld_schema_integration_guide
  - bld_schema_thinking_config
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Experiment tracker defines the configuration and results schema for tracking controlled experiments comparing model versions, prompt variants, or system configurations. It captures hypothesis, experimental variables, control/treatment setup, metric results, and statistical significance. Experiment tracker artifacts enable reproducible research and informed model selection decisions.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `experiment_tracker` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Experiment name + version |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| hypothesis | string | yes | Testable prediction being evaluated |
| control | object | yes | Control configuration (model, prompt, config) |
| treatments | list | yes | Treatment configurations to compare against control |
| metrics | list | yes | Eval metrics tracked for each run |
| results | object | no | Populated after experiment completion |
| conclusion | string | no | Decision and rationale from experiment results |

## When to use
- Comparing two LLM models for a nucleus role before committing to one
- Testing a prompt variant against the current production prompt
- Tracking the results of a hyperparameter sweep for a fine-tuned model

## Builder
`archetypes/builders/experiment_tracker-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind experiment_tracker --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence runs experiments; N07 orchestrator reviews conclusions
- `{{SIN_LENS}}` -- Analytical Envy: rigorous controls, statistical validity
- `{{TARGET_AUDIENCE}}` -- ML engineers and architects making model selection decisions
- `{{DOMAIN_CONTEXT}}` -- experiment domain, available compute, decision deadline

## Example (minimal)
```yaml
---
id: experiment_tracker_sonnet_vs_opus_n01
kind: experiment_tracker
pillar: P07
nucleus: n01
title: "Sonnet vs Opus for N01 Intelligence -- Experiment"
version: 1.0
quality: null
---
hypothesis: "claude-sonnet-4-6 matches opus-4-6 quality at 60% cost for N01 tasks"
control: {model: opus-4-6, nucleus: n01}
treatments:
  - {model: claude-sonnet-4-6, nucleus: n01}
metrics: [artifact_quality_score, cost_per_run_usd, p50_latency_ms]
```

## Related kinds
- `benchmark` (P07) -- provides the measurement framework for each experiment run
- `regression_check` (P07) -- checks that experiment winner doesn't regress in production
- `eval_dataset` (P07) -- test data used across control and treatment runs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_experiment_config]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.39 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.37 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
| [[bld_schema_eval_metric]] | upstream | 0.36 |
| [[bld_schema_integration_guide]] | upstream | 0.36 |
| [[bld_schema_thinking_config]] | upstream | 0.36 |
| [[bld_schema_sandbox_spec]] | upstream | 0.36 |
