---
kind: tools
id: bld_tools_workflow_node
pillar: P04
llm_function: CALL
purpose: Real tools used during workflow_node production
quality: 9.0
title: "Tools Workflow Node"
version: "1.1.0"
author: n03_hybrid_review4
tags: [workflow_node, builder, tools]
tldr: "Real CEX pipeline tools + real external frameworks used to author and validate workflow_node artifacts."
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_tools_eval_framework
  - bld_tools_judge_config
  - bld_tools_dataset_card
  - bld_tools_customer_segment
  - bld_sp_tools_software_project
  - bld_tools_visual_workflow
  - bld_tools_builder
  - bld_tools_skill
  - bld_tools_playground_config
  - bld_tools_integration_guide
---

## Production Tools (CEX pipeline -- real, on disk)

| Tool | Purpose | When |
|------|---------|------|
| _tools/cex_compile.py | Compile .md artifact to .yaml | After writing ISO, before commit |
| _tools/cex_doctor.py | Health check (builder completeness, schema drift) | Before dispatch |
| _tools/cex_score.py | Rubric + semantic scoring | After draft, before publish |
| _tools/cex_retriever.py | TF-IDF similarity over existing artifacts | During F3 INJECT (find examples) |
| _tools/cex_hooks.py | Pre-commit validation + ASCII check | git add hook |
| _tools/cex_wave_validator.py | Validate 13-ISO builder integrity | After builder generation |
| _tools/signal_writer.py (write_signal) | Nucleus completion signal | End of F8 COLLABORATE |

## Domain Tools (external, installable -- real projects)

| Tool | Purpose | When |
|------|---------|------|
| langgraph (pip) | Reference StateGraph node/edge patterns for LLM agent workflows | Drafting node_type + state_schema |
| prefect (pip) | Task decorator semantics (retries, timeout, cache_key_fn) | Designing retry_policy |
| temporalio (pip) | Activity and workflow primitives (heartbeat, compensation) | Long-running node patterns |
| dagster (pip) | Op/asset graph with typed ins/outs and config_schema | Designing typed I/O contracts |
| apache-airflow (pip) | Operator + trigger_rule + XCom patterns | Cross-task state handoff |

## MCP / Filesystem Tools

| Tool | Purpose |
|------|---------|
| Read, Write, Edit, Glob, Grep | Filesystem tools for loading ISOs and emitting artifacts |
| brain_query (MCP) | Semantic search across CEX knowledge base |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_eval_framework]] | sibling | 0.41 |
| [[bld_tools_judge_config]] | sibling | 0.32 |
| [[bld_tools_dataset_card]] | sibling | 0.29 |
| [[bld_tools_customer_segment]] | sibling | 0.27 |
| [[bld_sp_tools_software_project]] | sibling | 0.26 |
| [[bld_tools_visual_workflow]] | sibling | 0.26 |
| [[bld_tools_builder]] | sibling | 0.26 |
| [[bld_tools_skill]] | sibling | 0.26 |
| [[bld_tools_playground_config]] | sibling | 0.26 |
| [[bld_tools_integration_guide]] | sibling | 0.26 |
