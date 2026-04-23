---
kind: config
id: bld_config_tokenizer_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions and operational constraints for tokenizer_config
quality: null
title: "Tokenizer Config Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, config]
tldr: "Production config for tokenizer config: naming, paths, and constraints."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_tokenizer_config
---

# Config: tokenizer_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p09_tc_{tokenizer_slug}.md | p09_tc_cl100k_base.md |
| Builder directory | kebab-case | tokenizer-config-builder/ |
| Frontmatter fields | snake_case | vocab_size, max_length |

## File Paths

1. Output: P09_config/examples/p09_tc_{slug}.md
2. Compiled: P09_config/compiled/p09_tc_{slug}.yaml

## Size Limits

1. Body: max 1024 bytes
2. Density: >= 0.85

## Common Tokenizers

| Tokenizer | Algorithm | Vocab Size | Used By |
|-----------|-----------|------------|---------|
| cl100k_base | BPE | 100K | GPT-4, GPT-3.5 |
| o200k_base | BPE | 200K | GPT-4o |
| llama_tokenizer | SentencePiece | 32K | LLaMA family |
| bert_tokenizer | WordPiece | 30K | BERT family |
