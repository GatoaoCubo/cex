---
kind: knowledge_card
id: bld_knowledge_card_model_architecture
pillar: P01
llm_function: INJECT
quality: 9.0
title: "Knowledge Card: model_architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, knowledge_card, P02, deep_learning]
tldr: "Core knowledge for model_architecture artifacts: architecture types, layer patterns, connectivity, and compute profiles."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p10_lr_model_architecture_builder
  - bld_instruction_model_architecture
  - bld_examples_model_architecture
  - p03_sp_model_architecture_builder
  - bld_output_template_model_architecture
  - p11_qg_model_architecture
  - bld_schema_model_architecture
  - bld_tools_model_architecture
  - bld_architecture_model_architecture
  - bld_collaboration_model_architecture
---

# Knowledge: model_architecture

## Architecture Type Reference
| Type | Core Mechanism | Strengths | Weaknesses |
|------|---------------|-----------|-----------|
| transformer | self-attention O(n^2) | long-range deps, parallelizable | quadratic memory |
| cnn | local receptive field | translation invariance, efficient | limited global context |
| rnn | recurrent hidden state | sequential modeling | vanishing gradients, slow |
| mlp | fully connected layers | universal approximator | no inductive bias |
| diffusion | iterative denoising | high quality generation | slow inference |
| graph | message passing | relational reasoning | scalability limits |
| hybrid | combined mechanisms | best of both | higher complexity |

## Layer Structure Patterns
| Pattern | Description | Used In |
|---------|-------------|---------|
| encoder-only | Bidirectional attention over full input | BERT, RoBERTa |
| decoder-only | Causal (left-to-right) attention | GPT, LLaMA, Claude |
| encoder-decoder | Encode input, decode output | T5, BART, Whisper |
| prefix-decoder | Bidirectional prefix + causal | UniLM, GLM |
| U-Net | Encoder + decoder with skip connections | Diffusion, segmentation |

## Parameter Distribution (Transformer)
| Component | % of Params | Notes |
|-----------|-----------|-------|
| Token embeddings | 10-20% | vocab_size x hidden_dim |
| Attention (Q,K,V,O) | 30-40% | 4 x hidden_dim^2 per layer |
| FFN | 40-50% | 2 x hidden_dim x ffn_dim per layer |
| Layer norm | <1% | 2 x hidden_dim per layer |
| Output head | <5% | tied with embeddings often |

## Compute Profiles by Scale
| Scale | Params | Training FLOPs | Inference Memory |
|-------|--------|---------------|-----------------|
| small | <1B | <10^22 | <4GB |
| medium | 1-13B | 10^22-10^23 | 4-26GB |
| large | 13-70B | 10^23-10^24 | 26-140GB |
| xlarge | >70B | >10^24 | >140GB (distributed) |

## Boundary Conditions
| Situation | Use This | Not This |
|-----------|----------|---------|
| "Define transformer layer structure" | model_architecture | finetune_config |
| "Configure LoRA training job" | finetune_config | model_architecture |
| "Document GPT-4o capabilities" | model_card | model_architecture |
| "Route requests to Claude vs GPT" | model_provider | model_architecture |
| "Training paradigm for pre-training" | training_method | model_architecture |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_model_architecture_builder]] | downstream | 0.46 |
| [[bld_instruction_model_architecture]] | downstream | 0.42 |
| [[bld_examples_model_architecture]] | downstream | 0.41 |
| [[p03_sp_model_architecture_builder]] | downstream | 0.37 |
| [[bld_output_template_model_architecture]] | downstream | 0.35 |
| [[p11_qg_model_architecture]] | downstream | 0.29 |
| [[bld_schema_model_architecture]] | downstream | 0.29 |
| [[bld_tools_model_architecture]] | downstream | 0.27 |
| [[bld_architecture_model_architecture]] | downstream | 0.25 |
| [[bld_collaboration_model_architecture]] | downstream | 0.21 |
