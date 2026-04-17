---
id: ex_api_client_bling
kind: api_client
pillar: P04
title: Bling ERP API v3 Client
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
tags: [commerce, template, distillation, bling, erp, api_client]
---

## Purpose

HTTP client specification for Bling ERP REST API v3 — covers product CRUD, stock management, and batch sync with OAuth 2.0 bearer token authentication and integrated rate limiting.

## When to Use

- Pushing product data from Supabase to Bling ERP for Brazilian NF-e compliance.
- Pulling current stock quantities from Bling to reconcile against Shopify/Supabase.
- Batch-creating missing Bling products found during catalog audit.

## Base Configuration

| Field | Value |
|-------|-------|
| `base_url` | `https://www.bling.com.br/Api/v3` |
| `auth_strategy` | Bearer token (OAuth 2.0 access token) |
| `auth_header` | `Authorization: Bearer {access_token}` |
| `content_type` | `application/json` |
| `timeout_ms` | `30000` |
| `max_retries` | `3` |
| `backoff` | exponential, base 2s, cap 30s |
| `token_source` | Supabase `bling_tokens` table; auto-refresh if expired |

## Endpoints

| Method | Path | Params | Returns | Error Codes |
|--------|------|--------|---------|-------------|
| GET | `/produtos` | `pagina`, `limite`, `situacao` | `data.produtos[]` | 401, 429 |
| GET | `/produtos/{id}` | — | `data` (product) | 404, 401 |
| POST | `/produtos` | body: product object | `data` (created) | 400, 422 |
| PUT | `/produtos/{id}` | body: partial product | `data` (updated) | 400, 422, 404 |
| GET | `/estoques` | `pagina`, `limite` | `data.estoques[]` | 401 |
| POST | `/estoques` | body: stock entry | `data` | 400, 422 |
| GET | `/oauth/token` | — | (token endpoint, not resources) | 400, 401 |
| POST | `/oauth/token` | body: grant params | `access_token`, `refresh_token` | 400, 401 |

## Rate Limiting

| Limit | Window | Behavior on exceed |
|-------|--------|--------------------|
| 3 req/s | Per account | `429` response |
| ~1000 req/day | Varies by plan | `429` with `Retry-After` |

**Strategy**: enforce 400ms minimum delay between requests; batch operations use `Promise` queue with concurrency 1.

```typescript
const bling = {
  lastCall: 0,
  async fetch(path: string, opts: RequestInit = {}) {
    const wait = Math.max(0, 400 - (Date.now() - this.lastCall));
    if (wait) await new Promise(r => setTimeout(r, wait));
    this.lastCall = Date.now();
    return fetch(`https://www.bling.com.br/Api/v3${path}`, {
      ...opts,
      headers: { Authorization: `Bearer ${await getValidToken()}`, 'Content-Type': 'application/json', ...opts.headers },
    });
  },
};
```

## Pagination

Pattern: **offset-based** via `pagina` (1-based page) and `limite` (max 100).

```
GET /produtos?pagina=1&limite=100
GET /produtos?pagina=2&limite=100
...until data.produtos.length < limite
```

## Error Handling

| HTTP Status | Meaning | Action |
|-------------|---------|--------|
| `200` | Success | Parse `data` field |
| `400` | Validation error | Log `erros[]`; do not retry |
| `401` | Token expired | Refresh token; retry once |
| `404` | Not found | Skip; log for audit |
| `422` | Business rule violation | Log; escalate to human |
| `429` | Rate limited | Back off per `Retry-After` |
| `500` | Bling server error | Exponential retry (max 3) |

## Token Management Pattern

```typescript
async function getValidToken(): Promise<string> {
  const { access_token, expires_at, refresh_token } = await db.getBlingToken();
  if (new Date(expires_at) > new Date(Date.now() + 60_000)) return access_token;
  // Refresh
  const res = await fetch('https://www.bling.com.br/Api/v3/oauth/token', {
    method: 'POST',
    body: new URLSearchParams({ grant_type: 'refresh_token', refresh_token,
      client_id: Deno.env.get('BLING_CLIENT_ID')!, client_secret: Deno.env.get('BLING_CLIENT_SECRET')! }),
  });
  const tokens = await res.json();
  await db.saveBlingToken(tokens);
  return tokens.access_token;
}
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_BLING_CLIENT_ID}}` | OAuth client ID env name |
| `{{BRAND_BLING_CLIENT_SECRET}}` | OAuth client secret env name |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_integration_guide_bling.md` | integration_guide | Full setup guide |
| `ex_webhook_bling.md` | webhook | Inbound stock events |
| `ex_oauth_app_config_bling.md` | oauth_app_config | OAuth flow config |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Orchestrated sync |
