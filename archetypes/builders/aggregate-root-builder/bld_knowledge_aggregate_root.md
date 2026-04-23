---
id: bld_knowledge_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Knowledge Card"
version: 1.1.0
quality: 8.6
tags: [builder, aggregate_root, knowledge, ddd, schema, consistency]
llm_function: INJECT
density_score: 0.93
created: "2026-04-17"
updated: "2026-04-22"
author: knowledge-card-builder
domain: domain_driven_design
tldr: "Aggregate Root = transactional consistency boundary with one root entity. External refs only to root. All mutations through root."
related:
  - bld_architecture_aggregate_root
  - bld_model_aggregate_root
  - bld_prompt_aggregate_root
  - bld_schema_aggregate_root
  - bld_memory_aggregate_root
  - bld_tools_aggregate_root
  - bld_knowledge_card_value_object
  - bld_knowledge_card_domain_event
  - bld_knowledge_card_bounded_context
  - bld_knowledge_card_interface
---
# Knowledge: aggregate_root

## Core Concept

Aggregate Root is the Evans DDD pattern for transactional consistency boundaries.
The root is the ONLY object within its cluster accessible from outside. All mutations
go through the root, which enforces domain invariants atomically.

## Quick Reference

| Property | Value |
|----------|-------|
| Pattern origin | Eric Evans, DDD (2003) |
| Pillar | P06 (Schema) |
| Builder | aggregate-root-builder (12 ISOs) |
| Producer | N03 (Engineering) |
| Key invariant | One transaction = one aggregate |

## When to Use

| Scenario | Use aggregate_root? | Alternative |
|----------|---------------------|-------------|
| Business rules span multiple sub-entities | YES | -- |
| Multiple objects must change atomically | YES | -- |
| Need clear entry point for domain operations | YES | -- |
| Simple CRUD, no cross-entity rules | NO | type_def, input_schema |
| Data contract between services | NO | interface |
| Event routing across aggregates | NO | process_manager |

## Key Rules (Evans)

1. Each aggregate has ONE root entity with a global identity
2. External objects hold references only to the root
3. Objects inside the boundary may reference each other freely
4. A database transaction must not cross aggregate boundaries
5. Delete root = cascade delete everything inside

## Anti-Patterns

| Anti-pattern | Problem | Fix |
|-------------|---------|-----|
| God aggregate (100+ fields) | Perf + contention | Split by invariant boundary |
| Cross-aggregate transaction | Distributed lock hell | Use saga or domain events |
| Exposing internal entities | Breaks encapsulation | Return value objects instead |
| Aggregate referencing aggregate by object | Memory leak + coupling | Reference by ID only |

## CEX Integration Points

| Artifact | Relationship | Why |
|----------|-------------|-----|
| value_object (P06) | Internal component | Immutable data inside the boundary |
| domain_event (P06) | Emitted by root | Cross-aggregate communication |
| bounded_context (P06) | Parent scope | Aggregate lives inside one BC |
| interface (P06) | External contract | How other services call the root |
| saga (P12) | Coordination | Multi-aggregate workflows |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_aggregate_root]] | sibling | 0.35 |
| [[bld_model_aggregate_root]] | sibling | 0.32 |
| [[bld_prompt_aggregate_root]] | sibling | 0.30 |
| [[bld_schema_aggregate_root]] | sibling | 0.28 |
| [[bld_memory_aggregate_root]] | sibling | 0.28 |
| [[bld_tools_aggregate_root]] | sibling | 0.25 |
| [[bld_knowledge_card_value_object]] | downstream | 0.22 |
| [[bld_knowledge_card_domain_event]] | downstream | 0.22 |
| [[bld_knowledge_card_bounded_context]] | upstream | 0.20 |
| [[bld_knowledge_card_interface]] | downstream | 0.18 |
