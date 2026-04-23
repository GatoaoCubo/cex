---
kind: memory
id: p10_mem_discovery_questions_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for discovery_questions construction
quality: 8.7
title: "Memory Discovery Questions Builder"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, memory]
tldr: "Learned patterns and pitfalls for discovery_questions construction"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_discovery_questions
  - bld_examples_discovery_questions
  - p03_sp_discovery_questions_builder
  - discovery-questions-builder
  - bld_knowledge_card_discovery_questions
  - kc_discovery_questions
  - p01_qg_discovery_questions
  - p10_mem_sales_playbook_builder
  - bld_output_template_discovery_questions
  - p03_sp_sales_playbook_builder
---

## Observation
Discovery questions often lack alignment with specific buyer personas or deal stages, leading to generic, unactionable prompts. Over-reliance on broad frameworks without contextual customization reduces relevance and engagement.

## Pattern
Effective questions are structured around MEDDIC/BANT pillars (e.g., Budget, Authority) and tailored to persona roles (e.g., CTO vs. IT manager) and stage-specific pain points (e.g., evaluation vs. negotiation).

## Evidence
Reviewed artifacts showed higher engagement when questions explicitly referenced persona responsibilities and stage-specific obstacles (e.g., "How does your current vendor’s support impact your team’s productivity?").

## Recommendations
- Map questions to MEDDIC/BANT pillars and persona roles (e.g., "What metrics define success for your team?").
- Segment questions by deal stage (e.g., early-stage: "What challenges are you facing now?" vs. late-stage: "What’s your timeline for implementation?").
- Use open-ended prompts to uncover unspoken needs (e.g., "What’s the biggest hurdle you’ve faced in adopting new solutions?").
- Avoid sales jargon; focus on the buyer’s priorities (e.g., "How does this impact your department’s goals?").
- Test questions with real buyers to refine clarity and relevance.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_discovery_questions]] | upstream | 0.50 |
| [[bld_examples_discovery_questions]] | upstream | 0.50 |
| [[p03_sp_discovery_questions_builder]] | upstream | 0.47 |
| [[discovery-questions-builder]] | upstream | 0.45 |
| [[bld_knowledge_card_discovery_questions]] | upstream | 0.43 |
| [[kc_discovery_questions]] | upstream | 0.36 |
| [[p01_qg_discovery_questions]] | downstream | 0.33 |
| [[p10_mem_sales_playbook_builder]] | sibling | 0.26 |
| [[bld_output_template_discovery_questions]] | upstream | 0.25 |
| [[p03_sp_sales_playbook_builder]] | upstream | 0.24 |
