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
