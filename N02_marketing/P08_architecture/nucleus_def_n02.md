---
id: p02_nd_n02.md
kind: nucleus_def
pillar: P02
nucleus_id: N02
role: marketing
sin_lens: "Creative Lust (Luxuria Criativa)"
cli_binding: claude
model_tier: sonnet
model_specific: claude-sonnet-4-6
context_tokens: 200000
boot_script: boot/n02.ps1
agent_card_path: N02_marketing/agent_card_n02.md
pillars_owned:
  - P03
crew_templates_exposed:
  - product_launch
  - campaign_sprint
  - brand_refresh
domain_agents:
  - agent_copywriter
  - agent_brand_voice
fallback_cli: codex
title: "Nucleus Def N02"
version: "1.0.0"
author: n07_crewwiring
domain: "marketing copy, campaigns, brand voice"
quality: 8.9
tags: [nucleus_def, n02, marketing, composable]
tldr: "N02 is the marketing nucleus: ad copy, taglines, landing pages, brand voice."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N02 |
| Role | marketing |
| Sin Lens | Creative Lust (Luxuria Criativa) |
| CLI Binding | claude |
| Model Tier | sonnet |
| Model | claude-sonnet-4-6 |
| Context | 200K tokens |
| Boot Script | `boot/n02.ps1` |
| Agent Card | `N02_marketing/agent_card_n02.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P03 | prompt | prompt_template, tagline, chain |

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|--------------|--------|---------|
| product_launch | copywriter | positioning brief | launch copy pack |
| campaign_sprint | creative_lead | campaign brief | ad variants + landing page |
| brand_refresh | brand_voice | audit + examples | brand book update |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_copywriter | Conversion copy | `N02_marketing/P02_model/` |
| agent_brand_voice | Brand consistency | `N02_marketing/P02_model/` |

## Boot Contract

- Boot file: `boot/n02.ps1`
- Task source: `.cex/runtime/handoffs/n02_task.md`
- Signal: `write_signal('n02', 'complete', {score})`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | N05 | landing page assets for deploy |
| outbound | N06 | launch copy for monetization funnels |
| inbound | N01 | positioning briefs |
| inbound | N07 | campaign handoffs |
