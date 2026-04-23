---
kind: tools
id: bld_tools_sales_playbook
pillar: P04
llm_function: CALL
purpose: Tools available for sales_playbook production
quality: 8.9
title: "Tools Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, tools]
tldr: "Tools available for sales_playbook production"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_discovery_questions
  - bld_tools_roi_calculator
  - bld_tools_churn_prevention_playbook
  - bld_tools_benchmark_suite
  - bld_tools_pricing_page
  - bld_tools_competitive_matrix
  - bld_tools_customer_segment
  - bld_tools_eval_metric
  - bld_tools_legal_vertical
  - bld_tools_rbac_policy
---

## Production Tools
| Tool | Purpose | When |
|---|---|---|
| cex_compile.py | Compile artifact after production | F8 COLLABORATE |
| cex_score.py | Score artifact quality (5D dimensions) | F7 GOVERN |
| cex_retriever.py | Retrieve similar sales playbook artifacts for reuse | F3 INJECT |
| cex_doctor.py | Validate builder health, ISO completeness | F7 GOVERN |

## Validation Tools
| Tool | Purpose | When |
|---|---|---|
| cex_wave_validator.py | Structural YAML + frontmatter validation | Post-production |
| cex_hooks.py | Pre-commit ASCII and schema checks | Pre-commit |

## External References
- HubSpot Sales Playbook methodology (persona-driven content)
- MEDDPICC qualification framework (Miller Heiman Group)
- Challenger Sale (Adamson & Dixon) - insight-based selling
- Gong.io conversation analytics (close pattern data)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_discovery_questions]] | sibling | 0.54 |
| [[bld_tools_roi_calculator]] | sibling | 0.49 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.45 |
| [[bld_tools_benchmark_suite]] | sibling | 0.37 |
| [[bld_tools_pricing_page]] | sibling | 0.35 |
| [[bld_tools_competitive_matrix]] | sibling | 0.34 |
| [[bld_tools_customer_segment]] | sibling | 0.34 |
| [[bld_tools_eval_metric]] | sibling | 0.34 |
| [[bld_tools_legal_vertical]] | sibling | 0.33 |
| [[bld_tools_rbac_policy]] | sibling | 0.33 |
