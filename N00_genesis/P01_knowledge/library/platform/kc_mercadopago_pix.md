---
id: kc_mercadopago_pix
kind: knowledge_card
pillar: P01
quality: 9.1
tldr: "Integration patterns for MercadoPago PIX payments — preference creation, IPN webhooks, HMAC-SHA256 verification, and sandbox testing."
tags: ["mercadopago", "PIX", "BRL", "webhook", "IPN", "payments", "Brazil"]
when_to_use: "Apply when integration patterns for mercadopago pix payments — preference creation, ipn webhooks, hmac-sha25..."
keywords: [knowledge-card, brazilian, card, market, pending]
linked_artifacts:
  primary: null
  related: []
density_score: 1.0
related:
  - p04_ex_content_monetization_ecommerce
  - n06_kc_content_monetization
  - kc_hotmart_api
  - p12_dr_content_monetization
  - bld_examples_integration_guide
  - bld_examples_faq_entry
  - bld_knowledge_card_webhook
  - kc_credit_system_design
  - p04_tpl_content_monetization
  - bld_instruction_content_monetization
---

# MercadoPago PIX Integration Patterns

Patterns for integrating MercadoPago as a payment provider with focus on PIX — the instant payment system that dominates the Brazilian market with 40% lower abandonment rates than credit cards.

## 1. PIX vs Card in the Brazilian Market

| Dimension | PIX | Card (Crédito/Débito) |
|-----------|-----|----------------------|
| Settlement | Instant (< 10s) | 1-30 days |
| Fees | 0-0.99% | 2.5-4.5% |
| Chargeback risk | None | Yes |
| Abandonment rate | ~15% | ~55% |
| User friction | QR code scan | Form + 3DS |
| Available 24/7 | Yes (including holidays) | Yes |
| Max per transaction | R$1M (configurable by bank) | Credit limit |

**Rule**: For BRL transactions under R$500, PIX should always be the default payment option. The conversion rate advantage alone justifies the implementation cost.

## 2. Preference Creation (Checkout Pro)

MercadoPago's Checkout Pro model uses "preferences" — server-side payment intents that define what the user is buying.

```python
def create_preference(title: str, unit_price_centavos: int, 
                      payer_email: str, external_ref: str) -> dict:
    """Create MercadoPago preference for PIX/card/boleto."""
    preference_data = {
        "items": [{
            "title": title,
            "quantity": 1,
            "unit_price": unit_price_centavos / 100,  # MP expects float BRL
            "currency_id": "BRL"
        }],
        "payer": {"email": payer_email},
        "external_reference": external_ref,  # Your order ID
        "payment_methods": {
            "excluded_payment_types": [],  # Allow all: PIX, card, boleto
            "installments": 1              # No installments for credits
        },
        "back_urls": {
            "success": "{BASE_URL}/payment/success",
            "failure": "{BASE_URL}/payment/failure",
            "pending": "{BASE_URL}/payment/pending"
        },
        "auto_return": "approved",
        "notification_url": "{BASE_URL}/webhooks/mercadopago"
    }
    return sdk.preference().create(preference_data)
```

**Key**: `external_reference` is your idempotency anchor — it links the MP payment to your internal order/credit pack purchase.

## 3. IPN (Instant Payment Notification) Webhooks

MercadoPago uses IPN — push notifications sent to your `notification_url` when payment status changes.

### Event Flow
```
User pays via PIX
    │
    ▼
MercadoPago processes (< 10s for PIX)
    │
    ▼
IPN POST to notification_url
    │  topic: "payment"
    │  id: payment_id
    ▼
Your server fetches payment details
    │  GET /v1/payments/{payment_id}
    ▼
Status check: "approved" → add_credits()
```

### Critical Statuses
| Status | Action |
|--------|--------|
| `approved` | Add credits, send confirmation email |
| `pending` | Show "waiting for payment" (boleto, PIX timeout) |
| `rejected` | Log reason, show retry option |
| `refunded` | Remove credits, send refund email |
| `cancelled` | No action (user abandoned) |

