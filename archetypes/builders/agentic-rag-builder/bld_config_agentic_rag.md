---
kind: config
id: bld_config_agentic_rag
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for agentic_rag production
quality: 8.7
title: "Config Agentic RAG"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, config]
tldr: "Naming, paths, limits for agentic RAG retrieval + agent tool plan + reflection loop"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_graph_rag_config
  - bld_config_playground_config
  - bld_config_ab_test_config
  - bld_config_rl_algorithm
  - bld_config_workflow_node
  - bld_config_sandbox_spec
  - bld_config_eval_framework
  - bld_config_usage_quota
  - bld_config_transport_config
  - bld_config_benchmark_suite
---

## Naming Convention
Pattern: `p01_arag_<name>.yaml`
Examples: `p01_arag_research_agent.yaml`, `p01_arag_sales_query.yaml`

## Paths
Artifacts: `/mnt/cex/data/artifacts/agentic_rag/`
Tool traces: `/var/log/cex/agentic_rag/traces/`
Retrieval cache: `/tmp/cex/agentic_rag/retrieval_cache/`
Reflection plans: `/mnt/cex/data/agentic_rag/plans/`

## Limits
max_bytes: 4096
max_turns: 8
max_tool_calls: 12
max_retrieval_depth: 3
max_reflection_iterations: 4
effort_level: 4

## Agent Tool Registry
tools: [retrieve_vector, retrieve_graph, generate_subquery, reflect_plan, rerank_results]
plan_strategy: react
retrieval_policy: adaptive

## Hooks
pre_build: validate_retriever_registry
post_build: score_tool_plan_coverage
on_error: rollback_plan_state
on_quality_fail: trigger_reflection_retry

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_graph_rag_config]] | sibling | 0.49 |
| [[bld_config_playground_config]] | sibling | 0.38 |
| [[bld_config_ab_test_config]] | sibling | 0.38 |
| [[bld_config_rl_algorithm]] | sibling | 0.36 |
| [[bld_config_workflow_node]] | sibling | 0.35 |
| [[bld_config_sandbox_spec]] | sibling | 0.34 |
| [[bld_config_eval_framework]] | sibling | 0.31 |
| [[bld_config_usage_quota]] | sibling | 0.31 |
| [[bld_config_transport_config]] | sibling | 0.31 |
| [[bld_config_benchmark_suite]] | sibling | 0.30 |
