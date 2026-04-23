---
kind: tools
id: bld_tools_sdk_example
pillar: P04
llm_function: CALL
purpose: Tools available for sdk_example production
quality: 8.9
title: "Tools Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, tools]
tldr: "Tools available for sdk_example production"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_api_reference
  - bld_tools_quickstart_guide
  - bld_tools_github_issue_template
  - bld_tools_changelog
  - bld_tools_vad_config
  - bld_tools_playground_config
  - bld_tools_competitive_matrix
  - bld_tools_rbac_policy
  - p01_kc_git_hooks_ci
  - bld_tools_integration_guide
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles ISOs to deployable artifact | During build phase |
| cex_score.py | Scores quality via 3-layer rubric | Post-validation |
| cex_retriever.py | Finds related SDK artifacts via TF-IDF | Pre-runtime setup |
| cex_doctor.py | Diagnoses frontmatter and structure issues | On first run or deployment |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validates frontmatter, ISO count, kind fields | Pre-commit |
| cex_hooks.py | Pre/post build validation hooks | On build events |
| cex_system_test.py | Full system validation (54 checks) | Release gate |

## External References
- Twilio Quickstart SDK style (auth + retry + pagination canonical patterns)
- GitHub idiomatic code examples (language-specific README conventions)
- PEP8 (Python) / Google Java Style / StandardJS (language style guides)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_api_reference]] | sibling | 0.59 |
| [[bld_tools_quickstart_guide]] | sibling | 0.56 |
| [[bld_tools_github_issue_template]] | sibling | 0.31 |
| [[bld_tools_changelog]] | sibling | 0.31 |
| [[bld_tools_vad_config]] | sibling | 0.29 |
| [[bld_tools_playground_config]] | sibling | 0.29 |
| [[bld_tools_competitive_matrix]] | sibling | 0.29 |
| [[bld_tools_rbac_policy]] | sibling | 0.28 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.28 |
| [[bld_tools_integration_guide]] | sibling | 0.28 |
