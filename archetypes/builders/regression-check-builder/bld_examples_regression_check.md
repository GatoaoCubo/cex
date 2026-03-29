---
kind: examples
id: bld_examples_regression_check
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of regression_check artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: regression-check-builder
## Golden Example
INPUT: "Create regression check for the summarization pipeline comparing against last week's production experiment"
OUTPUT:
```yaml
id: p07_rc_summarization_prod_weekly
kind: regression_check
pillar: P07
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "Summarization Pipeline Weekly Regression"
baseline_ref: "experiment/summarization-prod-2026-03-22"
threshold: 5.0
metrics:
  - accuracy
  - faithfulness
  - latency_p95
  - cost_per_call
quality: null
tags: [regression_check, summarization, production, P07]
tldr: "Weekly regression check for summarization pipeline vs prod baseline. 5% threshold. Blocks deploy on accuracy/faithfulness drop."
description: "Compares current summarization pipeline against last production experiment on accuracy, faithfulness, latency, and cost"
tool: braintrust
comparison_mode: relative
fail_action: block
notify: [ml-team-slack, oncall-pager]
cadence: on_deploy
scope: "summarization-pipeline-v2"
```
## Overview
Weekly regression gate for the summarization pipeline.
Runs on every deployment attempt; blocks release if any metric drops beyond threshold vs the prior production experiment.
## Baseline
**baseline_ref**: `experiment/summarization-prod-2026-03-22`
The production experiment captured on 2026-03-22 after the v2.1 release passed QA. Represents the stable production quality bar.
**Update policy**: Rotate baseline after each successful production deployment. Previous baseline archived with date tag.
## Metrics
### accuracy
- **Definition**: Percentage of summaries rated correct by LLM judge (covers factual accuracy and completeness)
- **Method**: Braintrust LLM-as-judge scorer comparing summary against source document
- **Threshold**: 5.0% relative drop (lower is worse)
- **Direction**: Decrease signals regression
### faithfulness
- **Definition**: Proportion of summary claims grounded in source text (no hallucination)
- **Method**: Braintrust faithfulness scorer using claim decomposition
- **Threshold**: 3.0% relative drop (lower is worse — tighter tolerance than accuracy)
- **Direction**: Decrease signals regression
### latency_p95
- **Definition**: 95th percentile end-to-end latency in milliseconds
- **Method**: Braintrust timing metadata across eval dataset
- **Threshold**: 20.0% relative increase
- **Direction**: Increase signals regression
### cost_per_call
- **Definition**: Average token cost per summarization request in USD
- **Method**: Braintrust cost tracking from model provider billing
- **Threshold**: 15.0% relative increase
- **Direction**: Increase signals regression
## Failure Protocol
- **fail_action**: block
- **Notify**: #ml-team-slack (immediate), oncall-pager (if accuracy or faithfulness fails)
- **Remediation**: Check recent prompt changes, model version updates, and dataset distribution shifts. Review Braintrust diff for failing examples.
- **Escalation**: If not resolved within 2 hours of deploy attempt, escalate to ML lead.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_rc_ pattern (H02 pass)
- kind: regression_check (H04 pass)
- baseline_ref is a concrete experiment ID (H07 pass)
- threshold is numeric > 0 (H08 pass)
- metrics list has 4 items (H09 pass)
- body has all 4 sections: Overview, Baseline, Metrics, Failure Protocol
- per-metric thresholds documented with direction and units
- tool specified (Braintrust) with measurement method per metric
- fail_action: block with notify channels and remediation steps
- baseline update policy defined
- tldr: 130 chars <= 160 (S01 pass)
- tags: 4 items, includes "regression_check" (S02 pass)

## Anti-Example
INPUT: "Create regression check for the chatbot"
BAD OUTPUT:
```yaml
id: chatbot-regression
kind: eval
baseline_ref: previous
threshold: good
quality: 8.5
tags: [regression]
```
Checks if chatbot got worse.
FAILURES:
1. id: "chatbot-regression" has hyphens and no `p07_rc_` prefix -> H02 FAIL
2. kind: "eval" not "regression_check" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. baseline_ref: "previous" is not resolvable — cannot reproduce comparison -> H07 FAIL
5. threshold: "good" is not numeric -> H08 FAIL
6. Missing fields: metrics, pillar, version, created, updated, author, name, tldr -> H06 FAIL
7. tags: only 1 item, missing "regression_check" -> SOFT FAIL
8. Body missing ## Baseline, ## Metrics, ## Failure Protocol sections
9. No metrics defined — nothing to compare -> H09 FAIL
10. No fail_action — regression detected but nothing happens -> SOFT FAIL
