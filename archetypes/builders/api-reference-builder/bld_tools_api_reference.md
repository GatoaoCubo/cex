---
kind: tools
id: bld_tools_api_reference
pillar: P04
llm_function: CALL
purpose: Tools available for api_reference production
quality: 8.9
title: "Tools Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, tools]
tldr: "Tools available for api_reference production"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_quickstart_guide
  - bld_tools_sdk_example
  - bld_tools_playground_config
  - bld_tools_changelog
  - bld_tools_vad_config
  - bld_tools_competitive_matrix
  - bld_tools_nps_survey
  - bld_tools_integration_guide
  - bld_tools_churn_prevention_playbook
  - bld_tools_case_study
---

## Production Tools
| Tool              | Purpose                  | When                          |
|-------------------|--------------------------|-------------------------------|
| cex_compile.py    | Compiles ISOs to deployable artifact | During reference generation |
| cex_score.py      | Scores quality via 3-layer rubric | Post-validation             |
| cex_retriever.py  | Finds related API artifacts via TF-IDF | Pre-processing            |
| cex_doctor.py     | Diagnoses frontmatter and structure issues | On error detection      |

## Validation Tools
| Tool              | Purpose                  | When                          |
|-------------------|--------------------------|-------------------------------|
| cex_wave_validator.py | Validates frontmatter, ISO count, kind fields | Pre-commit      |
| cex_hooks.py      | Pre/post build validation hooks | On build events              |
| cex_system_test.py | Full system validation (54 checks) | Release gate              |

## External References
- OpenAPI Specification 3.1 (endpoint/method/param/response structure)
- Swagger UI / ReDoc (interactive API documentation rendering)
- JSON Schema (request/response payload validation)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_quickstart_guide]] | sibling | 0.58 |
| [[bld_tools_sdk_example]] | sibling | 0.53 |
| [[bld_tools_playground_config]] | sibling | 0.35 |
| [[bld_tools_changelog]] | sibling | 0.35 |
| [[bld_tools_vad_config]] | sibling | 0.31 |
| [[bld_tools_competitive_matrix]] | sibling | 0.31 |
| [[bld_tools_nps_survey]] | sibling | 0.31 |
| [[bld_tools_integration_guide]] | sibling | 0.31 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.29 |
| [[bld_tools_case_study]] | sibling | 0.29 |
