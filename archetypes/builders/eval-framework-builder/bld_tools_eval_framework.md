---
kind: tools
id: bld_tools_eval_framework
pillar: P04
llm_function: CALL
purpose: Real tools used during eval_framework production
quality: 9.0
title: "Tools Eval Framework"
version: "1.1.0"
author: n03_hybrid_review4
tags: [eval_framework, builder, tools]
tldr: "Real CEX pipeline tools + real external eval frameworks used to author eval_framework artifacts."
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_knowledge_card_eval_framework
  - bld_tools_workflow_node
  - bld_tools_judge_config
  - bld_collaboration_eval_dataset
  - bld_schema_eval_framework
  - bld_tools_unit_eval
  - bld_tools_e2e_eval
  - bld_tools_smoke_eval
  - bld_collaboration_red_team_eval
  - bld_collaboration_unit_eval
---

## Production Tools (CEX pipeline -- real, on disk)

| Tool | Purpose | When |
|------|---------|------|
| _tools/cex_compile.py | Compile .md artifact to .yaml | After writing ISO, before commit |
| _tools/cex_doctor.py | Health check (schema + ISO completeness) | Before dispatch |
| _tools/cex_score.py | Rubric + semantic scoring for artifacts | After draft |
| _tools/cex_retriever.py | Find existing eval_framework artifacts to template from | During F3 INJECT |
| _tools/cex_wave_validator.py | Validate 13-ISO builder integrity | After generation |
| _tools/signal_writer.py (write_signal) | Nucleus completion signal | End of F8 |

## Domain Tools (external LLM eval frameworks -- real projects)

| Tool | Purpose | When |
|------|---------|------|
| lm-evaluation-harness (EleutherAI) | Canonical task-based LLM eval runner (200+ tasks) | Reference task schema + fewshot_config |
| openai-evals (openai) | Eval spec + completion/classify templates | Reference eval_class + modelgraded specs |
| helm (Stanford CRFM) | Holistic eval across scenarios + metrics + adapters | Reference scenario/adapter/metric separation |
| big-bench (google) | Task zoo + JSON task specs + programmatic tasks | Reference programmatic vs dataset tasks |
| deepeval (confident-ai) | Pytest-style LLM test cases with G-Eval metrics | Reference metric + test_case schemas |
| ragas (explodinggradients) | RAG-specific metrics (faithfulness, answer_relevance) | RAG eval patterns |
| giskard (giskard-ai) | Vulnerability + bias scanning for LLMs | Red-team eval patterns |

## MCP / Filesystem Tools

| Tool | Purpose |
|------|---------|
| Read, Write, Edit, Glob, Grep | Filesystem tools |
| brain_query (MCP) | Semantic search across CEX knowledge base |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_eval_framework]] | upstream | 0.46 |
| [[bld_tools_workflow_node]] | sibling | 0.39 |
| [[bld_tools_judge_config]] | sibling | 0.32 |
| [[bld_collaboration_eval_dataset]] | downstream | 0.28 |
| [[bld_schema_eval_framework]] | downstream | 0.28 |
| [[bld_tools_unit_eval]] | sibling | 0.25 |
| [[bld_tools_e2e_eval]] | sibling | 0.25 |
| [[bld_tools_smoke_eval]] | sibling | 0.25 |
| [[bld_collaboration_red_team_eval]] | downstream | 0.24 |
| [[bld_collaboration_unit_eval]] | downstream | 0.24 |
