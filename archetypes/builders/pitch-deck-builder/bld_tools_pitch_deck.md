---
kind: tools
id: bld_tools_pitch_deck
pillar: P04
llm_function: CALL
purpose: Tools available for pitch_deck production
quality: 8.9
title: "Tools Pitch Deck"
version: "1.0.1"
author: n02_marketing
tags: [pitch_deck, builder, tools]
tldr: "Tools available for pitch_deck production"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_pitch_deck_builder
  - bld_knowledge_card_pitch_deck
  - bld_tools_product_tour
  - bld_tools_interactive_demo
  - bld_tools_rbac_policy
  - bld_tools_api_reference
  - bld_tools_usage_quota
  - bld_tools_competitive_matrix
  - bld_tools_customer_segment
  - bld_tools_quickstart_guide
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles pitch_deck artifact and validates frontmatter | After draft complete |
| cex_score.py | Scores deck against quality gate dimensions | After each draft |
| cex_retriever.py | Fetches comparable pitch decks and market data KCs | Research phase |
| cex_doctor.py | Validates structural integrity and required slide presence | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit gate: ASCII check + frontmatter validation | On git add |
| cex_hygiene.py | Artifact CRUD enforcement: naming, kind, quality=null | Post-generation |

## External References (informational, not CEX tools)
| Resource | Purpose |
|----------|---------|
| Sequoia pitch deck template | 10-slide structure reference (problem/why now/solution/market/product/biz model/traction/team/financials/ask) |
| Y Combinator application | Traction metrics benchmarks and narrative framing |
| Guy Kawasaki 10/20/30 rule | Slide count, duration, and font-size discipline |
| Crunchbase / PitchBook | Market size and competitive landscape data sources |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_pitch_deck_builder]] | upstream | 0.38 |
| [[bld_knowledge_card_pitch_deck]] | upstream | 0.37 |
| [[bld_tools_product_tour]] | sibling | 0.34 |
| [[bld_tools_interactive_demo]] | sibling | 0.34 |
| [[bld_tools_rbac_policy]] | sibling | 0.32 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_usage_quota]] | sibling | 0.30 |
| [[bld_tools_competitive_matrix]] | sibling | 0.29 |
| [[bld_tools_customer_segment]] | sibling | 0.29 |
| [[bld_tools_quickstart_guide]] | sibling | 0.29 |
