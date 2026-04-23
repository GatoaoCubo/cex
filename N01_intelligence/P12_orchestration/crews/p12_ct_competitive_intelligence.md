---
id: p12_ct_competitive_intelligence.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: competitive_intelligence
purpose: "Coordinate a 3-role crew that produces a peer-reviewed competitive intelligence brief -- market scan, synthesis, and fact-validated output"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "analyst -> synthesizer -> validator"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: 0.92
title: "Competitive Intelligence Crew Template"
version: "1.0.0"
author: n01_intelligence
tags: [crew_template, competitive_intelligence, intelligence, composable, crewai, sequential]
tldr: "3-role sequential crew: market scan -> pattern synthesis -> fact validation"
domain: "competitive intelligence orchestration"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_analyst.md
  - p02_ra_synthesizer.md
  - p02_ra_validator.md
  - team_charter_intelligence_default.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
  - bld_schema_crew_template
  - bld_output_crew_template
---

## Overview
Instantiate when a market, competitor, or technology domain requires a structured
intelligence brief with traceable sources and a validated quality gate. Producer: N01.
Consumers: N06 (commercial strategy), N02 (marketing positioning), N07 (mission planning).
Each role emits a deliverable the next role grounds on. Handoff via a2a Task.

## Roles
| Role | Role Assignment ID | Reason |
|------|--------------------|--------|
| analyst | p02_ra_analyst.md | Scan market, identify competitors (>=3), collect raw data with source trail |
| synthesizer | p02_ra_synthesizer.md | Cross-reference findings, identify patterns, produce structured brief (knowledge_card P01) |
| validator | p02_ra_validator.md | Fact-check all claims, verify sources, enforce quality gate >= 9.0 |

## Process
Topology: `sequential`. Rationale: synthesizer depends on analyst raw data; validator
depends on synthesizer brief. Parallelism would produce ungrounded output. Single
active role = predictable token budget and reproducible quality.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| analyst | shared | persistent (raw data KC saved to P01 for reuse) |
| synthesizer | shared | per-crew-instance (brief is instance-specific) |
| validator | shared | per-crew-instance + regression_check archive |

## Handoff Protocol
`a2a-task-sequential` -- each role emits `artifact_path` + `quality_score` +
`source_count`. Next role reads signal before F1 CONSTRAIN. Validator final
signal adds `verdict: approved | rejected` + `issues` list; N01/N07 decides
on re-run or escalation.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] analyst raw data KC cites >= 3 competitors with source URLs
- [ ] synthesizer brief quality >= 8.5 (pre-validation floor)
- [ ] validator attests final brief quality >= 9.0 (gate p11_qg_crew_template)
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No role produced an artifact without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run competitive_intelligence \
    --charter N01_intelligence/P12_orchestration/crews/team_charter_intelligence_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_analyst.md]] | upstream | 0.45 |
| [[p02_ra_synthesizer.md]] | upstream | 0.43 |
| [[p02_ra_validator.md]] | upstream | 0.41 |
| [[team_charter_intelligence_default.md]] | downstream | 0.38 |
| [[bld_instruction_crew_template]] | upstream | 0.31 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.27 |
| [[p03_sp_crew_template_builder]] | upstream | 0.25 |
| [[bld_schema_crew_template]] | upstream | 0.24 |
| [[bld_output_crew_template]] | upstream | 0.22 |
