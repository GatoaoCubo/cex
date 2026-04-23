---
id: p12_ct_deep_research.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: deep_research
purpose: "4-role sequential crew: scan sources -> synthesize -> fact-validate -> produce research brief"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "scout -> analyst -> fact_checker -> writer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: 0.93
title: "Deep Research Crew Template"
version: "1.0.0"
author: n01_intelligence
tags: [crew_template, deep_research, intelligence, composable, crewai, sequential]
tldr: "4-role sequential crew: source scan -> synthesis -> fact validation -> research brief"
domain: "deep research orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_scout.md
  - p02_ra_deep_analyst.md
  - p02_ra_fact_checker.md
  - p02_ra_research_writer.md
  - p12_ct_competitive_intelligence.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
  - bld_schema_crew_template
---

## Overview
Instantiate when a topic requires a comprehensive, fact-validated research report.
Producer: N01. Consumers: N07 (mission planning), N06 (strategy), N02 (positioning).
Each role emits a deliverable the next role grounds on. Distinct from
`competitive_intelligence` (3-role market scan): this crew covers any research domain
and adds a confidence-scored fact-checking gate before the final brief.

## Roles
| Role | Role Assignment ID | Reason |
|------|--------------------|--------|
| scout | p02_ra_scout.md | Scan sources, find papers/data, produce raw findings KC with >= 5 citations |
| analyst | p02_ra_deep_analyst.md | Synthesize findings into structured analysis KC with patterns and gap identification |
| fact_checker | p02_ra_fact_checker.md | Validate all claims, score per-claim confidence, block passage if overall < 0.65 |
| writer | p02_ra_research_writer.md | Produce final research brief (executive summary + findings + recommendations) |

## Process
Topology: `sequential`. Rationale: each role strictly depends on the prior artifact;
parallelism breaks the confidence-scoring chain and produces ungrounded output.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| scout | shared | persistent (raw findings KC saved to P01) |
| analyst | shared | per-crew-instance |
| fact_checker | shared | per-crew-instance + regression_check archive |
| writer | shared | per-crew-instance |

## Handoff Protocol
`a2a-task-sequential` -- each role emits `artifact_path` + `quality_score`.
Fact_checker adds `confidence_score` + `verdict: pass | block` + `low_confidence_claims`.
On `block`, analyst revises before writer proceeds.

## Success Criteria
- [ ] All 4 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] scout raw findings KC cites >= 5 sources with URLs and access dates
- [ ] analyst KC quality >= 8.5 (pre-validation floor)
- [ ] fact_checker overall confidence score >= 0.65 (gate p11_qg_crew_template)
- [ ] writer brief quality >= 9.0 (final output gate)
- [ ] Handoff protocol signals present for 4/4 roles
- [ ] No role produced an artifact without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run deep_research \
    --charter N01_intelligence/P12_orchestration/crews/team_charter_intelligence_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| [[p02_ra_scout.md]] | upstream |
| [[p02_ra_deep_analyst.md]] | upstream |
| [[p02_ra_fact_checker.md]] | upstream |
| [[p02_ra_research_writer.md]] | upstream |
| [[p12_ct_competitive_intelligence.md]] | sibling |
| [[bld_instruction_crew_template]] | upstream |
| [[bld_collaboration_crew_template]] | related |
| [[p11_qg_crew_template]] | upstream |
| [[p03_sp_crew_template_builder]] | upstream |
| [[bld_schema_crew_template]] | upstream |
