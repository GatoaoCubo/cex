---
quality: null
id: kc_saga
kind: knowledge_card
title: "Saga: Long-Running Distributed Transaction with Compensation"
tldr: "Sequence of local transactions with compensating actions for rollback on partial failure in distributed systems"
version: 1.1.0
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, saga, P12, orchestration, distributed_transaction]
density_score: 0.93
updated: "2026-04-22"
related:
  - p11_qg_workflow
  - bld_knowledge_card_workflow
  - p01_kc_workflow
  - bld_architecture_workflow
  - bld_memory_workflow
  - bld_instruction_chain
  - p10_lr_chain_builder
  - p03_ins_workflow
  - p10_lr_instruction_builder
  - workflow-builder
---

# saga

## Spec
```yaml
kind: saga
pillar: P12
llm_function: COLLABORATE
max_bytes: 4096
naming: p12_saga_{{name}}.md + .yaml
core: false
```

## What It Is
A saga is a long-running distributed transaction composed of a sequence of local transactions (steps), each with a compensating transaction that undoes its effect if a subsequent step fails. On partial failure, completed steps are rolled back in reverse order via their compensating actions.

Origin: Garcia-Molina & Salem (1987), "SAGAS", ACM SIGMOD. Industry: AWS Step Functions, Apache Camel Saga EIP, Eventuate Tram, MassTransit Saga State Machine.

It is NOT:
- `workflow` (sequential/parallel steps without compensation -- workflow has no rollback semantics)
- `process_manager` (event-driven coordination -- routes events between services; no transaction rollback)
- `chain` (prompt-level LLM sequencing -- P03; no services, no compensation)

## When to Use
- Multi-service transactions where ACID is not possible (distributed systems)
- Long-running processes that may fail mid-way and need partial rollback
- Any transaction spanning multiple nuclei or services that must be reversible
- Replacing 2-phase commit in microservices architectures (eventual consistency)

## When NOT to Use
- Single-service transaction with ACID guarantees -> use database transaction
- Event routing between services without transaction semantics -> use `process_manager`
- Sequential agent steps without undo requirement -> use `workflow`
- Simple prompt chaining -> use `chain`

## Structure
```yaml
# Required frontmatter fields
id: p12_saga_{name_slug}
kind: saga
pillar: P12
saga_name: "..."
steps_count: N
topology: choreography | orchestration
on_failure: compensate_all | compensate_partial | abort
quality: null
```

```markdown
## Goal
One-sentence business transaction outcome

## Steps
Table: id, participant, action, compensating_action, on_failure
(EVERY step MUST have a non-null compensating_action)

## Rollback Sequence
Ordered list of compensating actions on failure (reverse order of steps)

## Topology
choreography or orchestration, with participant diagram
```

## Compensation Model
```
Forward:       T1 -> T2 -> T3 -> ... -> Tn  (success: commit)
Rollback (at k): T1 -> T2 -> ... -> Tk FAIL
                              -> C(k-1) -> C(k-2) -> ... -> C1
```
Every Ti must have a Ci. Ci must be idempotent (safe to retry).

## Topology Comparison
| Style | Mechanism | Pros | Cons |
|-------|-----------|------|------|
| Choreography | Services react to events | Decoupled, no SPOF | Hard to trace, emergent behavior |
| Orchestration | Central coordinator sends commands | Easy to trace, explicit flow | Central SPOF, coupling |

## Cross-Framework Map
| Framework | Saga Implementation |
|-----------|-------------------|
| AWS Step Functions | Express Workflows with catch/retry + compensating Lambda |
| Apache Camel | Saga EIP with compensation endpoints |
| Eventuate Tram | Java saga orchestration framework |
| MassTransit | .NET saga state machine |
| Temporal | Workflow with compensation activities |

## Relationships
```
[workflow] --(extends with compensation)--> [saga]
[signal] <-- [saga step completion]
[saga] --> [workflow] (on success: cascade to next workflow)
[process_manager] -- sibling -- [saga]
```

