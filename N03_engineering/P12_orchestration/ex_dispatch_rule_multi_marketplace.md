---
id: ex_dispatch_rule_multi_marketplace
kind: dispatch_rule
pillar: P12
title: Multi-Marketplace Dispatch Rule
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_VERTICAL
tags: [commerce, template, distillation, dispatch, marketplace, routing]
---

## Purpose

Routing rules that determine which marketplace each product sync operation targets — controls conditional dispatch to Shopify, Bling ERP, and Mercado Livre based on product attributes, sync mode, and marketplace availability.

## When to Use

- Routing product updates to the correct marketplace(s) without hardcoded if-else logic.
- Skipping marketplaces that are not enabled for a specific product category or brand.
- Implementing marketplace-specific field filtering before dispatch.

## Rule Set

### Rule 1 — Route by Product Status

| Product Status | Shopify | Bling | Mercado Livre |
|---------------|---------|-------|---------------|
| `active` | YES | YES | optional |
| `draft` | NO | YES (internal) | NO |
| `archived` | NO (delete) | NO | NO |

### Rule 2 — Route by Sync Mode

| Sync Mode | Shopify | Bling | Mercado Livre |
|-----------|---------|-------|---------------|
| `pull` | source | NO | enrichment only |
| `push` | target | target | NO |
| `bidirectional` | source + target | target | enrichment |
| `single` | target | target | enrichment |

### Rule 3 — Route by Product Category

| Category | Shopify | Bling | Mercado Livre |
|----------|---------|-------|---------------|
| `pet_food` | YES | YES | YES |
| `accessories` | YES | YES | YES |
| `digital` | YES | NO (NF-e not applicable) | NO |
| `B2B_only` | NO | YES | NO |

### Rule 4 — Route by Field Changed

| Changed Field | Shopify | Bling | Notes |
|--------------|---------|-------|-------|
| `title` | YES | YES | SEO + catalog label |
| `price` | YES | YES | Both require price sync |
| `stock` | NO | YES | Shopify uses inventory_levels API separately |
| `description` | YES | NO | Bling descriptions are set at creation only |
| `images` | YES | NO | Bling does not manage images via API |
| `status` | YES | YES | Publish/unpublish controls |

## Dispatch Logic (Pseudocode)

```typescript
function getTargets(product: Product, mode: SyncMode, changedFields: string[]): Marketplace[] {
  const targets: Marketplace[] = [];

  if (product.status === 'archived') return [];

  // Shopify
  if (mode !== 'pull' && product.status === 'active') {
    if (product.category !== 'B2B_only' && product.category !== 'digital') {
      if (changedFields.some(f => ['title', 'price', 'description', 'images', 'status'].includes(f))) {
        targets.push('shopify');
      }
    }
  }

  // Bling
  if (['push', 'bidirectional', 'single'].includes(mode) && product.category !== 'digital') {
    if (changedFields.some(f => ['title', 'price', 'stock', 'status'].includes(f))) {
      targets.push('bling');
    }
  }

  // Mercado Livre (enrichment only — no push)
  if (mode === 'pull' || mode === 'bidirectional') {
    if (product.meli_id || product.ean) {
      targets.push('meli_enrich');
    }
  }

  return targets;
}
```

## Priority Order (on conflict)

| Priority | Marketplace | Rationale |
|----------|-------------|-----------|
| 1 | Supabase | Internal source of truth |
| 2 | Shopify | Customer-facing; freshness critical |
| 3 | Bling | ERP sync; can lag by minutes |
| 4 | Mercado Livre | Read-only enrichment; no write authority |

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `product` | Product object | Full product with all fields |
| `mode` | enum | Current sync mode |
| `changed_fields` | string[] | Which fields changed |

| Output | Type | Description |
|--------|------|-------------|
| `targets` | Marketplace[] | Ordered list of dispatch targets |
| `skip_reason` | string? | Why a marketplace was skipped |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Shopify target store |
| `{{BRAND_VERTICAL}}` | Drives category rules (ecommerce vs edtech) |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_workflow_multi_marketplace_sync.md` | workflow | Consumes these dispatch rules |
| `ex_dag_multi_marketplace_sync.md` | dag | DAG node routing |
| `ex_api_client_shopify.md` | api_client | Shopify target client |
| `ex_api_client_bling.md` | api_client | Bling target client |
