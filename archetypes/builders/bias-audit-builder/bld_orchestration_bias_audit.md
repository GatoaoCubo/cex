---
kind: collaboration
id: bld_collaboration_bias_audit
pillar: P12
llm_function: COLLABORATE
purpose: How bias_audit-builder works in crews with other builders
quality: 8.9
title: "Collaboration Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, collaboration]
tldr: "How bias_audit-builder works in crews with other builders"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bias-audit-builder
  - kc_bias_audit
  - bld_tools_bias_audit
  - p03_sp_bias_audit_builder
  - p10_lr_bias_audit_builder
  - bld_architecture_bias_audit
  - bld_examples_bias_audit
  - bld_instruction_bias_audit
  - bld_output_template_bias_audit
  - bld_knowledge_card_bias_audit
---

## Crew Role  

This ISO drives a bias audit: measuring fairness across demographic slices.
Audits models and datasets for bias, analyzes fairness metrics, and generates actionable bias mitigation recommendations. Collaborates with data preprocessors and model evaluators to ensure equitable outcomes.  

## Receives From  
| Builder        | What                  | Format      |  
|----------------|-----------------------|-------------|  
| data_preprocessor | Raw dataset           | CSV/JSON    |  
| model_evaluator   | Model predictions     | JSON        |  
| fairness_spec     | Bias criteria         | YAML        |  

## Produces For  
| Builder        | What                        | Format      |  
|----------------|-----------------------------|-------------|  
| report_generator | Bias audit report           | PDF/Markdown|  
| model_evaluator  | Fairness metric breakdown   | JSON        |  
| mitigation_team  | Mitigation action plan      | YAML        |  

## Boundary  
Does NOT handle benchmarking (use `benchmark_builder`) or define single evaluation metrics (use `eval_metric_builder`). Data preprocessing is handled by `data_preprocessor`.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bias-audit-builder]] | upstream | 0.48 |
| [[kc_bias_audit]] | upstream | 0.45 |
| [[bld_tools_bias_audit]] | upstream | 0.44 |
| [[p03_sp_bias_audit_builder]] | upstream | 0.36 |
| [[p10_lr_bias_audit_builder]] | upstream | 0.36 |
| [[bld_architecture_bias_audit]] | upstream | 0.35 |
| [[bld_examples_bias_audit]] | upstream | 0.35 |
| [[bld_instruction_bias_audit]] | upstream | 0.35 |
| [[bld_output_template_bias_audit]] | upstream | 0.28 |
| [[bld_knowledge_card_bias_audit]] | upstream | 0.27 |
