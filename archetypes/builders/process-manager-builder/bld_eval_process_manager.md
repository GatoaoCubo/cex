---
id: bld_quality_gate_process_manager
kind: quality_gate
pillar: P12
title: "Process Manager Builder -- Quality Gate"
version: 1.0.0
quality: 8.3
tags: [builder, process_manager, quality_gate]
llm_function: GOVERN
tldr: "Process Manager orchestration: quality gate with scoring dimensions and pass/fail criteria"
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_kind_builder
  - p11_qg_agent_computer_interface
  - p11_qg_quality_gate
  - p11_qg_runtime_state
  - p07_qg_eval_metric
  - p11_qg_creation_artifacts
  - p11_qg_mental_model
  - p11_qg_naming_rule
  - p11_qg_retriever_config
  - p11_qg_lifecycle_rule
---

## Quality Gate

# Gate: process_manager
## Threshold
>= 7.0 to publish; >= 9.0 for reference
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p12_pm_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `process_manager` | Any other value |
| H05 | quality == null | Non-null |
| H06 | correlation_key defined | Missing |
| H07 | start_event defined | Missing |
| H08 | terminal_states has >= 2 entries (success + failure) | Fewer than 2 |
| H09 | subscribed_events has >= 1 entry | Empty |
| H10 | commands_issued has >= 1 entry | Empty |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Event routing table complete (event -> state + command) | 0.25 |
| S02 | Compensation actions defined for each failure path | 0.20 |
| S03 | Timeout strategy defined for waiting states | 0.15 |
| S04 | No business data in process manager (state + key only) | 0.20 |
| S05 | Idempotency key specified for commands | 0.10 |
| S06 | Persistence strategy specified | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |

## Examples

# Examples: process_manager
## Golden Example: Order Fulfillment
```yaml
id: p12_pm_order_fulfillment
kind: process_manager
correlation_key: orderId
start_event: OrderPlaced
terminal_states: [FULFILLED, CANCELLED]
states: [PAYMENT_PENDING, INVENTORY_PENDING, SHIPPING_PENDING, FULFILLED, CANCELLED]
subscribed_events: [OrderPlaced, PaymentConfirmed, InventoryReserved, ShipmentCreated, PaymentFailed]
commands_issued:
  - "ProcessPayment -> PaymentService"
  - "ReserveInventory -> InventoryService"
  - "CreateShipment -> ShippingService"
  - "ReleaseInventory -> InventoryService (compensation)"
  - "RefundPayment -> PaymentService (compensation)"
```
## Golden Example: User Onboarding
```yaml
id: p12_pm_user_onboarding
kind: process_manager
correlation_key: userId
start_event: UserRegistered
terminal_states: [ONBOARDED, REJECTED]
subscribed_events: [UserRegistered, EmailVerified, ProfileCompleted, KycApproved, KycRejected]
commands_issued:
  - "SendVerificationEmail -> NotificationService"
  - "InitiateKyc -> KycService"
  - "ActivateAccount -> AccountService"
  - "NotifyRejection -> NotificationService (compensation)"
```
## Anti-Pattern: Process Manager with Business Data
```yaml
# WRONG -- storing customer data in process manager
states: [CREATED, PROCESSING, DONE]
customer_email: "user@example.com"  # belongs in domain, not here
# CORRECT: process manager holds correlation_key + state only
```
## Anti-Pattern: Missing Compensation
```yaml
# WRONG -- no rollback on failure
commands_issued: ["ProcessPayment -> PaymentService"]
compensation: []
# CORRECT: every forward step needs a compensating command
compensation:
  - "On CANCELLED: RefundPayment -> PaymentService"
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
