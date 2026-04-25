---
quality: 8.0
quality: 7.6
id: kc_aggregate_root
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, aggregate_root, ddd, P06]
tldr: "DDD entry-point entity owning a consistency boundary, enforcing invariants over sub-entities"
when_to_use: "When a domain concept has cross-entity business rules requiring atomic transactional consistency"
density_score: 0.92
updated: "2026-04-17"
related:
  - p10_lr_kind_builder
  - bld_knowledge_card_axiom
  - p03_sp_type-def-builder
---
# Knowledge Card: aggregate_root

## Definition
An `aggregate_root` is a DDD entry-point entity that owns a consistency boundary (the "aggregate cluster"),
enforces domain invariants, and controls all external access to the objects within its boundary.
Coined by Eric Evans in Domain-Driven Design (2003). The root is the ONLY object in the cluster
that external code may hold a reference to -- all mutations go through it.

## When to Use
- A domain concept has business rules that span multiple sub-entities or value objects
- Multiple objects must change together atomically in one transaction
- You need a clear, authoritative entry point for domain operations on a cluster
- The domain has explicit invariants (rules that must always be true after any command)

## When NOT to Use
- Simple CRUD with no cross-entity business rules: use `type_def` or `input_schema`
- Data contract between services: use `interface`
- Generic type alias: use `type_def`
- Immutable attribute: use `value_object`
- Event routing coordination: use `process_manager`

## Structure
Every `aggregate_root` defines:
1. **Identity**: a globally unique identifier (UUID, natural key, surrogate)
2. **Cluster members**: which entities and value_objects live inside the boundary
3. **Invariants**: concrete, verifiable rules that must hold after every command
4. **Commands**: operations that mutate state, with preconditions and postconditions
5. **Domain events**: facts emitted when state changes (past tense, e.g. OrderPlaced)
6. **Repository**: persistence interface -- find_by_id and save only (no query methods)

## Invariant Contract
Invariants are not guidelines. They are enforced by the root after every command:
- If a command would violate an invariant, the root raises a domain exception
- The repository saves the entire aggregate atomically
- External callers never see an inconsistent state

## Cross-Aggregate Reference Rule (Critical)
Other aggregates are referenced by ID only (a `value_object` wrapping the foreign key).
Never hold an object reference to another aggregate. This prevents distributed consistency
issues and keeps transactional boundaries clean.

## Use Cases
1. **E-commerce Order**: owns LineItems (entities) and Money (value_objects), enforces "total >= 0 and all items are in stock before confirmation"
2. **User Account**: owns credentials and profile data, enforces "email is unique and password is never stored in plaintext"
3. **Shipping Route**: owns Waypoints (entities), enforces "route must have at least 2 waypoints and departure < arrival"

## Relationships to Other Kinds
| Kind | Relationship |
|------|-------------|
| `value_object` | immutable typed attributes inside the aggregate cluster |
| `interface` | contract that the aggregate's repository implements |
| `input_schema` | validates raw data BEFORE it enters the aggregate |
| `process_manager` | subscribes to domain events emitted by the aggregate |
| `domain_event` | fact emitted by the aggregate on state change |

## Anti-Patterns
- **God aggregate**: one root that owns too much -- split by consistency boundary
- **Anemic aggregate**: root with no invariants, just getters and setters -- use type_def instead
- **Cross-aggregate object reference**: always use ID value_objects to reference other aggregates
- **Repository with query methods**: read models / query services handle queries; the aggregate repository is find_by_id + save

## CEX Metadata
| Property | Value |
|----------|-------|
| Pillar | P06 (Schema) |
| ID pattern | `p06_ar_{slug}` |
| max_bytes | 4096 |
| llm_function | CONSTRAIN |
| Builder | aggregate-root-builder (13 ISOs) |
| Nucleus | N03 (Engineering) |
| Pattern source | Evans DDD (2003), Vernon IDDD (2013) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_kind_builder]] | downstream | 0.16 |
| [[bld_knowledge_card_axiom]] | sibling | 0.16 |
| [[p03_sp_type-def-builder]] | downstream | 0.15 |
