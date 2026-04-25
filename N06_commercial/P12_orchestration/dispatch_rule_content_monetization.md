---
id: p12_dr_content_monetization
title: "Dispatch Rule Content Monetization"
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
domain: content-monetization
quality: 9.2
updated: 2026-04-07
tags: [dispatch_rule, content-monetization, billing, checkout, credits, PIX, N06]
tldr: Routes billing, checkout, credit, course generation, and payment tasks to content-monetization-builder via N06.
axioms:
  - "ALWAYS validate payment provider credentials before routing checkout tasks."
  - "NEVER route monetization tasks without brand_config.yaml loaded — pricing inherits brand positioning."
linked_artifacts:
  primary: p12_wf_content_monetization
  related: [p04_fn_content_monetization, p12_dr_commercial, p01_kc_brand_monetization_models]
scope: content-monetization
keywords: [monetize, billing, checkout, payment, PIX, boleto, credits, wallet, balance, course, subscription, plan, pricing, invoice, charge, revenue, MercadoPago, Stripe, Hotmart, Digistore24, DS24, Kiwify, Monetizze, Eduzz, course-generation, ads-checkout, transactional-email, ERP-sync, BaseLinker, credit-pack, IPN, webhook, affiliate, EU-VAT, GDPR, Widerrufsrecht, credit-wallet, idempotency, payment-provider]
agent_group: content_monetization_builder
model: sonnet
priority: 9
confidence_threshold: 0.65
fallback: commercial_hub
routing_strategy: keyword_match
related:
  - n06_integration_content_factory
  - content-monetization-builder
  - n06_kc_content_monetization
  - bld_collaboration_content_monetization
  - p03_sp_content_monetization_builder
  - p12_wf_content_monetization
  - p01_kc_content_monetization
  - p04_fn_content_monetization
  - p12_dr_content_factory
  - bld_collaboration_subscription_tier
---

# Content Monetization Dispatch Rule

## Purpose

Routes tasks related to billing execution, credit wallet management, checkout session setup, course content generation, ad monetization, transactional email dispatch, and ERP synchronization to `content_monetization_builder` (N06 Commercial Nucleus).

## Trigger Conditions

Route to `content_monetization_builder` when intent contains ANY of:

### Primary Triggers (confidence >= 0.85 — immediate route)

| Keyword | Language | Intent |
|---------|----------|--------|
| monetizar / monetize | PT/EN | Content monetization task |
| billing / faturamento | PT/EN | Billing execution |
| checkout / pagamento | PT/EN | Payment session creation |
| PIX / boleto | PT | Brazilian payment methods |
| créditos / credits | PT/EN | Credit wallet operation |
| credit pack / pack de créditos | PT/EN | Credit pack purchase |
| geração de curso / course generation | PT/EN | LLM course content pipeline |
| assinatura / subscription | PT/EN | Recurring billing setup |
| plano de cobrança / billing plan | PT/EN | Pricing tier config |

### Secondary Triggers (route if no higher-priority nucleus matches)

- invoice, cobrança, charge, receita, revenue, wallet, saldo
- MercadoPago, Stripe, Hotmart, Digistore24, DS24, Kiwify, Monetizze, Eduzz
- BaseLinker, Bling, ERP sync
- email transacional, transactional email, email sequence
- anúncio monetizado, ads checkout, ad billing
- PIPELINE_COSTS, PARSE, PRICING, CREDITS
- IPN, webhook, affiliate, afiliado, EU VAT, GDPR, Widerrufsrecht, Impressum

## Routing Decision Tree

```
Does intent involve payment, billing, or checkout?
  YES → content_monetization_builder (N06)

Does intent involve credit wallet or pack purchase?
  YES → content_monetization_builder (N06)

Does intent involve LLM course generation (outline→module→sales_page→emails)?
  YES → content_monetization_builder (N06)

Does intent involve ad content validation with billing gate?
  YES → content_monetization_builder (N06)

Does intent involve ERP sync (BaseLinker/Bling) for paid orders?
  YES → content_monetization_builder (N06)

Does intent involve writing production payment code?
  NO → Route to N05 (engineering_hub) — implementation, not config

Does intent involve general pricing strategy without billing execution?
  NO → Route to commercial_hub (N06 general) — strategy only
```

## Keyword Rationale

PT-BR terms are primary because codexa-core targets Brazilian market (MercadoPago, PIX, boleto). English terms cover SaaS integrations (Stripe, USD billing). Technical terms (PIPELINE_COSTS, BillingExecutor, idempotency_key) route direct integration queries. Both language sets are required for hybrid PT/EN codebases.

## Priority Tiers

| Priority | Keywords | Action |
|----------|----------|--------|
| 10 (critical) | PIX aprovado, webhook payment.approved, checkout.session.completed | Immediate route — live payment event |
| 9 (high) | monetizar, billing, checkout, créditos, assinatura | Standard route to builder |
| 7 (medium) | curso, email sequence, ad validation | Route after checking N02/N05 first |
| 0 (fallback) | * (any unmatched) | Escalate to commercial_hub |

## Fallback Logic

If confidence < 0.65:
1. Check commercial_hub (N06 general) — generic monetization?
2. Check N05 (engineering) — payment code implementation?
3. If still ambiguous: request clarification: "billing execution, course generation, credit config, or checkout setup?"
4. Never silently drop a content monetization task

## Non-Routes (Explicit Exclusions)

| Task | Correct Target |
|------|---------------|
| Write Stripe/MP Python code | N05 engineering_hub |
| Design pricing strategy (no execution) | commercial_hub (N06 general) |
| Research competitor payment models | N01 research_hub |
| Write marketing copy for course | N02 marketing_hub |
| Build RAG knowledge base for billing docs | N04 knowledge_hub |
| Deploy payment microservice to prod | N05 engineering_hub |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_integration_content_factory]] | upstream | 0.35 |
| [[content-monetization-builder]] | upstream | 0.33 |
| [[n06_kc_content_monetization]] | upstream | 0.33 |
| [[bld_collaboration_content_monetization]] | related | 0.32 |
| [[p03_sp_content_monetization_builder]] | upstream | 0.32 |
| [[p12_wf_content_monetization]] | related | 0.31 |
| [[p01_kc_content_monetization]] | upstream | 0.30 |
| [[p04_fn_content_monetization]] | upstream | 0.30 |
| [[p12_dr_content_factory]] | sibling | 0.27 |
| [[bld_collaboration_subscription_tier]] | related | 0.26 |
