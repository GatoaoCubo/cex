---
id: p12_wf_brand_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "workflow-builder"
title: "Complete Brand Pipeline Orchestration"
steps_count: 4
execution: mixed
agent_nodes: [n01, n02, n06, n03]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [brand_research_complete, brand_voice_complete, brand_strategy_complete, brand_assets_complete, workflow_complete]
spawn_configs: [p12_spawn_n01_research, p12_spawn_n02_marketing, p12_spawn_n06_commercial, p12_spawn_n03_builder]
domain: "brand_development"
quality: 8.8
tags: [workflow, brand, pipeline, multi-nucleus, orchestration]
tldr: "4-step brand pipeline: N01 researches market/competitors, N02 develops voice/messaging, N06 creates monetization strategy, N03 builds brand assets"
density_score: 0.92
---
## Purpose
Orchestrates end-to-end brand development from market research through asset creation. N01 conducts competitive analysis and market positioning research, N02 develops brand voice and messaging framework, N06 designs monetization and pricing strategy, and N03 builds comprehensive brand guidelines and assets. Steps 1-3 run in parallel (independent research domains), step 4 synthesizes all outputs into actionable brand system.

## Steps

### Step 1: Market Research & Competitive Analysis [n01]
- **Agent**: n01 (intelligence nucleus)
- **Action**: Research target market, analyze competitors, identify positioning opportunities
- **Input**: brand brief from handoff file, target market parameters
- **Output**: market analysis report with competitor matrix and positioning recommendations
- **Signal**: brand_research_complete with competitive landscape insights
- **Depends on**: none (wave 1)

### Step 2: Brand Voice & Messaging Development [n02]
- **Agent**: n02 (marketing nucleus)
- **Action**: Define brand personality, tone of voice, key messages, and communication framework
- **Input**: brand brief from handoff file, target audience profiles
- **Output**: brand voice guide with messaging hierarchy and communication templates
- **Signal**: brand_voice_complete with voice guidelines
- **Depends on**: none (wave 1)

### Step 3: Monetization Strategy Design [n06]
- **Agent**: n06 (commercial nucleus)
- **Action**: Develop pricing models, revenue streams, and go-to-market strategy
- **Input**: brand brief from handoff file, business model requirements
- **Output**: monetization framework with pricing strategy and revenue projections
- **Signal**: brand_strategy_complete with commercial roadmap
- **Depends on**: none (wave 1)

### Step 4: Brand Asset Creation & Guidelines [n03]
- **Agent**: n03 (builder nucleus)
- **Action**: Synthesize research outputs into comprehensive brand system with visual identity and usage guidelines
- **Input**: outputs from steps 1-3, market analysis, voice guide, monetization framework
- **Output**: complete brand guidelines with logo, colors, typography, templates, and implementation guide
- **Signal**: brand_assets_complete with deliverable brand system
- **Depends on**: Steps 1, 2, 3

## Dependencies
- Brand brief handoff file must exist with target market, business goals, and stakeholder requirements
- spawn_configs for all four nuclei must be validated and accessible
- Access to market research databases and competitive intelligence sources for N01
- Brand asset creation tools and templates available for N03

## Signals
- **On step complete**: {nucleus}_complete signal emitted with quality score and deliverable paths
- **On workflow complete**: workflow_complete signal with aggregated brand system and implementation timeline
- **On error**: {nucleus}_error signal with retry attempt (max 1 per step), escalate to orchestrator if retry fails
- **Wave coordination**: Steps 1-3 emit completion signals independently, Step 4 waits for all three before starting

## References
- Market research methodologies from N01 intelligence protocols
- Brand voice frameworks from N02 marketing templates
- Pricing strategy models from N06 commercial playbooks
- Brand guideline templates from N03 builder archetypes