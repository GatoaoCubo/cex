---
id: prospective-memory-builder
kind: type_builder
pillar: P10
parent: null
domain: prospective_memory
llm_function: BECOME
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
tags: [kind-builder, prospective-memory, P10, memory, scheduled, future-actions, reminders]
keywords: [prospective memory, future actions, reminders, scheduled tasks, deferred execution, triggers]
triggers: ["create prospective memory", "schedule future action", "agent reminder", "deferred task store"]
capabilities: >
  L1: Specialist in building prospective_memory artifacts -- stores of scheduled future actions and reminders for agents. L2: Define trigger conditions, scheduled times, action payloads, and expiry policies. L3: When user needs to create, build, or scaffold prospective memory for agent reminders.
quality: 7.6
title: "Manifest Prospective Memory"
tldr: "Builds prospective_memory artifacts -- scheduled future actions and reminders an agent must execute at a future time or trigger condition."
density_score: 0.90
---
# prospective-memory-builder

## Identity
Specialist in building prospective_memory artifacts -- stores of future-directed actions
and reminders that an agent must execute at a specified time or trigger condition.
Grounded in cognitive science prospective memory (intention to perform an action in the future).
Masters trigger design, action payload schema, expiry policies, and the boundary between
prospective_memory (future actions), schedule (workflow config), and session_state (current session).

## Capabilities
1. Define trigger conditions: time-based, event-based, or condition-based
2. Structure action_payload: what the agent should do when triggered
3. Set priority ordering for multiple pending actions
4. Declare expiry for time-sensitive reminders
5. Define completion_policy: mark_done or re_schedule
6. Map to execution mechanism (schedule, wake_signal, polling)
7. Validate artifact against quality gates
8. Distinguish prospective_memory from schedule and session_state

## Properties

| Property | Value |
|----------|-------|
| Kind | `type_builder` |
| Pillar | P10 |
| Domain | prospective_memory |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
