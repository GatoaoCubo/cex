---
id: p02_nd_n02.md
kind: nucleus_def
8f: F2_become
pillar: P02
nucleus_id: N02
role: marketing
sin_lens: "Creative Lust"
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
  - content_campaign
  - brand_audit
  - seo_pipeline
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
related:
  - p02_nd_n01.md
  - p02_nd_n06.md
  - kc_nucleus_def
  - p02_nd_n03.md
  - p02_nd_n05.md
  - p02_nd_n04.md
  - p02_nd_n07.md
  - p12_sc_admin_orchestrator
  - bld_knowledge_card_nucleus_def
  - n02_marketing
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N02 |
| Role | marketing |
| Sin Lens | Creative Lust |
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

| Template | Process | Roles | Inputs | Outputs |
|----------|---------|-------|--------|---------|
| product_launch | sequential | 4 (researcher, copywriter, designer, qa) | product spec | launch copy pack + visual assets |
| content_campaign | sequential | 3 (strategist, creator, reviewer) | campaign brief | multi-channel template pack |
| brand_audit | sequential | 3 (scanner, checker, reporter) | brand_config | prioritized audit report |
| seo_pipeline | sequential | 3 (researcher, optimizer, scorer) | content + topic | SEO-optimized content |

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n01.md]] | sibling | 0.52 |
| [[p02_nd_n06.md]] | sibling | 0.50 |
| [[kc_nucleus_def]] | upstream | 0.48 |
| [[p02_nd_n03.md]] | sibling | 0.45 |
| [[p02_nd_n05.md]] | sibling | 0.45 |
| [[p02_nd_n04.md]] | sibling | 0.40 |
| [[p02_nd_n07.md]] | sibling | 0.36 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.33 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.31 |
| [[n02_marketing]] | downstream | 0.28 |
