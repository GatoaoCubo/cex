---
id: bld_quality_gate_saga
kind: quality_gate
pillar: P07
title: "Gate: saga"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: 8.7
tags: [quality_gate, saga, P12]
llm_function: GOVERN
tldr: "Validates saga for compensation completeness, rollback sequence, and topology definition."
density_score: null
related:
  - p11_qg_workflow
  - p11_qg_instruction
  - bld_instruction_chain
  - p11_qg_chain
  - p12_wf_builder_8f_pipeline
  - p10_lr_instruction_builder
  - p11_qg_quality_gate
  - p11_qg_system_prompt
  - bld_knowledge_card_workflow
  - tpl_instruction
---

## Quality Gate

## Definition
A saga must be fully compensable: every step that executes a side effect must have a compensating action that undoes it. This gate ensures no saga enters production with uncompensable steps.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML valid |
| H02 | ID matches namespace | `^p12_saga_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `saga` |
| H04 | Quality is null | `quality: null` |
| H05 | Topology specified | topology is choreography or orchestration |
| H06 | All steps have compensating_action | No null or empty compensating_action in any step |
| H07 | steps_count matches list | frontmatter count = actual step count |
| H08 | on_failure at saga level | on_failure is non-null |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Rollback sequence explicit | 1.0 | Rollback Sequence section present with ordered list |
| Compensating actions are idempotent | 1.0 | Actions described as retry-safe |
| Goal statement present | 0.5 | ## Goal section has one-sentence description |
| Participant identified per step | 0.5 | Each step has participant field |
| Tags include saga | 0.5 | tags contains "saga" |

Sum of weights: 3.5. `soft_score = sum / 3.5 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT -- do not deploy without compensation completeness |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
