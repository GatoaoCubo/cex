---
kind: knowledge_card
id: bld_knowledge_card_llm_judge
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for llm_judge production — LLM-as-Judge configuration
sources: Braintrust scorer, DeepEval LLMTestCase, RAGAS metrics, Promptfoo llm-rubric, OpenAI Evals, Zheng et al. 2023 (MT-Bench)
quality: 9.2
title: "Knowledge Card Llm Judge"
version: "1.0.0"
author: n03_builder
tags: [llm_judge, builder, examples]
tldr: "Golden and anti-examples for llm judge construction, demonstrating ideal structure and common pitfalls."
domain: "llm judge construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_llm_judge_builder
  - p11_qg_llm_judge
  - bld_instruction_llm_judge
  - p03_sp_llm_judge_builder
  - bld_output_template_llm_judge
  - p07_llm_judge
  - p01_kc_llm_judge
  - llm-judge-builder
  - bld_collaboration_llm_judge
  - bld_tools_llm_judge
---

# Domain Knowledge: llm_judge
## Executive Summary
LLM-as-Judge uses a language model to evaluate another model's output, returning a score on a defined scale. Quality depends on three spec-time decisions: which model judges (capability), what criteria it uses (coverage), and how it is calibrated (consistency). Uncalibrated judges exhibit position bias, verbosity bias, and self-enhancement bias.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (Evals) |
| llm_function | GOVERN (controls quality signal) |
| Scale types | binary, likert (1-5), extended (1-10), continuous (0.0-1.0) |
| Recommended judge models | gpt-4o, claude-3-5-sonnet, gemini-1.5-pro |
| Chain-of-thought | Required for subjective criteria |
| Temperature | 0.0 for reproducibility; 0.2 max |
| Few-shot minimum | 2 examples (1 high, 1 low); 5+ for production |

## Framework Patterns
- **braintrust**: `score()` returns `{score: float, metadata: {rationale}}`. Scale: 0.0-1.0.
- **deepeval**: GEval metric with `criteria -> evaluation_steps -> model`. `LLMTestCase(input, actual_output, expected_output)`.
- **ragas**: Core metrics: faithfulness, answer_relevancy, context_precision, context_recall (0-1).
- **promptfoo**: `assert type: llm-rubric`, `value: "rubric text"`, optional `rubricPrompt` override.
- **openai_evals**: `eval_type: model-graded-closedqa`, `completion_fn` = judge model.

## Patterns
| Pattern | Use case | Bias risk |
|---------|----------|-----------|
| Single criterion | Targeted quality dimension | Low |
| Multi-criteria | Holistic evaluation | Medium (criteria bleed) |
| Pairwise | A/B comparison | Low (relative scale) |
| Reference-based | Factual accuracy | Low |
| Reference-free | Style, tone, creativity | High (needs calibration) |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No few-shot examples | Judge drifts on edge cases; inconsistent scores |
| Overlapping criteria | Double-penalizes same flaw; inflates variance |
| Vague scale anchors | Judge assigns arbitrary scores |
| judge_model == evaluated_model | Self-enhancement bias |
| temperature > 0.2 | Score variance increases across identical inputs |
| Criteria count > 7 | Later criteria get less attention |

## Key Biases
| Bias | Mitigation |
|------|-----------|
| Position bias | Randomize order in pairwise; use reference-based |
| Verbosity bias | Penalize length explicitly in criteria anchors |
| Self-enhancement | Use different model family as judge |
| Sycophancy | Few-shot with confident-but-wrong = low score |

## Application
1. Choose judge_model: frontier model from different family than evaluated model
2. Define criteria: 1-5 independent dimensions, each measuring ONE quality aspect
3. Set scale: likert 1-5 for most cases; binary for pass/fail gates
4. Write anchors: define what score 1, 3, 5 look like explicitly
5. Compose few_shot: minimum 1 high + 1 low score example with rationale
6. Set chain_of_thought: true (default); false only if latency < 500ms required
7. Set temperature: 0.0 for reproducibility

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_llm_judge_builder]] | downstream | 0.50 |
| [[p11_qg_llm_judge]] | downstream | 0.46 |
| [[bld_instruction_llm_judge]] | downstream | 0.45 |
| [[p03_sp_llm_judge_builder]] | downstream | 0.43 |
| [[bld_output_template_llm_judge]] | downstream | 0.42 |
| [[p07_llm_judge]] | downstream | 0.40 |
| [[p01_kc_llm_judge]] | sibling | 0.39 |
| [[llm-judge-builder]] | downstream | 0.39 |
| [[bld_collaboration_llm_judge]] | downstream | 0.36 |
| [[bld_tools_llm_judge]] | downstream | 0.36 |
