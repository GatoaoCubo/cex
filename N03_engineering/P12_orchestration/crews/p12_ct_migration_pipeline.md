---
id: p12_ct_migration_pipeline.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: migration_pipeline
purpose: "Coordinate a 3-role crew that analyzes, transforms, and validates artifact migrations and refactoring operations across the CEX taxonomy"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "analyzer -> transformer -> migration_validator"
handoff_protocol_id: a2a-task-sequential
quality: null
title: "Migration Pipeline Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, migration_pipeline, engineering, composable, crewai, refactor]
tldr: "3-role sequential crew: state mapping + migration plan -> in-place transformation -> regression validation"
domain: "engineering migration pipeline"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_analyzer.md
  - p02_ra_transformer.md
  - p02_ra_migration_validator.md
  - p12_ct_artifact_factory.md
  - bld_output_template_crew_template
  - crew-template-builder
---

## Overview
Instantiate when a set of artifacts needs structured migration: schema changes,
field renames, pillar reassignment, naming convention updates, or cross-reference
rewiring. Owner: N03 (engineering). Consumers: N07 (system-wide refactoring
missions) + N05 (CI/CD migration gates). Typical trigger: a spec change that
affects 10+ artifacts (e.g., ISO 12P refactor, HERMES kind additions, naming
convention sweep). Handoff via a2a Task with `scope_id` + `artifact_count` +
`regression_count` + `verdict`.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| analyzer | p02_ra_analyzer.md | Map current state of target artifacts; identify all required transformations |
| transformer | p02_ra_transformer.md | Apply transformations in dependency order; compile after each edit |
| migration_validator | p02_ra_migration_validator.md | Check for regressions, broken references, and naming drift post-migration |

## Process
Topology: `sequential`. Rationale: strict dependency chain -- transformer
needs the migration plan to know what to change; migration_validator needs
completed changes to verify. The analysis phase produces the dependency
ordering that the transformer must respect -- parallelizing would break this
ordering guarantee.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| analyzer | shared | per-crew-instance (migration plan saved to .cex/runtime/crews/) |
| transformer | shared | per-crew-instance (change log + before/after hashes) |
| migration_validator | shared | persistent (validation report saved to P07 for audit trail) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal to
`.cex/runtime/signals/` with `output_path` + `role_name` + status fields.
transformer reads analyzer's migration plan before starting;
migration_validator reads transformer's change log before validating.

## Success Criteria
- [ ] Migration plan exists with per-artifact change instructions and dependency ordering
- [ ] All transformations applied in dependency order (transformer change log complete)
- [ ] All modified artifacts compile to valid YAML (transformer-verified per edit)
- [ ] Zero regressions: no broken cross-references (migration_validator-verified)
- [ ] cex_doctor.py exits 0 on the full migration scope (migration_validator-verified)
- [ ] No files modified outside the declared migration scope (migration_validator-verified)
- [ ] 3/3 a2a-task handoff signals present in `.cex/runtime/signals/`

## Instantiation
```bash
python _tools/cex_crew.py run migration_pipeline \
    --charter N03_engineering/P12_orchestration/crews/team_charter_migration.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_analyzer.md]] | upstream | 0.58 |
| [[p02_ra_transformer.md]] | upstream | 0.56 |
| [[p02_ra_migration_validator.md]] | upstream | 0.52 |
| [[p12_ct_artifact_factory.md]] | sibling | 0.42 |
| [[p12_ct_code_review_pipeline.md]] | sibling | 0.38 |
| [[bld_output_template_crew_template]] | upstream | 0.35 |
| [[crew-template-builder]] | related | 0.28 |
