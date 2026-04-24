---
id: ex-oauth-app-config-meli
kind: oauth_app_config
8f: F1_constrain
pillar: P04
title: Mercado Livre OAuth App Config
version: 0.1.0
quality: 8.8
status: template
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
  - BRAND_MELI_CLIENT_SECRET
  - BRAND_DOMAIN
  - BRAND_MELI_AUTH_URL
tags: [commerce, template, distillation, mercado_livre, oauth]
density_score: 1.0
related:
  - bld_output_template_oauth_app_config
  - bld_knowledge_card_oauth_app_config
  - kc_oauth_app_config
  - oauth-app-config-builder
  - p09_qg_oauth_app_config
  - bld_examples_oauth_app_config
  - p03_sp_oauth_app_config_builder
  - p01_kc_canva_connect_api
  - bld_instruction_oauth_app_config
  - bld_schema_oauth_app_config
---

# Mercado Livre OAuth App Config

## Purpose
OAuth 2.0 authorization-code flow for Mercado Livre. Obtains a 6-hour `access_token` + long-lived `refresh_token` (rotating) bound to one seller account.

## When to use
- First connect of a brand's ML seller account.
- Adding a new ML site (MLB/MLA/MLM) to a multi-country seller.
- Recovery after refresh-token rotation failure.

## Interface
- Authorize URL: `{{BRAND_MELI_AUTH_URL}}` -- `https://auth.mercadolivre.com.br/authorization` (MLB) or regional equivalent.
- Query params: `response_type=code&client_id={{BRAND_MELI_CLIENT_ID}}&redirect_uri=https://{{BRAND_DOMAIN}}/oauth/meli/callback&state=<nonce>`.
- Token exchange: `POST https://api.mercadolibre.com/oauth/token` with body `grant_type=authorization_code&client_id=...&client_secret=...&code=...&redirect_uri=...`.

## Brand variables used
- `{{BRAND_MELI_CLIENT_ID}}` (public), `{{BRAND_MELI_CLIENT_SECRET}}` (secret).
- `{{BRAND_DOMAIN}}` -- drives redirect_uri; MUST be the EXACT URL whitelisted in the ML dev console.
- `{{BRAND_MELI_AUTH_URL}}` -- regional; Brazil = mercadolivre.com.br, Mexico = mercadolibre.com.mx, etc.

## Scopes
ML uses topic-based permissions on the app, not OAuth scope strings. Configure in dev console:
- `read` (always on once approved).
- `write` (required for stock + order updates).
- `offline_access` (required to receive refresh_token).

## Refresh-token rotation (CRITICAL)
Every refresh call returns a NEW refresh_token; the old one is dead within minutes. Consequences:
- Token-manager MUST serialize refresh (mutex per brand); concurrent refreshes crash both.
- Persist `new_refresh_token` atomically with `new_access_token` + `expires_at` in one DB row.
- If persistence fails after API call succeeds, you lose the account -- wrap in DB transaction OR write-ahead log.

## Callback handler contract
```ts
// /oauth/meli/callback
const { code, state } = parseQuery(url);
assert(stateValid(state), "csrf");
const tokens = await postForm(tokenUrl, {
  grant_type: "authorization_code",
  client_id: Deno.env.get("{{BRAND_MELI_CLIENT_ID}}"),
  client_secret: Deno.env.get("{{BRAND_MELI_CLIENT_SECRET}}"),
  code,
  redirect_uri: `https://{{BRAND_DOMAIN}}/oauth/meli/callback`,
});
await db.tx(async t => {
  await t.upsert("meli_tokens", { user_id: tokens.user_id, ...tokens, expires_at: now()+tokens.expires_in*1000 });
});
return redirect("/admin/integracoes?meli=ok");
```

## Related artifacts
- `ex_api_client_meli.md`
- `ex_integration_guide_meli.md`
- `ex_oauth_app_config_bling.md` (parallel pattern, different rotation semantics)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_oauth_app_config]] | downstream | 0.39 |
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.35 |
| [[kc_oauth_app_config]] | upstream | 0.32 |
| [[oauth-app-config-builder]] | downstream | 0.27 |
| [[p09_qg_oauth_app_config]] | downstream | 0.27 |
| [[bld_examples_oauth_app_config]] | downstream | 0.25 |
| [[p03_sp_oauth_app_config_builder]] | upstream | 0.24 |
| [[p01_kc_canva_connect_api]] | upstream | 0.24 |
| [[bld_instruction_oauth_app_config]] | upstream | 0.23 |
| [[bld_schema_oauth_app_config]] | downstream | 0.22 |
