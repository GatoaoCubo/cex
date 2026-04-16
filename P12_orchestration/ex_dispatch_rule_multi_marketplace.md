---
id: ex-dispatch-rule-multi-marketplace
kind: dispatch_rule
pillar: P12
title: Multi-Marketplace Authority Dispatch Rules
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_NAME
tags: [commerce, template, distillation, orchestration, dispatch_rule]
---

# Multi-Marketplace Authority Dispatch Rules

## Purpose
Declarative rules that tell the sync workflow WHICH channel is authoritative for WHICH field of WHICH entity. Without this, concurrent updates create thrash: Shopify overwrites ERP title, ERP overwrites Shopify stock, etc.

## When to use
- Two or more channels mutate overlapping fields.
- You need conflict resolution that is predictable and auditable.
- Brand policy is "ERP is fiscal truth, Shopify is copy truth, ML is enrichment only".

## Interface
- Consumed by: reconcile node of `ex_dag_multi_marketplace_sync.md`.
- Inputs: `{entity, field, channel_values: {shopify, bling, meli}}`
- Outputs: `{winning_channel, winning_value, reason}`

## Brand variables used
- `{{BRAND_NAME}}` -- rule labeling for operator UI; rules themselves are channel-keyed.

## Rule matrix (default policy)

| Entity | Field | Authoritative channel | Tie-breaker |
|--------|-------|-----------------------|-------------|
| product | title | shopify | latest updated_at |
| product | description | shopify | latest updated_at |
| product | price | bling | shopify fallback if bling null |
| product | sku / codigo | bling | immutable after first set |
| product | gtin | bling | meli enrichment fills if missing |
| product | brand | bling | meli enrichment fills if missing |
| product | category | shopify (channel nav) | bling ncm for fiscal |
| product | seo_title / seo_description | shopify | writer only in shopify |
| product | media (images) | shopify | never overwrite with ML thumbs |
| inventory | available_quantity | bling (ERP truth) | shopify pushes per warehouse |
| inventory | per-warehouse | bling | no fallback |
| orders | status | origin channel | do NOT cross-update status |
| orders | tracking | bling (fulfillment) | push to all others |

## Rule language
```yaml
- entity: product
  field: price
  authority: bling
  fallback:
    - channel: shopify
      condition: bling_value IS NULL
  tie_breaker: latest_updated_at
  on_conflict: log_and_use_authority
```

## Conflict handling
- Level `log` -- record in `sync_conflicts` table; continue with authority value.
- Level `alert` -- log + send notifier event for ops review.
- Level `block` -- abort the row's sync; require human resolution (rare, reserved for SKU mismatches).

## Override hooks
Brand can override a cell by adding a row to `dispatch_rule_overrides` table with `(entity, field, authority, reason, valid_until)`. Overrides expire automatically to avoid forgotten hacks.

## Related artifacts
- `ex_workflow_multi_marketplace_sync.md`
- `ex_dag_multi_marketplace_sync.md`
- `ex_validator_inventory_invariants.md`
