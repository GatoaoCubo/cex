---
kind: quality_gate
id: p11_qg_state_machine
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of state_machine artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 8.8
title: "Gate: state_machine"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, state-machine, P12, fsm, entity-lifecycle]
tldr: "Pass/fail gate for state_machine: id pattern, initial/final states, determinism, transitions completeness, all 4 sections."
domain: "state machine -- formal FSM for entity lifecycle"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_chunk_strategy
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_lifecycle_rule
  - p11_qg_constraint_spec
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_prompt_version
  - p11_qg_hook_config
  - p11_qg_checkpoint
---

## Quality Gate

# Gate: state_machine

## Definition

| Field | Value |
|---|---|
| metric | state_machine artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: state_machine` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p12_sm_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p12_sm_foo but file is p12_sm_bar.md |
| H04 | Kind equals literal `state_machine` | kind: fsm or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | initial_state is in states list | initial_state refers to undeclared state |
| H07 | All final_states are in states list | final_state refers to undeclared state |
| H08 | states_count matches body count | Declared 7 but listed 5 |
| H09 | transitions_count matches body count | Declared 9 but listed 7 |
| H10 | Body has all 4 required sections | Missing States, Transitions, Guards, or Actions |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| State completeness | 1.0 | All meaningful lifecycle states documented |
| Transition completeness | 1.0 | All valid state changes covered |
| Guard implementability | 1.0 | All guards defined as boolean expressions |
| Action completeness | 1.0 | All side-effects defined with triggers and effects |
| Determinism | 1.0 | No ambiguous transitions without guards |
| Final state coverage | 1.0 | All entity termination paths have final states |
| Event naming | 0.5 | Events in UPPER_SNAKE_CASE |
| Boundary clarity | 1.0 | Explicitly NOT workflow (DAG), NOT process_manager |
| tldr quality | 0.5 | tldr includes entity name, state count, transition count |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Examples

# Examples: state-machine-builder

## Golden Example

INPUT: "Create state machine for Order entity lifecycle"

WHY THIS IS GOLDEN:
- id matches `^p12_sm_[a-z][a-z0-9_]+$` -- H02 pass
- initial_state declared and in states list -- H04 pass
- final_states declared and in states list -- H05 pass
- states_count matches body -- H06 pass
- transitions_count matches body -- H07 pass
- All 4 required sections present -- H08 pass
- No non-deterministic transitions -- H09 pass
- quality: null -- H01 pass

```yaml
id: p12_sm_order_lifecycle
kind: state_machine
pillar: P12
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
entity: "Order"
initial_state: "DRAFT"
final_states: ["CANCELLED", "DELIVERED"]
states_count: 7
transitions_count: 9
quality: null
tags: [state_machine, order, ecommerce]
tldr: "Order lifecycle FSM: 7 states, 9 transitions. DRAFT -> SUBMITTED -> PAID -> FULFILLING -> SHIPPED -> DELIVERED | CANCELLED."
```

## States

| State | Type | Description |
|-------|------|-------------|
| DRAFT | initial | Order being built by customer |
| SUBMITTED | intermediate | Order submitted, awaiting payment |
| PAID | intermediate | Payment confirmed |
| FULFILLING | intermediate | Warehouse processing the order |
| SHIPPED | intermediate | Order dispatched to carrier |
| DELIVERED | final | Order received by customer |
| CANCELLED | final | Order cancelled (any stage before SHIPPED) |

## Transitions

| from_state | event | to_state | guard | action |
|------------|-------|----------|-------|--------|
| DRAFT | SUBMIT | SUBMITTED | hasItems() AND hasShippingAddress() | reserveInventory() |
| SUBMITTED | PAYMENT_CONFIRMED | PAID | - | sendOrderConfirmation() |
| SUBMITTED | PAYMENT_FAILED | DRAFT | - | releaseInventory() |
| PAID | START_FULFILLMENT | FULFILLING | - | notifyWarehouse() |
| FULFILLING | SHIP | SHIPPED | allItemsPacked() | sendTrackingNumber() |
| SHIPPED | DELIVER | DELIVERED | - | releasePayment() |
| DRAFT | CANCEL | CANCELLED | - | releaseInventory() |
| SUBMITTED | CANCEL | CANCELLED | - | refundPayment() |
| PAID | CANCEL | CANCELLED | - | initiateRefund(); releaseInventory() |

## Guards

| Guard | Expression | Notes |
|-------|-----------|-------|
| hasItems() | order.items.length > 0 | Cannot submit empty order |
| hasShippingAddress() | order.shipping_address != null | Required for fulfillment |
| allItemsPacked() | order.items.all(packed: true) | Warehouse confirms all packed |

## Actions

| Action | Trigger | Effect |
|--------|---------|--------|
| reserveInventory() | DRAFT -> SUBMITTED | Lock inventory for 30 minutes |
| releaseInventory() | SUBMITTED -> DRAFT or CANCELLED | Unlock reserved inventory |
| sendOrderConfirmation() | SUBMITTED -> PAID | Email customer receipt |
| notifyWarehouse() | PAID -> FULFILLING | Dispatch fulfillment task |
| sendTrackingNumber() | FULFILLING -> SHIPPED | Email tracking to customer |
| releasePayment() | SHIPPED -> DELIVERED | Release funds to merchant |
| refundPayment() | SUBMITTED -> CANCELLED | Initiate payment reversal |
| initiateRefund() | PAID -> CANCELLED | Initiate payment reversal |

---

## Anti-Example

INPUT: "State machine for order"
BAD OUTPUT:
```yaml
id: order-states
kind: fsm
states: [new, processing, done]
transitions:
  - new -> processing
  - processing -> done
quality: 8.0
```

FAILURES:
1. id: "order-states" has hyphens, no p12_sm_ prefix -> H02 FAIL
2. kind: "fsm" not "state_machine" -> H04 FAIL
3. No initial_state, final_states declared -> H04/H05 FAIL
4. No events on transitions (just state names) -> H08 FAIL
5. quality: 8.0 (not null) -> H01 FAIL
6. Missing all 4 required sections -> H08 FAIL
7. No guards, no actions defined -> incomplete spec
8. states_count not declared -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
