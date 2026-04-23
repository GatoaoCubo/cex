---
id: p12_tc_launch_demo.md
kind: team_charter
pillar: P12
llm_function: GOVERN
charter_id: launch_demo_20260414
crew_template_ref: p12_ct_product_launch.md
mission_statement: "Ship a launch package for 'CEX Flywheel v2' targeting senior AI engineers at Series A+ SaaS companies."
quality_gate: 9.0
deadline: "2026-04-18T18:00:00-03:00"
deliverables:
  - "Positioning brief (knowledge_card P01) -- source of truth for copy + design"
  - "Launch copy pack (tagline + headline + 3 body variants)"
  - "Visual assets spec (hero + social + email header)"
  - "Final verdict report (quality scores + pass/fail)"
budget:
  tokens: 120000
  wall_clock_seconds: 1800
  usd: 5.00
stakeholders: ["{{BRAND_NAME}}", n07_orchestrator, n02_marketing]
escalation_protocol: "If any role crosses budget ceiling, escalate to n07 via signal; do NOT silently truncate."
termination_criteria: "ANY of: (1) qa_reviewer signals launch-approved; (2) budget exhausted; (3) deadline passed; (4) 3 consecutive QA rejects on same artifact."
quality: 8.9
density_score: 0.99
title: "Team Charter -- Launch Demo"
version: "1.0.0"
tags: [team_charter, product_launch, demo]
tldr: "Mission contract for product_launch crew instance targeting CEX Flywheel v2 launch."
domain: "product launch governance"
created: "2026-04-14"
related:
  - p12_ct_product_launch.md
  - p02_ra_copywriter.md
  - p02_ra_qa_reviewer.md
  - bld_examples_team_charter
  - p02_ra_designer.md
  - team-charter-builder
  - p01_kc_token_budgeting
  - p03_pt_orchestration_task_dispatch
  - cost-budget-builder
  - bld_collaboration_cost_budget
---

## Mission Statement
Ship a launch package for **CEX Flywheel v2** targeting senior AI engineers at Series A+ SaaS companies.

## Deliverables
1. Positioning brief (knowledge_card under P01) -- source of truth for copy + design
2. Launch copy pack (tagline + headline + 3 body variants)
3. Visual assets spec (hero + social + email header)
4. Final verdict report (quality scores + pass/fail)

## Success Metrics
- Each deliverable quality >= 9.0 (QA-attested)
- Wall-clock under 1800s for the full crew
- Token budget under 120000 total
- All 4 a2a-task handoff signals present

## Budget
- Tokens: 120000 (hard ceiling; role-level ceilings allocated 30k each)
- Wall-clock: 1800s
- USD: 5.00 at Sonnet pricing (roughly 40k input + 80k output tokens)

## Stakeholders
- {{BRAND_NAME}} (product owner -- decides WHAT)
- n07_orchestrator (dispatches + monitors + consolidates)
- n02_marketing (nucleus that owns the crew instance)

## Escalation Protocol
If any role crosses its budget ceiling or fails 3 consecutive QA rejects, emit
`signal_{role}_escalate.json` to `.cex/runtime/signals/`. n07 reads and either
extends budget (if justified) or kills the crew.

## Termination Criteria
ANY of:
1. qa_reviewer signals `launch-approved`
2. Token or wall-clock budget exhausted
3. Deadline passed (2026-04-18T18:00 local)
4. 3 consecutive QA rejects on the same artifact (stuck loop)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_product_launch.md]] | related | 0.33 |
| [[p02_ra_copywriter.md]] | upstream | 0.25 |
| [[p02_ra_qa_reviewer.md]] | upstream | 0.24 |
| [[bld_examples_team_charter]] | upstream | 0.23 |
| [[p02_ra_designer.md]] | upstream | 0.23 |
| [[team-charter-builder]] | related | 0.22 |
| [[p01_kc_token_budgeting]] | upstream | 0.20 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.20 |
| [[cost-budget-builder]] | upstream | 0.19 |
| [[bld_collaboration_cost_budget]] | related | 0.19 |
