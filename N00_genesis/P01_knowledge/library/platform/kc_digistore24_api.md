---
id: kc_digistore24_api
kind: knowledge_card
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: payment_platform
quality: 9.1
tldr: "Digistore24 REST API — API key auth, product/purchase/affiliate endpoints, Merchant of Record model, EU VAT handling, and sandbox testing."
tags: [digistore24, api, payment, eu, vat, merchant-of-record, dach]
density_score: 1.0
when_to_use: "Apply when digistore24 rest api — api key auth, product/purchase/affiliate endpoints, merchant of record mod..."
keywords: [knowledge-card, core, endpoints, rest, authentication]
linked_artifacts:
  primary: null
  related: []
---

# Digistore24 REST API Integration Patterns

Digistore24 is the leading digital product platform in Europe (especially DACH — Germany, Austria, Switzerland). It operates as a **Merchant of Record** (MoR), meaning DS24 is the legal seller, handles EU VAT collection/remittance, and pays vendors their share. This fundamentally changes the integration model vs. platforms like Stripe or Hotmart.

## 1. Authentication — API Key

DS24 uses a simple API key model. No OAuth2 flow needed.

```python
import httpx

DS24_BASE = "https://www.digistore24.com/api/v1"

def ds24_request(endpoint: str, api_key: str,
                 method: str = "GET", data: dict = None) -> dict:
    """Make authenticated request to DS24 API."""
    headers = {
        "X-DS-API-KEY": api_key,
        "Accept": "application/json",
    }
    if method == "GET":
        resp = httpx.get(f"{DS24_BASE}{endpoint}", headers=headers)
    else:
        resp = httpx.post(f"{DS24_BASE}{endpoint}", headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()
```

**Key management**: Store `DS24_API_KEY` as ENV_VAR. The API key has full vendor access — treat it like a database password. Rotate quarterly.

## 2. Core API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/products` | GET | List all vendor products |
| `/products/{id}` | GET | Single product details |
| `/purchases` | GET | Purchase/transaction history |
| `/purchases/{id}` | GET | Single purchase details |
| `/affiliates` | GET | Affiliate performance data |
| `/transactions` | GET | Financial transactions (payouts, refunds) |
| `/subscriptions` | GET | Active subscriptions (rebilling) |
| `/coupons` | GET/POST | Manage discount coupons |

### Pagination
DS24 API uses `page` and `items_per_page` parameters:

```python
def fetch_all_purchases(api_key: str) -> list[dict]:
    """Paginate through all DS24 purchases."""
    purchases, page = [], 1
    while True:
        resp = ds24_request(
            f"/purchases?page={page}&items_per_page=50",
            api_key,
        )
        items = resp.get("data", [])
        if not items:
            break
        purchases.extend(items)
        page += 1
    return purchases
```

### Rate Limits
- **120 requests/minute** (documented).
- HTTP 429 on exceed — respect `Retry-After` header.
- Batch queries with date range filters to minimize calls.

## 3. Merchant of Record Model

This is the most critical difference from Hotmart/Stripe:

| Aspect | DS24 (MoR) | Hotmart / Stripe (Seller) |
|--------|-----------|--------------------------|
| Legal seller | DS24 | You (the vendor) |
| EU VAT | DS24 collects and remits | You must register + file |
| Invoice to buyer | DS24 issues invoice | You issue invoice |
| Refund liability | DS24 processes | You process |
| Chargeback | DS24 handles initially | You handle |
| Payout | DS24 pays you net of VAT + fees | Platform pays gross minus fees |

**Implication**: You do NOT need EU VAT registration to sell via DS24. DS24 handles all tax compliance. This is a massive advantage for non-EU vendors selling into EU.

### Revenue Flow
```
Buyer pays EUR 99.00
    │
    ▼
DS24 collects (as MoR)
    ├── EU VAT: -EUR 18.81 (19% DE rate)
    ├── DS24 fee: -EUR 7.98 (variable %)
    ├── Affiliate commission: -EUR 24.75 (if applicable)
    └── Vendor payout: EUR 47.46
```

## 4. Product Configuration

