---
id: p04_rp_weekly_market_intelligence_brief_output_template
kind: research_pipeline
pillar: P04
title: "Weekly Market Intelligence Brief — Output Template Pipeline"
version: "1.0.0"
created: "2026-04-02"
author: "research-pipeline-builder"
domain: market_intelligence
quality: 9.1
tags: [research-pipeline, STORM, CRAG, CRITIC, market-intelligence, weekly-brief, output-template]
tldr: "7-stage pipeline with 4 standardized output templates for weekly market intelligence briefs — competitive, trend, pricing, and sentiment domains."
density_score: 1.0
---
# Weekly Market Intelligence Brief — Output Template Pipeline

## Pipeline (7 Stages)

| Stage | Name | Model | Input | Output |
|-------|------|-------|-------|--------|
| 1 | INTENT | gemini-2.5-flash | query + week_range | brief_type, scope, routing |
| 2 | PLAN (STORM) | gpt-5-mini | intent + 5 perspectives | 25–35 atomic sub-queries |
| 3 | RETRIEVE (CRAG) | APIs + scraping | sub-queries | scored results (≥0.65) |
| 4 | RESOLVE | deterministic | raw results | deduplicated entities |
| 5 | SCORE | gemini-2.5-flash | entities | Gartner 7-dim ranked list |
| 6 | SYNTHESIZE (GoT) | claude-sonnet | scored data | structured brief sections |
| 7 | VERIFY (CRITIC) | o4-mini | synthesis + sources | verified report (max 3 iter) |

### Stage 2: STORM Perspectives (weekly brief defaults)

| Role | Focus |
|------|-------|
| competitor_analyst | launches, pricing changes, campaign shifts |
| market_researcher | volume trends, segment growth, demand signals |
| consumer_voice | review sentiment, complaints, NPS, forum discussion |
| pricing_strategist | price movements, promo patterns, value-to-price ratio |
| regulatory_monitor | policy changes, compliance updates, standards |

### Stage 3: CRAG Thresholds

| Source Category | Min Score | Fallback |
|----------------|-----------|---------|
| inbound (marketplace) | 0.70 | next marketplace → serper → skip |
| search (web) | 0.60 | next engine → brave → skip |
| outbound (social/review) | 0.50 | volume signal — lower threshold |
| trends | 0.40 | directional only → skip if below |
| rag (internal) | 0.80 | reject if below — high trust required |

## Output Templates

### Template A: Competitive Intelligence Brief
```markdown
# Competitive Brief — {{WEEK}} — {{NICHO}}
**Sources**: {{COUNT}} | **Entities tracked**: {{N}} | **CRAG avg**: {{SCORE}}

## Competitor Moves
| Competitor | Action | Signal Strength | Date | Source |
|-----------|--------|----------------|------|--------|
| {{NAME}} | {{ACTION}} | {{HIGH/MED/LOW}} | {{DATE}} | {{URL}} |

## Pricing Snapshot
| Competitor | SKU | Prev | Curr | Δ% | Promo |
|-----------|-----|------|------|----|-------|
| {{NAME}} | {{SKU}} | {{OLD}} | {{NEW}} | {{%}} | {{Y/N}} |

## Opportunities Detected
- {{OPPORTUNITY_1}}
- {{OPPORTUNITY_2}}

## CRITIC Log
Score: {{SCORE}}/10 | Iterations: {{N}} | Corrections applied: {{COUNT}}
```

### Template B: Market Trend Brief
```markdown
# Market Trend Brief — {{WEEK}} — {{NICHO}}
**Trend horizon**: {{PERIOD}} | **Confidence**: {{HIGH/MED/LOW}}

## Demand Signals
| Segment | Vol WoW | Vol YoY | Sentiment | Source |
|---------|---------|---------|----------|--------|
| {{SEG}} | {{Δ%}} | {{Δ%}} | {{POS/NEG}} | {{SRC}} |

## Emerging Keywords
| Keyword | Volume | Growth | Intent |
|---------|--------|--------|--------|
| {{KW}} | {{VOL}} | {{%}} | {{INTENT}} |

## Seasonal Alerts
- {{ALERT_1}}
- {{ALERT_2}}
```

### Template C: Pricing Intelligence Brief
```markdown
# Pricing Intelligence — {{WEEK}} — {{NICHO}}

## Price Index
| Category | Avg | Min | Max | WoW Δ |
|---------|-----|-----|-----|-------|
| {{CAT}} | {{AVG}} | {{MIN}} | {{MAX}} | {{%}} |

## Anomalies
| SKU | Expected | Actual | Signal |
|----|---------|--------|--------|
| {{SKU}} | {{EXP}} | {{ACT}} | {{SIGNAL}} |
```

### Template D: Consumer Sentiment Brief
```markdown
# Sentiment Brief — {{WEEK}} — {{NICHO}}
**Reviews analyzed**: {{N}} | **Sources**: {{LIST}}

## Sentiment Matrix
| Dimension | Score | WoW Δ | Top Theme |
|-----------|-------|-------|----------|
| Overall | {{/10}} | {{Δ}} | {{THEME}} |
| Delivery | {{/10}} | {{Δ}} | {{THEME}} |
| Quality | {{/10}} | {{Δ}} | {{THEME}} |
| Support | {{/10}} | {{Δ}} | {{THEME}} |

## Top Verbatims
1. "{{QUOTE}}" — {{SOURCE}} ({{COUNT}} mentions)
2. "{{QUOTE}}" — {{SOURCE}} ({{COUNT}} mentions)
```

## Config Reference

```yaml
weekly_brief:
  cadence: weekly
  day: monday
  lookback_days: 7
  brief_types: [competitive, trend, pricing, sentiment]

sources:
  inbound: [mercadolivre, shopee, amazon_br]
  outbound: [reclameaqui, reddit, youtube]
  search: [serper, exa]
  trends: [pytrends, keepa]

storm_perspectives:
  - {role: competitor_analyst, focus: "launches pricing campaigns"}
  - {role: market_researcher, focus: "volume growth segments"}
  - {role: consumer_voice, focus: "sentiment complaints NPS"}
  - {role: pricing_strategist, focus: "price movements promos"}
  - {role: regulatory_monitor, focus: "policy compliance standards"}

multi_model:
  extraction: gemini-2.5-flash
  reasoning: claude-sonnet
  critic: o4-mini

budget:
  serper_daily: 100
  firecrawl_monthly: 3000
  firecrawl_per_brief: 15

quality:
  crag_min_score: 0.65
  critic_max_iterations: 3
  final_min_score: 8.0

output:
  formats: [html, json, md]
  template: consulting
  idioma: "{{idioma}}"
```

## Quality Gates

| Gate | Check | Status |
|------|-------|--------|
| H1 | All 7 stages documented | REQUIRED |
| H2 | Min 2 source categories (inbound + search) | REQUIRED |
| H3 | Min 3 STORM perspectives | REQUIRED |
| H4 | crag_min_score defined (0.0–1.0) | REQUIRED |
| H5 | critic_max_iterations defined (1–5) | REQUIRED |
| H6 | Zero plaintext secrets — ENV_VAR only | REQUIRED |
| H7 | Budget cap: monthly or per-brief | REQUIRED |
| H8 | multi_model: extraction + reasoning + critic | REQUIRED |
| S1 | All 4 brief types covered with template | SOFT |
| S2 | Fallback chain per source category | SOFT |
| S3 | CRITIC log block in each template | SOFT |