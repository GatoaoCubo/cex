---
kind: tools
id: bld_tools_nps_survey
pillar: P04
llm_function: CALL
purpose: Tools available for nps_survey production
quality: 8.9
title: "Tools Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, tools]
tldr: "Tools available for nps_survey production"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_churn_prevention_playbook
  - bld_tools_api_reference
  - bld_tools_changelog
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_competitive_matrix
  - bld_tools_roi_calculator
  - bld_tools_playground_config
  - bld_tools_white_label_config
  - bld_tools_integration_guide
---

## Production Tools
| Tool               | Purpose                                  | When                         |
|--------------------|------------------------------------------|------------------------------|
| cex_compile.py     | Compile .md to .yaml                     | After every save             |
| cex_score.py       | Apply peer-review quality score          | Post-production              |
| cex_retriever.py   | Find similar NPS survey artifacts        | During F3 INJECT             |
| cex_doctor.py      | Diagnose schema issues                   | Pre-publish validation       |
| cex_wave_validator.py | Validate domain keywords present      | Post-build CI gate           |

## Validation Tools
| Tool               | Purpose                                  | When                         |
|--------------------|------------------------------------------|------------------------------|
| cex_schema_hydrate.py | Enforce schema constraints            | Pre-commit                   |
| cex_hooks.py       | Pre-commit ASCII and schema checks       | git commit                   |

## External References
- Gainsight API: Survey trigger + response routing integration
- ChurnZero SDK: Health score signal for detractor escalation
- Delighted / Wootric API: Survey distribution and response collection
- Bain & Company NPS standard: Scale and phrasing reference

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.52 |
| [[bld_tools_api_reference]] | sibling | 0.41 |
| [[bld_tools_changelog]] | sibling | 0.38 |
| [[bld_tools_rbac_policy]] | sibling | 0.37 |
| [[bld_tools_usage_quota]] | sibling | 0.36 |
| [[bld_tools_competitive_matrix]] | sibling | 0.35 |
| [[bld_tools_roi_calculator]] | sibling | 0.34 |
| [[bld_tools_playground_config]] | sibling | 0.34 |
| [[bld_tools_white_label_config]] | sibling | 0.34 |
| [[bld_tools_integration_guide]] | sibling | 0.33 |
