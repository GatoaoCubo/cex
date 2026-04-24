---
id: p12_ct_content_campaign.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: content_campaign
purpose: Coordinate a 3-role crew that produces a multi-channel content campaign -- audience strategy, channel templates, and brand quality gate
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "strategist -> creator -> reviewer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Content Campaign Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, content_campaign, marketing, composable, crewai, multi_channel]
tldr: "3-role sequential crew: audience strategy -> channel content templates -> brand voice QA gate"
domain: "multi-channel content campaign orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_campaign_strategist.md
  - p02_ra_content_creator.md
  - p02_ra_content_reviewer.md
  - p12_ct_product_launch.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - bld_collaboration_handoff_protocol
---

## Overview
Instantiate when N02 needs to produce a coordinated content package across
social, email, and blog channels for a defined audience. The crew runs three
roles in strict sequence: strategist defines audience segments and messaging
angles, creator produces channel-specific content templates grounded on the
strategy brief, reviewer gates brand voice consistency and CTA effectiveness.
Producer is N02 (marketing); consumers are content ops, growth, and social teams.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| strategist | p02_ra_campaign_strategist.md | Define audience segments, channels, and messaging angles |
| creator | p02_ra_content_creator.md | Produce content templates for social, email, and blog |
| reviewer | p02_ra_content_reviewer.md | Score brand voice, CTA effectiveness; enforce quality gate |

## Process
Topology: `sequential`. Rationale: creator requires a validated strategy brief
before writing templates (no brief = no audience grounding); reviewer requires
all templates before scoring consistency across channels. Parallelism would
allow creator to start without segments, introducing misalignment risk.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| strategist | shared | persistent (strategy brief saved to P01) |
| creator | shared | per-crew-instance |
| reviewer | shared | per-crew-instance + regression_check archive |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` + `quality_score`. Next role reads prior artifact before
starting its own F1 CONSTRAIN. Creator reads `strategy_brief_id` from
strategist signal; reviewer reads `template_pack_id` from creator signal.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] strategy_brief contains >= 2 audience segments with channel mapping
- [ ] template_pack covers all 3 channels: social, email, blog
- [ ] reviewer quality_score >= 9.0 for brand voice + CTA dimensions
- [ ] Handoff protocol signals present for 3/3 roles

## Instantiation
```bash
python _tools/cex_crew.py run content_campaign \
    --charter N02_marketing/P12_orchestration/crews/team_charter_content_campaign.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_campaign_strategist.md]] | upstream | 0.52 |
| [[p02_ra_content_creator.md]] | upstream | 0.50 |
| [[p02_ra_content_reviewer.md]] | upstream | 0.48 |
| [[p12_ct_product_launch.md]] | sibling | 0.41 |
| [[bld_instruction_crew_template]] | related | 0.31 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.27 |
| [[bld_collaboration_handoff_protocol]] | related | 0.25 |
