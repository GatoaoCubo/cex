---
quality: 8.3
kind: instruction
id: bld_instruction_prospective_memory
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prospective_memory
title: "Instruction Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, instruction]
tldr: "3-phase: define triggers and action payloads, compose with priority and expiry, validate gates."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_instruction_schedule
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_handoff_protocol
  - bld_instruction_hook_config
  - bld_instruction_context_doc
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_constraint_spec
---

# Instructions: How to Produce a prospective_memory

## Phase 1: DEFINE
1. Identify the agent that owns this prospective memory store
2. List the future actions/reminders to schedule
3. For each action, determine trigger_type: time (cron/datetime), event (signal received), condition (state meets criterion)
4. Define action_payload for each: what should the agent do when triggered
5. Set priority for ordering concurrent triggers
6. Determine expiry: when does the reminder become irrelevant
7. Define completion_policy: mark_done (one-shot) or re_schedule (recurring)
8. Identify execution_mechanism: CEX schedule signal, polling, wake notification

## Phase 2: COMPOSE
1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter with all required fields (quality: null)
3. Write reminders array: each entry has trigger, action_payload, priority, expiry
4. Declare owner and execution_mechanism
5. Write Overview: what agent and what kinds of future actions
6. Write Reminders table: trigger type, action, priority, expiry
7. Write Execution section: how reminders are checked and fired
8. Verify body <= 2048 bytes

## Phase 3: VALIDATE
1. Confirm id matches `^p10_pm_[a-z][a-z0-9_]+$`
2. Confirm kind == prospective_memory
3. Confirm reminders array has >= 1 entry
4. Confirm each reminder has trigger_type and action_payload
5. Confirm owner declared
6. Cross-check: not schedule kind (no cron workflow config), not session_state (not current session)
7. Revise if score < 8.0


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_schedule]] | sibling | 0.37 |
| [[bld_instruction_memory_scope]] | sibling | 0.34 |
| [[bld_instruction_output_validator]] | sibling | 0.33 |
| [[bld_instruction_retriever_config]] | sibling | 0.32 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.31 |
| [[bld_instruction_hook_config]] | sibling | 0.31 |
| [[bld_instruction_context_doc]] | sibling | 0.31 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.30 |
| [[bld_instruction_prompt_version]] | sibling | 0.30 |
| [[bld_instruction_constraint_spec]] | sibling | 0.29 |
