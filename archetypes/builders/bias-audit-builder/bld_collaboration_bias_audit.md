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
