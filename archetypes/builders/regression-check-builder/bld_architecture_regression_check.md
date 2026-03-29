---
kind: architecture
id: bld_architecture_regression_check
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of regression_check — inventory, dependencies, and architectural position
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
| From | To | Type | Data |
|------|----|------|------|
| eval_dataset | baseline_ref | produces | scored experiment snapshot used as reference |
| eval_dataset | metrics | produces | measured dimensions available for comparison |
| baseline_ref | comparison_mode | depends | reference point for delta calculation |
| threshold | comparison_mode | depends | acceptable deviation boundary |
| metrics | comparison_mode | depends | dimensions fed into deviation calculation |
| comparison_mode | fail_action | produces | pass/fail signal per metric |
| fail_action | guardrail | depends | deployment gate receives block/warn/log signal |
| fail_action | notify | depends | alert system receives regression report |
| guardrail | ci_pipeline | depends | CI/CD gate enforces block on pipeline |
| agent | metrics | depends | agent runtime requests metric evaluation |

## Boundary Table
| regression_check IS | regression_check IS NOT |
|--------------------|------------------------|
| Compares current vs a named baseline_ref | Measures absolute performance without comparison (benchmark) |
| Detects relative or absolute deviation from known-good | Tests isolated correctness of a single input (unit_eval) |
| Config for framework execution (Braintrust, Promptfoo, etc.) | Validates one specific reference case (golden_test) |
| Runtime gate for deploy or PR pipeline | Rapid sanity check without baseline (smoke_eval) |
| Governs deployment decisions via fail_action | Generates training data or fine-tuning signals |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| reference | baseline_ref, eval_dataset | Supply the known-good comparison point |
| comparison | threshold, comparison_mode, metrics | Define what to measure and how much deviation is acceptable |
| response | fail_action, notify | Define what happens when regression is detected |
| scheduling | cadence, scope | Define when and on what system the check runs |
| governance | guardrail, ci_pipeline | Enforce deployment decisions based on check output |
| callers | agent, ci_pipeline | Runtime consumers that invoke the check |