### Product Types
| Type | Billing | Use Case |
|------|---------|----------|
| Single purchase | One-time | E-book, course, template |
| Subscription | Recurring (monthly/yearly) | Membership, SaaS, community |
| Installment | Split payment (3-12x) | High-ticket courses |
| Free + shipping | Physical product lead magnet | Book funnel |

### Multi-Language Support
DS24 natively supports 7 languages for checkout pages:
- DE (German), EN (English), ES (Spanish), FR (French)
- IT (Italian), NL (Dutch), PL (Polish)

Auto-detect by buyer's browser language or force via URL parameter `?language=de`.

### Per-Country Payment Methods
| Country/Region | Methods |
|---------------|---------|
| Germany | SEPA Direct Debit, Sofort, cards, PayPal |
| Netherlands | iDEAL, cards, PayPal |
| Austria/Switzerland | SEPA, cards, PayPal |
| France | Carte Bancaire, cards, PayPal |
| Global | Visa, Mastercard, PayPal |

DS24 auto-shows relevant methods based on buyer's country.

## 5. Sandbox / Test Mode

DS24 provides a test mode per product:

1. Set product status to "test mode" in vendor dashboard.
2. Use your real API key — test mode is per-product, not per-key.
3. Test purchases generate real IPN events but no real charges.
4. Test IPN events carry `is_test=1` in the payload.

```python
def is_test_event(ipn_data: dict) -> bool:
    """Check if DS24 IPN event is from test mode."""
    return ipn_data.get("is_test") == "1"
```

**Gotcha**: Unlike Stripe (separate test keys), DS24 uses the same API key for test and production. Test mode is toggled per-product in the dashboard. Always check `is_test` flag in IPN handlers.

## 6. Coupon System

DS24 has a native coupon system:

```python
# Create a coupon via API
coupon_data = {
    "code": "LAUNCH50",
    "discount_type": "percent",  # or "amount"
    "discount_value": 50,        # 50% off
    "max_uses": 100,
    "valid_from": "2026-04-01",
    "valid_until": "2026-04-30",
    "product_ids": [12345],      # Specific products
}
ds24_request("/coupons", api_key, method="POST", data=coupon_data)
```

**PPP via coupons**: Create country-specific coupons (e.g., `BR40` for 40% off) and distribute via geo-targeted landing pages. DS24 doesn't have built-in PPP, but coupons per country achieve the same result.

## 7. Affiliate API

```python
# Fetch affiliate performance
affiliates = ds24_request("/affiliates", api_key)
for aff in affiliates["data"]:
    print(f"{aff['name']}: {aff['total_sales']} sales, "
          f"EUR {aff['total_commission']/100:.2f} commission")
```

| Data Point | Available |
|-----------|-----------|
| Affiliate name/ID | Yes |
| Total sales count | Yes |
| Total commission (cents) | Yes |
| Click-through rate | Yes |
| Conversion rate | Yes |
| Refund rate | Yes |

## 8. Common Gotchas

| Gotcha | Impact | Fix |
|--------|--------|-----|
| MoR means DS24 invoices buyer | Your brand not on invoice | Add brand info in product description |
| Payout is NET of VAT | Revenue appears lower than expected | Calculate net revenue in your projections |
| Same API key for test/prod | Accidental live operations | Always check `is_test` flag |
| EUR cents in API, EUR decimals in dashboard | Confusion on amounts | Standardize to cents internally |
| Affiliate cookie 180 days default | Long attribution window | Good for affiliates, plan accordingly |
| Monthly payouts (not instant) | Cash flow delay | Plan 30-45 day payout cycle |

## Regras de Ouro

1. **MoR = no EU VAT headaches** — DS24 handles all tax compliance.
2. **API key is god-mode** — rotate quarterly, never expose, ENV_VAR only.
3. **Test mode per product** — always set new products to test first.
4. **Net revenue planning** — your payout = gross - VAT - DS24 fee - affiliate commission.
5. **7 languages native** — let DS24 auto-detect language; don't force English on German buyers.
6. **Pair with Hotmart** — DS24 (EU/DACH) + Hotmart (BR/LATAM) = global coverage.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
