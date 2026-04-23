---
id: bld_quality_gate_aggregate_root
kind: quality_gate
pillar: P06
title: "Aggregate Root Builder -- Quality Gate"
version: 1.0.0
quality: 8.3
tags: [builder, aggregate_root, quality_gate]
llm_function: GOVERN
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_quality_gate
  - p11_qg_creation_artifacts
  - p11_qg_agent_computer_interface
  - p11_qg_naming_rule
  - p11_qg_boot_config
  - p11_qg_input_schema
  - p11_qg_marketing_artifacts
  - p11_qg_few_shot_example
  - p11_qg_pattern
  - p11_qg_glossary_entry
---

## Quality Gate

# Gate: aggregate_root
## Threshold
>= 7.0 to publish; >= 9.0 for reference
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p06_ar_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `aggregate_root` | Any other value |
| H05 | quality == null | Non-null |
| H06 | bounded_context present | Missing |
| H07 | invariants list has >= 2 entries | Fewer than 2 |
| H08 | commands list has >= 1 entry | Empty |
| H09 | domain_events list has >= 1 entry | Empty |
| H10 | repository field present | Missing |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Invariants are concrete measurable rules, not aspirational | 0.20 |
| S02 | Commands have pre/postconditions | 0.15 |
| S03 | Domain events have payload defined | 0.10 |
| S04 | cluster_members lists all entities and value_objects | 0.15 |
| S05 | No cross-aggregate object references (ID only) | 0.20 |
| S06 | repository interface is find_by_id + save only | 0.10 |
| S07 | Boundaries section distinguishes inside vs outside | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |

## Examples

# Examples: aggregate_root
## Golden Example: Order
```yaml
id: p06_ar_order
kind: aggregate_root
bounded_context: sales
invariants:
  - "Total price equals sum of all line items * quantity"
  - "Order cannot be shipped if payment status is not confirmed"
commands:
  - "AddItem(productId, qty): pre=order.status==draft, post=lineItems contains item"
  - "ConfirmPayment(paymentRef): pre=total>0, post=status==paid"
domain_events:
  - "OrderPlaced: emitted on first AddItem + ConfirmPayment, payload={orderId, total}"
  - "PaymentConfirmed: payload={orderId, paymentRef}"
repository: OrderRepository
cluster_members: ["LineItem (entity)", "Money (value_object)"]
```
## Golden Example: User Account
```yaml
id: p06_ar_user_account
kind: aggregate_root
bounded_context: identity
invariants:
  - "Email must be unique within the system (enforced at domain level)"
  - "Password hash must never be empty after account activation"
commands:
  - "Activate(emailToken): pre=status==pending, post=status==active"
  - "ChangePassword(newHash): pre=status==active"
domain_events:
  - "AccountActivated: payload={userId, email}"
repository: UserAccountRepository
```
## Anti-Pattern: Anemic Root
```yaml
# WRONG -- no invariants, just a data bag
id: p06_ar_product_bad
invariants: []
commands: ["Update(data): no precondition, no postcondition"]
# CORRECT: if no invariants, use type_def instead
```
## Anti-Pattern: Cross-Aggregate Object Reference
```yaml
# WRONG
cluster_members: ["Order (aggregate_root object)"]
# CORRECT
cluster_members: ["orderId: OrderId (value_object representing foreign key)"]
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
