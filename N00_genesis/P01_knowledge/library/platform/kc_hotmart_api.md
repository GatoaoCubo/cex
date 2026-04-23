---
id: kc_hotmart_api
kind: knowledge_card
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: payment_platform
quality: 9.1
tldr: "Hotmart REST API integration — OAuth2 auth, sales endpoints, webhook sha256 HMAC verification, sandbox testing, and affiliate management."
tags: [hotmart, api, payment, webhook, oauth2, brazil, infoproduct]
density_score: 1.0
when_to_use: "Apply when hotmart rest api integration — oauth2 auth, sales endpoints, webhook sha256 hmac verification, sa..."
keywords: [knowledge-card, core, client, oauth2, endpoints]
linked_artifacts:
  primary: null
  related: []
related:
  - kc_api_reference
  - bld_tools_content_monetization
  - kc_digistore24_api
  - kc_hotmart_club
  - n06_api_access_pricing
  - kc_integration_guide
  - p01_kc_ayrshare_api
  - kc_erp_integration
  - p01_kc_canva_connect_api
  - tpl_launch_checklist
---

# Hotmart REST API Integration Patterns

Hotmart is the dominant infoproduct platform in Brazil and LATAM, serving 500K+ affiliates and millions of digital product transactions. This KC covers the REST API, authentication, webhook handling, and sandbox testing.

## 1. Authentication — OAuth2 Client Credentials

Hotmart uses OAuth2 with client_credentials grant. The token is a Bearer token sent in the Authorization header.

```python
import httpx

def get_hotmart_token(client_id: str, client_secret: str,
                      base: str = "https://developers.hotmart.com") -> str:
    """Obtain OAuth2 Bearer token from Hotmart."""
    resp = httpx.post(
        f"{base}/security/oauth/token",
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    resp.raise_for_status()
    return resp.json()["access_token"]
```

**Token lifecycle**: Tokens expire (typically 5 minutes). Cache and refresh before expiry. Store `HOTMART_CLIENT_ID` and `HOTMART_CLIENT_SECRET` as ENV_VARs — never hardcode.

## 2. Core API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/payments/api/v1/sales/summary` | GET | Aggregated sales data |
| `/payments/api/v1/sales/history` | GET | Paginated sales list |
| `/payments/api/v1/sales/commissions` | GET | Affiliate commissions |
| `/payments/api/v1/subscriptions` | GET | Active subscriptions |
| `/club/api/v1/modules` | GET | Course modules in Hotmart Club |
| `/club/api/v1/modules/{id}/pages` | GET | Lessons within module |
| `/affiliation/api/v1/affiliations` | GET | Affiliate program data |

### Pagination
All list endpoints use `page_token` and `max_results` (max 50). Loop until `page_token` is absent:

```python
def fetch_all_sales(token: str) -> list[dict]:
    """Paginate through all sales."""
    sales, page_token = [], None
    while True:
        params = {"max_results": 50}
        if page_token:
            params["page_token"] = page_token
        resp = httpx.get(
            "https://developers.hotmart.com/payments/api/v1/sales/history",
            params=params,
            headers={"Authorization": f"Bearer {token}"},
        )
        data = resp.json()
        sales.extend(data.get("items", []))
        page_token = data.get("page_info", {}).get("next_page_token")
        if not page_token:
            break
    return sales
```

### Rate Limits
- **60 requests/minute** per endpoint (undocumented but enforced).
- Retry with exponential backoff on HTTP 429.
- Batch operations where possible (e.g., query date ranges instead of individual sales).

## 3. Webhook System

Hotmart sends POST requests to your configured webhook URL when purchase events occur.

### Event Types
| Event | Trigger |
|-------|---------|
| `PURCHASE_COMPLETE` | Payment confirmed (PIX, card, boleto cleared) |
| `PURCHASE_CANCELED` | Buyer canceled before payment |
| `PURCHASE_REFUNDED` | Refund processed (within guarantee period) |
| `PURCHASE_CHARGEBACK` | Card chargeback initiated |
| `PURCHASE_DELAYED` | Boleto generated but not yet paid |
| `PURCHASE_PROTEST` | Buyer disputed via consumer protection |
| `SUBSCRIPTION_CANCELLATION` | Recurring subscription canceled |
| `SWITCH_PLAN` | Subscriber changed plan tier |

