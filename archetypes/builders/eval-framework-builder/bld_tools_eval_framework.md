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
