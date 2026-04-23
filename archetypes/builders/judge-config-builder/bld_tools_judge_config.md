---
kind: tools
id: bld_tools_judge_config
pillar: P04
llm_function: CALL
purpose: Real tools used during judge_config production
quality: 9.0
title: "Tools Judge Config"
version: "1.1.0"
author: n03_hybrid_review4
tags: [judge_config, builder, tools]
tldr: "Real CEX pipeline tools + real external LLM-as-judge frameworks used to author judge_config artifacts."
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_knowledge_card_judge_config
  - bld_collaboration_llm_judge
  - bld_tools_eval_framework
  - llm-judge-builder
  - p01_kc_llm_judge
  - bld_tools_workflow_node
  - judge-config-builder
  - p07_llm_judge
  - bld_collaboration_judge_config
  - n01_atom_26_evaluation_taxonomy
---

## Production Tools (CEX pipeline -- real, on disk)

| Tool | Purpose | When |
|------|---------|------|
| _tools/cex_compile.py | Compile .md artifact to .yaml | After writing ISO, before commit |
| _tools/cex_doctor.py | Health check | Before dispatch |
| _tools/cex_score.py | Rubric scoring (dogfooding the judge pattern itself) | After draft |
| _tools/cex_retriever.py | Find similar judge_config artifacts | During F3 INJECT |
| _tools/cex_wave_validator.py | Validate builder integrity | After generation |
| _tools/signal_writer.py (write_signal) | Nucleus completion signal | End of F8 |

## Domain Tools (external LLM-as-judge frameworks -- real projects)

| Tool | Purpose | When |
|------|---------|------|
| mt-bench (lmsys/FastChat) | 80-question multi-turn judge + single-answer-grading prompts | Reference rubric + GPT-4-judge prompt patterns |
| chatbot-arena (lmsys) | Pairwise preference collection + Bradley-Terry ranking | Pairwise judge design |
| g-eval (deepeval / Liu et al. 2023) | CoT-based evaluator with auto-generated evaluation_steps | Criterion decomposition |
| prometheus (kaist-ai) | 5-level score rubric + reference answer + feedback | Anchored rubric design |
| pandalm (ByteDance) | Pairwise/ranking judge with OS reproducibility | Open judge fine-tuning patterns |
| alignbench, judgebench | Calibration benchmarks for LLM judges | Judge calibration validation |

## MCP / Filesystem Tools

| Tool | Purpose |
|------|---------|
| Read, Write, Edit, Glob, Grep | Filesystem tools |
| brain_query (MCP) | Semantic search across CEX knowledge base |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_judge_config]] | upstream | 0.49 |
| [[bld_collaboration_llm_judge]] | downstream | 0.43 |
| [[bld_tools_eval_framework]] | sibling | 0.40 |
| [[llm-judge-builder]] | downstream | 0.40 |
| [[p01_kc_llm_judge]] | downstream | 0.39 |
| [[bld_tools_workflow_node]] | sibling | 0.38 |
| [[judge-config-builder]] | downstream | 0.34 |
| [[p07_llm_judge]] | downstream | 0.33 |
| [[bld_collaboration_judge_config]] | downstream | 0.33 |
| [[n01_atom_26_evaluation_taxonomy]] | upstream | 0.31 |
