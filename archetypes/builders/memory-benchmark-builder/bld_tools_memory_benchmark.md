---
kind: tools
id: bld_tools_memory_benchmark
pillar: P04
llm_function: CALL
purpose: Tools available for memory_benchmark production
quality: 8.9
title: "Tools Memory Benchmark"
version: "1.1.0"
author: n05_operations
tags: [memory_benchmark, builder, tools]
tldr: "Tools available for memory_benchmark production"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_tools_benchmark_suite
  - bld_tools_eval_metric
  - bld_tools_roi_calculator
  - bld_tools_rbac_policy
  - bld_tools_churn_prevention_playbook
  - bld_tools_changelog
  - bld_tools_playground_config
  - bld_tools_discovery_questions
  - bld_tools_sales_playbook
  - bld_tools_usage_quota
---

## Production Tools

| Tool                      | Purpose                                            | When              |
|---------------------------|----------------------------------------------------|-------------------|
| cex_compile.py            | Compile memory_benchmark artifact after save       | F8 COLLABORATE    |
| cex_score.py              | Score artifact against quality gate (--apply)      | F7 GOVERN         |
| cex_retriever.py          | Find similar memory_benchmark artifacts for reuse  | F3 INJECT         |
| cex_doctor.py             | Validate builder health and ISO completeness       | F7 GOVERN         |
| cex_wave_validator.py     | Run schema + frontmatter validation on ISOs        | Pre-commit        |

## Validation Tools

| Tool                         | Purpose                                         | When              |
|------------------------------|-------------------------------------------------|-------------------|
| python -m pytest             | Run unit tests for memory_benchmark artifacts   | CI gate           |
| python _tools/cex_hooks.py pre-commit | Pre-commit hook: ASCII check + frontmatter | Before git add |

## External References

- lm-evaluation-harness (EleutherAI): Framework for running LLM evals incl. NarrativeQA
- LOCOMO dataset (Maharana 2024): Long-conversation memory benchmark dataset and code
- LongMemEval (Wu 2024): Multi-session memory QA benchmark and evaluation scripts
- ragas (ragas.io): RAG evaluation library with faithfulness, answer relevance metrics

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_benchmark_suite]] | sibling | 0.56 |
| [[bld_tools_eval_metric]] | sibling | 0.42 |
| [[bld_tools_roi_calculator]] | sibling | 0.36 |
| [[bld_tools_rbac_policy]] | sibling | 0.34 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.33 |
| [[bld_tools_changelog]] | sibling | 0.33 |
| [[bld_tools_playground_config]] | sibling | 0.33 |
| [[bld_tools_discovery_questions]] | sibling | 0.32 |
| [[bld_tools_sales_playbook]] | sibling | 0.32 |
| [[bld_tools_usage_quota]] | sibling | 0.32 |
