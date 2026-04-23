---
kind: instruction
id: bld_instruction_prompt_cache
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prompt_cache
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_examples_prompt_cache
  - bld_instruction_action_prompt
  - bld_instruction_context_window_config
  - bld_instruction_output_validator
  - bld_instruction_prompt_version
  - bld_instruction_retriever_config
  - bld_instruction_golden_test
  - p11_qg_prompt_cache
  - bld_instruction_multi_modal_config
---

# Instructions: How to Produce a prompt_cache
## Phase 1: RESEARCH
1. Identify the target workload: what prompts are being cached?
2. Assess query repetition rate: how many duplicate/similar queries?
3. Determine freshness requirements: how fast does source knowledge change?
4. Profile deployment: single-process, multi-agent, distributed?
5. Check existing cache configs to avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template
3. Set ttl_seconds based on freshness: 60 (real-time), 300 (default), 3600 (stable)
4. Choose eviction_strategy: LRU for varied workloads, LFU for skewed, FIFO for sequential
5. Set max_entries based on memory budget
6. Choose cache_key_method: hash_full for exact match, hash_prefix for shared contexts, semantic for similarity
7. Define invalidation_trigger: ttl_expire (default), content_change (accurate), manual (controlled)
8. Choose storage_backend: memory (fast), redis (shared), sqlite (persistent)
9. Set quality: null
10. Keep file under 2048 bytes
## Phase 3: VALIDATE
1. Verify ttl_seconds is positive integer
2. Check eviction_strategy is valid enum
3. Check cache_key_method is valid enum
4. Check storage_backend is valid enum
5. Verify id matches `p10_pc_[a-z][a-z0-9_]+`
6. Check total file under 2048 bytes
7. If any gate fails: fix and re-validate

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify prompt
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | prompt cache construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.34 |
| [[bld_examples_prompt_cache]] | downstream | 0.33 |
| [[bld_instruction_action_prompt]] | sibling | 0.32 |
| [[bld_instruction_context_window_config]] | sibling | 0.32 |
| [[bld_instruction_output_validator]] | sibling | 0.32 |
| [[bld_instruction_prompt_version]] | sibling | 0.32 |
| [[bld_instruction_retriever_config]] | sibling | 0.31 |
| [[bld_instruction_golden_test]] | sibling | 0.30 |
| [[p11_qg_prompt_cache]] | downstream | 0.30 |
| [[bld_instruction_multi_modal_config]] | sibling | 0.30 |
