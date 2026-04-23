---
kind: instruction
id: bld_instruction_case_study
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for case_study
quality: 8.9
title: "Instruction Case Study"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, instruction]
tldr: "Step-by-step production process for case_study"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_case_study
  - bld_schema_case_study
  - p05_qg_case_study
  - bld_output_template_case_study
  - p03_sp_case_study_builder
  - bld_instruction_customer_segment
  - case-study-builder
  - bld_instruction_press_release
  - bld_instruction_context_doc
  - bld_tools_case_study
---

## Phase 1: RESEARCH (case study discovery)
1. Confirm customer champion participation and quote approval rights.
2. Collect customer context: company size, industry, geography, persona (e.g., CTO, VP Sales).
3. Document the challenge: pain point, business impact, timeline (before state).
4. Gather solution details: product features used, implementation timeline, integrations.
5. Quantify outcomes: ROI percentage, cost savings, time-to-value, efficiency gains (after state).
6. Record direct pullquote from champion (50-80 words, attributable to name + title).
7. Validate all metrics against customer-approved data (no unverified statistics).

## Phase 2: COMPOSE
1. Structure per bld_schema_case_study.md Challenge -> Solution -> Outcome arc.
2. Write Challenge section (150-200 words): before-state, pain context, business stakes.
3. Write Solution section: named product features, deployment timeline, key integrations.
4. Write Outcome section: 3+ KPIs with before/after comparison (e.g., "30% downtime -> 2%").
5. Insert pullquote block per bld_output_template_case_study.md designated block.
6. Add ROI call-out box: headline metric, timeframe, verified source.
7. Add company sidebar: industry, size, region, champion name and title.
8. Write "Lessons Learned" closing (50-100 words) with transferable insight.
9. Edit for plain language: replace jargon with contextual terms.

## Phase 3: VALIDATE
- [ ] All bld_schema_case_study.md required fields populated.
- [ ] Pullquote is direct, attributed, and approved by customer.
- [ ] 3+ KPIs with before/after comparison present.
- [ ] ROI call-out includes headline number, timeframe, and source.
- [ ] No fabricated metrics or unverified vendor claims.
- [ ] Customer champion and product team approval obtained.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_case_study]] | upstream | 0.51 |
| [[bld_schema_case_study]] | downstream | 0.47 |
| [[p05_qg_case_study]] | downstream | 0.41 |
| [[bld_output_template_case_study]] | downstream | 0.37 |
| [[p03_sp_case_study_builder]] | related | 0.28 |
| [[bld_instruction_customer_segment]] | sibling | 0.20 |
| [[case-study-builder]] | downstream | 0.20 |
| [[bld_instruction_press_release]] | sibling | 0.20 |
| [[bld_instruction_context_doc]] | sibling | 0.19 |
| [[bld_tools_case_study]] | downstream | 0.19 |
