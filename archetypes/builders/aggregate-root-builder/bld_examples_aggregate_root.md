---
id: bld_examples_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Examples"
version: 1.0.0
quality: null
tags: [builder, aggregate_root, examples]
llm_function: GOVERN
---
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
