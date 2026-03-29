---
id: p12_dr_commercial_nucleus
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-06
updated: 2023-10-06
author: dispatch_rule_builder
domain: commercial
quality: null
tags: [dispatch, monetize, apollo]
tldr: Route tasks related to commercial operations and monetization to the apollo satellite
scope: commercial
keywords: [monetizar, monetize, comercial, commercial, receita, revenue, preço, price, funil, funnel]
satellite: apollo
model: sonnet
priority: 8
confidence_threshold: 0.70
fallback: minerva
routing_strategy: keyword_match
---
# Commercial Nucleus Dispatch Rule

## Purpose
Routes tasks related to commercial operations, monetization strategies, and revenue management to the Apollo satellite for processing.

## Keyword Rationale
Keywords ensure task precision by covering both Portuguese and English variants. Including terms like 'monetizar' and 'monetize' as triggers covers financial and commercial intent comprehensively.

## Fallback Logic
When confidence in keyword match falls below threshold, tasks are rerouted to the Minerva satellite, ensuring no commercial task is unprocessed despite temporary unavailability of Apollo.