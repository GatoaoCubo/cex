---
id: p12_ct_artifact_factory.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: artifact_factory
purpose: "Coordinate a 4-role crew that converts a spec into a peer-reviewed, doctor-clean artifact set for N03_engineering"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "architect -> builder -> reviewer -> integrator"
handoff_protocol_id: a2a-task-sequential
quality: null
title: "Artifact Factory Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, artifact_factory, engineering, composable, crewai]
tldr: "4-role sequential crew: spec decomposition -> 8F build -> peer review -> consistency integration"
domain: "engineering artifact factory"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_architect.md
  - p02_ra_builder.md
  - p02_ra_reviewer.md
  - p02_ra_integrator.md
  - team_charter_factory_default.md
  - bld_instruction_crew_template
  - p11_qg_crew_template
  - crew-template-builder
---

## Overview
Instantiate when a spec or mission plan must be converted into a
peer-reviewed, doctor-clean artifact set under N03_engineering.
Owner: N03 (engineering). Consumers: N07 (consolidation) + downstream nuclei.
Typical trigger: mission spec referencing 3+ kinds where cross-reference
consistency is critical. Handoff via a2a Task (`artifact_path` + `quality_score`).

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| architect | p02_ra_architect.md | Decompose spec into typed artifact list (kind + pillar + deps) |
| builder | p02_ra_builder.md | Produce each artifact via full 8F pipeline; emit artifact_path per item |
| reviewer | p02_ra_reviewer.md | Score each artifact via cex_score.py; reject below 9.0 with gate-specific fixes |
| integrator | p02_ra_integrator.md | Cross-reference all artifacts, run cex_doctor.py, emit crew-complete |

## Process
Topology: `sequential`. Each role strictly depends on the previous artifact set:
decomposition -> build -> review -> integrate. Parallelism breaks the dependency
chain (builder needs architect output; reviewer needs built artifacts).

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| architect | shared | persistent (decomposition KC saved to P01) |
| builder | shared | per-crew-instance (artifact list + 8F traces) |
| reviewer | shared | per-crew-instance + regression_check archive |
| integrator | shared | persistent (doctor report + consistency map saved to P01) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal to
`.cex/runtime/signals/` with `artifact_path` + `quality_score` + `role_name`.
Builder iterates the architect list (one 8F run per artifact); reviewer scores
each path in order; integrator verifies the full set.

## Success Criteria
- [ ] Decomposition list >= 1 entry with kind + pillar + path
- [ ] All decomposition artifacts exist on disk (builder produced)
- [ ] Every artifact quality >= 9.0 (reviewer-attested via cex_score.py)
- [ ] cex_doctor.py exits 0 on all artifacts (integrator-verified)
- [ ] 4/4 a2a-task handoff signals present in `.cex/runtime/signals/`
- [ ] No broken cross-references (integrator consistency report clean)

## Instantiation
```bash
python _tools/cex_crew.py run artifact_factory \
    --charter N03_engineering/P12_orchestration/crews/team_charter_factory_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_architect.md]] | upstream | 0.55 |
| [[p02_ra_builder.md]] | upstream | 0.54 |
| [[p02_ra_reviewer.md]] | upstream | 0.52 |
| [[p02_ra_integrator.md]] | upstream | 0.50 |
| [[team_charter_factory_default.md]] | upstream | 0.44 |
| [[bld_instruction_crew_template]] | upstream | 0.38 |
| [[p11_qg_crew_template]] | downstream | 0.32 |
| [[p12_ct_product_launch.md]] | sibling | 0.30 |
| [[crew-template-builder]] | related | 0.28 |
