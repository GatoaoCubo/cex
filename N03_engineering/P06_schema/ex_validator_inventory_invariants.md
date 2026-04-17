---
id: ex_validator_inventory_invariants
kind: validator
pillar: P06
title: Inventory Invariants Validator
version: 0.1.0
quality: 8.0
status: template
brand_placeholders:
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, validator, inventory, invariants]
density_score: 0.99
updated: "2026-04-17"
---

## Purpose

Validates business invariants for product inventory records — enforces non-negative stock, price floor, SKU format, and encoding integrity constraints before any write to Supabase, Shopify, or Bling.

## When to Use

- Before inserting or updating a product in any marketplace.
- During inventory reconciliation to flag records that violate business rules.
- As a pre-flight check in sync workflows to prevent corrupted data propagation.
- To detect and fix double-UTF-8 encoding in product strings.

## Invariants

### INV-01: Non-negative Stock

```
stock >= 0
```

Negative stock is a data error. Log and reject. Do not propagate to Shopify or Bling.

### INV-02: Price Floor

```
price > 0
```

Zero-price products are treated as incomplete catalog entries. Block publishing until corrected.

### INV-03: SKU Format

```
sku matches /^[A-Z0-9][A-Z0-9\-]{2,29}$/
```

SKUs must be uppercase alphanumeric with optional hyphens, 3-30 chars. Reject free-form strings.

### INV-04: Encoding Integrity (UTF-8)

Product titles and descriptions must not contain double-encoded UTF-8 sequences.

```typescript
function hasDoubleEncoding(str: string): boolean {
  const badPatterns = [/Ã£/, /Ã§/, /Ã£/, /Ã©/, /Ã/, /Ã\u00a3/];
  return badPatterns.some(p => p.test(str));
}

function fixDoubleEncoding(str: string): string {
  // Double-decode: treat the string as Latin-1 and re-encode as UTF-8
  return decodeURIComponent(escape(str));
}
```

Common double-encoded sequences from Shopify pull:
| Broken | Correct |
|--------|---------|
| `PortÃ£o` | `Portão` |
| `RetrÃ¡til` | `Retrátil` |
| `RaÃ§Ã£o` | `Ração` |

### INV-05: Title Length

```
title.length >= 3 && title.length <= 255
```

Shopify and Bling both enforce a 255-character title limit. Truncate at import with a warning.

### INV-06: Shopify ID Consistency

If `shopify_id` is set, it must be a positive integer. Null is valid (product not yet in Shopify).

```typescript
shopify_id === null || (Number.isInteger(shopify_id) && shopify_id > 0)
```

## Validator Schema

```typescript
interface InventoryRecord {
  sku: string;
  title: string;
  price: number;
  stock: number;
  shopify_id: number | null;
  bling_id: number | null;
}

function validateInventoryRecord(record: InventoryRecord): ValidationResult {
  const errors: string[] = [];

  if (record.stock < 0) errors.push(`INV-01: stock=${record.stock} is negative`);
  if (record.price <= 0) errors.push(`INV-02: price=${record.price} is not positive`);
  if (!/^[A-Z0-9][A-Z0-9\-]{2,29}$/.test(record.sku)) errors.push(`INV-03: invalid SKU format: ${record.sku}`);
  if (hasDoubleEncoding(record.title)) errors.push(`INV-04: double-encoding detected in title`);
  if (record.title.length < 3 || record.title.length > 255) errors.push(`INV-05: title length out of range`);
  if (record.shopify_id !== null && (!Number.isInteger(record.shopify_id) || record.shopify_id <= 0))
    errors.push(`INV-06: invalid shopify_id: ${record.shopify_id}`);

  return { valid: errors.length === 0, errors };
}
```

## Validation Result

```json
{
  "valid": false,
  "errors": [
    "INV-04: double-encoding detected in title",
    "INV-02: price=0 is not positive"
  ],
  "record_id": "uuid-here",
  "fixable": ["INV-04"],
  "requires_human": ["INV-02"]
}
```

## Auto-Fix Scope

| Invariant | Auto-fixable | Method |
|-----------|-------------|--------|
| INV-04 encoding | YES | `fixDoubleEncoding(title)` |
| INV-05 title too long | YES | Truncate to 255 |
| INV-01 negative stock | NO | Requires human review |
| INV-02 zero price | NO | Requires human review |
| INV-03 bad SKU | NO | Requires human review |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for validation logs |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_workflow_inventory_reconcile.md` | workflow | Calls this validator |
| `ex_interface_supabase_tables.md` | interface | Products table schema being validated |
| `ex_api_client_shopify.md` | api_client | Shopify data (source of encoding bugs) |