## Decision Tree
- IF steps need compensation on failure -> saga (not workflow)
- IF all services in same database -> use DB transaction instead
- IF eventual consistency acceptable -> saga
- IF strict ACID needed -> 2-phase commit (not saga)
- IF topology unclear -> default to orchestration (easier to debug)
- IF saga > 10 steps -> split into sub-sagas with signal handoffs

## Concrete Compensation Example: Order Processing Saga

```yaml
# p12_saga_order_processing.md
---
id: p12_saga_order_processing
kind: saga
pillar: P12
saga_name: "Order Processing"
steps_count: 4
topology: orchestration
on_failure: compensate_all
quality: null
---
```

### Steps Table

| Step | Participant | Action | Compensating Action | Idempotent? |
|------|------------|--------|---------------------|-------------|
| T1 | OrderService | Create order (status=PENDING) | Cancel order (status=CANCELLED) | Yes (by order_id) |
| T2 | PaymentService | Reserve payment (auth hold) | Release payment hold | Yes (by auth_id) |
| T3 | InventoryService | Reserve stock (decrement available) | Release stock (increment available) | Yes (by reservation_id) |
| T4 | ShippingService | Create shipment label | Void shipment label | Yes (by label_id) |

### Forward Flow (Success)

```
T1: CreateOrder(PENDING)
  |-- success -->
T2: ReservePayment(auth_hold)
  |-- success -->
T3: ReserveStock(decrement)
  |-- success -->
T4: CreateShipment(label)
  |-- success -->
COMMIT: Order confirmed, payment captured, stock committed, label printed
```

### Rollback Flow (T3 Fails)

```
T1: CreateOrder(PENDING)    -- completed
T2: ReservePayment(hold)    -- completed
T3: ReserveStock(decrement) -- FAILED (insufficient stock)
  |
  +-- rollback starts (reverse order) -->
  C2: ReleasePaymentHold(auth_id=xyz)  -- idempotent retry safe
  C1: CancelOrder(order_id=abc)        -- idempotent retry safe
  |
  RESULT: Order cancelled, payment released, no stock change
```

## Saga Patterns in Practice

| Pattern | Description | Trade-off |
|---------|-------------|-----------|
| **Orchestration** | Central coordinator (saga manager) sends commands to each participant | Easy debugging, single point of failure |
| **Choreography** | Each participant emits events; next participant reacts | Decoupled, hard to trace end-to-end |
| **Hybrid** | Orchestrator for critical path, events for side effects | Balanced, more complex to implement |
| **Nested Saga** | Sub-saga within a step (saga-within-saga) | Handles complex multi-step participants |
| **Parallel Saga** | Independent steps execute concurrently, barrier before next phase | Higher throughput, complex compensation |

## Idempotency Requirements

Every compensating action MUST be idempotent because:
- Network failures may cause retries
- The saga coordinator may re-send compensation commands
- Duplicate event delivery is normal in distributed systems

| Technique | How It Works | Example |
|-----------|-------------|---------|
| Idempotency key | Unique key per operation; server rejects duplicates | `X-Idempotency-Key: order-123-cancel` |
| Conditional update | Only apply if current state matches expected | `UPDATE orders SET status='CANCELLED' WHERE id=123 AND status='PENDING'` |
| Event deduplication | Track processed event IDs; skip duplicates | Redis SET with event_id, TTL 24h |

## Quality Criteria
- GOOD: All steps present with compensating_action, topology specified, rollback sequence defined
- GREAT: Compensating actions marked as idempotent, goal statement present, on_failure per step
- FAIL: Any step missing compensating_action, no rollback sequence, topology unspecified

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_workflow]] | downstream | 0.31 |
| [[bld_knowledge_card_workflow]] | sibling | 0.31 |
| [[p01_kc_workflow]] | sibling | 0.30 |
| [[bld_architecture_workflow]] | downstream | 0.28 |
| [[bld_memory_workflow]] | downstream | 0.28 |
| [[bld_instruction_chain]] | downstream | 0.28 |
| [[p10_lr_chain_builder]] | downstream | 0.28 |
| [[p03_ins_workflow]] | downstream | 0.26 |
| [[p10_lr_instruction_builder]] | downstream | 0.26 |
| [[workflow-builder]] | downstream | 0.25 |
