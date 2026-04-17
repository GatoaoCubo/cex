---
id: p01_kc_prospective_memory
kind: knowledge_card
type: kind
pillar: P10
title: "Prospective Memory -- Deep Knowledge for prospective_memory"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: prospective_memory
quality: null
tags: [prospective_memory, P10, COLLABORATE, kind-kc, agent-memory, future-actions]
tldr: "prospective_memory stores future-directed intentions for LLM agents: triggers, action payloads, expiry. NOT schedule (workflow config) or working_memory (current task)."
when_to_use: "Building, reviewing, or reasoning about prospective_memory artifacts"
keywords: [prospective_memory, future_actions, reminders, triggers, deferred_execution, ellis_hertel]
feeds_kinds: [prospective_memory]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
---

# Prospective Memory

## Spec
```yaml
kind: prospective_memory
pillar: P10
llm_function: COLLABORATE
max_bytes: 2048
naming: p10_pm_{scope}.md
core: true
```

## What It Is
Prospective memory (cognitive science: Ellis & Hertel, 1994) is the intention to perform an
action in the future. In LLM agents, prospective_memory stores scheduled future actions and
reminders that an agent must execute at a specified time or trigger condition.

NOT schedule (workflow schedule config -- P12). NOT working_memory (current task execution state).
NOT episodic_memory (what happened in the past). NOT entity_memory (persistent facts about entities).

## Cross-Framework Map
| Framework | Equivalent | Notes |
|-----------|-----------|-------|
| LangGraph | Interrupt/checkpoint-based future steps | State machine checkpoints |
| LangChain | ScheduledTool concept | Tool invocation at future time |
| AutoGPT | Task queue with future start | Deferred task execution |
| Temporal.io | Workflow signals + timers | Time-based trigger execution |
| CEX schedule (P12) | Workflow cron config | schedule is about workflow scheduling, not agent intentions |

## Trigger Types
| Trigger Type | Semantics | Example |
|-------------|-----------|---------|
| time | Fire at specific datetime or cron expression | "2026-04-18T09:00:00Z" |
| event | Fire when a specific signal is received | "signal:nucleus_complete" |
| condition | Fire when a state condition is met | "context.quality >= 9.0" |

## Key Parameters
| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| owner | string | YES | Agent/nucleus that executes reminders |
| reminders | list[Reminder] | YES | Array of future actions |
| execution_mechanism | enum | YES | schedule_signal, polling, wake_notification |
| completion_policy | enum | REC | mark_done, re_schedule |

## Reminder Schema
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string | YES | Unique reminder identifier |
| trigger_type | enum | YES | time, event, condition |
| trigger_value | string | YES | Datetime, signal name, or condition expr |
| action_payload | string | YES | What the agent should do when triggered |
| priority | int | REC | 1=highest; for concurrent trigger ordering |
| expiry | date or null | REC | When reminder becomes irrelevant |
| completion_policy | enum | REC | mark_done or re_schedule |

## Patterns
| Pattern | When to Use | Config |
|---------|-------------|--------|
| One-shot reminder | Single future action | completion_policy: mark_done |
| Recurring check | Periodic quality audit | trigger_type: time + completion_policy: re_schedule |
| Event-triggered follow-up | After nucleus completes | trigger_type: event |
| Priority queue | Multiple concurrent reminders | priority field ordering |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No owner | Reminders cannot be executed | Always declare owner |
| No action_payload | Trigger fires but does nothing | Describe exactly what agent should do |
| Conflating with schedule | schedule is workflow config (P12) | schedule != agent intention |
| Storing past events | Past -> episodic_memory | prospective = future only |

## Integration Graph
```
agent_card (owner) --> [prospective_memory] --> execution_mechanism
                              |
                       schedule (P12 workflow cron, separate concern)
                       episodic_memory (completed reminders recorded)
                       working_memory (reminder execution state)
```
