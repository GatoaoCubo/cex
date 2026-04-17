---
kind: knowledge_card
id: bld_knowledge_card_prospective_memory
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for prospective_memory production
sources: Ellis & Hertel (1994) prospective memory, ScheduleWakeup Claude Code, CEX cron system
quality: null
title: "Knowledge Card Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, knowledge_card]
tldr: "Prospective memory stores deferred future intentions for agents -- what to do later, when triggered, distinct from P12 schedule workflow config."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Domain Knowledge: prospective_memory

## Executive Summary
Prospective memory (Ellis & Hertel, 1994) is the intention to perform an action in the future. In LLM agent systems, prospective memory stores deferred tasks and reminders that an agent has committed to executing when a future condition is met: a time arrives, an event fires, or a state condition is satisfied.

## Cognitive Science Foundation
Prospective memory = "remembering to remember." Unlike retrospective memory (what happened), prospective memory is forward-directed. Two cognitive types:
- Time-based: "I will do X at time T"
- Event-based: "I will do X when Y happens"

## P10 vs P12: Memory vs Orchestration
| Aspect | prospective_memory (P10) | schedule (P12) |
|--------|--------------------------|----------------|
| Owner | Agent/nucleus | Workflow orchestrator |
| Granularity | Individual intention | System-level workflow |
| Persistence | Agent memory store | Workflow config file |
| Trigger | time, event, or condition | cron expression |
| Use case | Agent decides what to do next | Orchestrator defines when to run jobs |

## Trigger Types
| Type | Example | CEX Mechanism |
|------|---------|---------------|
| time | "2026-05-01T09:00:00Z" | ScheduleWakeup or cron check |
| event | "n01_signal_complete" | Signal file polling |
| condition | "quality_score < 7.0" | State polling |

## Action Payload Patterns
| Pattern | Example |
|---------|---------|
| Nucleus dispatch | "dispatch n01 to audit P01 knowledge cards" |
| File-based task | "write handoff to .cex/runtime/handoffs/" |
| Signal check | "check .cex/runtime/signals/ for completion" |
| Quality audit | "run cex_doctor.py --pillar P01" |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No owner | Reminder has no executor |
| No trigger_type | Agent cannot know when to fire |
| Vague action_payload | Agent cannot execute "do something later" |
| Confusing with schedule | schedule = orchestration config; prospective_memory = agent intention |
| No expiry on time-sensitive reminders | Stale reminders fire after they are irrelevant |
