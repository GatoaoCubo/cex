---
quality: 8.0
quality: 7.8
id: bld_output_template_process_manager
kind: output_template
pillar: P12
title: "Process Manager Builder -- Output Template"
version: 1.0.0
tags: [builder, process_manager, template]
llm_function: PRODUCE
author: builder
density_score: 1.0
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p06_vs_frontmatter
  - bld_memory_runtime_state
  - p11_qg_runtime_state
  - bld_knowledge_card_checkpoint
  - runtime-state-builder
  - p12_checkpoint
  - bld_schema_runtime_state
  - bld_knowledge_card_runtime_state
  - p01_kc_runtime_state
  - p09_arch_task_queue
---
# Output Template: process_manager
```yaml
---
id: p12_pm_{slug}
kind: process_manager
pillar: P12
title: "Process Manager: {Name}"
version: 0.1.0
correlation_key: "{fieldName (e.g., orderId, requestId)}"
start_event: "{DomainEventThatCreatesInstance}"
terminal_states: [COMPLETED, FAILED]
states: [CREATED, {STEP1_PENDING}, {STEP2_PENDING}, COMPLETED, FAILED]
subscribed_events:
  - "{EventName1}"
  - "{EventName2}"
commands_issued:
  - "{CommandName1} -> {TargetService}"
  - "{CommandName2} -> {TargetService}"
timeout_strategy:
  {STATE}: "{duration}: action={TIMEOUT_ACTION}"
compensation:
  - "On FAILED: issue {CompensatingCommand} to {TargetService}"
persistence: database
quality: null
tags: [process_manager, {domain_slug}, P12]
tldr: "{Name} process: starts on {StartEvent}, routes {N} events, issues {M} commands, compensates on failure"
---

## Correlation
**Key**: `{fieldName}` -- identifies a unique process instance
**Storage**: {persistence strategy}

## States
| State | Description | Terminal? |
|-------|-------------|-----------|
| CREATED | Process started, awaiting first step | No |
| {STEP_PENDING} | Waiting for {EventName} | No |
| COMPLETED | All steps succeeded | YES |
| FAILED | Compensation triggered | YES |

## Event Routing
| Event Received | Current State | Next State | Command Issued | Target |
|----------------|--------------|-----------|----------------|--------|
| {StartEvent} | (none) | CREATED | {Cmd1} | {Service} |
| {Event2} | CREATED | {STEP_PENDING} | {Cmd2} | {Service} |
| {Event3} | {STEP_PENDING} | COMPLETED | -- | -- |
| {FailureEvent} | any | FAILED | {CompensatingCmd} | {Service} |

## Commands
### {CommandName}
- Target: {ServiceOrAggregate}
- Payload: {field: type, ...}
- Idempotency: {key field}

## Timeout
| State | Timeout | Action |
|-------|---------|--------|
| {STEP_PENDING} | {duration} | issue {TimeoutCmd} -> transition to FAILED |

## Compensation
On FAILED from state {X}:
1. Issue {CompensatingCmd1} to {Service1}
2. Issue {CompensatingCmd2} to {Service2}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_vs_frontmatter]] | upstream | 0.31 |
| [[bld_memory_runtime_state]] | upstream | 0.27 |
| [[p11_qg_runtime_state]] | upstream | 0.21 |
| [[bld_knowledge_card_checkpoint]] | upstream | 0.21 |
| [[runtime-state-builder]] | upstream | 0.20 |
| [[p12_checkpoint]] | related | 0.19 |
| [[bld_schema_runtime_state]] | upstream | 0.19 |
| [[bld_knowledge_card_runtime_state]] | upstream | 0.19 |
| [[p01_kc_runtime_state]] | upstream | 0.18 |
| [[p09_arch_task_queue]] | upstream | 0.18 |
