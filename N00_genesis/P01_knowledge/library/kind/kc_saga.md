---
id: kc_saga
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 7.9
tags: [kind, taxonomy, saga, P12, orchestration, distributed_transaction]
density_score: 0.99
updated: "2026-04-17"
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

## Quality Criteria
- GOOD: All steps present with compensating_action, topology specified, rollback sequence defined
- GREAT: Compensating actions marked as idempotent, goal statement present, on_failure per step
- FAIL: Any step missing compensating_action, no rollback sequence, topology unspecified
