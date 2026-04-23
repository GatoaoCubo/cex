---
kind: architecture
id: bld_architecture_regression_check
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of regression_check — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Regression Check"
version: "1.0.0"
author: n03_builder
tags: [regression_check, builder, examples]
tldr: "Golden and anti-examples for regression check construction, demonstrating ideal structure and common pitfalls."
domain: "regression check construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_regression_check_builder
  - bld_knowledge_card_regression_check
  - regression-check-builder
  - bld_instruction_regression_check
  - bld_collaboration_regression_check
  - p01_kc_regression_check
  - p11_qg_regression_check
  - bld_schema_regression_check
  - bld_output_template_regression_check
  - bld_examples_regression_check
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| baseline_ref | Pointer to the reference experiment/version to compare against | regression_check | required |
| threshold | Maximum acceptable deviation before triggering failure | regression_check | required |
| metrics | Named dimensions to compare between current and baseline | regression_check | required |
| comparison_mode | How threshold is applied: relative (%) or absolute (fixed delta) | regression_check | required |
| fail_action | Response when regression is detected: block, warn, or log | regression_check | required |
| tool | Framework executing the comparison (Braintrust, Promptfoo, etc.) | regression_check | required |
| cadence | When the check runs: on_pr, on_deploy, daily, on_demand | regression_check | optional |
| notify | Channels or owners alerted on regression detection | regression_check | optional |
| scope | Which prompt, model, or pipeline is under test | regression_check | optional |
| eval_dataset | Dataset used for both baseline and current measurement | P07 | external |
| guardrail | Deployment gate that consumes fail_action output | P11 | external |
| agent | Runtime caller that triggers the comparison check | P02 | consumer |
| ci_pipeline | CI/CD system that invokes check on_pr or on_deploy | external | consumer |

## Dependency Graph
```
eval_dataset    --produces--> baseline_ref
eval_dataset    --produces--> metrics
baseline_ref    --depends-->  comparison_mode
threshold       --depends-->  comparison_mode
metrics         --depends-->  comparison_mode
comparison_mode --produces--> fail_action
fail_action     --depends-->  guardrail
fail_action     --depends-->  notify
guardrail       --depends-->  ci_pipeline
agent           --depends-->  metrics
```

## Boundary Table
| regression_check IS | regression_check IS NOT |
|--------------------|------------------------|
| Compares current vs a named baseline_ref | Measures absolute performance without comparison (benchmark) |
| Detects relative or absolute deviation from known-good | Tests isolated correctness of a single input (unit_eval) |
| Config for framework execution (Braintrust, Promptfoo, etc.) | Validates one specific reference case (golden_test) |
| Runtime gate for deploy or PR pipeline | Rapid sanity check without baseline (smoke_eval) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| reference | baseline_ref, eval_dataset | Supply the known-good comparison point |
| comparison | threshold, comparison_mode, metrics | Define what to measure and acceptable deviation |
| response | fail_action, notify | Define what happens when regression is detected |
| scheduling | cadence, scope | Define when and on what system the check runs |
| governance | guardrail, ci_pipeline | Enforce deployment decisions based on check output |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_regression_check_builder]] | upstream | 0.55 |
| [[bld_knowledge_card_regression_check]] | upstream | 0.50 |
| [[regression-check-builder]] | upstream | 0.49 |
| [[bld_instruction_regression_check]] | upstream | 0.48 |
| [[bld_collaboration_regression_check]] | downstream | 0.46 |
| [[p01_kc_regression_check]] | upstream | 0.45 |
| [[p11_qg_regression_check]] | downstream | 0.44 |
| [[bld_schema_regression_check]] | upstream | 0.43 |
| [[bld_output_template_regression_check]] | upstream | 0.42 |
| [[bld_examples_regression_check]] | upstream | 0.38 |
