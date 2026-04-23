---
quality: 7.9
quality: 7.5
id: bld_architecture_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Architecture"
version: 1.0.0
tags: [builder, process_manager, architecture]
llm_function: CONSTRAIN
author: builder
density_score: 0.99
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_signal
  - n03_competitive_architecture
  - bld_memory_runtime_state
  - bld_knowledge_card_checkpoint
  - bld_collaboration_hook
  - bld_knowledge_card_hook_config
  - p11_qg_runtime_state
  - bld_instruction_hook
  - bld_instruction_crew_template
  - p01_kc_router
---
# Architecture: process_manager
## Pattern Origin
Hohpe & Woolf Enterprise Integration Patterns (2003): Process Manager = stateful event router.
Also known as "Saga Orchestrator" in microservices contexts.
## Structural Topology
```
[Domain Event] --> ProcessManager (corr_key lookup)
                        |
              [state machine transition]
                        |
                [Command dispatch] --> [Service/Aggregate]
                        |
                [Wait for next event or timeout]
```
## Key Properties
1. Stateful: tracks position in process via state machine
2. Event-reactive: progresses only when events arrive (not polling)
3. Command-issuing: only output is commands to other services
4. No business data: holds only process state + correlation key
5. Compensatable: each forward step has a corresponding undo command
## Relationship to Other Kinds
| Kind | Relationship |
|------|-------------|
| workflow | sequential step execution (push model); process_manager is event-driven (pull/reactive) |
| supervisor | manages agent hierarchies for LLM workflows; process_manager routes domain events |
| dispatch_rule | routes by keyword/intent; process_manager routes by domain event + state |
| domain_event | inputs consumed by process_manager; outputs emitted by aggregates |
## EIP vs Saga
- EIP Process Manager: routes events AND holds coordination state (stateful router)
- Saga Orchestrator: same pattern, called "saga" in microservices contexts
- Saga Choreography: no central coordinator; aggregates react to each other's events
## Anti-Patterns
- Process manager that holds business data: only state + correlation key allowed
- Process manager that polls: it reacts to events, never polls
- Missing compensation: every forward step needs an undo path
- Single process manager for all flows: split by business process boundary

## Architecture Checklist

- Verify component inventory is complete (no orphans)
- Validate dependency graph has no cycles
- Cross-reference with boundary table for scope correctness
- Test layer map against actual codebase structure

## Architecture Pattern

```yaml
# Architecture validation
components: inventoried
dependencies: acyclic
boundaries: defined
layers: mapped
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope architecture
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_signal]] | sibling | 0.23 |
| [[n03_competitive_architecture]] | upstream | 0.20 |
| [[bld_memory_runtime_state]] | upstream | 0.18 |
| [[bld_knowledge_card_checkpoint]] | sibling | 0.17 |
| [[bld_collaboration_hook]] | related | 0.17 |
| [[bld_knowledge_card_hook_config]] | sibling | 0.17 |
| [[p11_qg_runtime_state]] | upstream | 0.17 |
| [[bld_instruction_hook]] | upstream | 0.17 |
| [[bld_instruction_crew_template]] | upstream | 0.16 |
| [[p01_kc_router]] | sibling | 0.16 |
