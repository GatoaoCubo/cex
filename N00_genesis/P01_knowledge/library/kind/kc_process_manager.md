---
id: kc_process_manager
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: null
tags: [kind, taxonomy, process_manager, eip, saga, P12]
---
# Knowledge Card: process_manager

## Definition
A `process_manager` is an event-driven coordinator for multi-step distributed processes.
It subscribes to domain events, maintains a state machine per process instance (identified
by a correlation key), and dispatches commands to participants at each step.
Pattern origin: Hohpe & Woolf Enterprise Integration Patterns (2003). Also known as
"Saga Orchestrator" in microservices contexts.

## When to Use
- A business process spans multiple services or aggregates and requires coordination
- Steps are event-driven (a service completes and emits an event, not polled)
- The process requires compensation (rollback) if any step fails
- Centralized visibility and audit trail of process state is required
- At least 2 services must participate in sequence or parallel with handoffs

## When NOT to Use
- Steps are sequential and synchronous in a single service: use `workflow`
- No cross-service coordination: use aggregate_root commands directly
- Single transaction, single aggregate: no orchestration needed
- Routing by keyword or intent pattern: use `dispatch_rule`
- Agent hierarchy management for LLM workflows: use `supervisor`

## Structure
Every `process_manager` defines:
1. **Correlation key**: field that identifies a process instance (e.g., orderId)
2. **Start event**: domain event that creates a new process instance
3. **States**: all possible states including start states and terminal states
4. **Event routing table**: for each incoming event x current state -> next state + command issued
5. **Commands issued**: commands dispatched to participants with target and payload
6. **Timeout strategy**: per-state timeouts with timeout actions (retry, escalate, fail)
7. **Compensation**: rollback commands for each failure path

## The Stateless Content Rule
A process manager holds ONLY process state and the correlation key.
It never stores business domain data (customer name, product details, amounts).
Domain data lives in the aggregates that own it.

## Compensation (Sagas)
Every forward step must have a compensating command:
- ProcessPayment -> CompensatingCommand: RefundPayment
- ReserveInventory -> CompensatingCommand: ReleaseInventory
- CreateShipment -> CompensatingCommand: CancelShipment
This is the saga pattern (Garcia-Molina 1987): each step can be undone.

## Use Cases
1. **Order Fulfillment**: OrderPlaced -> ProcessPayment -> ReserveInventory -> CreateShipment (with compensation on any failure)
2. **User Onboarding**: UserRegistered -> SendVerificationEmail -> InitiateKyc -> ActivateAccount
3. **Loan Application**: ApplicationSubmitted -> CreditCheck -> FraudCheck -> UnderwritingDecision -> Disburse

## Relationships to Other Kinds
| Kind | Relationship |
|------|-------------|
| `workflow` | sequential step execution (push/DAG model); process_manager is event-reactive |
| `supervisor` | agent hierarchy for LLM workflows; process_manager is for domain event routing |
| `dispatch_rule` | keyword/intent routing; process_manager routes by domain event + state |
| `domain_event` | inputs consumed by process_manager; emitted by participating aggregates |
| `schedule` | time-triggered orchestration; process_manager is event-triggered |

## Anti-Patterns
- **Process manager with business data**: stores name, amounts, addresses -- belongs in aggregates
- **Process manager that polls**: reacts to events, never polls services for status
- **Missing compensation**: every forward step needs an undo path; partial rollbacks cause inconsistency
- **Too many states**: > 10 states usually means the process should be split into sub-processes

## CEX Metadata
| Property | Value |
|----------|-------|
| Pillar | P12 (Orchestration) |
| ID pattern | `p12_pm_{slug}` |
| max_bytes | 4096 |
| llm_function | CALL |
| Builder | process-manager-builder (13 ISOs) |
| Nucleus | N07 (Orchestrator) or N03 (Engineering) |
| Pattern source | Hohpe & Woolf EIP (2003), Garcia-Molina Sagas (1987) |
