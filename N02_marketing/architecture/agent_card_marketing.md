---
id: p08_ac_marketingnucleus
kind: agent_card
pillar: P08
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n02_marketing
name: n02-marketing-hub
role: Marketing & Creative Nucleus — conversion copywriter for ads, landing pages, email sequences, brand voice, and social media
model: claude-sonnet-4-6
subscription: anthropic_max
api_cost: zero
mcps: [markitdown, fetch]
domain_area: copywriting_and_campaigns
boot_sequence:
  - load_system_prompt: N02_marketing/prompts/system_prompt_marketing.md
  - inject_knowledge: N02_marketing/knowledge/knowledge_card_marketing.md
  - load_mcp: markitdown (if web research needed)
  - load_mcp: fetch (if competitor page analysis needed)
constraints:
  - NEVER write legal claims without [LEGAL REVIEW NEEDED] marker
  - NEVER self-score quality (quality: null always)
  - NEVER write code (route to N05)
  - NEVER conduct statistical A/B analysis (route to N04)
  - ALWAYS produce A/B variants for headlines and CTAs
dispatch_keywords: [copy, ad, headline, CTA, campaign, landing_page, email, brand, social_media, copywriting, anuncio, campanha]
tools: [markitdown_mcp, fetch_mcp, headline_scorer, readability_analyzer, sentiment_checker]
dependencies: []
scaling:
  max_concurrent: 4
  timeout_minutes: 30
  memory_limit_mb: 2048
monitoring:
  signal_on_complete: true
  alert_on_failure: true
  health_check: python _tools/cex_doctor.py
runtime: claude
cli_command: claude
subscription_auth: anthropic_max
mcp_config: .claude/settings.json
flags: []
domain: copywriting_and_campaigns
quality: 8.9
tags: [agent_card, marketing, N02, copywriting, sonnet]
tldr: N02 deployment spec — claude-sonnet-4-6 on Anthropic Max, zero cost, markitdown + fetch MCPs, specializes in conversion copy.
---

## Role

N02 is the **Marketing & Creative Nucleus** of CEX. It is the persuasion engine:
given a product, audience, and goal, it produces conversion-optimized copy across
all channels — ads, email, landing pages, social media, brand voice, campaign briefs.

## Model & Subscription

| Field | Value |
|-------|-------|
| CLI | `claude` |
| Model | claude-sonnet-4-6 |
| Subscription | Anthropic Max |
| API Cost | Zero (subscription auth) |
| Login | Auto (subscription, no API key needed) |

## MCPs

| MCP | Purpose | Status |
|-----|---------|--------|
| markitdown | Ingest web pages as clean markdown for copy research and teardowns | Future |
| fetch | Pull competitor landing pages and ad copy for analysis | Future |

## Boot Sequence

1. Load `system_prompt_marketing.md` — establishes copywriter identity and 12 rules
2. Inject `knowledge_card_marketing.md` — loads formulas (AIDA, PAS, BAB, 4U, FAB), CTA patterns, funnel matrix
3. Connect MCPs if web research is in the task scope
4. Confirm task funnel stage (awareness / consideration / decision) before writing

## Dispatch

Route tasks to N02 when keywords include:
`copy`, `ad`, `headline`, `CTA`, `landing page`, `email sequence`, `brand voice`,
`social media post`, `campaign brief`, `copywriting`, `anuncio`, `campanha`

Do **NOT** route to N02:
- Statistical A/B test analysis → N04
- Ad platform management (Meta Ads Manager, Google Ads) → N05
- Legal compliance review → human/legal
- Visual design briefs → human/design

## Constraints

- `NEVER` write unverifiable superlatives without `[PROOF NEEDED]` tag
- `NEVER` override brand voice if a voice card is provided
- `ALWAYS` include A/B variants (minimum 3) for headlines and CTAs
- `ALWAYS` signal completion: `write_signal('n02', 'complete', score, mission)`

## Scaling & Monitoring

- Max 4 concurrent N02 instances
- Timeout: 30 minutes per task
- Memory: 2048 MB
- Signal on complete: YES — writes to `.cex/runtime/signals/`
- Health check: `python _tools/cex_doctor.py`
