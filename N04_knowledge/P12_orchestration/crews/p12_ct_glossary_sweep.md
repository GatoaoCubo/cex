---
id: p12_ct_glossary_sweep.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: glossary_sweep
purpose: Coordinate a 3-role sequential crew that scans a domain for undefined terms, authors glossary entries, and validates consistency across all nucleus vocabularies
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "term_scanner -> glossary_author -> cross_checker"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Glossary Sweep Crew Template"
version: "1.0.0"
author: n04_knowledge
tags: [crew_template, glossary_sweep, glossary, vocabulary, knowledge, composable, n04]
tldr: "3-role sequential crew: term extraction -> glossary authoring -> cross-nucleus consistency validation"
domain: "glossary management orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_term_scanner.md
  - p02_ra_glossary_author.md
  - p02_ra_cross_checker.md
  - p12_ct_knowledge_synthesis.md
  - p12_ct_taxonomy_audit.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
---

## Overview
Instantiate when a nucleus or pillar accumulates undefined domain terms, after
framework assimilation (new concepts enter the codebase), or on periodic
vocabulary hygiene cadence. Producer is N04; consumers are ALL nuclei (glossary
entries feed F2b SPEAK vocabulary loading across N01-N07).

Three roles run in strict sequence; the final deliverable is a validated set of
glossary entries ready for promotion to the P01 library. The cross_checker role
ensures no entry conflicts with any existing controlled vocabulary across nuclei.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| term_scanner | p02_ra_term_scanner.md | Scan domain artifacts for undefined/inconsistent terms |
| glossary_author | p02_ra_glossary_author.md | Write precise glossary_entry artifacts grounded in industry sources |
| cross_checker | p02_ra_cross_checker.md | Validate entries against all nucleus vocabularies for consistency |

## Process
Topology: `sequential`. Rationale: strict dependency -- glossary_author cannot
write definitions without the term_report; cross_checker cannot validate entries
that have not been authored. Parallelism would risk authoring definitions for
terms that are already defined (scanner exclusion list), or validating incomplete
entries.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| term_scanner | shared | persistent (term_report archived for audit trail) |
| glossary_author | shared | per-crew-instance (entries promoted to P01 on sweep_pass) |
| cross_checker | shared | persistent (consistency_report archived to P07) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a signal under `.cex/runtime/signals/`
with `artifact_path` + `quality_score` + role metadata (`candidate_count`,
`entry_count`, `sweep_pass`). Next role reads prior signal before F1 CONSTRAIN.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] term_scanner produced >= 10 undefined term candidates
- [ ] glossary_author produced entries for all high+medium priority terms
- [ ] cross_checker sweep_pass=true (FAIL rate <= 10% of total entries)
- [ ] No cross-nucleus vocabulary conflicts in final entries
- [ ] Handoff signals present for 3/3 roles with no quality_score below 8.0
- [ ] No artifact produced without reading upstream output (provenance enforced)

## Instantiation
```bash
python _tools/cex_crew.py run glossary_sweep \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_glossary_sweep.md

python _tools/cex_crew.py run glossary_sweep \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_glossary_sweep.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_term_scanner.md]] | upstream | 0.50 |
| [[p02_ra_glossary_author.md]] | upstream | 0.48 |
| [[p02_ra_cross_checker.md]] | upstream | 0.46 |
| [[p12_ct_knowledge_synthesis.md]] | sibling | 0.38 |
| [[p12_ct_taxonomy_audit.md]] | sibling | 0.36 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.26 |
| [[p03_sp_crew_template_builder]] | upstream | 0.24 |
