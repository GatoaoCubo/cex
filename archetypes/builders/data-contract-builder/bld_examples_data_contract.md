---
id: bld_examples_data_contract
kind: few_shot_example
pillar: P03
llm_function: GOVERN
version: 1.0.0
quality: 5.1
tags: [data_contract, examples, few-shot]
title: "Examples: data_contract"
density_score: 1.0
updated: "2026-04-17"
---
# Examples: data_contract
## Example 1: Sales -> Billing Order Contract
```yaml
id: dc_sales_billing_order
kind: data_contract
pillar: P06
title: "Sales -> Billing: Order Contract"
producer_system: sales-service
consumer_system: billing-service
entity: Order
contract_version: 1.2.0
effective_date: "2026-04-01"
quality: null
tags: [sales, billing, order, data-contract]
```
Schema: order_id (uuid, non-null), customer_id (uuid, non-null),
        total_amount (decimal, non-null), currency (ISO-4217, non-null),
        status (enum: pending|confirmed|cancelled)
SLA: freshness < 5s, availability 99.9%, latency_p99 < 200ms

## Example 2: Events -> Analytics Clickstream
```yaml
id: dc_events_analytics_clickstream
kind: data_contract
pillar: P06
title: "Events -> Analytics: Clickstream Contract"
producer_system: event-collector
consumer_system: analytics-warehouse
entity: ClickEvent
contract_version: 2.0.0
effective_date: "2026-03-01"
quality: null
tags: [events, analytics, clickstream, data-contract]
```
Schema: event_id (uuid), user_id (uuid, nullable), session_id (string),
        page_url (string), timestamp (ISO-8601)
SLA: freshness < 15min (batch), availability 99.5%, completeness >= 99%

## Anti-example (WRONG)
```yaml
id: llm_output_validator    # WRONG: this is validation_schema, not data_contract
kind: data_contract         # WRONG: LLM output validation != cross-system contract
# Missing producer_system   # WRONG: required field
```
