---
quality: 8.6
id: bld_architecture_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Architecture"
version: 1.1.0
quality: 8.4
tags: [builder, aggregate_root, architecture, ddd, consistency_boundary]
llm_function: CONSTRAIN
density_score: 0.93
created: "2026-04-17"
updated: "2026-04-22"
author: builder
domain: domain_driven_design
tldr: "Architecture constraints for aggregate_root: Evans topology, invariant enforcement, event emission, repository pattern."
related:
  - p09_path_{{SCOPE_SLUG}}
  - bld_knowledge_aggregate_root
  - bld_model_aggregate_root
  - bld_memory_aggregate_root
  - bld_schema_aggregate_root
  - bld_prompt_aggregate_root
  - bld_tools_aggregate_root
  - bld_architecture_value_object
  - bld_architecture_domain_event
  - bld_architecture_bounded_context
---
# Architecture: aggregate_root

## Pattern Origin

Evans DDD (2003): Aggregate = cluster of domain objects treated as a unit for data changes.
Aggregate Root = single entity responsible for maintaining cluster invariants.

## Structural Topology

```
AggregateRoot (identity + invariant enforcer)
  |-- Entity_A (child, no direct external access)
  |-- Entity_B (child, accessed only via root)
  |-- ValueObject_X (immutable, no identity)
  |-- ValueObject_Y (immutable, no identity)
  repository: AggregateRootRepository (find_by_id + save only)
```

## Invariant Enforcement

- Commands mutate state inside the boundary
- Root checks invariants AFTER applying command, BEFORE returning
- If invariant violated: raise domain exception, rollback state
- Repository saves ENTIRE aggregate atomically (one transaction)

## Event Emission

- Each command that succeeds emits one or more domain events
- Events are facts about what happened (past tense)
- Subscribers react to events outside the aggregate boundary

## Relationship to Other Kinds

| Kind | Relationship | Boundary role |
|------|-------------|---------------|
| value_object | Internal member | Immutable, no identity |
| interface | External contract | Repository or service impl |
| input_schema | Validation layer | Data validated BEFORE entering |
| domain_event | Output signal | Fact emitted on state change |
| bounded_context | Parent scope | Aggregate lives inside one BC |
| saga | Cross-boundary | Coordinates multiple aggregates |

## Anti-Patterns

| Anti-pattern | Signal | Fix |
|-------------|--------|-----|
| God aggregate | Root owns everything | Split by consistency boundary |
| Cross-aggregate object refs | Direct object pointers | Use IDs only |
| Anemic aggregate | No invariants, just getters | Add domain rules to root |
| Large aggregate | >7 members | Decompose by transaction need |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_path_{{SCOPE_SLUG}}]] | downstream | 0.20 |
| [[bld_knowledge_aggregate_root]] | sibling | 0.35 |
| [[bld_model_aggregate_root]] | sibling | 0.32 |
| [[bld_memory_aggregate_root]] | sibling | 0.28 |
| [[bld_schema_aggregate_root]] | sibling | 0.28 |
| [[bld_prompt_aggregate_root]] | sibling | 0.25 |
| [[bld_tools_aggregate_root]] | sibling | 0.25 |
| [[bld_architecture_value_object]] | downstream | 0.22 |
| [[bld_architecture_domain_event]] | downstream | 0.20 |
| [[bld_architecture_bounded_context]] | upstream | 0.18 |
