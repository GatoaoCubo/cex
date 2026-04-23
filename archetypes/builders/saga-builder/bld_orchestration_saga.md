---
quality: 8.3
quality: 7.9
id: bld_rules_saga
kind: knowledge_card
pillar: P08
title: "Rules: saga Builder Constraints"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
tags: [rules, saga, P12]
llm_function: COLLABORATE
tldr: "Hard constraints and edge cases for saga builder."
density_score: null
related:
  - bld_knowledge_card_workflow
  - bld_schema_workflow
  - p11_qg_workflow
  - bld_memory_workflow
  - p10_lr_instruction_builder
  - bld_config_workflow
  - p03_sp_workflow-builder
  - bld_instruction_chain
  - bld_norms
  - p03_ins_workflow
---

# Rules: saga Builder

## Hard Constraints
1. EVERY step MUST have a non-null compensating_action
2. steps_count MUST equal len(steps list)
3. topology MUST be specified: choreography | orchestration
4. on_failure MUST be specified at saga level
5. quality MUST be null
6. id pattern: `^p12_saga_[a-z][a-z0-9_]+$`
7. max_bytes: 4096 body

## Edge Cases
| Situation | Resolution |
|-----------|-----------|
| Step cannot be undone (e.g., send email) | Use idempotent compensation (send cancellation email) |
| User conflates with workflow | Teach: workflow has no compensation; saga does |
| User wants 2-phase commit | Redirect: 2PC for ACID; saga for eventual consistency |
| Saga too long (>10 steps) | Split into sub-sagas with handoff signals |
| Compensating action may fail | Mark as `retry` on_failure; compensating actions must be idempotent |
| Choreography vs orchestration unclear | Default to orchestration (easier to trace); document rationale |

## Naming Rules
- File: `p12_saga_{name_slug}.md`
- ID: `p12_saga_{name_slug}`
- Tags: MUST include "saga" + domain

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_workflow]] | sibling | 0.23 |
| [[bld_schema_workflow]] | upstream | 0.22 |
| [[p11_qg_workflow]] | downstream | 0.22 |
| [[bld_memory_workflow]] | downstream | 0.22 |
| [[p10_lr_instruction_builder]] | downstream | 0.20 |
| [[bld_config_workflow]] | downstream | 0.20 |
| [[p03_sp_workflow-builder]] | upstream | 0.20 |
| [[bld_instruction_chain]] | upstream | 0.19 |
| [[bld_norms]] | related | 0.19 |
| [[p03_ins_workflow]] | upstream | 0.18 |
