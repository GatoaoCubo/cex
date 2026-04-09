---
id: p02_mm_commercial_nucleus
kind: mental_model
pillar: P02
title: "Mental Model — Commercial Nucleus"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: brand_monetization
quality: 9.1
tags: [mental-model, commercial, N06, routing, decision, pricing, funnel]
tldr: "Decision logic for N06 — task routing, commercial reasoning frameworks, tool selection, cost optimization."
density_score: 0.90
---

# Mental Model: Commercial Nucleus

## Decision Tree

```
INTENT RECEIVED
├─ Brand-related?
│  ├─ First-time setup → cex_bootstrap.py (GDP required)
│  ├─ Brand audit → brand_audit.py → scoring report
│  ├─ Brand propagation → brand_propagate.py (atomic)
│  ├─ Brand config → GDP → brand_config_extractor.md prompt
│  └─ Brand book → GDP → brand_book_generator.md prompt
├─ Pricing-related?
│  ├─ New product pricing → AX09 competitor bench first → GDP tiers → output_pricing_page.md
│  ├─ Price optimization → pricing_optimization_memory.md → A/B hypothesis → experiment
│  └─ Revenue model → output_monetization_business_plan.md
├─ Funnel-related?
│  ├─ Landing page → N06 specs → N03 builds → N02 writes copy
│  ├─ Conversion analysis → fetch MCP → competitor pages → gap analysis
│  └─ Retention → churn analysis → pricing_optimization_memory.md update
├─ Content monetization?
│  ├─ Course → Hotmart MCP → content_monetization_tool.md
│  ├─ Subscription → Stripe MCP → pricing model
│  └─ Multi-stream → output_content_factory_business_model.md
└─ Analytics/metrics?
   ├─ Revenue dashboard → metrics template in pricing_optimization_memory.md
   ├─ Brand health → brand_audit.py (6 dimensions)
   └─ Quality gate → scoring_rubric_commercial.md
```

## Routing Rules

| Signal | Route | Tool | GDP? |
|--------|-------|------|------|
| "build brand" / "brand setup" | Full bootstrap pipeline | `cex_bootstrap.py` | Yes |
| "audit brand" / "brand health" | Brand consistency check | `brand_audit.py` | No |
| "price X" / "pricing for" | Value-based pricing flow | GDP → manual | Yes |
| "monetize X" / "revenue model" | Business plan generation | `content_monetization_tool.md` | Yes |
| "competitive analysis" | Competitor research + bench | `fetch` MCP → analysis | No |
| "landing page" / "sales page" | Cross-nucleus dispatch | N06 specs → N03+N02 | Yes |
| "update brand" / "rebrand" | Brand config → propagate | `brand_propagate.py` | Yes |
| "tagline" / "positioning" | Tagline builder | 8F pipeline, kind=tagline | Yes |
| "brand book" / "brand guide" | Full brand book | `brand_book_generator.md` | Yes |
| "funnel" / "conversion" | Funnel design | Manual analysis | Yes |

## Temperature Map

| Activity | Temp | Reason |
|----------|------|--------|
| Brand config extraction | 0.0 | Structured data, no creativity |
| Competitor pricing lookup | 0.0 | Factual retrieval |
| Pricing tier design | 0.3 | Some creativity within constraints |
| Business plan writing | 0.4 | Analytical with light narrative |
| Brand book generation | 0.6 | Creative expression of identity |
| Tagline creation | 0.8 | Maximum creative range |
| Brand naming | 0.9 | Divergent creative exploration |
| Brand audit scoring | 0.0 | Deterministic rubric application |

## Commercial Reasoning Frameworks

### Value-Based Pricing Flow
```
1. Identify customer job-to-be-done
2. Quantify value of solving it ($X/hour saved, $Y/error prevented)
3. Set price at 10-30% of value delivered
4. Validate: would YOU pay this?
5. Benchmark against 2+ competitors (AX09)
6. Build 3 tiers (AX05): anchored by enterprise price
7. Test with small cohort before full launch
```

### Funnel ROI Calculator
```
Traffic × CTR = Visitors
Visitors × Trial Rate = Trials
Trials × Conversion Rate = Customers
Customers × ARPU = Revenue
Revenue - (Traffic × CPC) - (Infra) = Profit

Key ratios:
- CAC = (Traffic × CPC) / Customers
- LTV = ARPU × (1 / Churn Rate)
- ROI = (LTV - CAC) / CAC
```

### Brand Health Score
```
6 Dimensions (from brand_audit.py):
1. Visual Consistency    — logos, colors, typography across touchpoints
2. Voice Consistency     — tone, vocabulary, cadence across content
3. Message Alignment     — tagline ↔ value prop ↔ product reality
4. Audience Fit          — ICP match to actual customers
5. Competitive Position  — clear differentiation from alternatives
6. Revenue Linkage       — brand → conversion pathway exists

Score: 0-10 per dimension, weighted average = Brand Health Index
Threshold: BHI < 7.0 → brand intervention needed
```

## Cross-Nucleus Handoffs

| From | To | What | When |
|------|-----|------|------|
| N06 | N02 | Copy brief + brand voice guide | Sales pages, email sequences |
| N06 | N03 | Landing page specs + pricing schema | Technical implementation |
| N06 | N01 | Research brief for competitor/market analysis | Before pricing decisions |
| N06 | N04 | Brand knowledge cards for system-wide reference | After brand decisions |
| N06 | N05 | Stripe/Hotmart integration specs | Payment implementation |
| N01 | N06 | Market research results | Feeds pricing decisions |
| N02 | N06 | Copy performance data | Feeds conversion analysis |
| N05 | N06 | Revenue/payment data | Feeds metrics dashboard |

## State Variables

| Variable | Type | Purpose |
|----------|------|---------|
| brand_bootstrapped | bool | Is brand config populated? |
| active_products | int | Number of live priced products |
| pricing_experiments_active | int | Running A/B tests |
| brand_health_index | float | Last audit score (0-10) |
| ltv_cac_ratio | float | Current LTV/CAC health |
| memory_entries | int | Items in commercial memory |

## Anti-Patterns

| Anti-Pattern | Why It's Bad | What To Do Instead |
|-------------|-------------|-------------------|
| Cost-plus pricing | Leaves 30-50% on the table | Value-based pricing (AX02) |
| Single price point | Misses market segments | 3+ tiers (AX05) |
| Pricing without research | Arbitrary numbers | Competitor benchmark first (AX09) |
| Brand-then-forget | Brand drifts over time | Quarterly brand_audit.py |
| Vanity metrics | False confidence | Revenue-linked metrics only (AX11) |
| One-time-only model | Linear growth ceiling | Recurring revenue preferred (AX12) |
