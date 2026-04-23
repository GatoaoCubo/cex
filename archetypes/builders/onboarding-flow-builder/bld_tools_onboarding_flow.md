---
kind: tools
id: bld_tools_onboarding_flow
pillar: P04
llm_function: CALL
purpose: Tools available for onboarding_flow production
quality: 8.9
title: "Tools Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, tools]
tldr: "Tools available for onboarding_flow production"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_pricing_page
  - bld_tools_referral_program
  - bld_tools_roi_calculator
  - bld_tools_legal_vertical
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_product_tour
  - bld_tools_discovery_questions
  - bld_tools_benchmark_suite
  - bld_tools_github_issue_template
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact after save | F8 COLLABORATE |
| cex_score.py | Score artifact against 5D rubric | F7 GOVERN |
| cex_retriever.py | Fetch similar onboarding_flow artifacts for Template-First | F3 INJECT |
| cex_doctor.py | Validate builder health and ISO completeness | Post-edit check |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validate builder ISO set (13-file check, frontmatter gates) | Pre-commit |
| cex_hygiene.py | Artifact CRUD rules, naming pattern enforcement | Post-save |

## External References
- Reforge Activation Framework (Sean Ellis aha-moment, TTV optimization)
- Intercom Product Tours (in-app guided onboarding patterns)
- Pendo Onboarding (empty-state design, progress checkmarks, invite hooks)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_pricing_page]] | sibling | 0.50 |
| [[bld_tools_referral_program]] | sibling | 0.40 |
| [[bld_tools_roi_calculator]] | sibling | 0.34 |
| [[bld_tools_legal_vertical]] | sibling | 0.33 |
| [[bld_tools_rbac_policy]] | sibling | 0.33 |
| [[bld_tools_usage_quota]] | sibling | 0.32 |
| [[bld_tools_product_tour]] | sibling | 0.31 |
| [[bld_tools_discovery_questions]] | sibling | 0.30 |
| [[bld_tools_benchmark_suite]] | sibling | 0.30 |
| [[bld_tools_github_issue_template]] | sibling | 0.29 |
