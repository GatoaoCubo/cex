---
kind: tools
id: bld_tools_discovery_questions
pillar: P04
llm_function: CALL
purpose: Tools available for discovery_questions production
quality: 8.9
title: "Tools Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, tools]
tldr: "Tools available for discovery_questions production"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_sales_playbook
  - bld_tools_roi_calculator
  - bld_tools_benchmark_suite
  - bld_tools_churn_prevention_playbook
  - bld_tools_eval_metric
  - bld_tools_competitive_matrix
  - bld_tools_pricing_page
  - bld_tools_legal_vertical
  - bld_tools_api_reference
  - bld_tools_rbac_policy
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact after production | F8 COLLABORATE |
| cex_score.py | Score artifact quality (5D dimensions) | F7 GOVERN |
| cex_retriever.py | Retrieve similar discovery question artifacts | F3 INJECT |
| cex_doctor.py | Validate builder health, ISO completeness | F7 GOVERN |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Structural YAML + frontmatter validation | Post-production |
| cex_hooks.py | Pre-commit ASCII and schema checks | Pre-commit |

## External References
- MEDDIC (Metrics/Economic-Buyer/Decision-Criteria/Decision-Process/Identify-Pain/Champion)
- BANT (Budget/Authority/Need/Timeline) - SiriusDecisions framework
- SPIN Selling - Neil Rackham methodology
- Challenger Sale - Adamson & Dixon framework

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_sales_playbook]] | sibling | 0.52 |
| [[bld_tools_roi_calculator]] | sibling | 0.50 |
| [[bld_tools_benchmark_suite]] | sibling | 0.36 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.35 |
| [[bld_tools_eval_metric]] | sibling | 0.33 |
| [[bld_tools_competitive_matrix]] | sibling | 0.33 |
| [[bld_tools_pricing_page]] | sibling | 0.33 |
| [[bld_tools_legal_vertical]] | sibling | 0.33 |
| [[bld_tools_api_reference]] | sibling | 0.33 |
| [[bld_tools_rbac_policy]] | sibling | 0.32 |
