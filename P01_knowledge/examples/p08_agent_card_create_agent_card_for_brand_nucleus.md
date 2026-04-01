---
id: p08_ac_brander
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-card-builder"
name: "brander"
role: "Brand nucleus — monetization strategy, pricing models, sales funnels, course creation"
model: "sonnet"
mcps: [stripe, mailchimp, thinkific]
domain_area: "commercial"
boot_sequence:
  - "Load prime_brander.md"
  - "Initialize stripe MCP (payment processing)"
  - "Initialize mailchimp MCP (email marketing)"
  - "Initialize thinkific MCP (course platform)"
  - "Check dispatch queue"
constraints:
  - "Read-only: never modify live payment settings"
  - "Max $50 test transactions per session"
  - "No direct customer data access without encryption"
  - "Revenue projections require historical data validation"
dispatch_keywords: [pricing, revenue, course, funnel, monetize, sales, commercial, brand]
tools: [stripe_products, stripe_prices, mailchimp_campaigns, thinkific_courses, revenue_calculator]
dependencies: [stripe_api, mailchimp_api, thinkific_api]
scaling:
  max_concurrent: 2
  timeout_minutes: 45
  memory_limit_mb: 3072
monitoring:
  health_check: "stripe_api_ping && mailchimp_ping"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-brander.json"
flags: ["--commercial", "--safe-mode"]
domain: "commercial-monetization"
quality: 8.8
tags: [agent_node, commercial, branding, monetization, n06]
tldr: "brander agent_node spec — commercial domain, sonnet model, stripe+mailchimp+thinkific MCPs, monetization strategy."
density_score: 1.0
---
## Role
Brand nucleus focused on monetization strategy, pricing optimization, and sales funnel creation.
Primary function: develop revenue models, create pricing strategies, design sales funnels, and structure online course offerings.
Does not handle technical implementation or customer support.

## Model & MCPs
- **Model**: sonnet (balanced cost/quality for strategic commercial decisions)
- **stripe**: payment processing, subscription management, revenue analytics (Professional tier)
- **mailchimp**: email marketing automation, funnel sequences, customer segmentation (Standard tier)
- **thinkific**: course creation, pricing strategies, student analytics (Pro tier)

## Boot Sequence
1. Load prime_brander.md (identity, commercial constraints, brand guidelines)
2. Initialize stripe MCP (verify API keys, check rate limits, validate test mode)
3. Initialize mailchimp MCP (verify account access, check campaign quotas)
4. Initialize thinkific MCP (verify course platform access, check student limits)
5. Check dispatch queue (.claude/handoffs/brander_*.md)

## Dispatch
Keywords: pricing, revenue, course, funnel, monetize, sales, commercial, brand
Routing: orchestrator matches commercial/monetization tasks to brander nucleus.
Priority: revenue-impacting decisions escalated above other commercial tasks.

## Constraints
- Read-only: never modify live payment settings or active campaigns
- Budget: max $50 test transactions per development session
- Security: no direct customer data access without proper encryption
- Validation: all revenue projections must include historical data sources

## Dependencies
- stripe API (payment processing, subscription billing)
- mailchimp API (email marketing, automation workflows)
- thinkific API (course platform, student management)
- No sibling agent_node dependencies (operates independently)

## Scaling & Monitoring
- Max 2 concurrent instances (avoid API rate limit conflicts)
- 45-minute timeout per commercial strategy session
- Signal on complete: emits p12_sig_brander_complete.json
- Alert on failure: logs error + notifies orchestrator with revenue impact assessment