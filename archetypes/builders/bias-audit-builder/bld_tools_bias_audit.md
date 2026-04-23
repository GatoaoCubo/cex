---
kind: tools
id: bld_tools_bias_audit
pillar: P04
llm_function: CALL
purpose: Tools available for bias_audit production
quality: 8.9
title: "Tools Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, tools]
tldr: "Tools available for bias_audit production"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_bias_audit
  - bld_instruction_bias_audit
  - bld_collaboration_bias_audit
  - bias-audit-builder
  - kc_bias_audit
  - p03_sp_bias_audit_builder
  - audit-log-builder
  - p10_lr_bias_audit_builder
  - bld_examples_bias_audit
  - bld_knowledge_card_bias_audit
---

## Production Tools

This ISO drives a bias audit: measuring fairness across demographic slices.
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Aggregates audit data from multiple sources | Pre-audit setup |
| cex_score.py | Quantifies bias metrics using statistical models | During audit execution |
| cex_retriever.py | Fetches training/test data for analysis | Pre-audit data collection |
| cex_doctor.py | Diagnoses inconsistent or missing audit inputs | Pre-audit validation |
| cex_analyzer.py | Identifies biased patterns in model outputs | During audit execution |
| cex_reporter.py | Generates bias audit summaries and visualizations | Post-audit completion |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| val_checker.py | Validates audit tool inputs/outputs for consistency | Pre/post audit |
| val_crosschecker.py | Cross-references results with external benchmarks | Post-audit |
| val_profiler.py | Profiles data distribution for fairness gaps | Pre-audit |
| val_validator.py | Ensures compliance with regulatory fairness standards | Post-audit |

## External References
- Fairlearn (Microsoft): Framework for mitigating algorithmic bias
- IBM AI Fairness 360: Open-source toolkit for bias detection
- TensorFlow Data Validation: For data quality and bias analysis

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_bias_audit]] | downstream | 0.40 |
| [[bld_instruction_bias_audit]] | upstream | 0.37 |
| [[bld_collaboration_bias_audit]] | downstream | 0.37 |
| [[bias-audit-builder]] | downstream | 0.35 |
| [[kc_bias_audit]] | upstream | 0.34 |
| [[p03_sp_bias_audit_builder]] | upstream | 0.33 |
| [[audit-log-builder]] | downstream | 0.31 |
| [[p10_lr_bias_audit_builder]] | downstream | 0.30 |
| [[bld_examples_bias_audit]] | downstream | 0.30 |
| [[bld_knowledge_card_bias_audit]] | upstream | 0.28 |
