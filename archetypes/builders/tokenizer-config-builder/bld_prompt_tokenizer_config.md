---
kind: instruction
id: bld_prompt_tokenizer_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for tokenizer_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: null
title: "Tokenizer Config Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, instruction]
tldr: "Prompt engineering for tokenizer config: structure template, token budget, style constraints, and role framing for bpe, sentencepiece, or tiktoken tokenizer parameters and vocabulary configuration."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_tokenizer_config
  - bld_schema_tokenizer_config
---

# Instructions: How to Produce a tokenizer_config

## Phase 1: RESEARCH

1. Identify the target model or pipeline that will consume this tokenizer
2. Determine the required tokenization algorithm (BPE, SentencePiece, WordPiece)
3. Look up model-specific tokenizer requirements (vocabulary size, special tokens)
4. Identify the tokenizer library (tiktoken, sentencepiece, huggingface/tokenizers)
5. Determine max_length and padding strategy for the use case
6. Check existing tokenizer_config artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Fill all frontmatter fields; set quality: null
3. Write Algorithm section: tokenizer type, library, version
4. Write Vocabulary section: size, encoding type, language coverage
5. Write Special Tokens section: BOS, EOS, PAD, UNK mappings
6. Write Limits section: max_length, truncation strategy, padding direction
7. Write Compatibility section: which models this config supports

## Phase 3: VALIDATE

1. Check HARD gates: YAML parses, id matches pattern, kind correct
2. Verify algorithm specified with library reference
3. Verify special tokens defined
4. Verify max_length set
5. Cross-check: this is TOKENIZER CONFIG, not model config or embedding config
6. If score < 8.0: revise before outputting

## Token Budget

| Component | Allocation | Notes |
|-----------|-----------|-------|
| System prompt | 15%% | Builder identity + sin lens |
| Context (ISOs) | 40%% | 12 ISOs loaded per builder |
| Domain knowledge | 25%% | KCs + examples + memory |
| Generation headroom | 20%% | Artifact output space |

## Style Constraints

| Dimension | Guideline |
|-----------|-----------|
| Voice | Technical, precise, builder-appropriate |
| Structure | Tables over prose; data over description |
| Density | >= 0.85; every sentence adds information |
| References | Use canonical kind names, not synonyms |

## Properties

| Property | Value |
|----------|-------|
| Kind | `prompt` |
| Pillar | P03 |
| Domain | tokenizer config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
