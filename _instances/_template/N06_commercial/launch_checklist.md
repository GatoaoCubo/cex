---
id: tpl_launch_checklist
kind: env_config
pillar: P09
version: 1.0.0
created: 2026-03-31
author: content-monetization-builder
domain: content_monetization
quality: 9.2
updated: 2026-04-07
tldr: "Launch checklist template — platform setup, checkout, webhooks, compliance for any content business"
tags: [template, checklist, launch, hotmart, digistore24, compliance]
density_score: 1.0
axioms:
  - "NEVER launch without completing all Phase 1 items — platform setup is non-negotiable."
  - "ALWAYS test checkout flow end-to-end before go-live — broken checkout = zero revenue."
linked_artifacts:
  primary: tpl_content_monetization_config
  related: [tpl_pricing_model, p12_wf_content_monetization, p04_fn_content_monetization]
title: "Launch Checklist"
related:
  - kc_content_platform_comparison
  - kc_digistore24_marketplace
  - kc_digistore24_api
  - bld_instruction_content_monetization
  - kc_digistore24_ipn
  - bld_knowledge_card_content_monetization
  - bld_collaboration_content_monetization
  - kc_hotmart_marketplace
  - bld_tools_content_monetization
  - bld_architecture_content_monetization
---

# Launch Checklist — Instance Template

> Copy to `_instances/{empresa}/N06_commercial/launch_checklist.md`
> Check items as you complete them. Both BR (Hotmart) and INT (DS24) tracks included.

## Phase 1: Product Setup

### Platform A — Hotmart (BR Market)
1. [ ] Hotmart account created and verified (CPF/CNPJ)
2. [ ] Product created: name, description, category, price in BRL
3. [ ] Checkout page configured: logo, colors, testimonials
4. [ ] Hotmart Club member area set up (if course/community)
5. [ ] Course modules and lessons uploaded (if applicable)
6. [ ] Offer links created (main + coupon variants)
7. [ ] Sandbox/test purchase completed successfully
8. [ ] Upsell/order bump configured (if applicable)

### Platform B — Digistore24 (International Market)
1. [ ] DS24 vendor account created and verified
2. [ ] Product created: name, description, price in EUR
3. [ ] Sales page URL connected to product
4. [ ] Thank-you page / member area URL configured
5. [ ] DS24 product set to "test mode" initially
6. [ ] Test purchase completed in sandbox
7. [ ] Multi-language configured (DE, EN, ES at minimum)
8. [ ] Payment methods enabled per region (SEPA/Sofort for DE, iDEAL for NL, cards+PayPal global)

## Phase 2: Webhook & Integration

### Hotmart Webhooks
1. [ ] Webhook endpoint deployed: `[URL_WEBHOOK_HOTMART]`
2. [ ] Hottok secret stored in environment: `HOTMART_HOTTOK`
3. [ ] SHA256 HMAC signature verification implemented
4. [ ] Events subscribed: PURCHASE_COMPLETE, PURCHASE_CANCELED, PURCHASE_REFUNDED, PURCHASE_CHARGEBACK, SUBSCRIPTION_CANCELLATION
5. [ ] Idempotency key dedup implemented (transaction_id)
6. [ ] Test webhook received and processed correctly
7. [ ] Error handling: retry logic with exponential backoff

### Digistore24 IPN
1. [ ] IPN endpoint deployed: `[URL_WEBHOOK_DS24]`
2. [ ] IPN passphrase stored in environment: `DS24_IPN_PASSPHRASE`
3. [ ] SHA512 signature verification implemented
4. [ ] IPN format: form-encoded parsing (NOT JSON)
5. [ ] IPN response: returns exact string "OK" (NOT JSON, NOT HTML)
6. [ ] Events handled: on_payment, on_refund, on_chargeback, on_rebill_resumed, on_rebill_cancelled
7. [ ] Test IPN sent from DS24 dashboard and processed correctly
8. [ ] Error handling: log failures, respond "OK" regardless (DS24 retries otherwise)

## Phase 3: Sales Page & Copy

1. [ ] Sales page published at `[URL_SALES_PAGE]`
2. [ ] Headline, sub-headline, and value proposition written
3. [ ] Social proof: testimonials, case studies, logos
4. [ ] CTA buttons linked to correct checkout (Hotmart for BR visitors, DS24 for INT)
5. [ ] Geo-detection or language-based routing implemented
6. [ ] Mobile-responsive design verified
7. [ ] Page load speed < 3 seconds
8. [ ] Pricing table with all tiers displayed

## Phase 4: Email Sequences

