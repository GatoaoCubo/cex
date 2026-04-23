---
kind: tools
id: bld_tools_gpai_technical_doc
pillar: P04
llm_function: CALL
purpose: Tools available for gpai_technical_doc production
quality: 8.9
title: "Tools GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, tools, GPAI, EU-AI-Act, Annex-IV, Article-53]
tldr: "Tools available for gpai_technical_doc production"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_safety_hazard_taxonomy
  - bld_tools_ai_rmf_profile
  - bld_tools_churn_prevention_playbook
  - bld_tools_roi_calculator
  - bld_tools_nps_survey
  - bld_tools_pricing_page
  - bld_tools_rbac_policy
  - bld_tools_api_reference
  - bld_tools_competitive_matrix
  - bld_knowledge_card_gpai_technical_doc
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md to .yaml after save | Post-production |
| cex_score.py | Peer-review quality scoring | Post-production |
| cex_retriever.py | Fetch similar gpai_technical_doc artifacts | During production |
| cex_doctor.py | Diagnose builder health | Pre-validation |
| cex_wave_validator.py | Validate 13-ISO completeness | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| val_check.py | Verify Annex IV field completeness | Pre-submission |
| cex_score.py --apply | Apply peer review quality score | Post-review |

## External References
- EU AI Act Official Text: artificialintelligenceact.eu/annex/4/ (Annex IV fields)
- EU AI Office Guidelines: digital-strategy.ec.europa.eu/en/policies/eu-ai-act (GPAI guidance)
- GHG Protocol Corporate Standard: ghgprotocol.org (energy consumption methodology)
- FLOP calculation reference: NVIDIA MLPerf Training benchmarks (compute budget comparison)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_safety_hazard_taxonomy]] | sibling | 0.43 |
| [[bld_tools_ai_rmf_profile]] | sibling | 0.42 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.35 |
| [[bld_tools_roi_calculator]] | sibling | 0.33 |
| [[bld_tools_nps_survey]] | sibling | 0.33 |
| [[bld_tools_pricing_page]] | sibling | 0.31 |
| [[bld_tools_rbac_policy]] | sibling | 0.31 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_competitive_matrix]] | sibling | 0.31 |
| [[bld_knowledge_card_gpai_technical_doc]] | upstream | 0.30 |
