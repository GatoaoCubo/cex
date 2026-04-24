---
id: p12_ct_taxonomy_audit.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: taxonomy_audit
purpose: Coordinate a 3-role sequential crew that audits the CEX kind taxonomy against industry standards, defines missing kinds, and validates new entries before promotion
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "gap_finder -> definer -> taxonomy_validator"
handoff_protocol_id: a2a-task-sequential
quality: null
title: "Taxonomy Audit Crew Template"
version: "1.0.0"
author: n04_knowledge
tags: [crew_template, taxonomy_audit, knowledge, composable, crewai, n04]
tldr: "3-role sequential crew: gap scan -> definition writing -> taxonomy validation"
domain: "taxonomy audit orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_gap_finder.md
  - p02_ra_definer.md
  - p02_ra_taxonomy_validator.md
  - p12_ct_knowledge_synthesis.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
---

## Overview
Instantiate after framework assimilation (HERMES, WAVE8), on quarterly review
cadence, or when cex_doctor reports kind coverage gaps. Producer is N04;
consumers are N03 (builder creation) and N05 (kinds_meta.json updates).
Three roles run in strict sequence; no new kind enters kinds_meta.json without
a validator PASS verdict.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| gap_finder | p02_ra_gap_finder.md | Scan kinds_meta.json vs industry standards, produce ranked gap report |
| definer | p02_ra_definer.md | Write precise glossary entries for identified gaps, assign pillar |
| taxonomy_validator | p02_ra_taxonomy_validator.md | Validate entries against existing taxonomy, check overlaps/conflicts |

## Process
Topology: `sequential`. Rationale: strict dependency -- definer needs the gap
report; validator needs definer's entries. Parallelism breaks provenance and
risks premature taxonomy promotion.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| gap_finder | shared | persistent (gap_report.md saved to P01 for audit trail) |
| definer | shared | per-crew-instance (entries promoted to P01 on crew_pass) |
| taxonomy_validator | shared | persistent (validation_report.md archived to P07) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a signal under `.cex/runtime/signals/`
with `artifact_path` + `quality_score` + role metadata (`gap_count`,
`entry_count`, `crew_pass`). Next role reads prior signal before F1 CONSTRAIN.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] gap_finder produced >= 5 validated gaps (gap_count >= 5 in signal)
- [ ] definer produced glossary entries for all high+medium priority gaps
- [ ] validator crew_pass=true (FAIL rate <= 10% of total entries)
- [ ] Handoff signals present for 3/3 roles with no quality_score below 8.0
- [ ] No artifact produced without reading upstream output (provenance enforced)

## Instantiation
```bash
python _tools/cex_crew.py run taxonomy_audit \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_taxonomy_audit.md

python _tools/cex_crew.py run taxonomy_audit \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_taxonomy_audit.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_gap_finder.md]] | upstream | 0.52 |
| [[p02_ra_definer.md]] | upstream | 0.51 |
| [[p02_ra_taxonomy_validator.md]] | upstream | 0.49 |
| [[p12_ct_knowledge_synthesis.md]] | sibling | 0.42 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.26 |
| [[p03_sp_crew_template_builder]] | upstream | 0.24 |
