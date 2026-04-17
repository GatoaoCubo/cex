---
id: ex_webhook_bling
kind: webhook
pillar: P04
title: Bling ERP Webhook Handler
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_BLING_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, bling, erp, webhook]
---

## Purpose

Inbound webhook handler for Bling ERP events — validates signatures and processes `produto_alterado`, `estoque_alterado` payloads to update Supabase product and stock records in real time.

## When to Use

- Reacting to stock level changes in Bling ERP without polling.
- Keeping Supabase inventory in sync when Bling is the stock source of truth.
- Triggering reconciliation workflows after bulk Bling operations.

## Events

| Event Type | Trigger Condition | Key Payload Fields |
|------------|------------------|-------------------|
| `produto_alterado` | Product fields updated in Bling | `id`, `codigo`, `nome`, `preco`, `situacao` |
| `produto_inserido` | New product created in Bling | Same as `produto_alterado` |
| `produto_excluido` | Product deleted from Bling | `id` |
| `estoque_alterado` | Stock quantity changed | `id`, `codigo`, `estoqueAtual` |

## Verification

| Field | Value |
|-------|-------|
| Method | HMAC-SHA256 (check Bling docs for current scheme) |
| Header | `X-Bling-Signature` (or equivalent) |
| Secret env | `{{BRAND_BLING_WEBHOOK_SECRET}}` |

> **Note**: Bling webhook signature scheme may vary by plan and version. Verify against current Bling developer documentation. If signature verification is unavailable, restrict the endpoint by IP allowlist (Bling's known IP ranges).

```typescript
async function verifyBlingSignature(req: Request, secret: string): Promise<boolean> {
  const sig = req.headers.get('X-Bling-Signature') ?? '';
  const body = await req.text();
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const mac = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(body));
  const computed = btoa(String.fromCharCode(...new Uint8Array(mac)));
  return computed === sig;
}
```

## Retry and Delivery

| Field | Value |
|-------|-------|
| Direction | Inbound |
| Delivery guarantee | At-least-once (Bling retries on non-2xx) |
| Idempotency key | `id` field in payload combined with event type |
| Response timeout | Respond within 5 seconds; async heavy work |

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `X-Bling-Signature` | header | HMAC signature (if available) |
| Request body | JSON | Bling event payload |

| Output | Description |
|--------|-------------|
| `200 OK` | Accepted |
| `401` | Signature invalid |
| Supabase update | Product/stock row updated |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_BLING_WEBHOOK_SECRET}}` | HMAC secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Target Supabase project |

## Example Handler

```typescript
Deno.serve(async (req) => {
  const body = await req.text();
  const payload = JSON.parse(body);
  const event = payload.event ?? 'unknown';

  switch (event) {
    case 'produto_alterado':
    case 'produto_inserido':
      await supabase.from('products')
        .upsert({ bling_id: payload.id, bling_code: payload.codigo,
                  bling_stock: payload.estoque, bling_synced_at: new Date().toISOString() },
                 { onConflict: 'bling_id' });
      break;
    case 'estoque_alterado':
      await supabase.from('products')
        .update({ bling_stock: payload.estoqueAtual, bling_synced_at: new Date().toISOString() })
        .eq('bling_id', payload.id);
      break;
  }
  return new Response('OK');
});
```

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_api_client_bling.md` | api_client | Outbound calls to Bling |
| `ex_integration_guide_bling.md` | integration_guide | Full setup guide |
| `ex_workflow_inventory_reconcile.md` | workflow | Inventory reconciliation |
