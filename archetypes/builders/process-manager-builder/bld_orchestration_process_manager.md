---
quality: 7.6
id: bld_rules_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Rules"
version: 1.0.0
quality: 7.3
tags: [builder, process_manager, rules]
llm_function: COLLABORATE
author: builder
tldr: "Process Manager orchestration: workflow coordination, handoffs, and lifecycle management"
density_score: 0.81
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_collaboration_schedule
  - p03_sp_system-prompt-builder
  - p03_sp_workflow-builder
  - bld_memory_runtime_state
  - bld_collaboration_supervisor
  - kind-builder
  - bld_collaboration_builder
  - p03_sp_director_builder
  - bld_collaboration_system_prompt
---
# Rules: process_manager
## Absolute Rules (HARD -- never violate)
1. Process manager holds state + correlation key ONLY. No business domain data.
2. Every forward command must have a compensation (undo) command.
3. Every waiting state must have a timeout action.
4. Start event must be defined -- one event creates a new process instance.
5. Terminal states must include at least one success state and one failure state.
6. Process manager issues only commands -- never queries, never direct service calls.
7. quality: null always -- never self-score.
## Soft Rules (RECOMMEND)
1. State count: prefer 3-7 states. More than 10 suggests splitting the process.
2. Correlation key should be an immutable identifier (orderId, userId) not a mutable field.
3. Persistence: use database or event_sourced for production; in_memory for tests only.
4. Idempotency key on every command: ensures at-most-once processing on retry.
## Boundary Rules
1. THIS BUILDER handles: process_manager (P12)
2. NOT this builder: workflow (step-sequential, DAG execution) -> workflow-builder
3. NOT this builder: supervisor (agent hierarchy for LLM orchestration) -> supervisor-builder
4. NOT this builder: dispatch_rule (keyword/intent routing) -> dispatch-rule-builder
5. NOT this builder: schedule (time-triggered) -> schedule-builder
## CEX-Specific Rules
1. id pattern: p12_pm_{slug} -- always prefix p12_pm_
2. Pillar: always P12 (Orchestration)
3. Producing nucleus: N07 (Orchestrator) or N03 (Engineering)
4. max_bytes: 4096

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_collaboration_schedule]] | related | 0.26 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.25 |
| [[p03_sp_workflow-builder]] | upstream | 0.25 |
| [[bld_memory_runtime_state]] | upstream | 0.24 |
| [[bld_collaboration_supervisor]] | related | 0.24 |
| [[kind-builder]] | upstream | 0.24 |
| [[bld_collaboration_builder]] | related | 0.23 |
| [[p03_sp_director_builder]] | upstream | 0.23 |
| [[bld_collaboration_system_prompt]] | upstream | 0.22 |
