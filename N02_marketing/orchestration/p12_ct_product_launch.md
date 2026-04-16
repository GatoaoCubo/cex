---
id: p12_ct_product_launch.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: product_launch
purpose: Coordinate a 4-role crew that ships a new product launch package -- positioning, copy, assets, and QA gate
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "researcher -> copywriter -> designer -> qa"
handoff_protocol_id: a2a-task-sequential
quality: 9.1
title: "Product Launch Crew Template"
version: "1.0.0"
author: n07_crewwiring
tags: [crew_template, product_launch, marketing, composable, crewai]
tldr: "4-role sequential crew: market intel -> positioning copy -> visual assets -> QA gate"
domain: "product launch orchestration"
created: "2026-04-14"
updated: "2026-04-14"
---

## Overview
Instantiate when a product or feature needs a cross-function launch package.
Producer is N02 (marketing), consumers are sales ops + growth. The crew
runs four roles in strict sequence; each emits a deliverable that the next
role grounds on. Handoff is via a2a Task with artifact attached.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| market_researcher | p02_ra_market_researcher.md | Scan market + competitors, produce positioning brief |
| copywriter | p02_ra_copywriter.md | Turn brief into launch copy (tagline, headline, body) |
| designer | p02_ra_designer.md | Compose visual assets spec (hero, social, email header) |
| qa_reviewer | p02_ra_qa_reviewer.md | Enforce quality gate 9.0 on every deliverable |

## Process
Topology: `sequential`. Rationale: each role strictly depends on the previous
artifact. Parallelism adds no value and introduces consistency risk
(copywriter needs positioning; designer needs copy; QA needs all three).

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| market_researcher | shared | persistent (KC saved to P01) |
| copywriter | shared | per-crew-instance |
| designer | shared | per-crew-instance |
| qa_reviewer | shared | per-crew-instance + regression_check archive |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` + `quality_score`. Next role reads prior artifact before
starting its own F1 CONSTRAIN.

## Success Criteria
- [ ] All 4 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Every deliverable has quality >= 9.0 (QA-attested)
- [ ] Handoff protocol signals present for 4/4 roles
- [ ] No role produced an artifact without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run product_launch --charter N02_marketing/crews/team_charter_launch_demo.md
```
