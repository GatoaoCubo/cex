---
kind: collaboration
id: bld_collaboration_analyst_briefing
pillar: P12
llm_function: COLLABORATE
purpose: How analyst_briefing-builder works in crews with other builders
quality: 9.0
title: "Collaboration Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, collaboration]
tldr: "How analyst_briefing-builder works in crews with other builders"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - analyst-briefing-builder
  - p03_sp_analyst_briefing_builder
  - bld_collaboration_llm_evaluation_scenario
  - bld_knowledge_card_analyst_briefing
  - bld_collaboration_agent_computer_interface
  - bld_instruction_analyst_briefing
  - bld_collaboration_ai_rmf_profile
  - bld_architecture_kind
  - bld_collaboration_gpai_technical_doc
  - bld_collaboration_prompt_technique
---

## Crew Role
Synthesizes product and market intelligence into structured analyst briefing narratives aligned with Gartner, Forrester, and IDC evaluation frameworks. Serves as the primary AR content production component in analyst-facing workflows.

## Receives From
| Builder / Source       | What                                  | Format   |
|------------------------|---------------------------------------|----------|
| knowledge_card-builder | Market and competitive intelligence   | Markdown |
| case_study-builder     | Customer reference proof points       | Markdown |
| benchmark-builder      | Performance and TCO proof points      | Markdown |
| Internal CRM           | ARR, win rate, customer count         | JSON     |
| Product marketing      | Positioning statements, roadmap       | Markdown |

## Produces For
| Builder / Consumer      | What                                   | Format   |
|-------------------------|----------------------------------------|----------|
| AR team                 | Final briefing document for analysts   | Markdown |
| RFI response workflow   | Vendor response to analyst RFI         | Markdown |
| knowledge_card-builder  | Analyst feedback and positioning notes | Markdown |

## Boundary
Does NOT produce sales pitch decks (handled by `landing_page-builder`), press releases (handled by marketing), or customer case studies (handled by `case_study-builder`). Legal review of embargo content is managed by the Legal Team, not this builder. Does NOT claim specific Magic Quadrant positions -- positions are analyst-determined; builder can only claim "target" or "submitted" positions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[analyst-briefing-builder]] | upstream | 0.38 |
| [[p03_sp_analyst_briefing_builder]] | upstream | 0.36 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.33 |
| [[bld_knowledge_card_analyst_briefing]] | upstream | 0.31 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.30 |
| [[bld_instruction_analyst_briefing]] | upstream | 0.30 |
| [[bld_collaboration_ai_rmf_profile]] | sibling | 0.28 |
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_collaboration_gpai_technical_doc]] | sibling | 0.28 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.28 |
