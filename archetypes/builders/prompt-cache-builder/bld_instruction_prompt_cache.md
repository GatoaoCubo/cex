---
kind: instruction
id: bld_instruction_prompt_cache
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prompt_cache
pattern: 3-phase pipeline (research -> compose -> validate)
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
