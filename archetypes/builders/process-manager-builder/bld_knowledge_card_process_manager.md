---
id: bld_knowledge_card_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Knowledge Card"
version: 1.0.0
quality: 5.3
tags: [builder, process_manager, knowledge]
llm_function: INJECT
density_score: 0.96
updated: "2026-04-17"
---
# Knowledge: process_manager
## Core Concept
Process Manager is the EIP pattern for coordinating multi-step distributed processes.
It subscribes to domain events, maintains a state machine per process instance (identified
by correlation key), and dispatches commands to participants at each step.
## When to Use
- Multi-step business process spans multiple services or aggregates
- Steps are event-driven (not time-driven or polled)
- Process needs compensation (rollback) on failure
- Centralized coordination visibility is required (audit trail)
## When NOT to Use
- Steps are sequential and synchronous: use workflow
- No cross-service coordination needed: use aggregate_root commands directly
- Single service, single transaction: use aggregate_root
- Routing by keyword/intent: use dispatch_rule
## State Machine Model
Every process_manager instance has:
1. Start state (created when start_event arrives)
2. One or more intermediate states (waiting for next event)
3. Terminal states: COMPLETED (success) and FAILED + compensation states
## CEX Integration
- Pillar: P12 (Orchestration)
- Builder: process-manager-builder (13 ISOs)
- Related: workflow (P12), supervisor (P02), dispatch_rule (P12)
- Produced by: N07 (Orchestrator) or N03 (Engineering)
- max_bytes: 4096
