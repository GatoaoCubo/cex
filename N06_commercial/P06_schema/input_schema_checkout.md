---
id: input_schema_checkout
kind: input_schema
pillar: P06
nucleus: n06
title: "Input Schema -- Checkout and Order Flow Contract"
version: 1.0.0
quality: 9.0
tags: [checkout, order, schema, payment, commercial, contract]
density_score: 1.0
---

# Input Schema: Checkout and Order Flow Contract

## Purpose

Defines the canonical data contract for all checkout and order-creation flows in N06's commercial pipeline. Every pricing page, cart, and payment handler MUST validate against this schema before processing.

## Schema Definition

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "checkout_order_flow_v1",
  "title": "Checkout Order Flow",
  "type": "object",
  "required": ["product", "customer", "payment_method", "price"],
  "properties": {
    "product": {
      "type": "object",
      "required": ["id", "name", "plan_tier", "billing_cycle"],
      "properties": {
        "id": { "type": "string", "pattern": "^prod_[A-Za-z0-9]+$" },
        "name": { "type": "string", "minLength": 1, "maxLength": 200 },
        "plan_tier": { "$ref": "#/$defs/plan_tier" },
        "billing_cycle": { "enum": ["monthly", "annual", "lifetime", "one_time"] },
        "quantity": { "type": "integer", "minimum": 1, "default": 1 },
        "addons": {
          "type": "array",
          "items": { "$ref": "#/$defs/addon" }
        }
      }
    },
    "customer": {
      "type": "object",
      "required": ["email"],
      "properties": {
        "id": { "type": "string", "description": "Existing customer ID if returning" },
        "email": { "type": "string", "format": "email" },
        "name": { "type": "string" },
        "company": { "type": "string" },
        "country": { "type": "string", "pattern": "^[A-Z]{2}$" },
        "tax_id": { "type": "string", "description": "VAT/EIN for B2B invoicing" }
      }
    },
    "payment_method": {
      "type": "object",
      "required": ["provider"],
      "properties": {
        "provider": { "enum": ["stripe", "paypal", "pix", "bank_transfer", "crypto"] },
        "token": { "type": "string", "description": "Provider payment token (e.g., Stripe pm_*)" },
        "save_for_future": { "type": "boolean", "default": false }
      }
    },
    "price": {
      "type": "object",
      "required": ["currency", "amount_cents"],
      "properties": {
        "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
        "amount_cents": { "type": "integer", "minimum": 0 },
        "discount_code": { "type": "string" },
        "discount_percent": { "type": "number", "minimum": 0, "maximum": 100 },
        "tax_amount_cents": { "type": "integer", "minimum": 0 },
        "trial_days": { "type": "integer", "minimum": 0, "default": 0 }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "utm_source": { "type": "string" },
        "utm_medium": { "type": "string" },
        "utm_campaign": { "type": "string" },
        "referral_code": { "type": "string" },
        "affiliate_id": { "type": "string" }
      }
    }
  },
  "$defs": {
    "plan_tier": { "enum": ["free", "starter", "pro", "enterprise", "custom"] },
    "addon": {
      "type": "object",
      "required": ["id", "name", "price_cents"],
      "properties": {
        "id": { "type": "string" },
        "name": { "type": "string" },
        "price_cents": { "type": "integer", "minimum": 0 }
      }
    }
  }
}
```

## Validation Rules

| Field | Rule | Error Code |
|-------|------|-----------|
| product.id | Must match `prod_*` pattern | E001_INVALID_PRODUCT_ID |
| customer.email | Valid RFC 5321 email | E002_INVALID_EMAIL |
| price.amount_cents | Non-negative integer | E003_INVALID_AMOUNT |
| payment_method.provider | From allowed enum | E004_UNSUPPORTED_PROVIDER |
| price.currency | ISO 4217 3-letter code | E005_INVALID_CURRENCY |
| price.discount_percent | 0-100 range | E006_INVALID_DISCOUNT |

## Integration Points

- **Pricing page** -> validates before Stripe session creation
- **API endpoint** `POST /checkout/create` -> validates request body
- **Webhook handler** -> validates reconstructed order on event replay
- **Referral system** -> reads `metadata.referral_code` for attribution

## Revenue Intelligence Notes

Track `metadata.utm_*` fields to measure channel ROI. `referral_code` attribution feeds into referral_program payout calculation. `trial_days > 0` triggers churn_prevention_playbook activation at day `trial_days - 3`.
