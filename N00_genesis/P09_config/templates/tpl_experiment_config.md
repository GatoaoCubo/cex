---
id: p09_ec_{{EXPERIMENT_SLUG}}
kind: experiment_config
8f: F7_govern
pillar: P09
version: 1.0.0
title: "Experiment: {{EXPERIMENT_NAME}}"
tags: [template, experiment, ab-test, prompt-opt, {{DOMAIN_TAG}}]
tldr: "{{ONE_SENTENCE_HYPOTHESIS_AND_VARIANT_SPACE}}"
quality: {{QUALITY_8_TO_10}}
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AUTHOR}}
domain: "experimentation"
density_score: {{0.80_TO_1.00}}
---

# Experiment: {{EXPERIMENT_NAME}}

## Hypothesis
{{WHAT_WE_EXPECT_TO_LEARN_OR_PROVE}} -- e.g., "prompt_v2 improves quality_score by >=5% without increasing latency >10%".

## Metadata

| Property | Value |
|----------|-------|
| Name | `{{EXPERIMENT_NAME}}` |
| Type | {{prompt_ab \| model_comparison \| temperature_sweep \| bandit \| holdback}} |
| Owner | {{TEAM_OR_NUCLEUS}} |
| Status | {{draft \| running \| paused \| concluded}} |
| Start | {{ISO_DATE}} |
| End | {{ISO_DATE_OR_min_sample_size}} |

## Variants

| ID | Label | Spec | Traffic % |
|----|-------|------|-----------|
| control | {{baseline_name}} | {{prompt_id / model_id / params}} | {{50}} |
| variant_a | {{alt_name}} | {{prompt_id / model_id / params}} | {{50}} |
| variant_b | {{optional}} | {{...}} | {{0}} |

Variants MUST be mutually exclusive. Min 2. Max 5 recommended.

## Traffic Allocation
- **Strategy**: {{fixed_split \| thompson_sampling \| epsilon_greedy}}
- **Assignment key**: {{user_id \| session_id \| request_id}}
- **Mutual exclusion group**: {{group_id_or_none}}
- **Sticky**: {{true \| false}} (same user always sees same variant)

## Metrics

| Role | Metric | Direction | Source |
|------|--------|-----------|--------|
| Primary | {{quality_score}} | higher_is_better | {{scoring_rubric_id}} |
| Guardrail | latency_p95_ms | lower_is_better | trace_config |
| Guardrail | cost_per_request_usd | lower_is_better | cost_budget |
| Secondary | {{user_satisfaction}} | higher_is_better | {{hitl_config}} |

## Success Criteria

| Criterion | Threshold |
|-----------|-----------|
| Statistical test | {{welch_t_test \| bayesian \| cuped}} |
| Significance level | p < {{0.05}} |
| Minimum effect size | {{5}}% relative lift |
| Minimum sample size | {{N_PER_VARIANT}} (power=0.8) |
| Max duration | {{14d}} |
| Stop-early rule | {{sequential_testing_alpha_spending \| none}} |

## Guardrails
- DO NOT ship if any guardrail metric degrades >{{10}}%
- DO NOT peek at results before min_sample_size reached (unless sequential)
- DO NOT run concurrent experiments on the same traffic pool without mutual exclusion

## Rollout on Win
- {{promote_variant_to_default}}
- {{archive_losing_variants_to_learning_record}}
- {{update_prompt_version_or_model_config}}

## Quality Gate
- [ ] Hypothesis stated (not just "test X vs Y")
- [ ] Variants mutually exclusive, sum of traffic = 100%
- [ ] Primary metric + >=1 guardrail defined
- [ ] Success criteria include p-value, effect size, sample size
- [ ] Rollout plan defined for both win and loss outcomes
