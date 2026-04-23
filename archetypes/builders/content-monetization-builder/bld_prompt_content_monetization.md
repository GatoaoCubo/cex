---
kind: instruction
id: bld_instruction_content_monetization
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for content_monetization artifacts
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Content Monetization"
version: "1.0.0"
author: n03_builder
tags: [content_monetization, builder, examples]
tldr: "Golden and anti-examples for content monetization construction, demonstrating ideal structure and common pitfalls."
domain: "content monetization construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_content_monetization
  - bld_knowledge_card_content_monetization
  - bld_tools_content_monetization
  - bld_collaboration_content_monetization
  - n06_kc_content_monetization
  - tpl_launch_checklist
  - bld_config_content_monetization
  - kc_content_platform_comparison
  - bld_examples_content_monetization
  - content-monetization-builder
---

# Instructions: How to Produce a content_monetization

## Phase 1: RESEARCH
1. Identify the business: niche, country, currency, target audience, content type
2. Audit existing monetization: current pricing, payment provider, course platform
3. Catalog content assets: what can be monetized (tools, reports, courses, data, API access)
4. Map pipeline costs: LLM tokens per operation, API calls, compute — express in credits
5. Research competitors: pricing ranges, tier names, feature bundling in the niche
6. Identify payment providers available in the target market:
   - Global: Stripe (cards + subscriptions + usage billing)
   - BR infoproducts: Hotmart, Kiwify, Monetizze, Eduzz (checkout pages + affiliates)
   - INT infoproducts: Digistore24 (EU leader, Merchant of Record, auto EU VAT)
   - Platform pair strategy: Hotmart (BR/LATAM) + Digistore24 (EU/DACH/INT)
7. For Hotmart: set up OAuth2 bearer token, webhook with sha256 HMAC (X-Hotmart-Hottok)
8. For Digistore24: set up API key (X-DS-API-KEY header), IPN with sha512 verification
   - DS24 IPN: POST form-encoded (NOT JSON), response must be exact string "OK"
   - DS24 sandbox: create test product, test IPN endpoint, verify "OK" response
   - DS24 features: 7 native languages (DE,EN,ES,FR,IT,NL,PL), per-country payment methods
   - DS24 as Merchant of Record: handles EU VAT collection/remittance automatically
9. Define email provider: Resend (dev-friendly), SendGrid (scale), SES (cost), Mailchimp (no-code)
8. Define ad platforms: Meta Ads (B2C), Google Ads (intent), LinkedIn Ads (B2B), TikTok Ads (gen-z)
9. Check existing content_monetization artifacts to avoid config overlap

## Phase 2: COMPOSE
1. Read bld_schema_content_monetization.md — source of truth for config fields
2. Read bld_output_template_content_monetization.md — template structure
3. Fill frontmatter: id, kind, pillar, title, version, quality: null
4. Write PARSE stage: inventory content assets, classify by monetization potential
5. Write PRICING stage: define strategy and tiers
   - Choose strategy: freemium (free + paid), tiered (good/better/best), usage (pay-per-use),
     credit_pack (prepaid bundles), hybrid (tier + overage credits)
   - Define tiers: name, monthly price (centavos/cents), yearly price, credits included, features
   - Set floor_margin_pct >= 0.30 — calculate: (price - pipeline_cost) / price >= 0.30
   - Optional: trial_days (7-30), annual discount (typically 2 months free)
   - Multi-currency: BRL for Hotmart/BR, EUR for DS24/INT, USD for global fallback
   - PPP: consider Purchasing Power Parity — lower pricing tiers for emerging markets
6. Write CREDITS stage: map pipeline operations to credit costs
   - Each operation: name, credit cost, underlying cost (LLM tokens, API, compute)
   - Define packs for pay-as-you-go users: name, credits, price
   - Set overdraft_policy: block (safest), notify_then_block, allow_negative (risky)
7. Write CHECKOUT stage: payment provider integration (multi-platform)
   - Platform A (Hotmart/BR): HOTMART_TOKEN env var, webhook URL, HOTMART_HOTTOK secret
     - Webhook: JSON payload, sha256 HMAC signature, idempotency via transaction_id
     - Events: PURCHASE_COMPLETE, PURCHASE_CANCELED, PURCHASE_REFUNDED, PURCHASE_CHARGEBACK
   - Platform B (Digistore24/INT): DS24_API_KEY env var, IPN URL, DS24_IPN_PASSPHRASE
     - IPN: form-encoded payload (NOT JSON), sha512 signature verification
     - Response: body must be exact string "OK" — DS24 retries until "OK" received
     - Events: on_payment, on_refund, on_chargeback, on_rebill_resumed, on_rebill_cancelled
   - Both platforms: idempotency_key dedup, success/cancel redirects, mock mode true by default
8. Write COURSES stage (if applicable):
   - Module structure: title, lessons (title + type + duration), drip_days
   - Certification: completion_threshold (default 0.80), certificate template
   - Content types: video, text, quiz, assignment, live session
9. Write ADS stage (if applicable):
   - Platform selection: Meta (B2C awareness), Google (intent capture), LinkedIn (B2B)
   - Budget allocation: monthly budget in centavos, target CPA
   - Tracking: pixel/tag env vars, conversion events
10. Write EMAILS stage (if applicable):
    - Sequences: onboarding (post-signup), upsell (after trial), churn prevention (pre-cancel)
    - Triggers: behavioral (used feature X), time-based (day 3), threshold (credits < 10%)
    - Provider config: API key env var, from address, reply-to
11. Write VALIDATE stage: pre-launch checks
    - Margin validation: every tier must pass floor_margin_pct
    - Webhook test: send test event, verify idempotent handling
    - Mock checkout: complete full flow with test credentials
12. Write DEPLOY stage: mock→production cutover checklist

## Phase 3: VALIDATE
1. Check all 9 pipeline stages documented with inputs/outputs
2. Verify pricing: all amounts in centavos/cents (integers, not floats)
3. Verify margins: floor_margin_pct >= 0.30 for every tier
4. Verify no API keys/secrets in plaintext — only ENV_VAR references
5. Verify webhook idempotency is configured (idempotency_key + dedup)
6. Verify mock_mode defaults to true
7. Verify credit costs cover all pipeline operations (no untracked ops)
8. Verify overdraft_policy is explicitly set (no implicit behavior)
9. Check body <= 4096 bytes per file (6144 for instruction)


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_content_monetization]] | downstream | 0.51 |
| [[bld_knowledge_card_content_monetization]] | upstream | 0.49 |
| [[bld_tools_content_monetization]] | downstream | 0.43 |
| [[bld_collaboration_content_monetization]] | downstream | 0.40 |
| [[n06_kc_content_monetization]] | upstream | 0.39 |
| [[tpl_launch_checklist]] | downstream | 0.37 |
| [[bld_config_content_monetization]] | downstream | 0.37 |
| [[kc_content_platform_comparison]] | upstream | 0.35 |
| [[bld_examples_content_monetization]] | downstream | 0.33 |
| [[content-monetization-builder]] | downstream | 0.33 |
