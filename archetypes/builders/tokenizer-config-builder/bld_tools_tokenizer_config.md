---
kind: tools
id: bld_tools_tokenizer_config
pillar: P04
llm_function: CALL
purpose: Tools available for tokenizer_config production
quality: null
title: "Tokenizer Config Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, tools]
tldr: "Tools available for tokenizer config production."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_tokenizer_config
---

# Tools: tokenizer-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile artifact to YAML | Phase 3 | ACTIVE |
| cex_score.py | Score artifact quality | Phase 3 | ACTIVE |
| cex_retriever.py | Find similar configs | Phase 1 | ACTIVE |
| cex_doctor.py | Health check | Phase 3 | ACTIVE |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions |
| tiktoken docs | github.com/openai/tiktoken | OpenAI tokenizer specs |
| SentencePiece docs | github.com/google/sentencepiece | Google tokenizer specs |
| HF Tokenizers | huggingface.co/docs/tokenizers | HuggingFace tokenizer library |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| DENIED | (none) | -- |
