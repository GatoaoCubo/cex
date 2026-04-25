---
id: bld_feedback_tokenizer_config
kind: builder_default
pillar: P11
title: "Tokenizer Config Builder - Feedback ISO"
domain: tokenizer_config
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, tokenizer_config]
related:
  - bld_eval_tokenizer_config
tldr: "Anti-patterns and correction protocol for tokenizer config builders."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Tokenizer Config

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score | H05 |
| No mismatched tokenizer | Never pair wrong tokenizer with model | D5 |
| No missing special tokens | Always define BOS, EOS, PAD, UNK | D3 |
| No unbounded length | Always set max_length | D4 |
| No frontmatter omission | Valid YAML frontmatter required | H01 |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| Wrong algorithm for model | Model produces garbage | Verify tokenizer-model compatibility |
| Missing EOS token | Infinite generation | Add EOS token mapping |
| Vocab size mismatch | Embedding table errors | Match vocab to model specs |
| No padding strategy | Batch processing fails | Specify padding direction |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify failed gate | F7 |
| 2 | Return to F6 with fix | F6 |
| 3 | Re-run F7 | F7 |
| 4 | Max 2 retries | F8 |

## Quality Dimensions

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| D1 Structural completeness | 20%% | All required sections present |
| D2 Domain accuracy | 25% | Content matches tokenizer config domain |
| D3 Density | 20%% | >= 0.85 information density |
| D4 Cross-references | 15%% | Valid links to related artifacts |
| D5 Actionability | 20%% | Builder can produce from this alone |

## Common Failures

| Failure | Frequency | Fix |
|---------|-----------|-----|
| Generic content | High | Add domain-specific examples |
| Missing boundary adherence | Medium | Check kinds_meta.json boundary |
| Low density score | Medium | Replace prose with tables |

## Properties

| Property | Value |
|----------|-------|
| Kind | `feedback` |
| Pillar | P11 |
| Domain | tokenizer config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
