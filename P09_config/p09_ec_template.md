---
# TEMPLATE: Experiment Config (A/B test)
# Fill {{VARS}} before use | Validate against P09_config/_schema.yaml
# Max 4096 bytes | density_min: 0.85 | quality_min: 9.0

id: p09_ec_{{EXPERIMENT_SLUG}}
kind: experiment_config
pillar: P09
title: "Experiment: {{EXPERIMENT_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_OR_TEAM}}
quality: null
tags: [{{TAG1}}, experiment, ab_test, P09]
tldr: "{{ONE_SENTENCE_HYPOTHESIS_AND_METRIC}}"
density_score: {{0.85_TO_1.00}}
---

# Experiment: {{EXPERIMENT_NAME}}

## Hypothesis

{{WHAT_YOU_EXPECT_AND_WHY}} -- measured by **{{PRIMARY_METRIC}}**.

## Config

| Property | Value |
|----------|-------|
| Experiment ID | `{{EXPERIMENT_SLUG}}` |
| Type | {{prompt_ab / model_ab / param_sweep / bandit}} |
| Owner | {{TEAM_OR_PERSON}} |
| Duration | {{START_ISO}} -> {{END_ISO}} |
| Traffic allocation | {{PERCENT_OF_TRAFFIC}}% of eligible requests |
| Stopping rule | {{FIXED_DURATION / BAYESIAN_WIN / MIN_SAMPLES}} |

## Variants

| Variant | Split | Description | Artifact |
|---------|-------|-------------|----------|
| `control` | {{50}}% | {{BASELINE_DESCRIPTION}} | {{PATH_OR_ID}} |
| `treatment_a` | {{25}}% | {{CHANGE_DESCRIPTION}} | {{PATH_OR_ID}} |
| `treatment_b` | {{25}}% | {{CHANGE_DESCRIPTION}} | {{PATH_OR_ID}} |

## Metrics

| Metric | Role | Direction | Target delta | Guardrail |
|--------|------|-----------|--------------|-----------|
| `{{PRIMARY_METRIC}}` | primary | {{higher_is_better}} | +{{X}}% | -- |
| `{{SECONDARY_METRIC}}` | secondary | {{higher_is_better}} | +{{Y}}% | -- |
| `{{GUARDRAIL_METRIC}}` | guardrail | {{lower_is_better}} | -- | max +{{Z}}% |
| `cost_per_call_usd` | guardrail | lower_is_better | -- | max +10% |

## Success Criteria

- Primary metric lift >= **{{X}}%** with p < **{{0.05}}** (or Bayesian P(winner) >= {{0.95}})
- No guardrail metric regresses beyond its cap
- Minimum sample size: **{{N}}** per variant

## Segmentation

- Include: {{USER_SEGMENTS_OR_NUCLEI}}
- Exclude: {{EXCLUSION_RULES}}
- Randomization unit: {{user_id / request_id / session_id}}

## Analysis

- Tool: {{statsig / growthbook / eppo / custom}}
- Method: {{frequentist_ttest / bayesian / sequential_testing}}
- Review cadence: {{daily / weekly}}

## Rollout

1. Launch at {{START_ISO}} at {{INITIAL_TRAFFIC}}% traffic
2. Ramp to {{FULL_TRAFFIC}}% after {{BURN_IN_PERIOD}} if guardrails hold
3. Winner decision at {{END_ISO}} -- promote to default via {{feature_flag_id}}
4. Losing variants archived to `.cex/experiments/archive/`

## Anti-patterns

- NOT a `feature_flag` (boolean toggle, no metrics)
- NOT a `benchmark` (one-time eval, not live traffic)
- NOT a `regression_check` (regression prevention, not hypothesis testing)
