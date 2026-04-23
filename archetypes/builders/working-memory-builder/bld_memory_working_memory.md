---
quality: 8.7
quality: 8.4
id: p10_lr_working_memory_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Tasks without working_memory bounds caused context overflow in 3 multi-step pipeline runs. Tasks with typed slots caught type errors at slot assignment rather than at downstream consumption. clear_on_complete: promote recovered 40% of intermediate discoveries that would have been lost."
pattern: "Always set capacity_limit. Always type context slots. Use clear_on_complete: promote for research tasks, clear for pure computation tasks. expiry: on_task_complete is the safe default."
confidence: 0.87
outcome: SUCCESS
domain: working_memory
tags: [working-memory, capacity-limit, typed-slots, clear-policy, promote]
tldr: "capacity_limit + typed slots + clear policy are load-bearing. Untyped unbounded working memory fails."
impact_score: 8.0
decay_rate: 0.02
memory_scope: project
title: "Memory Working Memory"
density_score: 0.90
llm_function: INJECT
related:
  - p01_kc_memory_persistence
  - kc_workflow_run_crate
  - p08_pat_continuous_batching
  - bld_instruction_benchmark_suite
  - p01_kc_session_state
  - bld_memory_session_state
  - bld_architecture_entity_memory
  - p03_sp_entity_memory_builder
  - bld_knowledge_card_memory_scope
  - p01_kc_memory_scope
---
## Summary
Working memory without capacity limits causes context window overflow in multi-step tasks. Typed slots catch errors early. The clear vs promote decision determines whether task insights survive completion -- for research and analysis tasks, promote is almost always the right choice.

## Pattern
**Typed slots + capacity_limit + expiry: on_task_complete + promote for insights.**
1. Type every slot: int counters, string text state, float scores, bool flags, list accumulators
2. Set capacity_limit before the task starts: estimate peak state size, add 20% buffer
3. expiry: on_task_complete is the safe default; TTL as fallback for stuck tasks
4. clear_on_complete: promote for tasks that discover facts, entities, or patterns
5. promote_targets: entity_memory for facts, episodic_memory for episode summaries, learning_record for patterns

## Anti-Pattern
1. No capacity_limit -- context overflow on long tasks
2. Untyped slots (`data: anything`) -- type errors at consumption time
3. Long-term facts in slots -- lost on clear; put those in entity_memory
4. clear_on_complete: clear for research tasks -- discovered knowledge lost
5. No expiry -- task hangs leave working memory allocated indefinitely
6. Mixing session state in task slots -- session_state has different lifecycle

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | working_memory |
| Pipeline | 8F |
| Target | 9.0+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_persistence]] | upstream | 0.25 |
| [[kc_workflow_run_crate]] | related | 0.24 |
| [[p08_pat_continuous_batching]] | upstream | 0.24 |
| [[bld_instruction_benchmark_suite]] | upstream | 0.20 |
| [[p01_kc_session_state]] | related | 0.20 |
| [[bld_memory_session_state]] | related | 0.19 |
| [[bld_architecture_entity_memory]] | upstream | 0.19 |
| [[p03_sp_entity_memory_builder]] | related | 0.19 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.19 |
| [[p01_kc_memory_scope]] | upstream | 0.19 |
