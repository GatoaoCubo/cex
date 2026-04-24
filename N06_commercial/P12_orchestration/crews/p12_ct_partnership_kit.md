---
id: p12_ct_partnership_kit.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: partnership_kit
purpose: 3-role sequential crew that researches partner ecosystem, designs partner program listing, and validates deal governance -- producing a launch-ready partner kit with SLA overlay
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "partner_researcher -> proposal_writer -> deal_reviewer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Partnership Kit Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, partnership_kit, commercial, composable, crewai, n06]
tldr: "3-role sequential: ecosystem mapping -> partner program listing + onboarding -> SLA governance + deal review"
domain: "partner program design and deal governance"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_partner_researcher.md
  - p02_ra_proposal_writer.md
  - p02_ra_deal_reviewer.md
  - p12_ct_sales_pipeline.md
  - p12_ct_pricing_workshop.md
  - p12_ct_subscription_design.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - kc_commercial_vocabulary
---

## Overview
Instantiate when N06 needs to design or expand a partner program. Owner is N06
(commercial); consumers are partnerships, BD, and channel sales. Three roles run
in strict sequence: partner_researcher maps the competitive partner landscape and
identifies high-value categories; proposal_writer designs the partner program
listing with tiers, commissions, and onboarding; deal_reviewer validates SLA terms,
revenue protection clauses, and governance cadence. The output is a launch-ready
partner kit with built-in deal safeguards.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| partner_researcher | p02_ra_partner_researcher.md | Map ecosystem, identify >= 3 partner categories with revenue potential |
| proposal_writer | p02_ra_proposal_writer.md | Design partner program: >= 3 tiers, commissions, co-marketing, onboarding |
| deal_reviewer | p02_ra_deal_reviewer.md | Define SLAs, review revenue protection, produce governance framework |

## Process
Topology: `sequential`. Rationale: proposal_writer requires the ecosystem map
before designing program tiers; deal_reviewer requires the complete listing
before defining SLA terms and governance. Each role grounds on the prior output.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| partner_researcher | shared | persistent (KC saved to P01 under N06) |
| proposal_writer | shared | per-crew-instance |
| deal_reviewer | shared | per-crew-instance + archive in P07 |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with `artifact_path`
+ `quality_score`. Next role reads prior artifact before starting its own F1
CONSTRAIN. No role begins without an upstream signal confirming quality >= 9.0.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Every deliverable quality >= 9.0 (gate p11_qg_crew_template)
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] Ecosystem map covers >= 3 partner categories with revenue projections
- [ ] Partner listing has >= 3 tiers with monotonically increasing commissions
- [ ] SLA terms defined per tier with escalation paths
- [ ] Governance includes QBR cadence + performance-based tier changes

## Instantiation
```bash
python _tools/cex_crew.py run partnership_kit \
    --charter N06_commercial/P12_orchestration/crews/team_charter_partnership_default.md
python _tools/cex_crew.py run partnership_kit \
    --charter N06_commercial/P12_orchestration/crews/team_charter_partnership_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_partner_researcher.md]] | upstream | 0.58 |
| [[p02_ra_proposal_writer.md]] | upstream | 0.56 |
| [[p02_ra_deal_reviewer.md]] | upstream | 0.54 |
| [[p12_ct_sales_pipeline.md]] | sibling | 0.44 |
| [[p12_ct_pricing_workshop.md]] | sibling | 0.42 |
| [[p12_ct_subscription_design.md]] | sibling | 0.40 |
| [[bld_instruction_crew_template]] | upstream | 0.38 |
| [[bld_collaboration_crew_template]] | related | 0.35 |
| [[p11_qg_crew_template]] | upstream | 0.33 |
| [[kc_commercial_vocabulary]] | related | 0.30 |
