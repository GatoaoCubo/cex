---
kind: architecture
id: bld_architecture_tokenizer_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of tokenizer_config
quality: null
title: "Tokenizer Config Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, architecture]
tldr: "Architecture context for tokenizer config: components, dependencies, and boundary."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_tokenizer_config
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| algorithm | Tokenization method (BPE, SentencePiece) | tokenizer-config-builder | required |
| library | Implementation (tiktoken, sentencepiece) | tokenizer-config-builder | required |
| vocab_size | Token vocabulary cardinality | tokenizer-config-builder | required |
| special_tokens | BOS, EOS, PAD, UNK token mappings | tokenizer-config-builder | required |
| max_length | Maximum sequence length | tokenizer-config-builder | required |
| padding | Padding direction and strategy | tokenizer-config-builder | optional |

## Dependency Graph

```
tokenizer_config --consumed_by--> embedding_config (P01, chunk tokenization)
tokenizer_config --consumed_by--> inference_config (P09, input processing)
tokenizer_config --consumed_by--> distillation_config (P02, training data prep)
tokenizer_config --independent-- knowledge_index (P10)
```

## Boundary Table

| tokenizer_config IS | tokenizer_config IS NOT |
|--------------------|------------------------|
| Tokenization parameters: algorithm, vocab, tokens | An embedding_config -- embedding configures vectorization |
| Defines how text becomes token sequences | An inference_config -- inference configures model serving |
| Infrastructure spec consumed by multiple pipelines | A model_provider -- provider manages model hosting |
