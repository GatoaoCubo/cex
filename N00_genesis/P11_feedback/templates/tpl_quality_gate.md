---
# TEMPLATE: Quality Gate
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P11_feedback/_schema.yaml (types.quality_gate)
# Max 1024 bytes | density_min: 0.80 | quality_min: 8.0

id: "p11_qg_{{GATE_SLUG}}"
kind: quality_gate
pillar: P11
title: "Gate: {{GATE_NAME}}"
version: 1.0.0
created: "{{ISO_DATE}}"
updated: "{{ISO_DATE}}"
author: "{{AGENT_GROUP_NAME}}"
quality: 8.1
tags: "[{{TAG1}}, {{TAG2}}, quality-gate, feedback]"
tldr: "{{ONE_SENTENCE_WHAT_THIS_GATE_ENFORCES}}"
density_score: "{{0.80_TO_1.00}}"
related:
  - bld_output_template_quality_gate
  - bld_output_template_scoring_rubric
  - bld_examples_quality_gate
  - bld_output_template_experiment_config
  - p07_qg_eval_metric
  - bld_examples_experiment_config
  - p11_qg_function_def
  - p03_qg_prompt_technique
  - bld_knowledge_card_quality_gate
  - p11_qg_incident_report
---

# Gate: {{GATE_NAME}}

## Definition

| Property | Value |
|----------|-------|
| Metric | {{METRIC_NAME}} |
| Threshold | {{NUMERIC_VALUE}} |
| Operator | {{>= / <= / == / !=}} |
| Scope | {{WHERE_GATE_APPLIES}} |

## Actions

| Result | Action | Escalation |
|--------|--------|------------|
| Pass | {{ACTION_ON_PASS}} | {{NONE_OR_NOTIFY}} |
| Fail | {{ACTION_ON_FAIL}} | {{RETRY_OR_BLOCK_OR_ALERT}} |

## Checklist

- [ ] {{CHECK_1}}: {{DESCRIPTION}}
- [ ] {{CHECK_2}}: {{DESCRIPTION}}
- [ ] {{CHECK_3}}: {{DESCRIPTION}}
- [ ] Verifier tool set: Read-only (no Write/Edit — independence required)
- [ ] Stubs check: stubs_count == 0 (existing-but-empty components are bugs, not progress)

## Scoring

| Dimension | Weight | What to Check |
|-----------|--------|---------------|
| {{DIM_1}} | {{PCT}}% | {{CRITERIA}} |
| {{DIM_2}} | {{PCT}}% | {{CRITERIA}} |
| {{DIM_3}} | {{PCT}}% | {{CRITERIA}} |
| Claims vs Reality | 20% | Compare stated deliverables (SUMMARY.md/commit msg) against grep results in actual code |

## Bypass

- Conditions: {{WHEN_GATE_CAN_BE_SKIPPED_OR_never}}
- Approver: {{WHO_CAN_OVERRIDE}}
- Audit: {{HOW_BYPASS_IS_LOGGED}}

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_quality_gate]] | upstream | 0.49 |
| [[bld_output_template_scoring_rubric]] | upstream | 0.23 |
| [[bld_examples_quality_gate]] | upstream | 0.22 |
| [[bld_output_template_experiment_config]] | upstream | 0.22 |
| [[p07_qg_eval_metric]] | sibling | 0.21 |
| [[bld_examples_experiment_config]] | upstream | 0.19 |
| [[p11_qg_function_def]] | sibling | 0.18 |
| [[p03_qg_prompt_technique]] | sibling | 0.18 |
| [[bld_knowledge_card_quality_gate]] | related | 0.17 |
| [[p11_qg_incident_report]] | sibling | 0.17 |
