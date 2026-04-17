---
id: bld_knowledge_card_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Knowledge Card"
version: 1.0.0
quality: 5.3
tags: [builder, aggregate_root, knowledge]
llm_function: INJECT
density_score: 0.93
updated: "2026-04-17"
---
# Knowledge: aggregate_root
## Core Concept
Aggregate Root is the Evans DDD pattern for transactional consistency boundaries.
The root is the ONLY object within its cluster accessible from outside. All mutations
go through the root, which enforces domain invariants atomically.
## When to Use
- Domain object has business rules that span multiple sub-entities
- Multiple objects must change together in one transaction
- Need a clear entry point for domain operations
## When NOT to Use
- Simple CRUD with no cross-entity rules: use type_def or input_schema
- Data contract between services: use interface
- Event routing: use process_manager
## Key Rules (from Evans)
1. Each aggregate has ONE root entity with a global identity
2. External objects hold references only to the root (never to internal entities)
3. Objects inside the boundary may reference each other freely
4. A database transaction should not cross aggregate boundaries
5. Delete root = delete everything inside the boundary
## CEX Integration
- Pillar: P06 (Schema)
- Builder: aggregate-root-builder (13 ISOs)
- Related: value_object (P06), interface (P06), input_schema (P06)
- Produced by: N03 (Engineering)
