---
id: bld_examples_domain_event
kind: few_shot_example
pillar: P03
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [domain_event, examples, few-shot]
title: "Examples: domain_event"
---
# Examples: domain_event
## Example 1: E-commerce OrderPlaced
```yaml
id: de_order_placed
kind: domain_event
pillar: P12
title: "OrderPlaced"
aggregate_root: Order
bounded_context: sales
event_version: v1
occurred_at: "2026-04-17T14:32:01Z"
causation_id: "cmd_place_order_abc123"
correlation_id: "saga_checkout_xyz789"
quality: null
tags: [order, sales, domain-event]
```
Payload: order_id (uuid), customer_id (uuid), total_amount (decimal),
         currency (ISO-4217), line_items (list[{sku, qty, price}])

## Example 2: SaaS PaymentFailed
```yaml
id: de_payment_failed
kind: domain_event
pillar: P12
title: "PaymentFailed"
aggregate_root: Payment
bounded_context: billing
event_version: v1
occurred_at: "2026-04-17T15:00:00Z"
causation_id: "cmd_charge_card_def456"
correlation_id: "saga_subscription_renewal_001"
quality: null
tags: [payment, billing, domain-event, failure]
```
Payload: payment_id (uuid), customer_id (uuid), amount (decimal),
         failure_reason (enum: insufficient_funds|card_expired|fraud_detected)

## Anti-example (WRONG)
```yaml
id: heartbeat_received   # WRONG: system event, not domain
kind: domain_event       # WRONG: should be signal
# No aggregate_root      # WRONG: missing required field
```
