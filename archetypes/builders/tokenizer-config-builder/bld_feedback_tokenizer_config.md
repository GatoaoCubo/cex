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
