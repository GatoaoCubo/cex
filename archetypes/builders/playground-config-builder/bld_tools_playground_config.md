---
kind: tools
id: bld_tools_playground_config
pillar: P04
llm_function: CALL
purpose: Tools available for playground_config production
quality: 8.9
title: "Tools Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, tools]
tldr: "Tools available for playground_config production"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_integration_guide
  - bld_tools_sandbox_spec
  - bld_tools_api_reference
  - bld_tools_github_issue_template
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_white_label_config
  - bld_tools_changelog
  - bld_tools_app_directory_entry
  - p01_kc_git_hooks_ci
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | Post-write (F8) |
| cex_retriever.py | TF-IDF similarity over 2184 docs | Find prior playground_config artifacts (F3) |
| cex_score.py | 3-layer scoring (structural + rubric + semantic) | Quality gate (F7) |
| cex_doctor.py | Builder health check across 13 ISOs | Pre-dispatch validation |
| cex_hygiene.py | Frontmatter + ASCII + naming enforcement | Pre-commit (F7) |
| cex_prompt_optimizer.py | Analyze builder ISOs for drift | When quality < 9.0 |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | D01-D15 defect checks across ISOs | After bulk generation |
| cex_sanitize.py --check | ASCII-only enforcement on .py/.ps1 | Pre-commit hook |
| cex_hooks.py pre-commit | YAML frontmatter + schema compliance | Git pre-commit |

## External References
- OpenAI Playground (interactive prompt eval reference)
- Swagger/OpenAPI "Try It Out" (in-browser API explorer pattern)
- Replit + CodeSandbox embed APIs (sandboxed runtime templates)
- JupyterLite (WASM-based ephemeral Python kernels)
- JSON Schema draft 2020-12 (config structure validation)
- 12-Factor App config principles (env-var externalization)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_integration_guide]] | sibling | 0.58 |
| [[bld_tools_sandbox_spec]] | sibling | 0.51 |
| [[bld_tools_api_reference]] | sibling | 0.42 |
| [[bld_tools_github_issue_template]] | sibling | 0.42 |
| [[bld_tools_rbac_policy]] | sibling | 0.41 |
| [[bld_tools_usage_quota]] | sibling | 0.39 |
| [[bld_tools_white_label_config]] | sibling | 0.38 |
| [[bld_tools_changelog]] | sibling | 0.38 |
| [[bld_tools_app_directory_entry]] | sibling | 0.36 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.36 |
