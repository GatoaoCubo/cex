---
id: kc_stripe_patterns
kind: knowledge_card
8f: F3_inject
pillar: P01
quality: 9.1
tldr: "Design patterns for integrating Stripe, including environment modes, webhook handling, and subscription management."
tags: ["stripe", "payment", "webhook", "subscription", "billing"]
updated: "2026-04-07"
domain: "knowledge management"
title: "Stripe Patterns"
version: "1.0.0"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.77
related:
  - bld_examples_integration_guide
  - bld_examples_faq_entry
  - bld_examples_webhook
  - p04_ex_content_monetization_saas
  - n06_integration_content_factory
  - webhook-builder
  - bld_knowledge_card_webhook
  - p01_kc_content_monetization
  - bld_collaboration_webhook
  - bld_config_webhook
---

# Stripe Integration Patterns

This document outlines key architectural patterns for robustly integrating the Stripe payment gateway.

## 1. Environment-Aware Executor

A fundamental pattern is to create a single service class (e.g., `BillingExecutor`) that operates in multiple modes to ensure safety and testability.

-   **LIVE**: The production environment using live API keys.
-   **TEST**: Uses Stripe's test environment and test keys for integration testing.
-   **MOCK**: A simulated environment that returns predictable responses without hitting the Stripe API, used for unit testing.

The application should select the mode at runtime based on configuration, which then determines the API keys and endpoints to use.

## 2. Secure Checkout Session Creation

Instead of building a payment form from scratch, the backend should generate a temporary, secure `checkout.session` via the Stripe API.

-   **Process**: The client requests a checkout session. The backend calls `create_checkout_session` with line items, prices, and success/cancel URLs. The backend returns the session ID to the client, which then redirects the user to the Stripe-hosted checkout page.
-   **Benefit**: This delegates PCI compliance to Stripe and simplifies the frontend implementation.

## 3. Idempotent Webhook Handling

Webhooks are essential for receiving asynchronous updates from Stripe about payment events. The webhook handler must be idempotent to prevent duplicate processing.

-   **Signature Verification**: Always verify the `Stripe-Signature` header to ensure the request is from Stripe.
-   **Event Parsing**: Parse the event payload to determine the `type` (e.g., `checkout.session.completed`, `invoice.paid`, `customer.subscription.deleted`).
-   **Idempotency**: Use the `idempotency_key` from the event or the event ID itself to ensure a given event is processed only once. This is critical as network issues can cause Stripe to resend the same event.
-   **Common Events**: A robust system should handle at least:
    -   `checkout.session.completed`
    -   `invoice.paid`
    -   `invoice.payment_failed`
    -   `customer.subscription.created`
    -   `customer.subscription.updated`
    -   `customer.subscription.deleted`

## 4. Subscription Lifecycle Management

The system needs functions to manage the full lifecycle of a customer's subscription.

-   **Create**: Initiate a subscription through a checkout session.
-   **Retrieve**: Fetch subscription status (`get_subscription`) using the subscription ID to check if it's active, past_due, or canceled.
-   **Update/Cancel**: Provide methods to change plans or cancel subscriptions.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `kc_stripe_patterns`
- **Tags**: ["stripe", "payment", "webhook", "subscription", "billing"]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_integration_guide]] | downstream | 0.36 |
| [[bld_examples_faq_entry]] | downstream | 0.30 |
| [[bld_examples_webhook]] | downstream | 0.29 |
| [[p04_ex_content_monetization_saas]] | downstream | 0.27 |
| [[n06_integration_content_factory]] | downstream | 0.26 |
| [[webhook-builder]] | downstream | 0.24 |
| [[bld_knowledge_card_webhook]] | sibling | 0.23 |
| [[p01_kc_content_monetization]] | sibling | 0.22 |
| [[bld_collaboration_webhook]] | downstream | 0.22 |
| [[bld_config_webhook]] | downstream | 0.21 |
