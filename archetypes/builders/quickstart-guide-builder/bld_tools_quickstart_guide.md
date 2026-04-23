---
kind: tools
id: bld_tools_quickstart_guide
pillar: P04
llm_function: CALL
purpose: Tools available for quickstart_guide production
quality: 8.9
title: "Tools Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, tools]
tldr: "Tools available for quickstart_guide production"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_api_reference
  - bld_tools_sdk_example
  - bld_tools_integration_guide
  - bld_tools_changelog
  - bld_tools_competitive_matrix
  - bld_tools_case_study
  - bld_tools_vad_config
  - bld_tools_playground_config
  - bld_tools_faq_entry
  - bld_tools_github_issue_template
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles guide ISOs into deployable artifact | Initial build |
| cex_score.py | Scores guide quality via 3-layer rubric | Post-creation validation |
| cex_retriever.py | Fetches related guides and examples via TF-IDF | During content integration |
| cex_doctor.py | Diagnoses structure and frontmatter issues | Debugging phase |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validates frontmatter, ISO count, kind fields | Pre-commit |
| cex_hooks.py | Pre/post build validation hooks | On build events |
| cex_system_test.py | Full system validation (54 checks) | Release gate |

## External References
- Diataxis framework (Tutorial / How-To / Reference / Explanation quadrants)
- Write the Docs (developer documentation standards)
- OpenAPI Specification (api_reference cross-reference)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_api_reference]] | sibling | 0.65 |
| [[bld_tools_sdk_example]] | sibling | 0.53 |
| [[bld_tools_integration_guide]] | sibling | 0.36 |
| [[bld_tools_changelog]] | sibling | 0.33 |
| [[bld_tools_competitive_matrix]] | sibling | 0.31 |
| [[bld_tools_case_study]] | sibling | 0.30 |
| [[bld_tools_vad_config]] | sibling | 0.30 |
| [[bld_tools_playground_config]] | sibling | 0.30 |
| [[bld_tools_faq_entry]] | sibling | 0.29 |
| [[bld_tools_github_issue_template]] | sibling | 0.28 |
