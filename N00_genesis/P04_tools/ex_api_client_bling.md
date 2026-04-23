---
id: ex-api-client-bling
kind: api_client
pillar: P04
title: Bling ERP API v3 Client
version: 0.1.0
quality: 9.0
status: template
brand_placeholders:
  - BRAND_BLING_API_URL
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
  - BRAND_BLING_ACCESS_TOKEN
tags: [commerce, template, distillation, bling, api_client]
density_score: 1.0
related:
  - kc_erp_integration
  - bld_knowledge_card_oauth_app_config
  - bld_knowledge_card_client
  - oauth-app-config-builder
  - p01_kc_bling_erp_field_parametrization
  - bld_knowledge_card_thinking_config
  - p01_kc_bling_erp_automation_boundary
  - kc_oauth_app_config
  - p11_qg_client
  - kc_api_reference
---

# Bling ERP API v3 Client

## Purpose
Typed client for Bling ERP (Brazilian fiscal + inventory system) v3. Wraps OAuth2 token refresh, rate-limited endpoints, and domain models (produtos, estoques, pedidos, depositos).

## When to use
- Push Supabase products into Bling as `produtos` for fiscal registration.
- Pull current stock (`estoques`) from Bling to reconcile with Shopify.
- Create/update notas fiscais (NF-e) tied to orders (requires emit permission in Bling).

## Interface
- Base URL: `{{BRAND_BLING_API_URL}}` (default `https://api.bling.com.br/Api/v3`).
- Auth: `Authorization: Bearer <access_token>` -- token rotates every 6h, refresh transparently.
- Rate limit: 3 req/sec, 120000 req/day. Client MUST enforce via token-bucket locally.

## Brand variables used
- `{{BRAND_BLING_API_URL}}` -- pinned base URL.
- `{{BRAND_BLING_CLIENT_ID}}`, `{{BRAND_BLING_CLIENT_SECRET}}` -- OAuth app credentials.
- `{{BRAND_BLING_ACCESS_TOKEN}}` -- env var name of the current token; token-manager rewrites this secret.

## Token refresh contract
- Check `expires_at` stored alongside token; refresh if <5 min remaining.
- Refresh endpoint: `POST /oauth/token` with `grant_type=refresh_token`.
- On 401 from any API call, force-refresh ONCE and retry; on second 401 fail loud (likely revoked).
- Persist new token via `ex_api_client_token_manager.md` -- never write directly to env.

## Example usage
```ts
const bling = createBlingClient({
  baseUrl: "{{BRAND_BLING_API_URL}}",
  getToken: () => tokenManager.get("bling"),
});
const { data } = await bling.request("GET", "/produtos", { limit: 100, pagina: 1 });
for (const p of data) await db.upsertBlingProduct(p);
```

## Error taxonomy
| HTTP | Meaning | Client action |
|------|---------|---------------|
| 200/201 | success | parse body |
| 400 | validation | surface field errors, no retry |
| 401 | token expired | refresh + retry once |
| 403 | scope missing | fail loud, operator must re-OAuth with new scope |
| 404 | entity not found | return `null`, not throw, for get-by-id ops |
| 422 | invalid payload | surface detail; often fiscal rule (e.g. missing NCM) |
| 429 | rate limited | sleep `X-RateLimit-Reset` seconds |
| 5xx | transient | exponential retry 3x |

## Data-model quirks (Bling v3)
- Products keyed by `id` (Bling internal) AND `codigo` (our SKU). Always store both.
- Stock is per-warehouse (`deposito`); the "current stock" requires summing across the default warehouse set defined per brand.
- `Produto.situacao` = `A` (ativo) / `I` (inativo). Deleted products stay in API with `I` forever.

## Related artifacts
- `ex_webhook_bling.md`
- `ex_oauth_app_config_bling.md`
- `ex_integration_guide_bling.md`
- `ex_api_client_token_manager.md` (referenced, not in this wave)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_erp_integration]] | upstream | 0.35 |
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.29 |
| [[bld_knowledge_card_client]] | upstream | 0.27 |
| [[oauth-app-config-builder]] | downstream | 0.26 |
| [[p01_kc_bling_erp_field_parametrization]] | upstream | 0.26 |
| [[bld_knowledge_card_thinking_config]] | upstream | 0.24 |
| [[p01_kc_bling_erp_automation_boundary]] | upstream | 0.24 |
| [[kc_oauth_app_config]] | upstream | 0.24 |
| [[p11_qg_client]] | downstream | 0.24 |
| [[kc_api_reference]] | upstream | 0.23 |
