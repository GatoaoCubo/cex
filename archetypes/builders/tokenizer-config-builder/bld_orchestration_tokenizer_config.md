---
kind: collaboration
id: bld_orchestration_tokenizer_config
pillar: P12
llm_function: COLLABORATE
purpose: How tokenizer-config-builder works in crews
quality: null
title: "Tokenizer Config Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, collaboration]
tldr: "Orchestration protocol for tokenizer config: workflow integration, handoff signals, dependency management, and cross-nucleus coordination for bpe, sentencepiece, or tiktoken tokenizer parameters and vocabulary configuration."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_tokenizer_config
---

# Collaboration: tokenizer-config-builder

## My Role in Crews

I am a SPECIALIST. I answer: "which tokenizer, with what parameters, for this model?"
I do not configure embeddings. I do not set up inference.
I configure tokenization so text is correctly split into tokens.

## Crew Compositions

### Crew: "Model Configuration Stack"
```
1. tokenizer-config-builder -> "tokenizer algorithm and vocabulary"
2. embedding-config-builder -> "embedding model and dimensions"
3. inference-config-builder -> "serving parameters"
```

## Handoff Protocol

### I Receive
- seeds: target model, use case, language requirements

### I Produce
- tokenizer_config artifact (.md with YAML frontmatter)

### I Signal
- signal: complete (with quality score)

## Builders I Depend On
None -- independent builder.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| embedding-config-builder | Needs tokenizer for chunk boundary calculation |
| inference-config-builder | Needs tokenizer for input processing |

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| embedding_config | upstream | Must exist before tokenizer config production |
| model_provider | upstream | Must exist before tokenizer config production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| embedding_config | yes | Upstream artifact for tokenizer config |
| model_provider | yes | Upstream artifact for tokenizer config |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | tokenizer config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
