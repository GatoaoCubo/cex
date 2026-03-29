---
id: p12_dr_york_commercial
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: dispatch_bot
domain: commercial
quality: null
tags: [dispatch, monetize, york, course]
tldr: Route tasks related to course monetization and pricing within York Commercial Nucleus.
scope: york_commercial
keywords: [monetizar, monetize, preço, price, curso, course, funnel, funil, venda, sell]
satellite: brain
model: sonnet
priority: 8
confidence_threshold: 0.70
fallback: gateway
conditions:
  exclude_domains: [knowledge_management, internal_docs]
load_balance: false
routing_strategy: hybrid
---
# York Commercial Nucleus Dispatch Rule
## Purpose
Routes tasks focused on course monetization, pricing strategies, and sales funnels to the appropriate satellite within the York Commercial Nucleus, ensuring accurate task handling and maximizing monetization potential.

## Keyword Rationale
Bilingual keyword set includes both Portuguese and English variants to capture tasks regardless of the language used. Keywords cover core concepts of monetization, pricing, and courses, important for routing within the commercial context.

## Fallback Logic
Fallback to the gateway node is triggered when confidence in keyword match is low or the primary satellite is unavailable, ensuring no task is left unprocessed and broader general handling is provided.