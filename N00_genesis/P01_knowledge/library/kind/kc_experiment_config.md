---
id: p01_kc_experiment_config
kind: knowledge_card
type: kind
pillar: P09
title: "experiment_config: A/B Testing and Prompt Experimentation"
version: 1.0.0
created: 2026-04-12
updated: 2026-04-12
author: n03_builder
domain: experiment_config
quality: 9.1
tags: [experiment_config, P09, GOVERN, kind-kc]
tldr: "experiment_config defines A/B tests on prompts, models, or parameters -- with variants, traffic splits, metrics, and statistical success criteria -- enabling data-driven prompt optimization."
when_to_use: "Building, reviewing, or reasoning about experiment_config artifacts"
keywords: [ab_testing, prompt_experiment, multi_armed_bandit]
feeds_kinds: [experiment_config]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
related:
  - experiment-config-builder
  - p03_sp_experiment_config_builder
  - p11_qg_experiment_config
  - bld_knowledge_card_experiment_config
  - bld_collaboration_experiment_config
  - bld_architecture_experiment_config
  - bld_instruction_experiment_config
  - bld_schema_experiment_config
  - p10_lr_experiment_config_builder
  - bld_examples_experiment_config
---

# Experiment Config

## Spec
```yaml
kind: experiment_config
pillar: P09
llm_function: GOVERN
max_bytes: 4096
naming: p09_ec_{{name}}.yaml
core: false
```

## What It Is
An experiment_config is a structured configuration for running controlled experiments -- A/B tests on prompts, model comparisons, parameter sweeps, or multi-armed bandit explorations -- with explicit variants, traffic allocation, metrics, duration, and statistical success criteria. It is NOT a feature_flag (binary on/off toggle without metrics), NOT a benchmark (one-time static evaluation without traffic splitting), NOT a scoring_rubric (quality criteria without experimentation logic).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| Statsig | `Experiment` config | Variants, metrics, traffic allocation, statistical significance |
| LaunchDarkly | `Experiment` + `Metric` | Feature flag experiments with metric binding |
| Eppo | `Experiment Assignment` | Randomized assignment with Bayesian analysis |
| GrowthBook | `Experiment` + `Metric` | SDK-integrated experiments with auto-analysis |
| DSPy | `BootstrapFewShotWithRandomSearch` | Prompt optimization via random variant search |
| Anthropic | `messages` API multi-call | Compare model/temperature variants manually |
| PromptLayer | `A/B Test` | Prompt versioning with traffic splitting |
| Weights & Biases | `Sweep` config | Hyperparameter sweeps with Bayesian optimization |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| experiment_name | string | required | Descriptive kebab-case -- uniqueness prevents cross-contamination |
| variants | list[variant] | required | Min 2 variants -- more variants = slower convergence but broader search |
| metric | string | required | Primary success metric (latency, quality_score, cost, user_satisfaction) |
| traffic_split | map | equal | Percentage per variant -- unequal splits accelerate winner detection |
| duration | duration | required | Too short = noise; too long = opportunity cost |
| success_criteria | object | required | p-value threshold, minimum effect size, confidence interval |
| min_sample_size | int | null | Statistical power -- higher = more reliable but slower |
| guardrail_metrics | list | [] | Secondary metrics that must not degrade (safety net) |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Prompt A/B test | Compare 2 prompt templates on quality | `variant_a: template_v1`, `variant_b: template_v2`, metric: `quality_score` |
| Model comparison | Evaluate model upgrade impact | `variant_a: sonnet-4-5`, `variant_b: opus-4-6`, metric: `latency + quality` |
| Temperature sweep | Find optimal temperature for task | `variants: [0.0, 0.3, 0.7, 1.0]`, metric: `output_diversity` |
| Multi-armed bandit | Dynamic traffic allocation to winner | `strategy: thompson_sampling`, auto-shift traffic to best variant |
| Holdback experiment | Measure feature lift vs. control | `control: 10%`, `treatment: 90%`, metric: `conversion_rate` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No success criteria | Experiment runs forever, no decision point | Define p-value, min effect size, max duration upfront |
| Too many variants | Splits traffic too thin, convergence takes months | Max 4-5 variants; use sequential testing for large search spaces |
| No guardrail metrics | Winner on primary metric degrades safety/cost | Always define 1-2 guardrails (cost, latency, error_rate) |
| Peeking at results | Checking significance daily inflates false positive rate | Use sequential testing or fixed-horizon with pre-set checkpoints |
| Shared traffic pool | Overlapping experiments contaminate each other | Isolate experiments by user segment or use mutual exclusion groups |

## Integration Graph
```
prompt_template, model_provider --> [experiment_config] --> scoring_rubric, benchmark
                                          |
                                    feature_flag, cost_budget, learning_record
```

## Decision Tree
- IF comparing 2+ prompt variants with statistical rigor THEN experiment_config
- IF simple on/off capability toggle THEN feature_flag
- IF one-time model evaluation THEN benchmark
- IF quality scoring criteria without experimentation THEN scoring_rubric
- DEFAULT: experiment_config when you need data-driven decisions with statistical confidence

## Quality Criteria
- GOOD: experiment_name, variants (2+), metric, success_criteria all present
- GREAT: guardrail_metrics defined, min_sample_size calculated, duration bounded, mutual exclusion documented
- FAIL: no success_criteria, single variant, no metric, unbounded duration

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[experiment-config-builder]] | related | 0.47 |
| [[p03_sp_experiment_config_builder]] | upstream | 0.44 |
| [[p11_qg_experiment_config]] | downstream | 0.41 |
| [[bld_knowledge_card_experiment_config]] | sibling | 0.40 |
| [[bld_collaboration_experiment_config]] | downstream | 0.38 |
| [[bld_architecture_experiment_config]] | upstream | 0.36 |
| [[bld_instruction_experiment_config]] | upstream | 0.35 |
| [[bld_schema_experiment_config]] | upstream | 0.34 |
| [[p10_lr_experiment_config_builder]] | downstream | 0.34 |
| [[bld_examples_experiment_config]] | upstream | 0.34 |
