---
id: kc_inference_config
kind: knowledge_card
8f: F3_inject
title: Inference Config -- Generation-Time Parameters
version: 1.0.0
quality: null
pillar: P01
tags:
  - inference
  - generation
  - sampling
  - decoding
  - P09
related:
  - kc_model_provider
  - kc_thinking_config
  - kc_context_window_config
  - kc_tokenizer_config
  - kc_prompt_template
  - kc_rate_limit_config
---

# Inference Config

An inference config defines the generation-time parameters that control how a language model samples its next token. These parameters do not change what the model knows -- they change how the model expresses what it knows. The same model with different inference configs can produce deterministic, factual output or creative, divergent output.

## Description

At inference time, a language model produces a probability distribution over its entire vocabulary for each next token. The inference config controls how that distribution is transformed into a selection: temperature reshapes the distribution's sharpness, top_p and top_k truncate it, frequency and presence penalties discourage repetition, stop sequences halt generation, and max_tokens caps output length.

These parameters interact non-linearly. Temperature 0.0 with top_p 1.0 is greedy decoding. Temperature 1.0 with top_p 0.1 is nucleus sampling with high entropy but tight truncation. Understanding these interactions is the difference between reliable production systems and systems that occasionally generate garbage.

In the LLM-as-operating-system paradigm, the inference config is analogous to process scheduling parameters: it does not change the program (the model's weights) but determines how the program executes (which outputs get selected).

## Key Concepts

| Concept | Definition | Typical Values |
|---------|-----------|----------------|
| Temperature | Scales logits before softmax; lower = more deterministic | 0.0 (greedy) -- 2.0 (very random); default 0.7-1.0 |
| Top-p (Nucleus Sampling) | Samples from the smallest set of tokens whose cumulative probability >= p | 0.1 (tight) -- 1.0 (full distribution); default 0.9-0.95 |
| Top-k | Samples from the k most probable tokens only | 1 (greedy) -- 100+; default 40-50 |
| Frequency Penalty | Penalizes tokens proportional to their frequency in the output so far | -2.0 -- 2.0; default 0.0 |
| Presence Penalty | Flat penalty for any token that has appeared in the output | -2.0 -- 2.0; default 0.0 |
| Stop Sequences | Strings that halt generation when produced | Task-specific (newlines, delimiters, end tags) |
| Max Tokens | Hard ceiling on output length in tokens | 1 -- model maximum (varies by provider) |
| Seed | Fixed random seed for reproducible sampling | Integer; not all providers support deterministic mode |
| Logit Bias | Per-token probability adjustments before sampling | Dict of token_id -> bias; use sparingly |

## Related Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| model_provider | P02 | Upstream -- the provider determines which parameters are available |
| thinking_config | P09 | Sibling -- thinking_config controls extended reasoning; inference_config controls sampling |
| context_window_config | P03 | Constraint -- max_tokens + input tokens must fit in the context window |
| tokenizer_config | P09 | Dependency -- token counts are measured in tokenizer units |
| prompt_template | P03 | Consumer -- prompts are designed around expected generation behavior |
| rate_limit_config | P09 | Constraint -- output token count affects rate limit consumption |
| guardrail | P11 | Downstream -- guardrails may override inference params for safety |

## Anti-Patterns

- **Temperature 0 everywhere**: Using greedy decoding for all tasks. Creative writing, brainstorming, and diverse generation require temperature > 0. Greedy decoding produces repetitive, mode-collapsed output.
- **Stacking temperature + top_p + top_k**: Applying all three truncation methods simultaneously without understanding their interaction. Pick one primary method (usually temperature + top_p) and leave others at defaults.
- **Ignoring stop sequences**: Letting the model decide when to stop. Without explicit stop sequences, models often generate padding, repeat themselves, or continue past the useful answer.
- **Max tokens as quality control**: Setting max_tokens very low to force concise output. The model does not know about the limit during generation -- it simply gets cut off mid-thought. Use prompt instructions for brevity; use max_tokens as a safety ceiling.
- **Frequency penalty on structured output**: Applying repetition penalties when generating JSON, code, or tables. These formats legitimately repeat tokens (braces, keywords, column headers). Penalties corrupt the structure.
- **No seed for evaluation**: Running evaluations without a fixed seed. Non-reproducible outputs make metric comparison meaningless across runs.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 (knowledge domain), P09 (config domain) |
| Domain | LLM inference, generation control |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_model_provider]] | upstream | 0.44 |
| [[kc_thinking_config]] | sibling | 0.40 |
| [[kc_context_window_config]] | constraint | 0.38 |
| [[kc_tokenizer_config]] | dependency | 0.36 |
| [[kc_prompt_template]] | consumer | 0.33 |
| [[kc_rate_limit_config]] | constraint | 0.30 |
| [[kc_guardrail]] | downstream | 0.27 |
