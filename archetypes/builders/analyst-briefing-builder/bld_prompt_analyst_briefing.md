---
kind: instruction
id: bld_instruction_analyst_briefing
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for analyst_briefing
quality: 8.9
title: "Instruction Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, instruction]
tldr: "Step-by-step production process for analyst_briefing"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_analyst_briefing_builder
  - analyst-briefing-builder
  - bld_knowledge_card_analyst_briefing
  - p05_qg_analyst_briefing
  - p10_mem_analyst_briefing_builder
  - bld_schema_analyst_briefing
  - bld_collaboration_analyst_briefing
  - bld_examples_analyst_briefing
  - bld_knowledge_card_competitive_matrix
  - bld_output_template_analyst_briefing
---

## Phase 1: RESEARCH
1. Identify the target analyst firm (Gartner, Forrester, IDC) and specific research track (Magic Quadrant, Wave, MarketScape).
2. Pull the firm's published evaluation criteria for the relevant research area.
3. Audit existing vendor positioning artifacts (pitch decks, case studies, win/loss data).
4. Collect quantified proof points: ARR, YoY growth, NPS score, customer retention rate, competitive win rate.
5. Map current product capabilities against analyst evaluation dimensions.
6. Identify coverage gaps where proof points are weak or missing.

## Phase 2: COMPOSE
1. Reference bld_schema_analyst_briefing.md for required fields (company_overview, market_position, product_strengths, competitive_landscape, roadmap, analyst_questions).
2. Write a concise company overview (max 150 words) positioning the vendor within the analyst's target market.
3. Articulate market position with Gartner/Forrester/IDC framework language (e.g., "Visionary," "Leader," "Strong Performer").
4. List 5-7 quantified product strengths mapped to analyst evaluation criteria.
5. Document competitive landscape: 3-5 named competitors with differentiation points.
6. Outline 12-month roadmap at briefable detail level (no under-NDA specifics without embargo flag).
7. Prepare 8-10 anticipated analyst questions with pre-approved one-paragraph responses.
8. Validate all proof points against approved data sources (no unverified claims).

## Phase 3: VALIDATE
- [ ] All required fields present (company_overview, market_position, product_strengths, competitive_landscape, roadmap, analyst_questions).
- [ ] Proof points are quantified and sourced (no unverified claims).
- [ ] Analyst firm and research track clearly identified (gartner, forrester, or idc).
- [ ] Competitive landscape names at least 2 competitors with differentiation.
- [ ] Roadmap section carries NDA/embargo flag if forward-looking specifics included.
- [ ] Analyst questions section contains at least 5 anticipated questions with answers.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_analyst_briefing_builder]] | related | 0.51 |
| [[analyst-briefing-builder]] | downstream | 0.47 |
| [[bld_knowledge_card_analyst_briefing]] | upstream | 0.46 |
| [[p05_qg_analyst_briefing]] | downstream | 0.46 |
| [[p10_mem_analyst_briefing_builder]] | downstream | 0.44 |
| [[bld_schema_analyst_briefing]] | downstream | 0.39 |
| [[bld_collaboration_analyst_briefing]] | downstream | 0.34 |
| [[bld_examples_analyst_briefing]] | downstream | 0.32 |
| [[bld_knowledge_card_competitive_matrix]] | upstream | 0.27 |
| [[bld_output_template_analyst_briefing]] | downstream | 0.25 |
