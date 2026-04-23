---
id: p12_tc_pipeline_default.md
kind: team_charter
pillar: P12
llm_function: GOVERN
charter_id: pipeline_default
crew_template_ref: p12_ct_sales_pipeline.md
mission_statement: "Build a complete B2B sales pipeline package for the primary product tier: strategy brief + collateral pack + closing playbook."
quality_gate: 9.0
deadline: "2026-12-31T23:59:59-03:00"
deliverables:
  - "Strategy brief (knowledge_card P01) -- market segments + pricing tiers + ICP + customer journey"
  - "Collateral pack (P05) -- pitch deck outline + case study template + ROI calculator"
  - "Closing package (P05) -- objection playbook + renewal workflow + expansion plays"
budget:
  tokens: 150000
  wall_clock_seconds: 2400
  usd: 6.00
stakeholders: ["{{BRAND_NAME}}", n07_orchestrator, n06_commercial]
escalation_protocol: "If any role crosses budget ceiling or fails 3 consecutive quality checks, emit signal_{role}_escalate.json to .cex/runtime/signals/. N07 reads and either extends budget or kills crew."
termination_criteria: "ANY of: (1) closer signals pipeline-complete; (2) budget exhausted; (3) deadline passed; (4) 3 consecutive quality rejects on same artifact."
quality: null
density_score: null
title: "Team Charter -- Sales Pipeline Default"
version: "1.0.0"
tags: [team_charter, sales_pipeline, commercial, default, n06]
tldr: "Default mission contract for sales_pipeline crew -- produces full B2B sales package in 3 sequential roles."
domain: "B2B sales pipeline governance"
created: "2026-04-22"
related:
  - p12_ct_sales_pipeline.md
  - p02_ra_strategist.md
  - p02_ra_content_producer.md
  - p02_ra_closer.md
  - kc_commercial_vocabulary
  - bld_examples_team_charter
  - p01_kc_token_budgeting
  - team-charter-builder
  - kc_ai_saas_monetization
  - bld_collaboration_cost_budget
---

## Mission Statement
Build a complete B2B sales pipeline package for the primary product tier.
Owner: N06 (commercial). Consumer: sales ops, growth, and renewal teams.

## Deliverables
1. Strategy brief (knowledge_card under P01) -- market segments + pricing tiers + ICP + customer journey map
2. Collateral pack (P05) -- pitch deck outline + case study template + ROI calculator
3. Closing package (P05) -- objection handling playbook + renewal workflow + expansion plays

## Success Metrics
- Each deliverable quality >= 9.0 (gate p11_qg_crew_template)
- Wall-clock under 2400s for the full crew
- Token budget under 150000 total (50k per role)
- All 3 a2a-task handoff signals present
- Closing package covers >= 5 objection types + >= 2 expansion plays per tier

## Budget
- Tokens: 150000 (hard ceiling; 50000 per role)
- Wall-clock: 2400s (40 min)
- USD: 6.00 at Sonnet pricing (roughly 50k input + 100k output tokens)

## Stakeholders
- {{BRAND_NAME}} (product owner -- decides WHAT)
- n07_orchestrator (dispatches + monitors + consolidates)
- n06_commercial (nucleus that owns the crew instance)

## Escalation Protocol
If any role crosses its token ceiling or fails 3 consecutive quality checks,
emit `signal_{role}_escalate.json` to `.cex/runtime/signals/`. N07 reads and
either extends budget (if justified) or terminates the crew with partial results.

## Termination Criteria
ANY of:
1. closer signals `pipeline-complete` with quality >= 9.0
2. Token or wall-clock budget exhausted
3. Deadline passed
4. 3 consecutive quality rejects on the same artifact (stuck loop)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_sales_pipeline.md]] | related | 0.56 |
| [[p02_ra_strategist.md]] | upstream | 0.44 |
| [[p02_ra_content_producer.md]] | upstream | 0.42 |
| [[p02_ra_closer.md]] | upstream | 0.40 |
| [[kc_commercial_vocabulary]] | upstream | 0.35 |
| [[bld_examples_team_charter]] | upstream | 0.28 |
| [[p01_kc_token_budgeting]] | upstream | 0.26 |
| [[team-charter-builder]] | related | 0.24 |
| [[kc_ai_saas_monetization]] | related | 0.22 |
| [[bld_collaboration_cost_budget]] | related | 0.20 |
