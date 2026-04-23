---
kind: knowledge_card
id: bld_knowledge_card_content_monetization
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for content monetization — pricing, billing, credits, checkout patterns
sources: Stripe docs, Hotmart API, SaaS pricing literature (ProfitWell, OpenView), CEX production systems
quality: 9.1
title: "Knowledge Card Content Monetization"
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
  - kc_content_platform_comparison
  - bld_instruction_content_monetization
  - n06_kc_content_monetization
  - bld_collaboration_content_monetization
  - bld_tools_content_monetization
  - tpl_launch_checklist
  - bld_examples_content_monetization
  - kc_digistore24_api
  - bld_config_content_monetization
---

# Domain Knowledge: content_monetization

## Executive Summary
Config-driven system that prices, bills, and delivers digital content via tiered
subscriptions, credit packs, or hybrid models. Three pillars: **pricing strategy**,
**credit economics**, and **checkout orchestration**.

## 3 Core Pillars

**Pricing**: freemium | tiered | usage | credit_pack | hybrid. Floor margin >= 30%.
**Credits**: map ops to cost (research=50cr, publish=10cr). Overdraft: block/notify/allow.
**Checkout**: Hotmart (BR) + Digistore24 (INT) + Stripe (global). Webhook-first.

## Platform KC Pointers

### Core Platforms (Tier 1)
| Platform | KC Reference | Key Strength |
|----------|-------------|--------------|
| Hotmart API | kc_hotmart_api | BR leader, REST API, OAuth2, webhook (JSON, sha256) |
| Hotmart Club | kc_hotmart_club | Native member area, course delivery, drip content |
| Hotmart Marketplace | kc_hotmart_marketplace | 500K+ affiliates, BR/LATAM reach |
| Digistore24 API | kc_digistore24_api | EU leader, REST API, Merchant of Record, auto VAT |
| Digistore24 IPN | kc_digistore24_ipn | form-encoded IPN, sha512, respond "OK", 8 event types |
| Digistore24 Marketplace | kc_digistore24_marketplace | EU affiliates, multi-language, per-country payments |

### Compliance & Comparison
| Topic | KC Reference | Key Strength |
|-------|-------------|--------------|
| EU Compliance | kc_content_platform_compliance | GDPR, EU VAT, Widerrufsrecht, Impressum, cookies |
| Platform Comparison | kc_content_platform_comparison | Hotmart vs DS24 vs Teachable vs Kiwify cross-comparison |

### Supporting
Stripe (kc_stripe_patterns), Kiwify, Monetizze, Eduzz, Resend, Meta/Google Ads — pending KCs.

## Multi-Platform Strategy
| Aspect | Hotmart (BR) | Digistore24 (INT) |
|--------|-------------|-------------------|
| Market | BR / LATAM | EU / DACH / Global |
| Currency | BRL | EUR |
| MoR | Seller | DS24 (auto EU VAT) |
| Webhook | JSON, sha256 | form-encoded, sha512 |
| Affiliates | Marketplace 500K+ | DS24 Marketplace |
| Languages | PT-BR | DE,EN,ES,FR,IT,NL,PL |

**Pairing**: Hotmart (BR) + DS24 (INT). T2: +Udemy, +ClickBank.

## Anti-Patterns
| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Float prices (49.90) | Use centavos (4990) |
| No margin tracking | Pipeline costs eat profit |
| Hardcoded provider | No switching flexibility |
| No mock mode | Real charges in dev |
| No webhook idempotency | Double-charge/credit |
| DS24 IPN as JSON | DS24 sends form-encoded |
| DS24 response != "OK" | Retries indefinitely |
| Hotmart-only for INT | Weak INT reach |
| Ignoring EU compliance | GDPR/Widerrufsrecht required |

## Pipeline: PARSE→PRICING→CREDITS→CHECKOUT→COURSES→ADS→EMAILS→VALIDATE→DEPLOY

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_content_monetization]] | downstream | 0.54 |
| [[kc_content_platform_comparison]] | sibling | 0.54 |
| [[bld_instruction_content_monetization]] | downstream | 0.53 |
| [[n06_kc_content_monetization]] | sibling | 0.49 |
| [[bld_collaboration_content_monetization]] | downstream | 0.47 |
| [[bld_tools_content_monetization]] | downstream | 0.44 |
| [[tpl_launch_checklist]] | downstream | 0.42 |
| [[bld_examples_content_monetization]] | downstream | 0.38 |
| [[kc_digistore24_api]] | sibling | 0.37 |
| [[bld_config_content_monetization]] | downstream | 0.36 |
