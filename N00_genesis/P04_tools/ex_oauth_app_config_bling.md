---
id: ex-oauth-app-config-bling
kind: oauth_app_config
pillar: P04
title: Bling ERP OAuth App Config
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
  - BRAND_DOMAIN
  - BRAND_BLING_AUTH_URL
tags: [commerce, template, distillation, bling, oauth]
density_score: 1.0
---

# Bling ERP OAuth App Config

## Purpose
OAuth 2.0 authorization-code flow for Bling API v3. Obtains a 6-hour access token + 30-day refresh token for the target Bling company account, scoped to the resources we operate on.

## When to use
- First-time connection of a brand's Bling account.
- Scope upgrade (e.g. adding `emissao_nfe`).
- Recovery after refresh-token expiration (>30 days of inactivity).

## Interface
- Authorize URL: `{{BRAND_BLING_AUTH_URL}}` -- e.g. `https://bling.com.br/Api/v3/oauth/authorize`.
- Query params: `response_type=code&client_id={{BRAND_BLING_CLIENT_ID}}&state=<nonce>&redirect_uri=https://{{BRAND_DOMAIN}}/oauth/bling/callback`.
- Token exchange: `POST https://api.bling.com.br/Api/v3/oauth/token` with Basic Auth header `Base64(client_id:client_secret)` and body `grant_type=authorization_code&code=<code>&redirect_uri=<redirect>`.

## Brand variables used
- `{{BRAND_BLING_CLIENT_ID}}` (public), `{{BRAND_BLING_CLIENT_SECRET}}` (secret).
- `{{BRAND_DOMAIN}}` -- drives redirect_uri; must match Bling dev console exactly.
- `{{BRAND_BLING_AUTH_URL}}` -- parameterized in case Bling sandbox vs production is swapped.

## Scopes (minimal + justification)
| Scope | Why |
|-------|-----|
| `98450` produtos (read/write) | catalog push |
| `98451` estoques (read/write) | reconcile |
| `98452` depositos (read) | stock-per-warehouse breakdown |
| `98453` pedidos de venda (read/write) | order mirror |
| `98454` contatos (read/write) | B2B partner mirror (optional) |
| `98455` nfe (write) | fiscal emission (optional, production only) |

## Token lifecycle
- `access_token` lifetime: 6 hours.
- `refresh_token` lifetime: 30 days of no use.
- Token-manager refreshes at 5h55m (leave 5 min safety); see `ex_api_client_token_manager.md`.
- Rotate refresh tokens on every use (Bling issues a new refresh_token in the response).

## Callback handler contract
```ts
// receives ?code=...&state=...
assert(stateMatchesStoredNonce(state), "csrf");
const tokens = await postJson(tokenUrl, { grant_type:"authorization_code", code, redirect_uri });
await tokenManager.put("bling", {
  access_token: tokens.access_token,
  refresh_token: tokens.refresh_token,
  expires_at: Date.now() + tokens.expires_in*1000,
  scope: tokens.scope,
});
return redirect("/admin/integracoes?bling=ok");
```

## Related artifacts
- `ex_api_client_bling.md`
- `ex_webhook_bling.md`
- `ex_integration_guide_bling.md`
- `ex_oauth_app_config_meli.md` -- parallel pattern for ML.