**Rule**: Always fetch payment details from the API — never trust the IPN payload alone. The IPN only carries `topic` and `id`; you must GET the full payment object to get status, amount, and payer info.

## 4. HMAC-SHA256 Webhook Verification

Verify every IPN request to prevent forged webhooks.

```python
import hmac, hashlib

def verify_mp_webhook(request_id: str, ts: str, body: bytes, 
                      secret: str, received_signature: str) -> bool:
    """Verify MercadoPago webhook HMAC-SHA256 signature."""
    manifest = f"id:{request_id};request-id:{request_id};ts:{ts};"
    computed = hmac.new(
        secret.encode(), manifest.encode(), hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"ts={ts},v1={computed}", received_signature)
```

**Headers to extract**:
- `x-request-id` → request_id
- `x-signature` → `ts=TIMESTAMP,v1=HASH`

**Rule**: Reject any webhook that fails HMAC verification with HTTP 401. Log the attempt for security audit.

## 5. Sandbox Testing

MercadoPago provides a full sandbox environment with test credentials and simulated PIX payments.

### Setup
1. Create sandbox access token at `mercadopago.com.br/developers`
2. Use test user emails: `TESTUSER{N}@testuser.com`
3. Sandbox PIX: payment auto-approves after 5 seconds (no real bank interaction)

### Test Scenarios
| Scenario | How to Trigger |
|----------|----------------|
| Approved payment | Use test credit card `5031 4332 1540 6351` |
| Rejected payment | Use card ending `0004` |
| Pending payment | Use boleto method |
| PIX approved | Create preference, use sandbox PIX QR |
| Webhook delivery | Sandbox sends real IPNs to `notification_url` |

**Rule**: Never use production credentials in CI/staging. Environment variable `MP_ACCESS_TOKEN` must resolve to sandbox token outside production.

## 6. Preapproval (Subscriptions)

For recurring billing (SaaS subscriptions), MercadoPago offers Preapproval:

```python
preapproval = {
    "reason": "Assinatura Pro - {product_name}",
    "auto_recurring": {
        "frequency": 1,
        "frequency_type": "months",
        "transaction_amount": amount_brl,  # Float BRL
        "currency_id": "BRL"
    },
    "payer_email": email,
    "back_url": "{BASE_URL}/subscription/callback",
    "external_reference": subscription_id
}
```

**Limitation**: PIX is NOT available for preapprovals (card only). For PIX-based recurring, implement manual renewal reminders + one-time preferences each billing cycle.

## Regras de Ouro

1. **PIX first for BRL** — always offer PIX as default; 40% lower abandonment.
2. **Never trust IPN payload** — always GET `/v1/payments/{id}` to confirm status and amount.
3. **HMAC-SHA256 on every webhook** — reject unverified requests with 401.
4. **`external_reference` is your anchor** — links MP payment to your internal order ID.
5. **Sandbox in CI** — `MP_ACCESS_TOKEN` must be sandbox token outside production.
6. **Integer internally, float for MP API** — store centavos, convert to BRL float only at the API boundary.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ex_content_monetization_ecommerce]] | downstream | 0.41 |
| [[n06_kc_content_monetization]] | sibling | 0.35 |
| [[kc_hotmart_api]] | sibling | 0.28 |
| [[p12_dr_content_monetization]] | downstream | 0.27 |
| [[bld_examples_integration_guide]] | downstream | 0.25 |
| [[bld_examples_faq_entry]] | downstream | 0.25 |
| [[bld_knowledge_card_webhook]] | sibling | 0.23 |
| [[kc_credit_system_design]] | sibling | 0.23 |
| [[p04_tpl_content_monetization]] | downstream | 0.22 |
| [[bld_instruction_content_monetization]] | downstream | 0.22 |
