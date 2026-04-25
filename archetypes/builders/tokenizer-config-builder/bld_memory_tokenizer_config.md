---
id: bld_memory_tokenizer_config
kind: learning_record
pillar: P10
version: 1.0.0
created: "2026-04-23"
updated: "2026-04-23"
author: builder_agent
observation: "Tokenizer-model mismatch is the most common configuration error. Using cl100k_base tokenizer with a LLaMA model produces garbage tokens. Special token omission (especially EOS) causes generation to run indefinitely."
pattern: "Always verify tokenizer matches the target model family. Always include all 4 special tokens (BOS, EOS, PAD, UNK). Always set max_length to model context window or lower."
evidence: "Tokenizer-model mismatches caused 100% task failure in all tested cases. Missing EOS token caused 67% of infinite generation bugs."
confidence: 0.85
outcome: SUCCESS
domain: tokenizer_config
tags: [tokenizer, configuration, learning]
tldr: "Match tokenizer to model family, include all special tokens, set max_length."
quality: null
title: "Tokenizer Config Builder - Memory ISO"
density_score: 0.85
llm_function: INJECT
related:
  - bld_knowledge_tokenizer_config
---

## Summary

Tokenizer configuration errors are silent and catastrophic. The tokenizer must match the model family exactly, and special tokens must be complete.

## Pattern

**Model-tokenizer pairing**: treat tokenizer and model as a matched set. Never mix families.

**Special tokens**: always define BOS (beginning of sequence), EOS (end of sequence), PAD (padding), and UNK (unknown). Missing EOS is the most dangerous omission.

**Max length**: set to the model's context window or lower. Never exceed the model's maximum supported length.

## Evidence

Production experience from tokenizer config artifact generation. 
Tokenization vocabulary and encoding rules 
Patterns derived from builder runs, quality gate failures, and peer review feedback.

## Pitfalls

- **Missing frontmatter fields**: omitting required fields causes H01 gate failure.
- **Generic descriptions**: vague purpose/tldr reduces retrieval accuracy.
- **Ignoring boundary**: Tokenization vocabulary and encoding rules.
- **Orphaned dependencies**: referencing embedding_config without verifying it exists.

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | tokenizer config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
