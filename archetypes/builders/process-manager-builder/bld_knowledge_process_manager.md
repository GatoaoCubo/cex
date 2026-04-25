---
quality: 7.5
id: bld_knowledge_card_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Knowledge Card"
version: 1.0.0
quality: 7.3
tags: [builder, process_manager, knowledge]
llm_function: INJECT
author: builder
tldr: "Process Manager orchestration: domain knowledge, terminology, and contextual background"
density_score: 0.96
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_workflow
  - bld_memory_workflow
  - bld_architecture_workflow
  - p10_lr_chain_builder
  - workflow-builder
  - n03_competitive_architecture
  - p01_kc_chain
  - bld_knowledge_card_workflow
  - p12_wf_create_orchestration_agent
  - p11_qg_workflow
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

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_workflow]] | sibling | 0.23 |
| [[bld_memory_workflow]] | upstream | 0.22 |
| [[bld_architecture_workflow]] | upstream | 0.22 |
| [[p10_lr_chain_builder]] | upstream | 0.22 |
| [[workflow-builder]] | related | 0.21 |
| [[n03_competitive_architecture]] | upstream | 0.21 |
| [[p01_kc_chain]] | sibling | 0.20 |
| [[bld_knowledge_card_workflow]] | sibling | 0.20 |
| [[p12_wf_create_orchestration_agent]] | related | 0.20 |
| [[p11_qg_workflow]] | related | 0.19 |
