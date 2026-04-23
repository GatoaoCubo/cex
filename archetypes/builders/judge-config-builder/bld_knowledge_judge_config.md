---
kind: knowledge_card
id: bld_knowledge_card_judge_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for judge_config production
quality: 9.2
title: "Knowledge Card Judge Config"
version: "1.1.0"
author: n03_hybrid_review4
tags: [judge_config, builder, knowledge_card]
tldr: "A judge_config is the full spec for an LLM-as-a-judge: judge_type, judge_model, rubric, and bias controls. Canonical references: MT-Bench, Chatbot Arena, G-Eval, Prometheus, PandaLM."
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.92
related:
  - bld_tools_judge_config
  - bld_knowledge_card_llm_judge
  - p07_qg_judge_config
  - p07_llm_judge
  - p01_kc_llm_judge
  - bld_collaboration_llm_judge
  - p10_lr_llm_judge_builder
  - llm-judge-builder
  - bld_schema_judge_config
  - n01_atom_26_evaluation_taxonomy
---

## Domain Overview

An LLM-as-a-Judge pattern replaces expensive human annotators with a strong LLM scoring model outputs against a rubric. Zheng et al. (MT-Bench, 2023) established the modern template: single-answer grading with Chain-of-Thought + an anchored rubric, or pairwise preference judgment. Chatbot Arena (LMSYS) uses pairwise human votes combined with LLM judges and Bradley-Terry ranking to build leaderboards. G-Eval (Liu et al. 2023) auto-generates evaluation_steps from a criterion and uses weighted logprobs for fine-grained scores. Prometheus (Kim et al. 2024) adds explicit 5-level anchored rubrics + reference answers and is tuned as an open judge. PandaLM is an open pairwise judge with reproducibility as a goal.

A well-specified judge_config makes the judgment reproducible and calibrated: it declares judge_type (pairwise/rubric/reference_based/direct), judge_model (provider + model + temperature), scoring_scale, the criteria being judged, the prompt_template, and -- critically -- the bias mitigations in place. Judge bias is the main failure mode: LLM judges exhibit position bias (favoring first answer in pairwise), verbosity/length bias, self-enhancement bias (favoring their own outputs), and stylistic bias (favoring their own prose style).

## Key Concepts

| Concept | Definition | Canonical Source |
|---------|-----------|------------------|
| Judge type | pairwise / rubric / reference_based / direct | MT-Bench taxonomy |
| Rubric anchoring | Descriptor per scale level (score_1 .. score_5) | Prometheus |
| Reference answer | Gold answer for reference_based judging | MT-Bench reference-based prompts |
| Position bias | Preference for first (or second) answer in pairwise | Zheng et al. 2023 |
| Length / verbosity bias | Preference for longer answers | MT-Bench analysis |
| Self-enhancement bias | Judge favoring outputs from its own model family | Zheng et al. 2023 |
| Swap-order mitigation | Run pairwise judge twice with A/B swapped; require consistency | MT-Bench, PandaLM |
| Self-consistency aggregation | Sample n judgments, majority or mean | G-Eval, Wang et al. 2022 |
| Bradley-Terry ranking | Pairwise preferences -> scalar ranking | Chatbot Arena, Elo |
| Calibration example | Few-shot exemplar of (input, gold score) to anchor the judge | Prometheus calibration |
| Chain-of-Thought judging | Judge emits reasoning before score | G-Eval, MT-Bench |
| Weighted-logprob score | Score = sum over scale * P(score) from token logprobs | G-Eval |

## Industry Standards

- MT-Bench (LMSYS FastChat) -- 80 multi-turn questions, GPT-4 single-answer + pairwise judge
- Chatbot Arena (LMSYS) -- pairwise human + LLM judges, Bradley-Terry leaderboard
- G-Eval (Liu et al. 2023) -- CoT + weighted-logprob, integrated in DeepEval
- Prometheus, Prometheus-2 (KAIST) -- open judge with 5-level anchored rubric + reference answer
- PandaLM (ByteDance) -- open pairwise judge, reproducibility-first
- JudgeBench, AlignBench, MT-Bench-Extended -- calibration benchmarks for judges
- HELM-judge, OpenAI Evals modelgraded -- embedded judge patterns in eval harnesses

## Common Patterns

1. Declare judge_type explicitly; do not mix pairwise and rubric in one artifact
2. Use temperature=0 and fixed decoding for determinism; relax only when self_consistency_n > 1
3. Anchor every level of the scoring scale with a descriptor + a worked example (Prometheus pattern)
4. For pairwise: always swap A/B positions and report agreement rate; low agreement => unreliable judge
5. Provide calibration examples (few-shot) with gold scores; report judge agreement with humans
6. Separate judge_model from the model being judged to mitigate self-enhancement bias
7. Track and report judge version + prompt template version; pin both in the artifact

## Pitfalls

- No bias controls -- position, length, or self-enhancement bias silently inflates scores
- Free-form scoring scale without descriptors -- inter-judge variance becomes untraceable
- Using the same model as both judge and subject (self-enhancement bias)
- Missing reference_answer for reference_based judges -- equivalent to a direct judge
- No self-consistency or swap-order control -- single noisy sample treated as ground truth
- Prompt template embedded in code instead of referenced as a prompt_template artifact (no versioning)
- Reporting judge scores without a judge-vs-human calibration number

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_judge_config]] | downstream | 0.61 |
| [[bld_knowledge_card_llm_judge]] | sibling | 0.52 |
| [[p07_qg_judge_config]] | downstream | 0.50 |
| [[p07_llm_judge]] | downstream | 0.50 |
| [[p01_kc_llm_judge]] | sibling | 0.48 |
| [[bld_collaboration_llm_judge]] | downstream | 0.46 |
| [[p10_lr_llm_judge_builder]] | downstream | 0.43 |
| [[llm-judge-builder]] | downstream | 0.43 |
| [[bld_schema_judge_config]] | downstream | 0.42 |
| [[n01_atom_26_evaluation_taxonomy]] | sibling | 0.40 |
