---
id: p12_ct_pricing_workshop.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: pricing_workshop
purpose: 3-role sequential crew that designs and validates a complete pricing model -- competitive analysis, tier architecture, and revenue validation
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "market_analyst -> pricing_architect -> revenue_validator"
handoff_protocol_id: a2a-task-sequential
quality: null
title: "Pricing Workshop Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, pricing_workshop, commercial, composable, crewai, n06]
tldr: "3-role sequential: competitive matrix -> tier model + feature gates -> revenue projections + cannibalization check"
domain: "pricing model design and validation"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_market_analyst.md
  - p02_ra_pricing_architect.md
  - p02_ra_revenue_validator.md
  - p12_ct_sales_pipeline.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - kc_commercial_vocabulary
  - kc_ai_saas_monetization
---

## Overview
Instantiate when N06 needs to design or validate a pricing model before launch.
Owner is N06 (commercial); consumers are product, growth, and finance. Three roles
run in strict sequence: market_analyst maps competitive landscape and WTP signals;
pricing_architect designs tiers, feature gates, and discount rules;
revenue_validator stress-tests the model and checks cannibalization. Handoff via
a2a Task with artifact path attached.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| market_analyst | p02_ra_market_analyst.md | Audit >= 3 competitors, extract WTP signals, map positioning white-space |
| pricing_architect | p02_ra_pricing_architect.md | Design tier structure, feature gate matrix, discount strategy |
| revenue_validator | p02_ra_revenue_validator.md | Model 3-scenario projections, check cannibalization, stress-test margins |

## Process
Topology: `sequential`. Rationale: pricing_architect requires the competitive
matrix before designing tiers; revenue_validator requires the final tier model
before running projections. Parallelism produces ungrounded outputs at each stage.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| market_analyst | shared | persistent (KC saved to P01 under N06) |
| pricing_architect | shared | per-crew-instance |
| revenue_validator | shared | per-crew-instance + archive in P07 |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with `artifact_path`
+ `quality_score`. Next role reads the prior artifact before its F1 CONSTRAIN.
No role begins without an upstream signal confirming quality >= 9.0.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Every deliverable quality >= 9.0 (gate p11_qg_crew_template)
- [ ] Handoff signals present for 3/3 roles
- [ ] Competitive matrix: >= 3 competitors x >= 4 dimensions
- [ ] Revenue validation: base + optimistic + pessimistic scenarios present
- [ ] Cannibalization check: upgrade_delta >= 25% value uplift per adjacent tier pair

## Instantiation
```bash
python _tools/cex_crew.py run pricing_workshop \
    --charter N06_commercial/P12_orchestration/crews/team_charter_pricing_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_market_analyst.md]] | upstream | 0.58 |
| [[p02_ra_pricing_architect.md]] | upstream | 0.56 |
| [[p02_ra_revenue_validator.md]] | upstream | 0.54 |
| [[p12_ct_sales_pipeline.md]] | sibling | 0.44 |
| [[bld_instruction_crew_template]] | upstream | 0.38 |
| [[bld_collaboration_crew_template]] | related | 0.35 |
| [[p11_qg_crew_template]] | upstream | 0.33 |
| [[kc_commercial_vocabulary]] | related | 0.30 |
| [[kc_ai_saas_monetization]] | related | 0.28 |
| [[p12_ct_product_launch.md]] | sibling | 0.25 |
