---
id: tpl_launch_checklist
kind: env_config
pillar: P09
version: 1.0.0
created: 2026-03-31
author: content-monetization-builder
domain: content_monetization
quality: null
tldr: "Launch checklist template — platform setup, checkout, webhooks, compliance for any content business"
tags: [template, checklist, launch, hotmart, digistore24, compliance]
---

# Launch Checklist — Instance Template

> Copy to `_instances/{empresa}/N06_commercial/launch_checklist.md`
> Check items as you complete them. Both BR (Hotmart) and INT (DS24) tracks included.

## Phase 1: Product Setup

### Platform A — Hotmart (BR Market)
- [ ] Hotmart account created and verified (CPF/CNPJ)
- [ ] Product created: name, description, category, price in BRL
- [ ] Checkout page configured: logo, colors, testimonials
- [ ] Hotmart Club member area set up (if course/community)
- [ ] Course modules and lessons uploaded (if applicable)
- [ ] Offer links created (main + coupon variants)
- [ ] Sandbox/test purchase completed successfully
- [ ] Upsell/order bump configured (if applicable)

### Platform B — Digistore24 (International Market)
- [ ] DS24 vendor account created and verified
- [ ] Product created: name, description, price in EUR
- [ ] Sales page URL connected to product
- [ ] Thank-you page / member area URL configured
- [ ] DS24 product set to "test mode" initially
- [ ] Test purchase completed in sandbox
- [ ] Multi-language configured (DE, EN, ES at minimum)
- [ ] Payment methods enabled per region (SEPA/Sofort for DE, iDEAL for NL, cards+PayPal global)

## Phase 2: Webhook & Integration

### Hotmart Webhooks
- [ ] Webhook endpoint deployed: `[URL_WEBHOOK_HOTMART]`
- [ ] Hottok secret stored in environment: `HOTMART_HOTTOK`
- [ ] SHA256 HMAC signature verification implemented
- [ ] Events subscribed: PURCHASE_COMPLETE, PURCHASE_CANCELED, PURCHASE_REFUNDED, PURCHASE_CHARGEBACK, SUBSCRIPTION_CANCELLATION
- [ ] Idempotency key dedup implemented (transaction_id)
- [ ] Test webhook received and processed correctly
- [ ] Error handling: retry logic with exponential backoff

### Digistore24 IPN
- [ ] IPN endpoint deployed: `[URL_WEBHOOK_DS24]`
- [ ] IPN passphrase stored in environment: `DS24_IPN_PASSPHRASE`
- [ ] SHA512 signature verification implemented
- [ ] IPN format: form-encoded parsing (NOT JSON)
- [ ] IPN response: returns exact string "OK" (NOT JSON, NOT HTML)
- [ ] Events handled: on_payment, on_refund, on_chargeback, on_rebill_resumed, on_rebill_cancelled
- [ ] Test IPN sent from DS24 dashboard and processed correctly
- [ ] Error handling: log failures, respond "OK" regardless (DS24 retries otherwise)

## Phase 3: Sales Page & Copy

- [ ] Sales page published at `[URL_SALES_PAGE]`
- [ ] Headline, sub-headline, and value proposition written
- [ ] Social proof: testimonials, case studies, logos
- [ ] CTA buttons linked to correct checkout (Hotmart for BR visitors, DS24 for INT)
- [ ] Geo-detection or language-based routing implemented
- [ ] Mobile-responsive design verified
- [ ] Page load speed < 3 seconds
- [ ] Pricing table with all tiers displayed

## Phase 4: Email Sequences

- [ ] Email provider configured: `[PROVIDER]` with API key in env
- [ ] Onboarding sequence: welcome email (t+0h), value email (t+24h), feature highlight (t+72h)
- [ ] Upsell sequence: triggered after [EVENT], offers next tier
- [ ] Churn prevention: triggered when [CONDITION], retention offer
- [ ] Abandoned cart: triggered 1h after checkout start without completion
- [ ] Double opt-in configured (REQUIRED for EU/DS24 customers)
- [ ] Unsubscribe link in every email (CAN-SPAM + GDPR)
- [ ] From address and reply-to verified in provider

## Phase 5: Affiliate Program

### Hotmart Affiliates
- [ ] Affiliate program created in Hotmart marketplace
- [ ] Commission rate set: `[PERCENTUAL]%`
- [ ] Cookie duration set: `[DIAS]` days
- [ ] Affiliate rules and terms published
- [ ] Promo materials uploaded (banners, email swipes, social posts)
- [ ] Affiliate approval mode: `[auto|manual]`

### Digistore24 Affiliates
- [ ] Affiliate program enabled in DS24 vendor dashboard
- [ ] Commission rate set: `[PERCENTUAL]%`
- [ ] Promo tools page configured with materials
- [ ] Affiliate tracking tested (click → sale → commission)
- [ ] Marketplace listing active (for DS24 affiliate discovery)

## Phase 6: Compliance

### EU Compliance (Required for DS24)
- [ ] GDPR: Data Processing Agreement (DPA) signed with DS24
- [ ] GDPR: Privacy policy published at `[URL_PRIVACY_POLICY]`
- [ ] GDPR: Double opt-in for email collection
- [ ] GDPR: Right to erasure process documented
- [ ] EU VAT: DS24 handles as Merchant of Record (no per-country VAT registration needed)
- [ ] Widerrufsrecht: 14-day cancellation policy published (or digital content waiver with explicit consent)
- [ ] Impressum: published at `[URL_IMPRESSUM]` (required for DACH region sellers)
- [ ] Cookie consent: banner with opt-in before analytics/pixels fire

### BR Compliance (Required for Hotmart)
- [ ] Terms of use published
- [ ] Refund policy aligned with CDC (7-day regret right for digital products)
- [ ] CNPJ or CPF registered in Hotmart
- [ ] Nota fiscal process defined: `[manual|automated|not_applicable]`

## Phase 7: Analytics & Tracking

- [ ] UTM convention defined: `[source]_[medium]_[campaign]_[content]`
- [ ] Meta Pixel installed: `META_PIXEL_ID` in env
- [ ] Google Ads tag installed: `GOOGLE_ADS_TAG` in env
- [ ] Conversion events configured: purchase, lead, add_to_cart
- [ ] Hotmart postback URL configured for ad attribution
- [ ] DS24 tracking parameters configured (ds24_aff, ds24_campaign)
- [ ] Dashboard set up: revenue, CAC, LTV, churn, conversion rates
- [ ] A/B test framework ready for sales page variants

## Phase 8: Go-Live

- [ ] All sandbox/test modes switched to production
- [ ] Hotmart product set to "active"
- [ ] DS24 product set to "live" (not test mode)
- [ ] Webhook endpoints verified with live test purchase
- [ ] Real payment received and processed correctly (both platforms)
- [ ] Refund tested on both platforms
- [ ] Email sequences triggered correctly on live purchase
- [ ] Affiliate tracking confirmed with live transaction
- [ ] Monitoring/alerting active for webhook failures
- [ ] Team notified: launch is live

## Post-Launch Review (Week 1)

- [ ] Revenue matches expected (both platforms)
- [ ] Webhook error rate < 1%
- [ ] Email delivery rate > 95%
- [ ] Checkout completion rate tracked
- [ ] CAC within target range
- [ ] No compliance complaints received
- [ ] Affiliate first sales tracked
- [ ] Pricing review scheduled for `[DATE — 30 days post-launch]`
