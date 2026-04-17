---
kind: knowledge_card
id: bld_knowledge_card_eval_framework
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for eval_framework production
quality: 9.2
title: "Knowledge Card Eval Framework"
version: "1.1.0"
author: n03_hybrid_review4
tags: [eval_framework, builder, knowledge_card]
tldr: "An eval_framework is a reproducible runner that executes a task suite against a model and computes metrics. Canonical references: EleutherAI lm-eval-harness, OpenAI Evals, HELM, BIG-Bench, DeepEval, Ragas, Giskard."
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.92
---

## Domain Overview

An eval_framework is the triple of (tasks, metrics, runner). Tasks define what is measured (datasets + input formatting), metrics define how a prediction is scored, the runner orchestrates model invocation, decoding, and aggregation. The field has converged on a small set of canonical frameworks: EleutherAI lm-evaluation-harness powers the HuggingFace Open LLM Leaderboard; OpenAI Evals defines the eval spec + modelgraded pattern; HELM (Stanford CRFM) separates scenarios/adapters/metrics for holistic coverage; BIG-Bench is the task zoo; DeepEval adds pytest-style LLM test cases; Ragas specializes in RAG faithfulness/answer_relevance/context_precision; Giskard covers red-team and bias.

The core distinction for modern agents is task-based eval (static datasets with exact_match / f1 / accuracy) vs judge-based eval (G-Eval, LLM-as-a-Judge) vs trajectory eval (agent tool-use traces, pass@k, success_rate). A well-specified eval_framework declares which pattern it uses and makes runs reproducible via seed, version pins, and a referenced prompt template.

## Key Concepts

| Concept | Definition | Canonical Source |
|---------|-----------|------------------|
| Task | Named dataset + input formatter + answer extractor | lm-eval-harness task registry |
| Metric | Function mapping (pred, gold) -> score | lm-eval-harness metrics, HELM metrics |
| Adapter | Model-I/O contract (chat vs completion vs logprobs vs tool_use) | HELM adapters, OpenAI Evals completion_fn |
| Scenario | Bundled task + adapter + metrics for a target capability | HELM scenarios |
| Few-shot k | Number of in-context exemplars | lm-eval-harness num_fewshot |
| pass@k | Probability at least one of k samples solves the task | HumanEval, APPS |
| G-Eval | LLM-judge metric with CoT-decomposed evaluation_steps | Liu et al. 2023, DeepEval |
| Faithfulness | RAG metric: does the answer stay grounded in retrieved context | Ragas |
| Modelgraded eval | Eval whose correctness is judged by another LLM | OpenAI Evals modelgraded |
| Contamination | Overlap between eval data and training data | data decontamination heuristics |
| Reproducibility manifest | Pinned versions + seed + prompt template + decoding params | HELM manifest, Open LLM Leaderboard config |

## Industry Standards

- EleutherAI lm-evaluation-harness -- de facto task runner; 200+ tasks incl. MMLU, HellaSwag, ARC, TruthfulQA, GSM8K
- OpenAI Evals -- eval spec + completion_fn + modelgraded templates
- HELM (Stanford CRFM) -- holistic eval: scenarios x metrics x adapters
- BIG-Bench / BIG-Bench Hard -- task zoo with programmatic + dataset tasks
- DeepEval -- pytest-style LLM test cases; G-Eval metrics
- Ragas -- RAG-specific metrics (faithfulness, answer_relevance, context_precision, context_recall)
- Giskard -- vulnerability + bias scan; red-team test generation
- Inspect (UK AISI), Simple-Evals (OpenAI) -- safety + capability eval stacks
- AgentBench, SWE-bench, TAU-bench -- agent + coding + tool-use benchmarks

## Common Patterns

1. Separate tasks, metrics, and runner into composable artifacts referenced by id
2. Pin the model version + prompt template + seed + decoding params in a reproducibility manifest
3. Use modelgraded eval (or G-Eval) only with a strong judge_config with reported calibration
4. Report confidence intervals (bootstrap over samples) not just point estimates
5. Run a contamination check against training data before publishing scores
6. For RAG, split eval into retrieval metrics (hit_rate, mrr, ndcg) and generation metrics (faithfulness, answer_relevance)
7. For agents, track trajectory metrics: success_rate, steps_to_solve, tool_error_rate, cost_per_task

## Pitfalls

- Free-form metric names that don't map to a canonical implementation (ambiguous `"accuracy"`)
- No seed or version pins -- scores irreproducible across runs
- Prompt template baked into runner code instead of referenced as a prompt_template artifact
- Single-sample pass@1 reported without variance; cherry-picking runs
- Using an LLM judge with undocumented judge_config (no calibration, no bias controls)
- RAG evals that only measure retrieval metrics without checking generation faithfulness
- Evaluating on training data leakage (contamination) and reporting inflated scores
