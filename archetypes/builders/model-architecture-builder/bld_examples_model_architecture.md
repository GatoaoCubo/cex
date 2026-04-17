---
kind: examples
id: bld_examples_model_architecture
pillar: P07
llm_function: GOVERN
quality: 9.1
title: "Examples Model Architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, examples, P02, deep_learning]
tldr: "Canonical examples for model_architecture: transformer decoder, CNN encoder, hybrid multimodal."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Examples: model_architecture Artifacts

## Example 1: Causal Decoder (LLaMA-style)
```yaml
---
id: p02_ma_llama_style_7b
kind: model_architecture
pillar: P02
title: "LLaMA-style 7B Causal Decoder"
architecture_type: transformer
parameter_count: "7B"
domain: NLP
quality: null
---
## Layer Structure
| # | Layer Type | Count | Hidden Dim | Heads | Notes |
|---|-----------|-------|-----------|-------|-------|
| 1 | Token Embedding | 1 | 4096 | - | vocab=32000 |
| 2 | RMSNorm | 32 | 4096 | - | pre-norm |
| 3 | Grouped Query Attention | 32 | 4096 | 32/8 | GQA |
| 4 | FFN (SwiGLU) | 32 | 11008 | - | gated activation |
## Parameter Profile
| Component | Params |
|-----------|--------|
| Embeddings | 131M |
| Attention | 2.1B |
| FFN | 4.5B |
| Norms + biases | 50M |
| Total | ~7B |
```

## Example 2: Vision Transformer (ViT-B)
```yaml
---
id: p02_ma_vit_base
kind: model_architecture
pillar: P02
title: "Vision Transformer ViT-B/16"
architecture_type: transformer
parameter_count: "86M"
domain: vision
quality: null
---
## Layer Structure
| Layer | Count | Dim | Notes |
|-------|-------|-----|-------|
| Patch Embedding | 1 | 768 | 16x16 patches |
| CLS Token | 1 | 768 | prepended |
| Position Embedding | 1 | 768 | learned |
| Transformer Encoder | 12 | 768 | 12 heads |
| MLP Head | 1 | num_classes | linear probe |
```

## Anti-Pattern: Incomplete Layer Table
```yaml
---
id: p02_ma_incomplete
kind: model_architecture
pillar: P02
title: "Some Transformer"
architecture_type: transformer
parameter_count: "unknown"
quality: 9.0
---
## Architecture
A transformer model with some layers.
```
### Why it fails
- `parameter_count: unknown` violates required specificity
- No Layer Structure table (required section)
- `quality: 9.0` -- never self-score, always null
- Prose instead of structured tables

## Pattern Recognition
| Anti-Pattern | Why Wrong | Correct Approach |
|-------------|-----------|-----------------|
| quality not null | Self-scoring | Set quality: null always |
| Missing layer table | Vague spec | Add ordered layer table |
| No param count | Incomplete | Specify count (e.g., "7B", "340M") |
| Prose only | Low density | Use tables for structure |
| Wrong architecture_type | Routing failure | Use exact enum value |
