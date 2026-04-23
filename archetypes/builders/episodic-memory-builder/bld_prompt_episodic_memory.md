---
quality: 8.7
quality: 8.0
kind: instruction
id: bld_instruction_episodic_memory
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for episodic_memory
title: "Instruction Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, instruction]
tldr: "3-phase: design episode schema and retrieval keys, compose with decay policy, validate gates."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_chunk_strategy
  - bld_instruction_retriever_config
  - bld_instruction_context_doc
  - bld_instruction_handoff_protocol
  - bld_instruction_prompt_version
  - bld_instruction_constraint_spec
  - bld_instruction_search_tool
  - bld_instruction_function_def
---

# Instructions: How to Produce an episodic_memory

## Phase 1: DESIGN
1. Identify the agent or nucleus this episodic store serves
2. Define episode schema: what fields each stored episode has (timestamp, context, outcome, retrieval_keys)
3. Choose retrieval method: recency (most recent N), relevance (embedding similarity), hybrid
4. Set episode_count limit: how many episodes to retain before pruning
5. Define decay policy: time-based decay, relevance decay, or no decay
6. Identify retrieval keys: what queries will surface relevant past episodes
7. Define promotion source: which working_memory promote_targets feed this store
8. Check for existing episodic_memory artifacts with overlapping scope

## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth
2. Read OUTPUT_TEMPLATE.md -- fill all template fields
3. Fill frontmatter: all required fields (quality: null)
4. Write episode_schema: field table with types
5. Write retrieval_config: method and parameters
6. Declare decay_policy with numeric values
7. Write episode_count limit
8. Write 1-2 example episodes to demonstrate schema
9. Write Overview: what agent this serves, why episodic memory is needed
10. Verify body <= 4096 bytes

## Phase 3: VALIDATE
1. Confirm id matches `^p10_ep_[a-z][a-z0-9_]+$`
2. Confirm kind == episodic_memory
3. Confirm episode_schema has >= 3 fields including timestamp
4. Confirm retrieval_method is declared
5. Confirm episode_count limit is numeric
6. Cross-check: no entity facts (entity_memory), no compressed summaries (memory_summary)
7. Revise if score < 8.0 -- most common fix: add retrieval keys or decay policy


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.35 |
| [[bld_instruction_output_validator]] | sibling | 0.34 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.34 |
| [[bld_instruction_retriever_config]] | sibling | 0.33 |
| [[bld_instruction_context_doc]] | sibling | 0.33 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.31 |
| [[bld_instruction_prompt_version]] | sibling | 0.31 |
| [[bld_instruction_constraint_spec]] | sibling | 0.31 |
| [[bld_instruction_search_tool]] | sibling | 0.30 |
| [[bld_instruction_function_def]] | sibling | 0.30 |
