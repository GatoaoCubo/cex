---
kind: tools
id: bld_tools_churn_prevention_playbook
pillar: P04
llm_function: CALL
purpose: Tools available for churn_prevention_playbook production
quality: 8.9
title: "Tools Churn Prevention Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [churn_prevention_playbook, builder, tools]
tldr: "Tools available for churn_prevention_playbook production"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_nps_survey
  - bld_tools_sales_playbook
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_changelog
  - bld_tools_api_reference
  - bld_tools_ai_rmf_profile
  - bld_tools_roi_calculator
  - bld_tools_dataset_card
  - bld_tools_benchmark_suite
---

## Production Tools
| Tool                  | Purpose                                         | When                     |
|-----------------------|-------------------------------------------------|--------------------------|
| cex_compile.py        | Compile .md to .yaml                            | After every save         |
| cex_score.py          | Apply peer-review quality score                 | Post-production          |
| cex_retriever.py      | Find similar churn playbook artifacts           | During F3 INJECT         |
| cex_doctor.py         | Diagnose schema and frontmatter issues          | Pre-publish validation   |
| cex_wave_validator.py | Validate domain keywords and ISO completeness  | Post-build CI gate       |

## Validation Tools
| Tool                  | Purpose                                         | When                     |
|-----------------------|-------------------------------------------------|--------------------------|
| cex_schema_hydrate.py | Enforce schema constraints on frontmatter       | Pre-commit               |
| cex_hooks.py          | Pre-commit ASCII and schema checks              | git commit               |

## External References
- Gainsight CS Platform: health score, CTA automation, playbook execution API
- ChurnZero: risk score signals and outreach sequence automation
- Salesforce CRM: account health tracking, escalation logging, save activity records
- Totango: SuccessBloc-based intervention playbook integration

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_nps_survey]] | sibling | 0.49 |
| [[bld_tools_sales_playbook]] | sibling | 0.41 |
| [[bld_tools_rbac_policy]] | sibling | 0.37 |
| [[bld_tools_usage_quota]] | sibling | 0.37 |
| [[bld_tools_changelog]] | sibling | 0.37 |
| [[bld_tools_api_reference]] | sibling | 0.36 |
| [[bld_tools_ai_rmf_profile]] | sibling | 0.36 |
| [[bld_tools_roi_calculator]] | sibling | 0.35 |
| [[bld_tools_dataset_card]] | sibling | 0.35 |
| [[bld_tools_benchmark_suite]] | sibling | 0.35 |
