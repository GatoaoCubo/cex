---
id: p12_ct_subscription_design.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: subscription_design
purpose: 3-role sequential crew that researches customer segments, designs subscription tiers, and validates retention -- producing a launch-ready tier model with churn prevention overlay
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "segment_researcher -> tier_architect -> retention_analyst"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Subscription Design Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, subscription_design, commercial, composable, crewai, n06]
tldr: "3-role sequential: customer segments -> tier model + feature gates -> churn prevention + NRR validation"
domain: "subscription tier design and retention validation"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_segment_researcher.md
  - p02_ra_tier_architect.md
  - p02_ra_retention_analyst.md
  - p12_ct_sales_pipeline.md
  - p12_ct_pricing_workshop.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - kc_commercial_vocabulary
  - kc_ai_saas_monetization
---

## Overview
Instantiate when N06 needs to design or redesign a subscription model from scratch.
Owner is N06 (commercial); consumers are product, finance, and growth. Three roles
run in strict sequence: segment_researcher profiles customer segments and maps
willingness-to-pay; tier_architect designs the tier structure, feature gates, and
pricing; retention_analyst stress-tests for churn risk and produces intervention
playbooks. The output is a launch-ready tier model with built-in retention
safeguards.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| segment_researcher | p02_ra_segment_researcher.md | Profile >= 3 segments with TAM, WTP, usage patterns, and churn risk |
| tier_architect | p02_ra_tier_architect.md | Design tier structure, feature gates, value metrics, and annual discount |
| retention_analyst | p02_ra_retention_analyst.md | Validate NRR under 3 scenarios, produce churn prevention playbook |

## Process
Topology: `sequential`. Rationale: tier_architect requires segment profiles before
designing tiers; retention_analyst requires the complete tier model before stress-testing.
Each role grounds on the prior role's artifact, ensuring coherent end-to-end output.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| segment_researcher | shared | persistent (KC saved to P01 under N06) |
| tier_architect | shared | per-crew-instance |
| retention_analyst | shared | per-crew-instance + archive in P07 |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with `artifact_path`
+ `quality_score`. Next role reads prior artifact (via Read tool on artifact_path)
before starting its own F1 CONSTRAIN. No role begins without an upstream signal
confirming quality >= 9.0.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Every deliverable quality >= 9.0 (gate p11_qg_crew_template)
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] Segment profile covers >= 3 segments with TAM, WTP, and churn risk
- [ ] Tier model has >= 3 tiers with no cannibalization (>= 25% value uplift per adjacent pair)
- [ ] NRR projection present for base + optimistic + pessimistic scenarios
- [ ] Churn prevention playbook covers >= 3 intervention triggers per tier

## Instantiation
```bash
python _tools/cex_crew.py run subscription_design \
    --charter N06_commercial/P12_orchestration/crews/team_charter_subscription_default.md
python _tools/cex_crew.py run subscription_design \
    --charter N06_commercial/P12_orchestration/crews/team_charter_subscription_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_segment_researcher.md]] | upstream | 0.58 |
| [[p02_ra_tier_architect.md]] | upstream | 0.56 |
| [[p02_ra_retention_analyst.md]] | upstream | 0.54 |
| [[p12_ct_sales_pipeline.md]] | sibling | 0.44 |
| [[p12_ct_pricing_workshop.md]] | sibling | 0.42 |
| [[bld_instruction_crew_template]] | upstream | 0.38 |
| [[bld_collaboration_crew_template]] | related | 0.35 |
| [[p11_qg_crew_template]] | upstream | 0.33 |
| [[kc_commercial_vocabulary]] | related | 0.30 |
| [[kc_ai_saas_monetization]] | related | 0.28 |
