---
id: p12_tc_subscription_default.md
kind: team_charter
8f: F8_collaborate
pillar: P12
llm_function: GOVERN
charter_id: subscription_default
crew_template_ref: p12_ct_subscription_design.md
mission_statement: "Design a complete subscription tier model: segment research + tier architecture + retention validation -- ready for launch."
quality_gate: 9.0
deadline: "2026-12-31T23:59:59-03:00"
deliverables:
  - "Segment profile (knowledge_card P01) -- >= 3 segments with TAM, WTP, usage patterns, churn risk"
  - "Tier model (P05) -- >= 3 tiers with pricing, feature gates, value metrics, annual discount"
  - "Retention playbook (P05) -- churn prevention triggers + NRR projections + win-back sequence"
budget:
  tokens: 150000
  wall_clock_seconds: 2400
  usd: 6.00
stakeholders: ["{{BRAND_NAME}}", n07_orchestrator, n06_commercial]
escalation_protocol: "If any role crosses budget ceiling or fails 3 consecutive quality checks, emit signal_{role}_escalate.json to .cex/runtime/signals/. N07 reads and either extends budget or kills crew."
termination_criteria: "ANY of: (1) retention_analyst signals subscription-design-complete; (2) budget exhausted; (3) deadline passed; (4) 3 consecutive quality rejects on same artifact."
quality: null
density_score: null
title: "Team Charter -- Subscription Design Default"
version: "1.0.0"
tags: [team_charter, subscription_design, commercial, default, n06]
tldr: "Default mission contract for subscription_design crew -- produces tier model with retention validation in 3 sequential roles."
domain: "subscription tier design governance"
created: "2026-04-23"
related:
  - p12_ct_subscription_design.md
  - p02_ra_segment_researcher.md
  - p02_ra_tier_architect.md
  - p02_ra_retention_analyst.md
  - kc_commercial_vocabulary
  - bld_examples_team_charter
  - p01_kc_token_budgeting
  - team-charter-builder
  - kc_ai_saas_monetization
  - enum_def_pricing_tiers
---

## Mission Statement
Design a complete subscription tier model for the primary product. Owner: N06
(commercial). Consumers: product, finance, growth, and renewal teams.

## Deliverables
1. Segment profile (knowledge_card under P01) -- >= 3 customer segments with TAM, WTP, usage patterns, churn risk
2. Tier model (P05) -- >= 3 tiers with pricing, feature gates, value metrics, and annual discount structure
3. Retention playbook (P05) -- churn prevention triggers, NRR projections (3 scenarios), win-back sequence

## Success Metrics
- Each deliverable quality >= 9.0 (gate p11_qg_crew_template)
- Wall-clock under 2400s for the full crew
- Token budget under 150000 total (50k per role)
- All 3 a2a-task handoff signals present
- NRR projection base scenario >= 110%
- No tier cannibalization (adjacent tier value uplift >= 25%)

## Budget
- Tokens: 150000 (hard ceiling; 50000 per role)
- Wall-clock: 2400s (40 min)
- USD: 6.00 at Sonnet pricing

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
1. retention_analyst signals `subscription-design-complete` with quality >= 9.0
2. Token or wall-clock budget exhausted
3. Deadline passed
4. 3 consecutive quality rejects on the same artifact (stuck loop)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_subscription_design.md]] | related | 0.56 |
| [[p02_ra_segment_researcher.md]] | upstream | 0.44 |
| [[p02_ra_tier_architect.md]] | upstream | 0.42 |
| [[p02_ra_retention_analyst.md]] | upstream | 0.40 |
| [[kc_commercial_vocabulary]] | upstream | 0.35 |
| [[bld_examples_team_charter]] | upstream | 0.28 |
| [[p01_kc_token_budgeting]] | upstream | 0.26 |
| [[team-charter-builder]] | related | 0.24 |
| [[kc_ai_saas_monetization]] | related | 0.22 |
| [[enum_def_pricing_tiers]] | related | 0.20 |
