---
kind: tools
id: bld_tools_legal_vertical
pillar: P04
llm_function: CALL
purpose: Tools available for legal_vertical production
quality: 8.9
title: "Tools Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, tools]
tldr: "Tools available for legal_vertical production"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_healthcare_vertical
  - bld_tools_github_issue_template
  - bld_tools_white_label_config
  - bld_tools_fintech_vertical
  - bld_tools_pricing_page
  - bld_tools_roi_calculator
  - bld_tools_changelog
  - bld_tools_competitive_matrix
  - bld_tools_churn_prevention_playbook
  - bld_tools_rbac_policy
---

## Production Tools
| Tool | Purpose (legal context) | When |
|---|---|---|
| cex_compile.py | Compile legal_vertical artifact to YAML + validate frontmatter | After authoring |
| cex_score.py | Score artifact against H01-H10 gates and 7D SOFT dimensions | Before publish |
| cex_retriever.py | Retrieve similar privilege/billing/contract artifacts from knowledge library | During research |
| cex_doctor.py | Health-check builder ISO completeness and frontmatter validity | QA pass |

## Validation Tools
| Tool | Purpose | When |
|---|---|---|
| cex_wave_validator.py | Validate all 13 ISOs in builder directory | Post-build |
| cex_hygiene.py | Enforce naming, frontmatter, ASCII rules | Pre-commit |

## External References
- Westlaw / LexisNexis -- primary law research
- iManage / NetDocuments -- DMS integration reference patterns
- Relativity / Everlaw -- eDiscovery platform integration

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_healthcare_vertical]] | sibling | 0.41 |
| [[bld_tools_github_issue_template]] | sibling | 0.34 |
| [[bld_tools_white_label_config]] | sibling | 0.34 |
| [[bld_tools_fintech_vertical]] | sibling | 0.34 |
| [[bld_tools_pricing_page]] | sibling | 0.33 |
| [[bld_tools_roi_calculator]] | sibling | 0.32 |
| [[bld_tools_changelog]] | sibling | 0.31 |
| [[bld_tools_competitive_matrix]] | sibling | 0.31 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.31 |
| [[bld_tools_rbac_policy]] | sibling | 0.31 |
