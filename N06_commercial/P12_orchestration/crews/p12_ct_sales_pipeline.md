---
id: p12_ct_sales_pipeline.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: sales_pipeline
purpose: Coordinate a 3-role sequential crew that builds a complete B2B sales package -- market strategy, collateral, and closing plays
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "strategist -> content_producer -> closer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Sales Pipeline Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, sales_pipeline, commercial, composable, crewai, n06]
tldr: "3-role sequential crew: market strategy -> sales collateral -> closing playbook"
domain: "B2B sales pipeline orchestration"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_strategist.md
  - p02_ra_content_producer.md
  - p02_ra_closer.md
  - team_charter_pipeline_default.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - kc_commercial_vocabulary
  - kc_ai_saas_monetization
  - p12_ct_product_launch.md
---

## Overview
Instantiate when N06 needs a complete B2B sales enablement package for a product,
tier, or market segment. Owner is N06 (commercial). The crew runs three roles in
strict sequence; each role emits a deliverable that grounds the next. Handoff is
via a2a Task with artifact attached. Outputs feed sales ops, growth, and renewal
teams directly.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| strategist | p02_ra_strategist.md | Analyze market segments, define pricing tiers, map customer journey + ICP |
| content_producer | p02_ra_content_producer.md | Produce sales collateral: pitch deck outline, case study template, ROI calculator |
| closer | p02_ra_closer.md | Build objection handling playbook, renewal workflow, expansion plays |

## Process
Topology: `sequential`. Rationale: strict dependency chain -- content_producer needs
the strategist's segment + pricing map before producing collateral; closer needs the
collateral pack before authoring objection plays. Sequential ensures every downstream
role is grounded on upstream artifact.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| strategist | shared | persistent (KC saved to P01 under N06) |
| content_producer | shared | per-crew-instance |
| closer | shared | per-crew-instance + archive in P05 |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with `artifact_path`
+ `quality_score`. Next role reads prior artifact (via Read tool on artifact_path)
before starting its own F1 CONSTRAIN. No role begins without an upstream signal
confirming quality >= 9.0.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Every deliverable quality >= 9.0 (gate p11_qg_crew_template)
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No role produced an artifact without reading upstream output
- [ ] Closer playbook covers >= 5 objection types + 1 expansion play

## Instantiation
```bash
python _tools/cex_crew.py run sales_pipeline \
    --charter N06_commercial/P12_orchestration/crews/team_charter_pipeline_default.md
python _tools/cex_crew.py run sales_pipeline \
    --charter N06_commercial/P12_orchestration/crews/team_charter_pipeline_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_strategist.md]] | upstream | 0.55 |
| [[p02_ra_content_producer.md]] | upstream | 0.54 |
| [[p02_ra_closer.md]] | upstream | 0.52 |
| [[team_charter_pipeline_default.md]] | downstream | 0.44 |
| [[bld_instruction_crew_template]] | upstream | 0.38 |
| [[bld_collaboration_crew_template]] | related | 0.35 |
| [[p11_qg_crew_template]] | upstream | 0.33 |
| [[kc_commercial_vocabulary]] | related | 0.30 |
| [[kc_ai_saas_monetization]] | related | 0.28 |
| [[p12_ct_product_launch.md]] | sibling | 0.27 |
