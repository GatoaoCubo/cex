---
quality: 8.4
id: bld_memory_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Memory"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-22"
author: builder
domain: process_manager
quality: 8.3
tags: [builder, process_manager, memory]
llm_function: INJECT
tldr: "Recalled session patterns, corrections, and vocabulary for process_manager builder."
density_score: 0.95
related:
  - bld_knowledge_process_manager
  - bld_schema_process_manager
  - bld_architecture_process_manager
  - bld_model_process_manager
  - bld_prompt_process_manager
  - bld_tools_process_manager
  - bld_output_process_manager
  - bld_eval_process_manager
  - bld_feedback_process_manager
  - bld_config_process_manager
---
# Memory: process_manager

## Session Patterns

| Pattern | Guidance | Gate |
|---------|----------|------|
| Correlation key | Always ask "how do you find the right process instance when an event arrives?" | H01 |
| State count | Most process managers have 3-7 states. More than 10 states suggests splitting. | H02 |
| Compensation mandatory | Every forward command needs an undo. Missing compensation = incomplete. | H03 |
| Timeout on every wait state | Infinite waits cause stuck processes. Every waiting state needs a timeout. | H04 |
| Start event | Every process manager must have exactly one event that creates a new instance. | H05 |
| FAILED terminal state | A process manager without explicit failure handling is dangerous. | H06 |

## Common Mistakes

| Mistake | Correction | Severity |
|---------|-----------|---------|
| Storing domain data | Process manager stores state + correlation key ONLY | BLOCK |
| Missing start_event | Add exactly one event that creates a new instance | BLOCK |
| No FAILED terminal state | Add explicit failure handling + compensation trigger | BLOCK |
| Confusing with workflow | workflow is explicit step ordering (DAG); process_manager is reactive event routing | TEACH |
| Missing compensation for forward command | Add undo action for every state transition | WARN |
| No timeout on waiting state | Add timeout + resolution strategy (fail/retry/escalate) | WARN |

## Vocabulary

| User Term | Industry Term | Source |
|-----------|--------------|--------|
| "Saga orchestrator" | process_manager | microservices context |
| "Compensation" | undo action | Sagas paper, Garcia-Molina 1987 |
| "Correlation" | matching events to the right process instance | Enterprise Integration Patterns |
| "Terminal state" | state where the process instance is complete and can be archived | EIP |
| "Process choreography" | decentralized saga without a central manager | contrast with process_manager |

## Timeout Patterns

| Pattern | Behavior | When to Use |
|---------|----------|-------------|
| Fast-fail | timeout -> FAILED + immediate compensation | SLA-critical, no retry budget |
| Retry | timeout -> re-issue same command (with counter limit) | Transient failures expected |
| Escalate | timeout -> notify human, pause process | Human-in-the-loop required |
| Dead-letter | timeout -> move to dead-letter queue for manual inspection | Audit-critical flows |

## State Count Decision

| State Count | Assessment | Action |
|-------------|-----------|--------|
| 3-7 | Healthy range | Proceed |
| 8-10 | Borderline | Review if any states can merge |
| >10 | Too complex | Split into multiple process managers |
| 1-2 | Too simple | Likely a simple state machine, not a process_manager |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_process_manager]] | sibling | 0.45 |
| [[bld_schema_process_manager]] | sibling | 0.43 |
| [[bld_architecture_process_manager]] | sibling | 0.41 |
| [[bld_model_process_manager]] | sibling | 0.39 |
| [[bld_prompt_process_manager]] | sibling | 0.37 |
| [[bld_tools_process_manager]] | sibling | 0.35 |
| [[bld_output_process_manager]] | sibling | 0.34 |
| [[bld_eval_process_manager]] | sibling | 0.33 |
| [[bld_feedback_process_manager]] | sibling | 0.31 |
| [[bld_config_process_manager]] | sibling | 0.29 |
