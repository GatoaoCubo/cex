---
id: bld_examples_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Examples"
version: 1.0.0
quality: null
tags: [builder, process_manager, examples]
llm_function: GOVERN
---
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
