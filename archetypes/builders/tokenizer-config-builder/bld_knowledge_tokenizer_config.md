---
kind: knowledge_card
id: bld_knowledge_tokenizer_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for tokenizer_config production -- tokenizer selection and configuration
sources: SentencePiece, tiktoken, HuggingFace tokenizers, BPE literature
quality: null
title: "Tokenizer Config Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, knowledge]
tldr: "Domain knowledge for tokenizer configuration: BPE, SentencePiece, tiktoken, vocabulary size, and special tokens."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_tokenizer_config
  - bld_schema_tokenizer_config
---

# Domain Knowledge: tokenizer_config

## Executive Summary

Tokenizer configs define how raw text is split into tokens for LLM processing. They specify the tokenization algorithm (BPE, WordPiece, Unigram, SentencePiece), vocabulary size, special tokens, and encoding parameters. A tokenizer_config is a P09 artifact -- it configures the TOKENIZATION process, not the model architecture.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| Algorithms | BPE, WordPiece, Unigram, SentencePiece |
| Key libraries | tiktoken, sentencepiece, huggingface/tokenizers |
| Vocab sizes | 32K (GPT-2), 50K (LLaMA), 100K (GPT-4/cl100k), 128K+ |
| Special tokens | BOS, EOS, PAD, UNK, SEP, MASK |

## Patterns

- **BPE (Byte Pair Encoding)** -- most common; merges frequent byte pairs iteratively; used by GPT family
- **SentencePiece** -- language-agnostic; treats input as raw bytes; used by LLaMA, T5
- **WordPiece** -- splits at word boundaries first then sub-word; used by BERT
- **Vocab size trade-off** -- larger vocab = shorter sequences but larger embedding table and memory
- **Special tokens** -- must match model expectations; mismatched BOS/EOS causes generation failures
- **Padding strategy** -- left-pad for generation, right-pad for classification

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Wrong tokenizer for model | Model expects specific tokenization; mismatch corrupts input |
| Missing special tokens | BOS/EOS omission causes generation to never terminate |
| Vocab size mismatch | Tokenizer vocab must match model embedding table size |
| No max_length config | Unbounded sequences cause OOM errors |
| Ignoring encoding | UTF-8 vs byte-level encoding affects multilingual support |
