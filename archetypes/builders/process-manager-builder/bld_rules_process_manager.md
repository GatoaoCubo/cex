---
id: bld_rules_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Rules"
version: 1.0.0
quality: null
tags: [builder, process_manager, rules]
llm_function: CONSTRAIN
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
