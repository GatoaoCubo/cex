---
id: p02_nd_n06.md
kind: nucleus_def
pillar: P02
nucleus_id: N06
role: commercial
sin_lens: "Strategic Greed"
cli_binding: claude
model_tier: sonnet
model_specific: claude-sonnet-4-6
context_tokens: 200000
boot_script: boot/n06.ps1
agent_card_path: N06_commercial/agent_card_n06.md
pillars_owned:
  - P11
crew_templates_exposed:
  - sales_pipeline
  - pricing_workshop
  - subscription_design
  - partnership_kit
domain_agents:
  - agent_pricing_strategist
  - agent_funnel_optimizer
fallback_cli: codex
title: "Nucleus Def N06"
version: "1.0.0"
author: n07_crewwiring
domain: "pricing, courses, funnels, monetization"
quality: 8.9
tags: [nucleus_def, n06, commercial, composable]
tldr: "N06 is the commercial nucleus: pricing, courses, funnels, CLV. Also owns team_charter (P12 GOVERN)."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - p02_nd_n01.md
  - p02_nd_n02.md
  - kc_nucleus_def
  - p02_nd_n03.md
  - p02_nd_n05.md
  - p02_nd_n04.md
  - p02_nd_n07.md
  - p12_sc_admin_orchestrator
  - bld_knowledge_card_nucleus_def
  - n06_commercial
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N06 |
| Role | commercial |
| Sin Lens | Strategic Greed |
| CLI Binding | claude |
| Model Tier | sonnet |
| Model | claude-sonnet-4-6 |
| Context | 200K tokens |
| Boot Script | `boot/n06.ps1` |
| Agent Card | `N06_commercial/agent_card_n06.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P11 (shared) | feedback | content_monetization |
| P12 (shared) | orchestration | team_charter |

## Crew Templates Exposed

| Template | Roles | Inputs | Outputs |
|----------|-------|--------|---------|
| sales_pipeline | strategist -> content_producer -> closer | team_charter + brand | strategy brief + collateral + closing playbook |
| pricing_workshop | market_analyst -> pricing_architect -> revenue_validator | team_charter + product spec | competitive matrix + tier model + revenue projections |
| subscription_design | segment_researcher -> tier_architect -> retention_analyst | team_charter + customer data | segment profiles + tier model + churn prevention playbook |
| partnership_kit | partner_researcher -> proposal_writer -> deal_reviewer | team_charter + competitive intel | ecosystem map + partner listing + deal governance |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_pricing_strategist | Tier + bundle design | `N06_commercial/P02_model/` |
| agent_funnel_optimizer | Conversion funnel | `N06_commercial/P02_model/` |

## Boot Contract

- Boot file: `boot/n06.ps1`
- Task source: `.cex/runtime/handoffs/n06_task.md`
- Signal: `write_signal('n06', 'complete', {score})`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | N02 | pricing data for copy |
| outbound | N07 | charter gate outcomes |
| inbound | N01 | competitor pricing |
| inbound | N02 | launch copy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n01.md]] | sibling | 0.54 |
| [[p02_nd_n02.md]] | sibling | 0.52 |
| [[kc_nucleus_def]] | upstream | 0.49 |
| [[p02_nd_n03.md]] | sibling | 0.46 |
| [[p02_nd_n05.md]] | sibling | 0.41 |
| [[p02_nd_n04.md]] | sibling | 0.40 |
| [[p02_nd_n07.md]] | sibling | 0.39 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.34 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.31 |
| [[n06_commercial]] | downstream | 0.30 |
