---
id: p08_ac_commercial_nucleus
kind: agent_card
pillar: P08
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n06_commercial
name: commercial_hub
role: Commercial & Monetization Nucleus — converts expertise into revenue via pricing, courses, and funnels.
model: sonnet
mcps: [hotmart_mcp, stripe_mcp, analytics_mcp]
domain_area: commercial-monetization
boot_sequence:
  - "Load N06_commercial/agents/agent_commercial.md (identity)"
  - "Load N06_commercial/knowledge/knowledge_card_commercial.md (domain KC)"
  - "Load N06_commercial/prompts/system_prompt_commercial.md (rules)"
  - "Initialize hotmart_mcp (course/product sales data)"
  - "Initialize stripe_mcp (subscription and churn analytics)"
  - "Ready for commercial task dispatch"
constraints:
  - "Never write production payment or deployment code — route to N05."
  - "Never execute financial transactions — advisory only."
  - "Never produce a price without a revenue model projection."
  - "Never write generic copy — all output must be audience-specific."
dispatch_keywords: [pricing, curso, funnel, monetizar, receita, conversão, upsell, checkout, oferta, venda, LTV, MRR, assinatura]
tools: [pricing_calculator, funnel_mapper, conversion_tracker, revenue_forecaster]
dependencies: [hotmart_mcp, stripe_mcp, analytics_mcp]
scaling:
  max_concurrent: 3
  timeout_minutes: 30
  memory_limit_mb: 2048
monitoring:
  health_check: "hotmart_mcp.health_check()"
  signal_on_complete: true
  alert_on_failure: true
runtime: claude
subscription: anthropic_max
flags: []
domain: commercial-monetization
quality: null
tags: [agent_card, commercial, N06, sonnet, monetization]
tldr: "commercial_hub: Sonnet model, Anthropic subscription, for pricing/course/funnel monetization tasks."
density_score: 0.88
---

## Role

The `commercial_hub` agent card defines the deployment spec for N06 Commercial Nucleus.
It handles all revenue-facing artifacts: pricing strategies, online course structures, sales funnels, upsell sequences, and conversion audits.

## Model & Subscription

- **Model**: `claude-sonnet` — selected for persuasive copywriting, structured reasoning, and creative commercial strategy
- **Subscription**: Anthropic Max (zero API cost, subscription-based)
- **NOT opus**: commercial tasks require creative fluency > deep reasoning. Sonnet is optimal.

## MCPs

| MCP | Purpose | Status |
|-----|---------|--------|
| hotmart_mcp | Course sales data, affiliate commissions, product performance | planned |
| stripe_mcp | Subscription analytics, churn rate, payment intent data | planned |
| analytics_mcp | Funnel conversion tracking, drop-off analysis | planned |

## Boot Sequence

1. Load `agent_commercial.md` — establish N06 identity and capabilities
2. Load `knowledge_card_commercial.md` — inject pricing frameworks and funnel benchmarks
3. Load `system_prompt_commercial.md` — activate ALWAYS/NEVER rules
4. Initialize MCPs (hotmart, stripe, analytics)
5. Ready for dispatch

## Dispatch

- **Keywords**: pricing, curso, funil, monetizar, receita, conversão, upsell, checkout, oferta, venda, LTV, MRR, assinatura, precificar, lançamento
- **Priority**: 9 (high — commercial intent is high-value, time-sensitive)
- **Fallback**: N03 Builder (for artifact construction) or N01 Research (for market data needs)

## Constraints

- Never handle payment transactions directly — advisory and specification only
- Never produce pricing without a revenue model (units × price × conversion)
- Never write generic copy — all commercial output must name the specific audience and pain
- Never recommend a single flat price — always explore tiered options

## Scaling & Monitoring

- Max 3 concurrent instances (commercial tasks can parallelize: pricing + copy + funnel simultaneously)
- 30-minute timeout for complex multi-artifact commercial builds
- Health check via hotmart_mcp connectivity
- Signal on complete: write to `.cex/runtime/signals/n06_complete.json`
- Alert on failure: write to `.cex/runtime/signals/n06_error.json`
