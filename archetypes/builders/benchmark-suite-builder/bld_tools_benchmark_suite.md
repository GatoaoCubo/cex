---
kind: tools
id: bld_tools_benchmark_suite
pillar: P04
llm_function: CALL
purpose: Tools available for benchmark_suite production
quality: 8.9
title: "Tools Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, tools]
tldr: "Tools available for benchmark_suite production"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_memory_benchmark
  - bld_tools_eval_metric
  - bld_tools_roi_calculator
  - bld_tools_changelog
  - bld_tools_rbac_policy
  - bld_tools_churn_prevention_playbook
  - bld_tools_playground_config
  - bld_tools_integration_guide
  - p01_kc_git_hooks_ci
  - bld_tools_usage_quota
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile benchmark_suite artifact after save | F8 COLLABORATE |
| cex_score.py | Score artifact against quality gate (--apply flag) | F7 GOVERN |
| cex_retriever.py | Find similar benchmark_suite artifacts for reuse | F3 INJECT |
| cex_doctor.py | Validate builder health and ISO completeness | F7 GOVERN |
| cex_wave_validator.py | Run schema + frontmatter validation on builder ISOs | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| python -m pytest | Run unit tests for benchmark suite artifacts | CI gate |
| python _tools/cex_hooks.py pre-commit | Pre-commit hook: ASCII check + frontmatter | Before git add |

## External References
- MLPerf (mlcommons.org): Reference suite for AI benchmarking standards
- lm-evaluation-harness (EleutherAI): Framework for LLM benchmark execution
- pytest-benchmark: For measuring benchmark execution performance

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_benchmark]] | sibling | 0.51 |
| [[bld_tools_eval_metric]] | sibling | 0.44 |
| [[bld_tools_roi_calculator]] | sibling | 0.38 |
| [[bld_tools_changelog]] | sibling | 0.35 |
| [[bld_tools_rbac_policy]] | sibling | 0.35 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.35 |
| [[bld_tools_playground_config]] | sibling | 0.34 |
| [[bld_tools_integration_guide]] | sibling | 0.34 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.33 |
| [[bld_tools_usage_quota]] | sibling | 0.33 |
