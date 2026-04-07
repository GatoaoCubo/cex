---
id: p01_kc_error_recovery
kind: knowledge_card
type: domain
pillar: P01
title: "Error Recovery Patterns for LLM Agents"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: operations
quality: 9.0
tags: [error-recovery, resilience, retry, fallback, circuit-breaker]
tldr: "Retry with backoff, circuit breaker, fallback chains, graceful degradation. Agents must recover from errors without crashing the workflow."
when_to_use: "Building resilient agent systems that handle failures gracefully"
keywords: [error-recovery, retry, circuit-breaker, fallback, graceful-degradation]
density_score: 1.0
updated: "2026-04-07"
linked_artifacts:
  primary: null
  related: []
---

# Error Recovery Patterns

## Strategy Ladder (try in order)

| Level | Strategy | Example |
|-------|----------|---------|
| 1 | Retry with same input | Transient API error |
| 2 | Retry with modified input | Add "Fix this error: ..." |
| 3 | Fallback to simpler approach | Use template instead of generation |
| 4 | Circuit breaker | Stop calling failing service |
| 5 | Graceful degradation | Skip optional step, continue |
| 6 | Escalate to user | "I need your help with..." |

## Circuit Breaker Pattern
```
CLOSED (normal) → error count > threshold → OPEN (reject all calls)
OPEN → wait cooldown → HALF-OPEN (try one)
HALF-OPEN → success → CLOSED | failure → OPEN
```

## CEX Recovery Points
1. F7 GOVERN fail → retry F6 (max 2)
2. Compile fail → auto-fix frontmatter → retry
3. Dispatch fail → check boot file → retry
4. Test fail → auto-debug → fix → retry
5. All retries fail → escalate (wf_auto_debug → user)


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
