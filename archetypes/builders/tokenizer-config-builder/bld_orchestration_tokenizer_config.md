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
tldr: "Crew collaboration protocol for tokenizer config builder."
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
