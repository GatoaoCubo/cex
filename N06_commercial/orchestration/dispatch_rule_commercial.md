---
id: p12_dr_commercial_nucleus
kind: dispatch_rule
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n06_commercial
domain: commercial-monetization
quality: null
tags: [dispatch, commercial, N06, pricing, funnels, monetization]
tldr: Route tasks related to pricing strategy, online courses, sales funnels, and revenue monetization to N06.
scope: commercial-monetization
keywords: [pricing, precificar, preço, price, curso, course, funil, funnel, monetizar, monetize, receita, revenue, upsell, downsell, checkout, conversão, conversion, LTV, MRR, assinatura, subscription, oferta, offer, venda, sale, lançamento, launch]
agent_node: commercial_hub
model: sonnet
priority: 9
confidence_threshold: 0.65
fallback: builder_hub
routing_strategy: keyword_match
---

# Commercial Nucleus Dispatch Rule

## Purpose

Routes tasks related to pricing strategy, online course monetization, sales funnel design, upsell architecture, and revenue optimization to the `commercial_hub` (N06 Commercial Nucleus).

## Trigger Conditions

Route to N06 when the intent contains ANY of:

### Primary Triggers (high confidence — always route to N06)
| Keyword | Language | Intent |
|---------|----------|--------|
| precificar / pricing | PT/EN | Pricing design task |
| funil de vendas / sales funnel | PT/EN | Funnel construction |
| curso online / online course | PT/EN | Course monetization |
| monetizar / monetize | PT/EN | Revenue generation |
| upsell / order bump / OTO | EN/PT | Upsell architecture |
| checkout otimizado | PT | Conversion optimization |
| modelo de receita / revenue model | PT/EN | Revenue modeling |
| lançamento / product launch | PT/EN | GTM planning |

### Secondary Triggers (route if no other nucleus matches first)
- receita, revenue, conversão, LTV, MRR, assinatura, oferta, venda

## Routing Decision Tree

```
Is the task about pricing, courses, funnels, or monetization?
  YES → Route to N06 (commercial_hub)

Is the task about writing production code for payments?
  YES → Route to N05 (engineering_hub) — NOT N06

Is the task about researching market size or competitors?
  YES → Route to N01 (research_hub) — N06 uses the output

Is the task about writing marketing copy for social media?
  YES → Route to N02 (marketing_hub) — N06 handles the funnel, N02 distributes
```

## Keyword Rationale

Portuguese and English keywords are included because the CEX user base is primarily Brazilian (infoprodutos market). Terms like `monetizar`, `funil`, `precificar` are direct trigger words in PT-BR commercial intent. English terms cover international/hybrid conversations.

## Fallback Logic

If confidence < 0.65:
1. First check N03 Builder (can it be structured as a generic artifact?)
2. If commercial domain confirmed but unclear artifact type: ask user to specify (pricing / course / funnel / upsell)
3. Never silently drop a commercial task

## Non-Routes (explicit exclusions)

| Task | Correct Nucleus |
|------|----------------|
| Deploy payment gateway | N05 Engineering |
| Write Stripe integration code | N05 Engineering |
| Research TAM/SAM/SOM market data | N01 Research |
| Create social media ads | N02 Marketing |
| Index commercial knowledge base | N04 Knowledge |
