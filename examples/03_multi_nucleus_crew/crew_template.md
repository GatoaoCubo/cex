---
id: ct_research_to_pricing
kind: crew_template
pillar: P12
title: "Research-to-Pricing Sequential Crew"
version: "1.0.0"
quality: 7.9
process: sequential
tags: [crew, research, pricing, multi-nucleus]
related:
  - bld_collaboration_research_pipeline
  - p01_kc_context_scoping
  - model-card-builder
  - p02_card_intelligence
  - crew-template-builder
  - p12_ct_product_launch.md
  - bld_instruction_crew_template
  - p02_nd_n01.md
  - bld_collaboration_model_card
  - bld_collaboration_crew_template
density_score: 1.0
updated: "2026-04-22"
---

# Research-to-Pricing Crew

## Purpose

Three-role sequential crew that takes a domain topic, researches it,
documents the findings, and produces a pricing model.

## Roles

| # | Role | Nucleus | Kind | Goal |
|---|------|---------|------|------|
| 1 | Domain Researcher | N01 | knowledge_card | Research the target domain and produce structured findings |
| 2 | Knowledge Documenter | N04 | knowledge_card | Transform raw research into a polished knowledge card |
| 3 | Pricing Strategist | N06 | content_monetization | Create pricing tiers based on documented knowledge |

## Process

```
sequential:
  step_1: N01 researches domain -> produces research_brief.md
  step_2: N04 reads research_brief.md -> produces kc_domain.md
  step_3: N06 reads kc_domain.md -> produces pricing_model.md
```

## Handoff Protocol

Each role receives the previous role's artifact as context injection (F3 INJECT).
The crew layer augments each role's 8F pipeline with upstream output.

## Quality Gate

All 3 artifacts must score >= 8.0 individually. The crew-level gate
checks cross-reference consistency between the pricing model and the
research findings.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_research_pipeline]] | related | 0.26 |
| [[p01_kc_context_scoping]] | upstream | 0.24 |
| [[model-card-builder]] | upstream | 0.23 |
| [[p02_card_intelligence]] | upstream | 0.22 |
| [[crew-template-builder]] | related | 0.21 |
| [[p12_ct_product_launch.md]] | sibling | 0.21 |
| [[bld_instruction_crew_template]] | upstream | 0.21 |
| [[p02_nd_n01.md]] | upstream | 0.20 |
| [[bld_collaboration_model_card]] | upstream | 0.20 |
| [[bld_collaboration_crew_template]] | related | 0.20 |
