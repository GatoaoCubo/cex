---
id: bld_qg_data_contract
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: 8.3
tags: [data_contract, quality-gate, schema, sla]
title: "Quality Gate: data_contract"
tldr: "Data Contract feedback: quality gate with scoring dimensions and pass/fail criteria"
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_citation
  - p06_vs_frontmatter
  - p11_qg_agent_computer_interface
  - p01_qg_faq_entry
  - p11_qg_input_schema
  - p11_qg_model_registry
  - p11_qg_few_shot_example
  - bld_examples_validation_schema
  - p11_qg_interface
  - p11_qg_context_window_config
---

## Quality Gate

# Quality Gate: data_contract
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | id matches `^dc_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | kind == "data_contract" | Wrong kind |
| H04 | quality == null | Non-null value |
| H05 | producer_system present and non-empty | Missing |
| H06 | consumer_system present and non-empty | Missing |
| H07 | entity present and PascalCase | Missing or snake_case |
| H08 | contract_version present (semver) | Missing or non-semver |
| H09 | Schema section with >= 1 typed field | Missing schema |
| H10 | Total file size <= 4096 bytes | Exceeds max_bytes |

## SOFT Scoring
| ID | Dimension | Weight | 10pts | 5pts | 0pts |
|----|-----------|--------|-------|------|------|
| S01 | SLA numeric thresholds | 1.0 | All metrics numeric | Some numeric | Vague only |
| S02 | Schema field completeness | 1.0 | type + nullable + desc per field | type + nullable | Type only |
| S03 | Versioning policy | 0.8 | backward_compat + policy + deprecation | Some policy | Absent |
| S04 | Enforcement documented | 0.7 | Schema registry + contract tests | One mechanism | Neither |
| S05 | Effective date set | 0.5 | Valid date | Date present | Absent |

## Score Tiers
| Score | Action |
|-------|--------|
| >= 9.0 | Publish; register in schema registry |
| >= 7.0 | Use with monitoring; improve SLA specifics |
| < 7.0 | Return: add numeric SLAs and typed schema fields |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