### Payload Structure (JSON)
```json
{
  "event": "PURCHASE_COMPLETE",
  "data": {
    "purchase": {
      "transaction": "HP12345678",
      "order_date": 1711900800000,
      "status": "COMPLETE",
      "price": {"value": 99.90, "currency_code": "BRL"},
      "payment": {"type": "PIX"}
    },
    "buyer": {
      "email": "buyer@example.com",
      "name": "Joao Silva"
    },
    "product": {
      "id": 123456,
      "name": "Curso de Python"
    }
  }
}
```

**Note**: `price.value` is a float in the webhook payload (not centavos). Convert to integer centavos immediately: `int(price_value * 100)`.

## 4. SHA256 HMAC Signature Verification

Every webhook carries an `X-Hotmart-Hottok` header with a SHA256 HMAC signature.

```python
import hmac
import hashlib

def verify_hotmart_webhook(body: bytes, hottok: str,
                           received_signature: str) -> bool:
    """Verify Hotmart webhook sha256 HMAC signature."""
    computed = hmac.new(
        hottok.encode("utf-8"),
        body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(computed, received_signature)
```

**Rules**:
- Reject any webhook that fails HMAC with HTTP 401.
- `HOTMART_HOTTOK` is your shared secret — store as ENV_VAR, never log.
- Verify BEFORE parsing the JSON body.

## 5. Idempotency

Use `data.purchase.transaction` as the idempotency key. Hotmart may resend the same event multiple times (network retries). Deduplicate:

```python
async def handle_hotmart_webhook(event: dict) -> bool:
    tx_id = event["data"]["purchase"]["transaction"]
    if await db.exists("hotmart_events", tx_id):
        return True  # Already processed — return 200 OK
    await db.insert("hotmart_events", tx_id, event)
    await process_event(event)
    return True
```

## 6. Sandbox Testing

1. Create a Hotmart developer account at `developers.hotmart.com`.
2. Generate sandbox credentials (client_id + client_secret).
3. Create a test product (free or R$1.00).
4. Configure webhook URL pointing to your staging environment.
5. Use Hotmart's "Test webhook" button to send sample events.
6. Verify: signature validation passes, idempotency dedup works, events are stored.

**Gotcha**: Sandbox webhooks use the same signature format as production. Your `HOTMART_HOTTOK` must match the sandbox product's configured hottok.

## 7. Common Gotchas

| Gotcha | Impact | Fix |
|--------|--------|-----|
| Token expires in ~5 min | 401 errors on API calls | Cache + auto-refresh |
| Webhook price is float | Rounding errors | Convert to centavos immediately |
| Boleto: PURCHASE_DELAYED first | Premature access grant | Only grant on PURCHASE_COMPLETE |
| No webhook retry config | Missed events | Implement polling fallback via sales/history |
| Affiliate commission in separate endpoint | Missing commission data | Query /commissions separately |
| Hotmart Club API is separate base URL | 404 on course endpoints | Use /club/api/v1/ prefix |

## Regras de Ouro

1. **OAuth2 refresh before expiry** — cache token, refresh at 80% of TTL.
2. **HMAC first, parse second** — verify signature before touching payload.
3. **Transaction ID is your anchor** — idempotency key for all webhook events.
4. **Centavos internally** — convert float prices to int immediately at the boundary.
5. **Sandbox in CI** — never use production credentials outside production.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_api_reference]] | sibling | 0.31 |
| [[bld_tools_content_monetization]] | downstream | 0.28 |
| [[kc_digistore24_api]] | sibling | 0.26 |
| [[kc_hotmart_club]] | sibling | 0.25 |
| [[n06_api_access_pricing]] | downstream | 0.25 |
| [[kc_integration_guide]] | sibling | 0.24 |
| [[p01_kc_ayrshare_api]] | sibling | 0.24 |
| [[kc_erp_integration]] | sibling | 0.23 |
| [[p01_kc_canva_connect_api]] | sibling | 0.22 |
| [[tpl_launch_checklist]] | downstream | 0.21 |
