---
kind: tools
id: bld_tools_ai_rmf_profile
pillar: P04
llm_function: CALL
purpose: Tools available for ai_rmf_profile production
quality: 8.9
title: "Tools AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, tools, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE]
tldr: "Tools available for ai_rmf_profile production"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_gpai_technical_doc
  - bld_tools_churn_prevention_playbook
  - bld_tools_safety_hazard_taxonomy
  - p03_sp_ai_rmf_profile_builder
  - bld_tools_rbac_policy
  - bld_knowledge_card_ai_rmf_profile
  - bld_tools_sales_playbook
  - bld_instruction_ai_rmf_profile
  - bld_tools_api_reference
  - bld_tools_nps_survey
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md to .yaml after save | Post-production |
| cex_score.py | Peer-review quality scoring | Post-production |
| cex_retriever.py | Fetch similar ai_rmf_profile artifacts for reference | During production |
| cex_doctor.py | Diagnose builder and artifact health | Pre-validation |
| cex_wave_validator.py | Validate ISO completeness per builder | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| val_check.py | Verify frontmatter schema compliance | Pre-deployment |
| cex_score.py --apply | Apply quality score from peer review | Post-review |

## External References
- NIST AI-RMF Playbook: airc.nist.gov/airmf-resources/playbook/ (action-ID reference)
- NIST AI 600-1: nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf (GenAI risk categories)
- ISO/IEC 42001:2023 (crosswalk reference for AIMS controls)
- EU AI Act Annex III + Article 9 (risk management crosswalk)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_gpai_technical_doc]] | sibling | 0.42 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.41 |
| [[bld_tools_safety_hazard_taxonomy]] | sibling | 0.40 |
| [[p03_sp_ai_rmf_profile_builder]] | upstream | 0.33 |
| [[bld_tools_rbac_policy]] | sibling | 0.33 |
| [[bld_knowledge_card_ai_rmf_profile]] | upstream | 0.32 |
| [[bld_tools_sales_playbook]] | sibling | 0.31 |
| [[bld_instruction_ai_rmf_profile]] | upstream | 0.31 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_nps_survey]] | sibling | 0.30 |
