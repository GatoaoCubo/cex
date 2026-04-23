---
kind: schema
id: bld_schema_tokenizer_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for tokenizer_config
quality: null
title: "Tokenizer Config Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, schema]
tldr: "Schema for tokenizer config artifacts -- fields, types, and constraints."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_tokenizer_config
  - bld_eval_tokenizer_config
---

# Schema: tokenizer_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_tc_{slug}) | YES | - | Namespace compliance |
| kind | literal "tokenizer_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| algorithm | enum (bpe, sentencepiece, wordpiece, unigram) | YES | - | Tokenization algorithm |
| library | string | YES | - | Implementation library |
| vocab_size | integer | YES | - | Vocabulary size |
| max_length | integer | YES | - | Maximum sequence length |
| padding | enum (left, right) | REC | "right" | Padding direction |
| truncation | boolean | REC | true | Truncate beyond max_length |
| special_tokens | map | REC | - | BOS, EOS, PAD, UNK mappings |
| domain | string | YES | - | Target domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "tokenizer" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p09_tc_[a-z][a-z0-9_]+$`

## Body Structure (required sections)

1. `## Algorithm` -- tokenizer type, library, version
2. `## Vocabulary` -- size, encoding, language coverage
3. `## Special Tokens` -- BOS, EOS, PAD, UNK mappings
4. `## Limits` -- max_length, truncation, padding
5. `## Compatibility` -- supported models

## Constraints

- naming: p09_tc_{tokenizer_slug}.md
- algorithm MUST be one of: bpe, sentencepiece, wordpiece, unigram
- vocab_size MUST be positive integer
- max_length MUST be positive integer
- quality: null always
