---
quality: 8.3
quality: 8.2
id: p10_lr_prospective_memory_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Agents without prospective_memory missed follow-up tasks when context windows were cleared. Vague action payloads ('check something later') could not be executed by agents rebooted after context loss."
pattern: "action_payload must be executable without the original context: include the full tool call or dispatch command. trigger_type=condition reminders require polling mechanism. time reminders require expiry for one-shot tasks."
confidence: 0.83
outcome: SUCCESS
domain: prospective_memory
tags: [prospective-memory, action-payload, trigger-type, execution-mechanism]
tldr: "action_payload must be self-contained executable instructions, not vague references. trigger_type mandatory."
impact_score: 7.5
decay_rate: 0.03
memory_scope: project
title: "Memory Prospective Memory"
density_score: 0.90
llm_function: INJECT
related:
  - schedule-builder
  - p03_sp_memory_scope_builder
  - p10_lr_memory_scope_builder
  - bld_collaboration_schedule
  - bld_knowledge_card_schedule
  - bld_instruction_agent
  - bld_collaboration_memory_type
  - p03_ins_mental_model
  - p03_sp_instruction_builder
  - bld_memory_system_prompt
---
## Summary
Prospective memory fails when action payloads are vague. An agent that restarts after context loss reads the reminder and must be able to execute it without any other context. This requires self-contained action payloads.

## Pattern
1. action_payload = full executable instruction (not "check something")
2. trigger_type: always declare one of time, event, condition
3. For time triggers: set expiry for one-shot, recurrence for recurring
4. For condition triggers: polling mechanism must be declared
5. owner: always declare -- orphaned reminders cannot be executed after reboot

## Anti-Pattern
1. action_payload: "do something later" -- not executable
2. No trigger_type -- agent cannot know when to fire
3. No owner -- cannot route on reboot
4. Confusing with schedule (P12) -- schedule is workflow config, not agent memory

## Properties
| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | prospective_memory |
| Target | 9.0+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[schedule-builder]] | downstream | 0.19 |
| [[p03_sp_memory_scope_builder]] | upstream | 0.18 |
| [[p10_lr_memory_scope_builder]] | sibling | 0.18 |
| [[bld_collaboration_schedule]] | downstream | 0.18 |
| [[bld_knowledge_card_schedule]] | upstream | 0.18 |
| [[bld_instruction_agent]] | upstream | 0.17 |
| [[bld_collaboration_memory_type]] | downstream | 0.17 |
| [[p03_ins_mental_model]] | upstream | 0.17 |
| [[p03_sp_instruction_builder]] | upstream | 0.17 |
| [[bld_memory_system_prompt]] | related | 0.17 |
