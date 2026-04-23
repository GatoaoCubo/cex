---
kind: quality_gate
id: bld_eval_tokenizer_config
pillar: P07
llm_function: GOVERN
purpose: Quality gate for tokenizer_config artifacts
quality: null
title: "Tokenizer Config Builder - Eval ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, quality_gate]
tldr: "Quality gate for tokenizer config: validates algorithm, vocabulary, special tokens, and compatibility."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_tokenizer_config
---

## Quality Gate

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match ^p09_tc_[a-z][a-z0-9_]+$ |
| H03 | kind field matches | kind is not 'tokenizer_config' |
| H04 | algorithm defined | algorithm field missing or not in enum |
| H05 | quality is null | quality must be null |
| H06 | Required fields present | Missing required fields |
| H07 | vocab_size is integer | vocab_size is not a positive integer |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Algorithm clarity | 0.20 | Algorithm and library specified with version |
| D2 | Vocab coverage | 0.15 | Vocabulary size justified for use case |
| D3 | Special tokens | 0.15 | BOS/EOS/PAD/UNK explicitly mapped |
| D4 | Limits defined | 0.15 | max_length and truncation strategy documented |
| D5 | Model compatibility | 0.15 | Compatible models listed |
| D6 | Encoding spec | 0.10 | UTF-8, byte-level, or other encoding specified |
| D7 | Documentation | 0.10 | tldr captures key info |

## Actions

| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |
