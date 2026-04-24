---
id: p02_nd_n01.md
kind: nucleus_def
8f: F2_become
pillar: P02
nucleus_id: N01
role: intelligence
sin_lens: "Analytical Envy"
cli_binding: claude
model_tier: sonnet
model_specific: claude-sonnet-4-6
context_tokens: 200000
boot_script: boot/n01.ps1
agent_card_path: N01_intelligence/agent_card_n01.md
pillars_owned:
  - P01
crew_templates_exposed:
  - taxonomy_audit
  - competitor_scan
domain_agents:
  - agent_market_analyst
  - agent_paper_reader
fallback_cli: codex
title: "Nucleus Def N01"
version: "1.0.0"
author: n07_crewwiring
domain: "research and competitive intelligence"
quality: 8.9
tags: [nucleus_def, n01, intelligence, composable]
tldr: "N01 is the research nucleus: knowledge_cards, market analysis, papers, benchmarks. Claude Sonnet 200K."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - kc_nucleus_def
  - p02_nd_n04.md
  - p02_nd_n03.md
  - p02_nd_n06.md
  - p02_nd_n02.md
  - p02_nd_n05.md
  - p02_nd_n07.md
  - p12_sc_admin_orchestrator
  - bld_knowledge_card_nucleus_def
  - p12_wf_intelligence_pipeline
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N01 |
| Role | intelligence |
| Sin Lens | Analytical Envy |
| CLI Binding | claude |
| Model Tier | sonnet |
| Model | claude-sonnet-4-6 |
| Context | 200K tokens |
| Boot Script | `boot/n01.ps1` |
| Agent Card | `N01_intelligence/agent_card_n01.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P01 | knowledge | knowledge_card, rag_source, research_pipeline |

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|--------------|--------|---------|
| taxonomy_audit | researcher | repo scan | audit report |
| competitor_scan | market_researcher | product spec | competitive matrix |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_market_analyst | Competitive analysis | `N01_intelligence/P02_model/` |
| agent_paper_reader | Academic paper synthesis | `N01_intelligence/P02_model/` |

## Boot Contract

- Boot file: `boot/n01.ps1`
- Task source: `.cex/runtime/handoffs/n01_task.md`
- Signal: `write_signal('n01', 'complete', {score})`
- Signal path: `.cex/runtime/signals/signal_n01_*.json`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | N02, N04 | positioning briefs, market intel |
| outbound | N06 | competitor pricing data |
| inbound | N07 | research handoffs |
| inbound | N04 | taxonomy gaps to research |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_nucleus_def]] | upstream | 0.51 |
| [[p02_nd_n04.md]] | sibling | 0.51 |
| [[p02_nd_n03.md]] | sibling | 0.50 |
| [[p02_nd_n06.md]] | sibling | 0.49 |
| [[p02_nd_n02.md]] | sibling | 0.48 |
| [[p02_nd_n05.md]] | sibling | 0.41 |
| [[p02_nd_n07.md]] | sibling | 0.38 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.34 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.33 |
| [[p12_wf_intelligence_pipeline]] | downstream | 0.30 |
