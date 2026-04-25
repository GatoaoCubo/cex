---
id: kc_tokenizer_config
kind: knowledge_card
8f: F3_inject
title: Tokenizer Config -- BPE/SentencePiece/Tiktoken Parameters
version: 1.0.0
quality: null
pillar: P01
tags:
  - tokenizer
  - bpe
  - sentencepiece
  - vocabulary
  - P09
tldr: "BPE/SentencePiece/Tiktoken parameters -- vocab size, special tokens, merge table, byte fallback"
when_to_use: "When configuring how text is segmented into tokens for an LLM pipeline"
related:
  - kc_embedding_config
  - kc_context_window_config
  - kc_model_provider
  - kc_inference_config
  - kc_finetune_config
---

# Tokenizer Config

A tokenizer config defines the parameters that control how raw text is segmented into tokens -- the atomic units that language models process. Tokenization is the first transformation in every LLM pipeline and the last transformation on every output. Errors at this layer propagate silently through every downstream component.

## Description

The tokenizer sits between human text and model computation. It determines vocabulary size (how many unique tokens the model knows), special tokens (control signals like beginning-of-sequence or end-of-turn), byte-fallback behavior (how unknown characters are handled), pre-tokenization rules (whitespace splitting, regex patterns), and merge operations (how subwords are combined).

Tokenizer choice has outsized impact: the same sentence can be 15 tokens or 45 tokens depending on the tokenizer, directly affecting context window utilization, inference cost, and multilingual performance. A poorly configured tokenizer makes some languages 3-5x more expensive to process than others -- not because the model is biased, but because the tokenizer undertrained on those scripts.

The key insight: tokenization is not a preprocessing detail. It is an architectural decision that constrains everything the model can learn and how efficiently it operates.

## Key Concepts

| Concept | Definition | Impact |
|---------|-----------|--------|
| Vocab Size | Total number of unique tokens in the vocabulary | Larger = better compression but bigger embedding table |
| BPE (Byte Pair Encoding) | Iterative merge algorithm: find most frequent byte pair, merge, repeat | Most common algorithm for modern LLMs |
| SentencePiece | Unigram or BPE tokenizer that treats input as raw bytes (no pre-tokenization) | Language-agnostic, handles any Unicode |
| Special Tokens | Control tokens (BOS, EOS, PAD, SEP, tool-use markers) | Must match model training; mismatches cause silent failures |
| Byte Fallback | Encoding unknown characters as raw byte sequences | Prevents UNK tokens but inflates sequence length |
| Pre-tokenization | Rules applied before BPE/unigram (whitespace split, digit split, regex) | Controls merge boundaries -- digits, punctuation, whitespace |
| Merge Table | Ordered list of subword merges learned during tokenizer training | Deterministic: same merges = same tokenization |
| Fertility | Average number of tokens per word for a given language | Measures tokenizer efficiency across languages |

## Related Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| embedding_config | P01 | Downstream -- embedding dimensions must match tokenizer vocab |
| context_window_config | P03 | Constraint -- token count determines context budget |
| model_provider | P02 | Upstream -- each provider ships a fixed tokenizer |
| inference_config | P09 | Sibling -- max_tokens is measured in tokenizer units |
| finetune_config | P02 | Downstream -- fine-tuning inherits the base tokenizer |
| prompt_template | P03 | Consumer -- templates must respect token boundaries |
| dataset_card | P01 | Consumer -- dataset stats are measured in tokens |

## Anti-Patterns

- **Ignoring fertility disparity**: Deploying a tokenizer trained predominantly on English text for multilingual applications. Non-Latin scripts may have 3-5x token inflation, making the model impractical for those languages.
- **Special token mismatch**: Using a tokenizer with different special tokens than the model expects. The model silently interprets control signals as content, producing incoherent output.
- **Counting characters instead of tokens**: Estimating context usage by character count. A 4000-character prompt can be anywhere from 800 to 2000 tokens depending on content and tokenizer.
- **Hardcoding token IDs**: Referencing tokens by numeric ID instead of canonical name. Token IDs change between tokenizer versions; names are stable.
- **Ignoring pre-tokenization rules**: Assuming the tokenizer handles all segmentation. Pre-tokenization rules (digit splitting, whitespace normalization) affect merge behavior and must be documented.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 (knowledge domain), P09 (config domain) |
| Domain | Text preprocessing, model infrastructure |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_embedding_config]] | downstream | 0.44 |
| [[kc_context_window_config]] | constraint | 0.40 |
| [[kc_model_provider]] | upstream | 0.38 |
| [[kc_inference_config]] | sibling | 0.36 |
| [[kc_finetune_config]] | downstream | 0.33 |
| [[kc_prompt_template]] | consumer | 0.30 |
| [[kc_dataset_card]] | consumer | 0.27 |
