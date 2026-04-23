---
kind: quality_gate
id: p11_qg_event_schema
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of event_schema artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Gate: event_schema"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, event-schema, P06, cloudevents, asyncapi]
tldr: "Pass/fail gate for event_schema: id pattern, event_type versioning, JSON Schema payload, schema_version, all 4 sections."
domain: "event schema -- CloudEvents/AsyncAPI payload schema for event-driven systems"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_chunk_strategy
  - p11_qg_function_def
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p11_qg_constraint_spec
  - p11_qg_handoff_protocol
  - bld_examples_validation_schema
  - p11_qg_output_validator
  - p11_qg_prompt_version
  - p11_qg_vision_tool
---

## Quality Gate

# Gate: event_schema

## Definition

| Field | Value |
|---|---|
| metric | event_schema artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: event_schema` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p06_evs_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p06_evs_foo but file is p06_evs_bar.md |
| H04 | Kind equals literal `event_schema` | kind: event or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | event_type includes version suffix (.v{N}) | "com.acme.order.created" without version |
| H07 | schema_version is semver | "v1" instead of "1.0.0" |
| H08 | datacontenttype is "application/json" | Missing or non-JSON content type |
| H09 | Payload Schema is JSON Schema format | Field list instead of JSON Schema |
| H10 | Body has all 4 required sections | Missing CloudEvents Attributes, Payload Schema, Versioning, or Consumers |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| Payload schema completeness | 1.0 | All fields typed; required fields explicit |
| CloudEvents attributes documented | 1.0 | All 7 CloudEvents attributes covered |
| Versioning strategy | 1.0 | ADDITIVE_ONLY or VERSIONED_TYPE declared with rules |
| Consumer table | 1.0 | At least one consumer identified with action |
| event_type naming convention | 0.5 | Follows reverse-DNS pattern |
| Breaking change policy | 1.0 | Clear rules for what triggers new version |
| subject field usage | 0.5 | Subject attribute identifies entity |
| Boundary clarity | 1.0 | Explicitly NOT data_contract, NOT event_stream |
| tldr quality | 0.5 | tldr <= 160ch, includes event name and version |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Examples

# Examples: event-schema-builder

## Golden Example

INPUT: "Create event schema for order created domain event"

WHY THIS IS GOLDEN:
- id matches `^p06_evs_[a-z][a-z0-9_]+$` -- H02 pass
- event_type follows reverse-DNS naming with .v1 suffix -- H04 pass
- schema_version as semver -- H05 pass
- All 4 required sections present -- H06 pass
- quality: null -- H01 pass
- Full JSON Schema in payload -- H07 pass
- Versioning strategy declared -- best practice

```yaml
id: p06_evs_order_created_v1
kind: event_schema
pillar: P06
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
event_type: "com.example.order.created.v1"
schema_version: "1.0.0"
source: "/orders-service"
datacontenttype: "application/json"
quality: null
tags: [event_schema, order, ecommerce]
tldr: "OrderCreated v1: order_id, customer_id, items, total_amount. CloudEvents 1.0 envelope. Source: /orders-service."
```

## CloudEvents Attributes

| Attribute | Value | Required | Notes |
|-----------|-------|----------|-------|
| specversion | "1.0" | YES | CloudEvents spec version |
| id | UUID | YES | Unique per event |
| type | "com.example.order.created.v1" | YES | Reverse-DNS + version |
| source | "/orders-service" | YES | Producer URI |
| subject | order_id | REC | Entity identifier |
| time | RFC3339 timestamp | REC | Event occurrence time |
| datacontenttype | "application/json" | YES | Payload format |

## Payload Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12",
  "type": "object",
  "required": ["order_id", "customer_id", "items", "total_amount", "currency"],
  "properties": {
    "order_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique order identifier"
    },
    "customer_id": {
      "type": "string",
      "description": "Customer who placed the order"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["sku", "quantity", "unit_price"],
        "properties": {
          "sku": {"type": "string"},
          "quantity": {"type": "integer", "minimum": 1},
          "unit_price": {"type": "number", "minimum": 0}
        }
      }
    },
    "total_amount": {
      "type": "number",
      "minimum": 0,
      "description": "Order total in minor units"
    },
    "currency": {
      "type": "string",
      "pattern": "^[A-Z]{3}$",
      "description": "ISO 4217 currency code"
    }
  }
}
```

## Versioning

| Strategy | ADDITIVE_ONLY | Notes |
|----------|---------------|-------|
| Adding new optional fields | ALLOWED (minor version bump) | Backward compatible |
| Changing existing field types | PROHIBITED | Create new v2 type |
| Removing fields | PROHIBITED | Create new v2 type |
| New required fields | PROHIBITED | Create new v2 type |

v1 -> v2 migration: publish `com.example.order.created.v2` alongside v1.
Deprecate v1 after all consumers migrate. Never delete v1 while consumers exist.

## Consumers

| Consumer | Context | Action |
|----------|---------|--------|
| Inventory Service | Reserves stock for order items | Subscribes, calls reserveInventory() |
| Payment Service | Initiates payment collection | Subscribes, calls initiatePayment() |
| Notification Service | Sends order confirmation email | Subscribes, sends email |
| Analytics Pipeline | Records order event for reporting | Subscribes, writes to data warehouse |

---

## Anti-Example

INPUT: "Event for when order is created"
BAD OUTPUT:
```yaml
id: order-event
kind: event
event_name: OrderCreated
fields:
  - order_id
  - customer
quality: 9.0
```

FAILURES:
1. id: "order-event" has hyphens, no p06_evs_ prefix -> H02 FAIL
2. kind: "event" not "event_schema" -> H04 FAIL
3. No event_type (no CloudEvents type attribute) -> H04 FAIL
4. No schema_version -> H05 FAIL
5. quality: 9.0 (not null) -> H01 FAIL
6. Missing all 4 body sections -> H06 FAIL
7. "fields" is not JSON Schema format -> H07 FAIL
8. No CloudEvents envelope attributes declared

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
