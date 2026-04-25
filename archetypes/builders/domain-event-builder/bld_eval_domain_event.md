---
id: bld_qg_domain_event
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: 8.3
tags: [domain_event, quality-gate, ddd]
title: "Quality Gate: domain_event"
tldr: "Domain Event feedback: quality gate with scoring dimensions and pass/fail criteria"
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_agent_computer_interface
  - p11_qg_few_shot_example
  - p11_qg_glossary_entry
  - p11_qg_citation
  - p11_qg_formatter
  - p11_qg_input_schema
  - p11_qg_knowledge_card
  - p11_qg_quality_gate
  - p11_qg_model_registry
  - p05_qg_github_issue_template
---

## Quality Gate

# Quality Gate: domain_event
## HARD Gates (all must pass)
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | id matches `^de_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | kind == "domain_event" | Wrong kind value |
| H04 | quality == null | Any non-null value |
| H05 | aggregate_root present and non-empty | Missing field |
| H06 | bounded_context present and non-empty | Missing field |
| H07 | occurred_at present and ISO-8601 format | Missing or wrong format |
| H08 | payload section present in body with >= 1 field | Empty or missing payload |
| H09 | Event title/name is past tense | Present or imperative tense |
| H10 | Total file size <= 3072 bytes | Exceeds max_bytes |

## SOFT Scoring
| ID | Dimension | Weight | 10pts | 5pts | 0pts |
|----|-----------|--------|-------|------|------|
| S01 | Causal chain (causation_id + correlation_id) | 1.0 | Both present | One present | Neither |
| S02 | Payload typed and documented | 1.0 | All fields typed | Partial | No types |
| S03 | Consumers documented | 0.8 | >= 1 consumer with reaction | Present, no detail | Absent |
| S04 | Business invariants stated | 0.8 | >= 1 invariant | Vague | Absent |
| S05 | Tags cover aggregate + context | 0.6 | >= 3 distinct tags | 2 tags | < 2 |

## Score Tiers
| Score | Action |
|-------|--------|
| >= 9.0 | Publish to bounded context event catalog |
| >= 7.0 | Use in workflows; flag for invariant improvement |
| < 7.0 | Return: add payload types, consumers, causal chain |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
