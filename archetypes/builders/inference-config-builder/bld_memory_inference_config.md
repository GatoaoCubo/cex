---
id: bld_memory_inference_config
kind: learning_record
pillar: P10
version: 1.0.0
created: "2026-04-23"
updated: "2026-04-23"
author: builder_agent
observation: "VRAM budget must account for model weights + KV-cache + overhead. A 7B fp16 model uses ~14GB VRAM for weights alone; KV-cache for long contexts adds 2-4GB. Continuous batching improves throughput 3-5x over static batching but requires framework support."
pattern: "Calculate VRAM as: model_params * bytes_per_param + kv_cache_budget + 2GB overhead. Use continuous batching when framework supports it. Always set max_concurrent based on measured VRAM usage, not estimates."
evidence: "Continuous batching improved throughput from 15 to 60 tokens/sec on identical hardware. VRAM overcommit caused OOM crashes in 100% of cases."
confidence: 0.82
outcome: SUCCESS
domain: inference_config
tags: [inference, serving, performance, learning]
tldr: "Budget VRAM for weights+KV+overhead, use continuous batching, measure before setting concurrency."
quality: null
title: "Inference Config Builder - Memory ISO"
density_score: 0.85
llm_function: INJECT
related:
  - bld_knowledge_inference_config
---

## Summary

VRAM budget and batching strategy are the two most impactful inference configuration decisions. Underestimating VRAM causes crashes; static batching wastes GPU cycles.

## Pattern

**VRAM calculation**: model_params * bytes_per_param (2 for fp16, 1 for int8, 0.5 for int4) + KV-cache budget + 2GB overhead margin.

**Continuous batching**: always prefer over static when the framework supports it. 3-5x throughput improvement at no quality cost.

**Concurrency**: measure actual VRAM usage under load before setting max_concurrent. Estimates are unreliable.
