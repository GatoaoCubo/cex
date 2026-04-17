---
kind: instruction
id: bld_instruction_model_architecture
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for model_architecture
quality: 8.7
title: "Instruction Model Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_architecture, builder, instruction]
tldr: "Step-by-step production process for model_architecture"
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

# Instructions: How to Produce a model_architecture
## Phase 1: RESEARCH
1. Identify architecture type: transformer, cnn, rnn, mlp, diffusion, graph, or hybrid
2. Define input/output modality: text, image, audio, video, multimodal, tabular
3. Specify scale: parameter count (e.g., 7B, 340M), depth (layers), width (hidden dim)
4. Map layer structure: encoder, decoder, encoder-decoder, causal, bidirectional
5. Define connectivity: sequential, residual/skip connections, attention heads, pooling
6. Determine compute profile: FLOPs per forward pass, memory footprint, inference latency
7. Check existing model_architecture artifacts via retriever -- avoid duplicating same family
## Phase 2: COMPOSE
1. Read bld_schema_model_architecture.md -- source of truth for all required fields
2. Fill required frontmatter: id, kind, pillar, title, architecture_type, parameter_count, quality: null
3. Write **Overview**: design goals, novelty vs prior work, target use cases
4. Write **Layer Structure**: ordered table with layer type, count, hidden dim, activation
5. Write **Connectivity Pattern**: attention patterns, residual connections, pooling strategy
6. Write **Parameter Profile**: total params, breakdown by component (embedding, attention, FFN)
7. Write **Compute Profile**: inference FLOPs, peak memory, throughput (tokens/s)
8. Write **Training Considerations**: init strategy, optimizer recommendation, LR schedule
9. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Confirm frontmatter parses without errors
2. Confirm `id` matches `^p02_ma_[a-z][a-z0-9_]+$`
3. Confirm `architecture_type` from allowed enum
4. Confirm `parameter_count` is explicit (not null or TBD)
5. Confirm Layer Structure table has at least 3 rows
6. Confirm Parameter Profile includes total count
7. Confirm no credentials, proprietary weights, or API keys appear
8. Confirm `quality` is null
9. Cross-check: structure spec -> model_architecture; training job -> finetune_config; deployed model docs -> model_card
10. If score < 8.0: revise before outputting

