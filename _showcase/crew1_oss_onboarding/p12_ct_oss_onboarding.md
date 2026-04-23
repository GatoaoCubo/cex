---
id: p12_ct_oss_onboarding.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: oss_onboarding
purpose: Coordinate a 4-role sequential crew that produces quickstart_guide + contributor_guide artifacts for the CEXAI OSS release
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "researcher -> doc_writer -> guide_writer -> validator"
handoff_protocol_id: a2a-task-sequential
quality: 8.8
title: "OSS Onboarding Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, oss, onboarding, composable, showcase]
tldr: "4-role sequential crew: repo research -> quickstart -> contributor guide -> release gate"
domain: "OSS documentation orchestration"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_repo_researcher.md
  - p02_ra_doc_writer.md
  - p02_ra_guide_writer.md
  - p02_ra_doc_validator.md
  - p12_ct_product_launch.md
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - crew-template-builder
  - bld_schema_crew_template
  - bld_instruction_crew_template
density_score: 1.0
---

## Overview
Instantiate when CEXAI prepares an OSS release requiring onboarding docs for two audiences:
new users (quickstart_guide) and contributors (contributor_guide). Producer spans N01+N04+N05
across four sequential roles; consumer is the N05 release gate. Each role grounds on the prior
role's artifact via a2a Task handoff. Showcases CEXAI composable-crew with P12 primitives.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| researcher | p02_ra_repo_researcher.md | N01: scan repo, map user journeys + friction, produce research brief |
| doc_writer | p02_ra_doc_writer.md | N04: author quickstart_guide from research brief + repo structure |
| guide_writer | p02_ra_guide_writer.md | N04: author contributor_guide from research brief + contribution patterns |
| validator | p02_ra_doc_validator.md | N05: enforce quality gate + release checklist on both guides |

## Process
Topology: `sequential`. Rationale: doc_writer + guide_writer both require the research brief;
validator requires both completed guides. Sequential prevents tone drift and audience bleed.
Hierarchical or consensus adds overhead without quality gain for this linear pipeline.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| researcher | shared | persistent (research brief saved to P01 KC) |
| doc_writer | shared | per-crew-instance |
| guide_writer | shared | per-crew-instance |
| validator | shared | per-crew-instance + regression_check archive |

## Handoff Protocol
`a2a-task-sequential` -- each role emits a completion signal with `artifact_path` +
`quality_score`. Next role reads the upstream artifact before F1 CONSTRAIN.
Payload: `{role, artifact_path, quality_score, timestamp}`. No role starts without
a complete signal from its predecessor.

## Success Criteria
- [ ] All 4 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] quickstart_guide quality >= 9.0 (gate p11_qg_crew_template)
- [ ] contributor_guide quality >= 9.0 (gate p11_qg_crew_template)
- [ ] Validator signals release-gate PASS (cex_release_check.py exit 0)
- [ ] a2a handoff signals present for 4/4 roles
- [ ] No role produced output without reading upstream artifact

## Instantiation
```bash
python _tools/cex_crew.py run oss_onboarding --charter _showcase/crew1_oss_onboarding/team_charter_oss_onboarding.md --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_repo_researcher.md]] | upstream | 0.42 |
| [[p02_ra_doc_writer.md]] | upstream | 0.40 |
| [[p02_ra_guide_writer.md]] | upstream | 0.38 |
| [[p02_ra_doc_validator.md]] | upstream | 0.36 |
| [[p12_ct_product_launch.md]] | sibling | 0.34 |
| [[bld_collaboration_crew_template]] | related | 0.31 |
| [[bld_instruction_crew_template]] | upstream | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.27 |
| [[crew-template-builder]] | related | 0.25 |
| [[bld_schema_crew_template]] | upstream | 0.23 |
