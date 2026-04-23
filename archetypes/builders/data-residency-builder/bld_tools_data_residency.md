---
kind: tools
id: bld_tools_data_residency
pillar: P04
llm_function: CALL
purpose: Tools available for data_residency production
quality: 8.7
title: "Tools Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, tools]
tldr: "Tools available for data_residency production"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_compliance_checklist
  - bld_tools_audit_log
  - bld_knowledge_card_data_residency
  - bld_tools_edit_format
  - bld_tools_pricing_page
  - data-residency-builder
  - p09_kc_data_residency
  - bld_tools_legal_vertical
  - bld_tools_onboarding_flow
  - bld_tools_roi_calculator
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles data_residency artifact to .yaml | After each save |
| cex_score.py | Scores artifact against 5D quality dimensions | Post-production |
| cex_retriever.py | Retrieves similar residency specs and KCs | During F3 INJECT |
| cex_doctor.py | Validates builder ISO completeness and structure | During F7 GOVERN |
| cex_hygiene.py | Enforces frontmatter rules and naming conventions | During F7 GOVERN |

## External References
- GDPR Articles 44-50 (third-country transfers)
- Schrems II ruling (C-311/18) and EU-US Data Privacy Framework 2023
- ISO/IEC 27701:2019 (Privacy Information Management)
- AWS Data Residency, Azure Sovereign Regions (regional data plane references)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_compliance_checklist]] | sibling | 0.50 |
| [[bld_tools_audit_log]] | sibling | 0.44 |
| [[bld_knowledge_card_data_residency]] | upstream | 0.32 |
| [[bld_tools_edit_format]] | sibling | 0.31 |
| [[bld_tools_pricing_page]] | sibling | 0.27 |
| [[data-residency-builder]] | downstream | 0.27 |
| [[p09_kc_data_residency]] | downstream | 0.26 |
| [[bld_tools_legal_vertical]] | sibling | 0.25 |
| [[bld_tools_onboarding_flow]] | sibling | 0.25 |
| [[bld_tools_roi_calculator]] | sibling | 0.24 |
