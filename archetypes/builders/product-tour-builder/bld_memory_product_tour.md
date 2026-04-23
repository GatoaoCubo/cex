---
kind: memory
id: p10_mem_product_tour_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for product_tour construction
quality: 8.7
title: "Memory Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, memory]
tldr: "Learned patterns and pitfalls for product_tour construction"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_product_tour
  - p10_mem_interactive_demo_builder
  - p03_sp_product_tour_builder
  - p10_mem_onboarding_flow_builder
  - bld_examples_product_tour
  - product-tour-builder
  - kc_product_tour
  - p10_lr_quickstart_guide_builder
  - p10_mem_github_issue_template_builder
  - p10_mem_user_journey_builder
---

## Observation
Common issues include misaligned tooltip positions, unclear trigger logic (e.g., scroll vs. click), and overloading steps with too much text. Tours often lack clear end goals, leading to user confusion.

## Pattern
Effective tours use concise, action-oriented steps with visual cues. Trigger specs are tightly coupled to user flows (e.g., "after form submission"), ensuring relevance.

## Evidence
Reviewed artifacts showed 30% higher completion rates when tooltips used icons + short text, and triggers were tied to specific UI interactions.

## Recommendations
- Define triggers based on user behavior, not arbitrary timing.
- Limit steps to 5–7, focusing on critical features.
- Use consistent tooltip styling and placement (e.g., bottom-right).
- Include a clear "Skip" option for user control.
- Test tours with real users to validate flow clarity.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_product_tour]] | upstream | 0.32 |
| [[p10_mem_interactive_demo_builder]] | sibling | 0.27 |
| [[p03_sp_product_tour_builder]] | upstream | 0.26 |
| [[p10_mem_onboarding_flow_builder]] | sibling | 0.25 |
| [[bld_examples_product_tour]] | upstream | 0.24 |
| [[product-tour-builder]] | upstream | 0.24 |
| [[kc_product_tour]] | upstream | 0.21 |
| [[p10_lr_quickstart_guide_builder]] | sibling | 0.19 |
| [[p10_mem_github_issue_template_builder]] | sibling | 0.19 |
| [[p10_mem_user_journey_builder]] | sibling | 0.18 |
