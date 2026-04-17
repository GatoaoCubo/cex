---
id: p12_dr_brand
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: dispatch-rule-builder
domain: brand
quality: 9.0
tags: [dispatch, brand, identity, monetizer, routing, P12]
tldr: Route brand identity, visual design, voice definition, and monetization tasks to monetizer
scope: brand
keywords: [brand, marca, identity, identidade, logo, visual, voice, voz, tone, monetize, monetizar, branding]
agent_group: monetizer
model: sonnet
priority: 8
confidence_threshold: 0.72
fallback: marketer
conditions:
  exclude_domains: [research, code_review, deployment, knowledge_indexing]
load_balance: false
routing_strategy: hybrid
density_score: 0.79
title: "P12 Dispatch Rule Create Dispatch Rule For Brand Routing"
---
# brand Dispatch Rule

## Purpose
Routes brand identity, visual design, voice definition, and monetization strategy tasks to the monetizer agent (N06). Monetizer specializes in brand consistency, visual identity systems, pricing strategy, and commercial positioning — making it the authoritative target for tasks that shape how a brand presents itself to its audience and generates revenue.

## Keyword Rationale
Bilingual PT/EN coverage fires on both Portuguese brand commands (`marca`, `identidade`, `monetizar`, `voz`) and English equivalents (`brand`, `identity`, `monetize`, `voice`). Visual terms (`logo`, `visual`) and voice terms (`tone`, `voz`) cover the full brand development spectrum from identity through implementation. `branding` as root form captures derived variants across language and tense. Keywords are scoped to avoid collision with research (`analise`) and marketing copy (`copy`, `ads`) domains which route to researcher and marketer respectively.

## Fallback Logic
marketer (N02) handles brand-adjacent tasks when monetizer is unavailable, covering brand voice and creative direction without specialized monetization depth. Marketer provides continuity for identity tasks while excluding commercial strategy coverage. Excluded domains (`research`, `code_review`, `deployment`, `knowledge_indexing`) prevent routing collisions with researcher, executor, and knowledge-engine domains that share surface-level vocabulary overlap.

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `dispatch rule`
- **Artifact ID**: `p12_dr_brand`
- **Tags**: [dispatch, brand, identity, monetizer, routing, P12]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `dispatch rule` | Artifact type |
| Pipeline | 8F (F1→F8) |
