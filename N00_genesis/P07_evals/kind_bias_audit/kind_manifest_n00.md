---
id: n00_bias_audit_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Bias Audit -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, bias_audit, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_audit_log
  - bld_schema_bias_audit
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_eval_metric
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Bias audit defines the fairness evaluation methodology and results documentation for an LLM system or pipeline. It specifies the protected attributes to test, evaluation metrics (disparate impact, equal opportunity difference), test dataset stratification, and remediation thresholds. Bias audit artifacts serve as evidence for responsible AI compliance and are required before deployment to regulated domains.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `bias_audit` |
| pillar | string | yes | Always `P07` |
| title | string | yes | System name + "Bias Audit" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_system | string | yes | System or model being audited |
| protected_attributes | list | yes | Attributes tested (gender, race, age, etc.) |
| fairness_metrics | list | yes | Metrics used (disparate_impact, EOD, etc.) |
| test_dataset_id | string | yes | ID of the stratified eval dataset used |
| remediation_threshold | float | yes | Max acceptable disparity before remediation required |
| audit_date | date | yes | When the audit was conducted |

## When to use
- Pre-deployment fairness evaluation for a customer-facing AI system
- Annual responsible AI compliance audit for a production model
- Investigating a bias complaint or anomaly detected in production

## Builder
`archetypes/builders/bias_audit-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind bias_audit --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence + N05 operations co-run bias audits
- `{{SIN_LENS}}` -- Analytical Envy: every disparity surfaced, none suppressed
- `{{TARGET_AUDIENCE}}` -- compliance officers, legal teams, AI ethics reviewers
- `{{DOMAIN_CONTEXT}}` -- deployment domain, regulatory requirements, demographic exposure

## Example (minimal)
```yaml
---
id: bias_audit_cex_hiring_assistant
kind: bias_audit
pillar: P07
nucleus: n01
title: "CEX Hiring Assistant -- Bias Audit Q1 2026"
version: 1.0
quality: null
---
target_system: "CEX N01 + resume_screening agent"
protected_attributes: [gender, ethnicity, age_group]
fairness_metrics: [disparate_impact_ratio, equal_opportunity_difference]
remediation_threshold: 0.80
```

## Related kinds
- `red_team_eval` (P07) -- adversarial testing that complements fairness evaluation
- `eval_dataset` (P07) -- stratified test dataset used for the audit
- `guardrail` (P11) -- safety mechanism that may be deployed after audit findings

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_audit_log]] | upstream | 0.48 |
| [[bld_schema_bias_audit]] | upstream | 0.48 |
| [[bld_schema_benchmark_suite]] | upstream | 0.47 |
| [[bld_schema_integration_guide]] | upstream | 0.47 |
| [[bld_schema_dataset_card]] | upstream | 0.46 |
| [[bld_schema_usage_report]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[bld_schema_search_strategy]] | upstream | 0.45 |
| [[bld_schema_eval_metric]] | upstream | 0.45 |
| [[bld_schema_action_paradigm]] | upstream | 0.43 |
