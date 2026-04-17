---
id: bld_examples_saga
kind: knowledge_card
pillar: P01
title: "Examples: saga"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: 7.4
tags: [examples, saga, P12]
llm_function: GOVERN
tldr: "Golden and anti-examples for saga construction."
density_score: null
---

# Examples: saga

## Golden Example: Order Fulfillment Saga
```yaml
---
id: p12_saga_order_fulfillment
kind: saga
pillar: P12
version: 1.0.0
saga_name: "Order Fulfillment"
steps_count: 4
topology: orchestration
on_failure: compensate_all
domain: commerce
quality: null
tags: [saga, commerce, order]
tldr: "4-step order fulfillment saga with compensation: reserve inventory, charge payment, ship, notify"
---
## Goal
Complete an order by reserving inventory, charging payment, shipping, and notifying the customer.

## Steps
| ID | Participant | Action | Compensating Action | On Failure |
|----|-------------|--------|---------------------|------------|
| s1_reserve | inventory-service | Reserve 1 unit of product | Release reservation | compensate |
| s2_charge | payment-service | Charge customer card | Refund charge | compensate |
| s3_ship | shipping-service | Create shipment label | Cancel shipment | compensate |
| s4_notify | notification-service | Send order confirmation | Send cancellation notice | skip |

## Rollback Sequence
On failure at s3_ship:
1. Compensate s2_charge: Refund charge to customer card
2. Compensate s1_reserve: Release inventory reservation

## Topology
**orchestration** -- Central saga orchestrator (N05) sends commands to each service and tracks state.
```

## Anti-Example (REJECTED)
```yaml
# FAILS H06: step without compensating action
steps:
  - id: s1_send_email
    action: Send welcome email
    compensating_action: null  # FAIL: cannot compensate?

# Fix: use idempotent compensating action
    compensating_action: Send cancellation email
```
