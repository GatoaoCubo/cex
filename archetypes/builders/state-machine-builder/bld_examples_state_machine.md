---
kind: examples
id: bld_examples_state_machine
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of state_machine artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: null
title: "Examples State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, examples]
tldr: "Golden and anti-examples for state_machine: states table, transitions with guards/actions, deterministic FSM."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

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
