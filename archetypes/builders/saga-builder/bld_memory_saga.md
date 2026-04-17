---
id: bld_memory_saga
kind: knowledge_card
pillar: P10
title: "Memory: saga Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: 6.6
tags: [memory, saga, P12]
llm_function: INJECT
tldr: "Recalled patterns and corrections for saga builder sessions."
density_score: null
---

# Memory: saga Builder

## Persistent Patterns
| Pattern | Frequency | Note |
|---------|-----------|------|
| Every step MUST have compensating_action | HIGH | Gate H06 |
| Make compensating actions idempotent | HIGH | Retry safety |
| Rollback is reverse order of completed steps | HIGH | Saga invariant |
| steps_count must match list | HIGH | Gate H07 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User conflates with workflow | Teach: workflow has no compensation; saga does |
| User designs step without undo | Block: every step needs compensating_action |
| User sets compensating_action: null | Reject: must be idempotent undo action |
| User mixes choreography and orchestration | Choose one topology per saga |
| User exceeds 10 steps | Suggest splitting into sub-sagas |