1. [ ] Email provider configured: `[PROVIDER]` with API key in env
2. [ ] Onboarding sequence: welcome email (t+0h), value email (t+24h), feature highlight (t+72h)
3. [ ] Upsell sequence: triggered after [EVENT], offers next tier
4. [ ] Churn prevention: triggered when [CONDITION], retention offer
5. [ ] Abandoned cart: triggered 1h after checkout start without completion
6. [ ] Double opt-in configured (REQUIRED for EU/DS24 customers)
7. [ ] Unsubscribe link in every email (CAN-SPAM + GDPR)
8. [ ] From address and reply-to verified in provider

## Phase 5: Affiliate Program

### Hotmart Affiliates
1. [ ] Affiliate program created in Hotmart marketplace
2. [ ] Commission rate set: `[PERCENTUAL]%`
3. [ ] Cookie duration set: `[DIAS]` days
4. [ ] Affiliate rules and terms published
5. [ ] Promo materials uploaded (banners, email swipes, social posts)
6. [ ] Affiliate approval mode: `[auto|manual]`

### Digistore24 Affiliates
1. [ ] Affiliate program enabled in DS24 vendor dashboard
2. [ ] Commission rate set: `[PERCENTUAL]%`
3. [ ] Promo tools page configured with materials
4. [ ] Affiliate tracking tested (click → sale → commission)
5. [ ] Marketplace listing active (for DS24 affiliate discovery)

## Phase 6: Compliance

### EU Compliance (Required for DS24)
1. [ ] GDPR: Data Processing Agreement (DPA) signed with DS24
2. [ ] GDPR: Privacy policy published at `[URL_PRIVACY_POLICY]`
3. [ ] GDPR: Double opt-in for email collection
4. [ ] GDPR: Right to erasure process documented
5. [ ] EU VAT: DS24 handles as Merchant of Record (no per-country VAT registration needed)
6. [ ] Widerrufsrecht: 14-day cancellation policy published (or digital content waiver with explicit consent)
7. [ ] Impressum: published at `[URL_IMPRESSUM]` (required for DACH region sellers)
8. [ ] Cookie consent: banner with opt-in before analytics/pixels fire

### BR Compliance (Required for Hotmart)
1. [ ] Terms of use published
2. [ ] Refund policy aligned with CDC (7-day regret right for digital products)
3. [ ] CNPJ or CPF registered in Hotmart
4. [ ] Nota fiscal process defined: `[manual|automated|not_applicable]`

## Phase 7: Analytics & Tracking

1. [ ] UTM convention defined: `[source]_[medium]_[campaign]_[content]`
2. [ ] Meta Pixel installed: `META_PIXEL_ID` in env
3. [ ] Google Ads tag installed: `GOOGLE_ADS_TAG` in env
4. [ ] Conversion events configured: purchase, lead, add_to_cart
5. [ ] Hotmart postback URL configured for ad attribution
6. [ ] DS24 tracking parameters configured (ds24_aff, ds24_campaign)
7. [ ] Dashboard set up: revenue, CAC, LTV, churn, conversion rates
8. [ ] A/B test framework ready for sales page variants

## Phase 8: Go-Live

1. [ ] All sandbox/test modes switched to production
2. [ ] Hotmart product set to "active"
3. [ ] DS24 product set to "live" (not test mode)
4. [ ] Webhook endpoints verified with live test purchase
5. [ ] Real payment received and processed correctly (both platforms)
6. [ ] Refund tested on both platforms
7. [ ] Email sequences triggered correctly on live purchase
8. [ ] Affiliate tracking confirmed with live transaction
9. [ ] Monitoring/alerting active for webhook failures
10. [ ] Team notified: launch is live

## Post-Launch Review (Week 1)

1. [ ] Revenue matches expected (both platforms)
2. [ ] Webhook error rate < 1%
3. [ ] Email delivery rate > 95%
4. [ ] Checkout completion rate tracked
5. [ ] CAC within target range
6. [ ] No compliance complaints received
7. [ ] Affiliate first sales tracked
8. [ ] Pricing review scheduled for `[DATE — 30 days post-launch]`

## Metadata

```yaml
id: tpl_launch_checklist
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply tpl-launch-checklist.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `env_config` |
| Pillar | P09 |
| Domain | content_monetization |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_content_platform_comparison]] | upstream | 0.41 |
| [[kc_digistore24_marketplace]] | upstream | 0.41 |
| [[kc_digistore24_api]] | upstream | 0.40 |
| [[bld_instruction_content_monetization]] | upstream | 0.40 |
| [[kc_digistore24_ipn]] | upstream | 0.38 |
| [[bld_knowledge_card_content_monetization]] | upstream | 0.38 |
| [[bld_collaboration_content_monetization]] | downstream | 0.36 |
| [[kc_hotmart_marketplace]] | upstream | 0.36 |
| [[bld_tools_content_monetization]] | downstream | 0.35 |
| [[bld_architecture_content_monetization]] | upstream | 0.34 |
