---
id: kc_credit_system_design
kind: knowledge_card
8f: F3_inject
pillar: P01
quality: 9.0
tldr: "Architectural patterns for a prepaid credit wallet system, including integer-based currency, service costs, and idempotent operations."
tags: ["credits", "wallet", "billing", "currency", "idempotency"]
related:
  - n06_content_factory_pricing
  - n06_integration_content_factory
  - n06_kc_content_monetization
  - p04_tpl_content_monetization
  - bld_instruction_content_monetization
  - kc_pricing_strategy
  - n06_pricing_content_factory
  - p12_wf_content_monetization
  - p12_dr_content_monetization
  - content-monetization-builder
---

# Prepaid Credit System Design

This card details common patterns for implementing a prepaid credit or "wallet" system, allowing users to purchase and spend credits on platform services.

## 1. Integer-Based Currency

To avoid floating-point precision errors, all currency and credit values should be stored and manipulated as integers representing the smallest currency unit (e.g., centavos for BRL, cents for USD).

-   **Example**: R$ 10,50 is stored as `1050`.
-   **Benefit**: Ensures transactional accuracy and prevents rounding issues that can occur with floating-point arithmetic.

## 2. Centralized Service Cost Mapping

Define the cost for various platform services or API calls in a centralized, human-readable dictionary or map.

-   **Pattern**: A constant like `PIPELINE_COSTS` maps service names to their integer credit cost.
-   **Example**:
    ```
    PIPELINE_COSTS = {
      "SERVICE_A": 100,  // Costs 100 credits
      "SERVICE_B": 75,
      "FULL_PIPELINE": 250
    }
    ```
-   **Benefit**: Simplifies pricing updates and makes the cost structure easy to audit.

## 3. Tiered Credit Packages

Offer credits for sale in predefined packages, often with discounts for larger volumes to encourage bulk purchases.

-   **Pattern**: A structure like `DEFAULT_PACKS` defines the tiers.
-   **Example**:
    ```
    DEFAULT_PACKS = [
      {"price": 500, "credits": 500},       // R$5,00 pack
      {"price": 2000, "credits": 2100},   // R$20,00 pack (5% bonus)
      {"price": 6000, "credits": 6600}    // R$60,00 pack (10% bonus)
    ]
    ```

## 4. Core Idempotent Wallet Operations

The wallet service class (`CreditSystem`) must expose a set of core, idempotent operations to manage the user's balance.

-   **`check_sufficient(amount)`**: Returns `True` if the user's balance is greater than or equal to `amount`.
-   **`consume(amount, idempotency_key)`**: Debits the user's balance. It must first check for sufficient funds and then record the `idempotency_key` to prevent the same transaction from being processed twice.
-   **`refund(amount, idempotency_key)`**: Credits the user's balance. Also uses an `idempotency_key` to prevent duplicate refunds.
-   **`add_credits(amount)`**: Increases the balance, typically called after a successful payment webhook is received.

## 5. Purchase Orchestration

A dedicated function (e.g., `purchase_pack_pix`) should orchestrate the process of buying a credit pack. This function is responsible for:
1.  Identifying the selected credit pack.
2.  Creating a payment order/intent with a payment provider (like Stripe or MercadoPago).
3.  Returning the necessary details for the client to complete the payment.
4.  The actual credits are added by the webhook handler only after payment is confirmed.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_content_factory_pricing]] | downstream | 0.35 |
| [[n06_integration_content_factory]] | downstream | 0.34 |
| [[n06_kc_content_monetization]] | sibling | 0.33 |
| [[p04_tpl_content_monetization]] | downstream | 0.30 |
| [[bld_instruction_content_monetization]] | downstream | 0.26 |
| [[kc_pricing_strategy]] | sibling | 0.26 |
| [[n06_pricing_content_factory]] | downstream | 0.25 |
| [[p12_wf_content_monetization]] | downstream | 0.24 |
| [[p12_dr_content_monetization]] | downstream | 0.24 |
| [[content-monetization-builder]] | downstream | 0.23 |
