---
quality: 8.9
quality: 8.1
kind: instruction
id: bld_instruction_user_model
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for user_model
pattern: 3-phase pipeline (design -> compose -> validate)
title: "Instruction: user-model-builder"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, instruction, honcho, dialectic]
tldr: "3-phase pipeline: design peer identity + configure dialectic loop + validate boundaries vs entity_memory/session_state."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_context_doc
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_enum_def
  - bld_instruction_hook_config
---

# Instructions: How to Produce a user_model

## Phase 1: DESIGN

1. Identify the peer: what human is being modeled? What is their peer_id and workspace?
2. Determine scope: single-tenant (default workspace) or multi-tenant (explicit workspace_id)?
3. Define Collections: what fact categories does this peer need? (minimum: preferences, working_style, context_history)
4. Choose storage backend: SQLite (default for local/dev), pgvector (production with vector search), fallback chain
5. Configure dialectic loop: pre_response_insight=true (default), post_response_derive=true (default), compaction_cadence_turns (default 50)
6. Set retention policy: messages_ttl_days (default 365), derived_facts_ttl_days (default null = keep forever)
7. Check for existing user_model for this peer -- update, don't duplicate
8. Confirm peer_id slug: snake_case, lowercase, no hyphens, <= 30 chars

## Phase 2: COMPOSE

1. Read bld_schema_user_model.md -- source of truth for all fields
2. Read bld_output_template_user_model.md -- fill template variables following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null -- never self-score)
4. Write peer profile section: 2 sentences -- who this peer is and workspace context
5. Write Collections section: tables for preferences, working_style, context_history
6. Write dialectic loop status table: phase, status, last_run
7. Write API surface table: all 5 methods with signatures and purposes
8. Write update history: initial version entry
9. Verify body <= 4096 bytes
10. Verify id matches `^um_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE

1. Check bld_quality_gate_user_model.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `um_` prefix
4. Confirm kind == user_model
5. Confirm storage.primary is one of: sqlite, pgvector, turbopuffer, lancedb
6. Confirm collections list is non-empty (>= 3 named collections)
7. Confirm dialectic.compaction_cadence_turns is a positive integer
8. HARD gates: frontmatter valid, id pattern matches, collections non-empty, storage declared
9. SOFT gates: score against quality gate -- target >= 8.0 before outputting
10. Cross-check kind boundaries:
    - No entity-centric attribute maps (that is entity_memory)
    - No ephemeral runtime flags (that is session_state)
    - Not describing the AI agent (that is agent_profile)
    - Not a raw event log (that is episodic_memory)
11. Revise if score < 8.0 -- most common fix: missing collections or undefined dialectic config


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.41 |
| [[bld_instruction_output_validator]] | sibling | 0.40 |
| [[bld_instruction_retriever_config]] | sibling | 0.40 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.38 |
| [[bld_instruction_prompt_version]] | sibling | 0.38 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.38 |
| [[bld_instruction_constraint_spec]] | sibling | 0.37 |
| [[bld_instruction_enum_def]] | sibling | 0.37 |
| [[bld_instruction_hook_config]] | sibling | 0.37 |
