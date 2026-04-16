---
kind: examples
id: bld_examples_analyst_briefing
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of analyst_briefing artifacts
quality: 9.1
title: "Examples Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, examples]
tldr: "Golden and anti-examples of analyst_briefing artifacts"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
kind: analyst_briefing
analyst_firm: gartner
research_track: magic-quadrant
vendor: Acme DataOps Inc.
briefing_date: 2026-06-15
embargo_flag: false
---

## Company Overview
Acme DataOps Inc. (founded 2019, HQ: Austin TX) provides cloud-native data pipeline orchestration to mid-market and enterprise customers. ARR: $48M. Employees: 312. YoY ARR growth: 67%.

## Market Position
Gartner Magic Quadrant -- Data Integration Tools (2026). Claimed position: Visionary.
Completeness of Vision score: 8.2/10. Ability to Execute: 7.4/10.

## Product Strengths
1. **Real-time CDC latency <50ms** -- P99 latency 42ms across 1,200 production pipelines (internal telemetry Q1 2026).
2. **NPS 72** -- measured across 380 customers (Medallia, Q4 2025); 94% retention rate.
3. **Connector library: 340 native connectors** -- highest in Gartner peer comparison set as of Jan 2026.

## Competitive Landscape
| Vendor | Our Advantage | Their Advantage |
|--------|---------------|-----------------|
| FivetranCo | 40% lower TCO (Forrester TEI 2025) | Larger connector ecosystem (380 vs 340) |
| AlteryxPro | Native ML-pipeline integration; no-code UI | More mature enterprise sales motion |

Win rate vs FivetranCo: 58%. Win rate vs AlteryxPro: 44%.

## Anticipated Analyst Questions
**Q1: How do you differentiate from Fivetran in the mid-market?**
Our CDC latency advantage (42ms vs 180ms P99) translates to a 40% TCO reduction for real-time analytics use cases. Three Fortune 500 customers switched from FivetranCo in H2 2025 (references available under NDA).
```

## Anti-Example 1: Unquantified Claims
```markdown
---
kind: analyst_briefing
analyst_firm: gartner
vendor: GenericSoft Inc.
---
## Product Strengths
1. We have the best performance in the market.
2. Customers love our product.
3. Our roadmap is exciting and innovative.
```
## Why it fails:
No quantified proof points. "Best performance" and "customers love" are unverifiable marketing claims. A Gartner analyst will reject a briefing without numeric evidence. Missing briefing_date, research_track, and competitive landscape.

## Anti-Example 2: Sales Pitch Confusion
```markdown
---
kind: analyst_briefing
vendor: SalesForcePro
---
## Why You Should Buy SalesForcePro
- 50% discount for new customers
- Free trial available
- Award-winning customer success team
```
## Why it fails:
This is a sales pitch, not an analyst briefing. The audience is an industry analyst (Gartner, Forrester, IDC), not a buyer. No framework alignment (no Magic Quadrant axes, no Wave criteria). Missing analyst_firm and research_track fields entirely.
