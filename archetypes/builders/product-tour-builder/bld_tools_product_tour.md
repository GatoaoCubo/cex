---
kind: tools
id: bld_tools_product_tour
pillar: P04
llm_function: CALL
purpose: Tools available for product_tour production
quality: 8.9
title: "Tools Product Tour"
version: "1.0.1"
author: n02_marketing
tags: [product_tour, builder, tools]
tldr: "Tools available for product_tour production"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_interactive_demo
  - bld_tools_onboarding_flow
  - bld_tools_pitch_deck
  - bld_knowledge_card_product_tour
  - product-tour-builder
  - bld_instruction_product_tour
  - bld_tools_rbac_policy
  - bld_tools_api_reference
  - bld_tools_usage_quota
  - bld_tools_playground_config
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles product_tour artifact and validates frontmatter | After draft complete |
| cex_score.py | Scores tour spec against quality gate dimensions | After each draft |
| cex_retriever.py | Fetches comparable tour specs and onboarding KCs | Research phase |
| cex_doctor.py | Validates structural integrity and required step fields | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit gate: ASCII check + frontmatter validation | On git add |
| cex_hygiene.py | Artifact CRUD enforcement: naming, kind, quality=null | Post-generation |

## External References (informational, not CEX tools)
| Resource | Purpose |
|----------|---------|
| Pendo / Appcues / WalkMe | In-app tour patterns: tooltip triggers, spotlight overlays, beacon positioning |
| Intercom Product Tours | Tooltip sequencing and empty-state coaching patterns |
| WCAG 2.1 AA guidelines | Accessibility compliance checklist for tour elements |
| time-to-value (TTV) metric | Onboarding activation benchmark: steps-to-aha-moment measurement |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_interactive_demo]] | sibling | 0.39 |
| [[bld_tools_onboarding_flow]] | sibling | 0.38 |
| [[bld_tools_pitch_deck]] | sibling | 0.36 |
| [[bld_knowledge_card_product_tour]] | upstream | 0.33 |
| [[product-tour-builder]] | downstream | 0.32 |
| [[bld_instruction_product_tour]] | upstream | 0.32 |
| [[bld_tools_rbac_policy]] | sibling | 0.31 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_usage_quota]] | sibling | 0.30 |
| [[bld_tools_playground_config]] | sibling | 0.30 |
