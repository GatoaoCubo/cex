---
id: p12_tc_partnership_default.md
kind: team_charter
pillar: P12
llm_function: GOVERN
charter_id: partnership_default
crew_template_ref: p12_ct_partnership_kit.md
mission_statement: "Design a complete partner program: ecosystem research + program listing + deal governance -- ready for launch."
quality_gate: 9.0
deadline: "2026-12-31T23:59:59-03:00"
deliverables:
  - "Ecosystem map (knowledge_card P01) -- >= 3 partner categories with value exchange, revenue multiplier, competitive landscape"
  - "Partner listing (P05) -- >= 3 tiers with commissions, co-marketing, onboarding sequence"
  - "Deal governance (P05) -- SLA terms per tier, revenue protection clauses, QBR cadence"
budget:
  tokens: 150000
  wall_clock_seconds: 2400
  usd: 6.00
stakeholders: ["{{BRAND_NAME}}", n07_orchestrator, n06_commercial]
escalation_protocol: "If any role crosses budget ceiling or fails 3 consecutive quality checks, emit signal_{role}_escalate.json to .cex/runtime/signals/. N07 reads and either extends budget or kills crew."
termination_criteria: "ANY of: (1) deal_reviewer signals partnership-kit-complete; (2) budget exhausted; (3) deadline passed; (4) 3 consecutive quality rejects on same artifact."
quality: null
density_score: null
title: "Team Charter -- Partnership Kit Default"
version: "1.0.0"
tags: [team_charter, partnership_kit, commercial, default, n06]
tldr: "Default mission contract for partnership_kit crew -- produces partner program with deal governance in 3 sequential roles."
domain: "partner program governance"
created: "2026-04-23"
related:
  - p12_ct_partnership_kit.md
  - p02_ra_partner_researcher.md
  - p02_ra_proposal_writer.md
  - p02_ra_deal_reviewer.md
  - kc_commercial_vocabulary
  - bld_examples_team_charter
  - p01_kc_token_budgeting
  - team-charter-builder
  - kc_ai_saas_monetization
  - kc_ai_compliance_gdpr
---

## Mission Statement
Design a complete partner program for the primary product. Owner: N06
(commercial). Consumers: partnerships, BD, channel sales, and legal.

## Deliverables
1. Ecosystem map (knowledge_card under P01) -- >= 3 partner categories with value exchange model, revenue multiplier, and competitive landscape
2. Partner listing (P05) -- >= 3 tiers with commissions, co-marketing benefits, and 7-day onboarding sequence
3. Deal governance (P05) -- SLA terms per tier, revenue protection (clawback, caps, sunset), QBR cadence

## Success Metrics
- Each deliverable quality >= 9.0 (gate p11_qg_crew_template)
- Wall-clock under 2400s for the full crew
- Token budget under 150000 total (50k per role)
- All 3 a2a-task handoff signals present
- Commission structure: monotonically increasing by tier
- SLA uptime: >= 99.5% for highest partner tier

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
1. deal_reviewer signals `partnership-kit-complete` with quality >= 9.0
2. Token or wall-clock budget exhausted
3. Deadline passed
4. 3 consecutive quality rejects on the same artifact (stuck loop)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_partnership_kit.md]] | related | 0.56 |
| [[p02_ra_partner_researcher.md]] | upstream | 0.44 |
| [[p02_ra_proposal_writer.md]] | upstream | 0.42 |
| [[p02_ra_deal_reviewer.md]] | upstream | 0.40 |
| [[kc_commercial_vocabulary]] | upstream | 0.35 |
| [[bld_examples_team_charter]] | upstream | 0.28 |
| [[p01_kc_token_budgeting]] | upstream | 0.26 |
| [[team-charter-builder]] | related | 0.24 |
| [[kc_ai_saas_monetization]] | related | 0.22 |
| [[kc_ai_compliance_gdpr]] | related | 0.20 |
