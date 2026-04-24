---
id: p12_ct_builder_factory.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: builder_factory
purpose: "Coordinate a 3-role crew that scaffolds a complete builder (12 ISOs + validation) for a new or unregistered kind in the CEX taxonomy"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "spec_writer -> iso_generator -> test_runner"
handoff_protocol_id: a2a-task-sequential
quality: null
title: "Builder Factory Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, builder_factory, engineering, composable, crewai, meta_builder]
tldr: "3-role sequential crew: kind analysis + spec -> 12-ISO production -> doctor + compile validation"
domain: "engineering builder factory"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_spec_writer.md
  - p02_ra_iso_generator.md
  - p02_ra_test_runner.md
  - p12_ct_artifact_factory.md
  - bld_output_template_crew_template
  - crew-template-builder
---

## Overview
Instantiate when a new kind needs a complete builder scaffold (12 ISOs, one per
pillar) or when an existing builder is incomplete and needs regeneration.
Owner: N03 (engineering). Consumers: N07 (kind registration pipeline) + any
nucleus that needs a new artifact type. Typical trigger: `cex_kind_register.py`
creates a new kind entry and the builder directory needs populating. Handoff
via a2a Task with `builder_dir` + `iso_count` + `verdict`.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| spec_writer | p02_ra_spec_writer.md | Analyze kind schema + existing builders; produce structured builder specification |
| iso_generator | p02_ra_iso_generator.md | Produce all 12 ISOs from the spec following pillar-to-function mapping |
| test_runner | p02_ra_test_runner.md | Validate ISOs via cex_doctor.py + cex_compile.py + naming + ASCII check |

## Process
Topology: `sequential`. Rationale: strict dependency chain -- iso_generator
needs the spec to know what to produce; test_runner needs produced ISOs to
validate. Parallelizing would force iso_generator to guess the spec, defeating
the purpose of structured specification.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| spec_writer | shared | per-crew-instance (spec saved to .cex/runtime/crews/) |
| iso_generator | shared | per-crew-instance (ISO list + compilation traces) |
| test_runner | shared | persistent (test report saved to P07 for regression tracking) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal to
`.cex/runtime/signals/` with `output_path` + `role_name` + status fields.
iso_generator reads spec_writer's spec before starting; test_runner reads
iso_generator's builder directory before validating.

## Success Criteria
- [ ] Builder specification exists with complete field inventory and all 12 ISO requirements
- [ ] All 12 ISOs exist in `archetypes/builders/{kind}-builder/` with correct naming
- [ ] cex_doctor.py exits 0 on the builder directory (test_runner-verified)
- [ ] All 12 ISOs compile to valid YAML (test_runner-verified)
- [ ] All ISOs have valid frontmatter (id, kind, pillar, llm_function, quality: null)
- [ ] ASCII compliance passes on any code-containing ISOs (test_runner-verified)
- [ ] 3/3 a2a-task handoff signals present in `.cex/runtime/signals/`

## Instantiation
```bash
python _tools/cex_crew.py run builder_factory \
    --charter N03_engineering/P12_orchestration/crews/team_charter_builder_factory.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_spec_writer.md]] | upstream | 0.58 |
| [[p02_ra_iso_generator.md]] | upstream | 0.56 |
| [[p02_ra_test_runner.md]] | upstream | 0.52 |
| [[p12_ct_artifact_factory.md]] | sibling | 0.45 |
| [[bld_output_template_crew_template]] | upstream | 0.38 |
| [[crew-template-builder]] | related | 0.30 |
