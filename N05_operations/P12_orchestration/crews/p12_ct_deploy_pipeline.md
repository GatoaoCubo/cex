---
id: p12_ct_deploy_pipeline.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: deploy_pipeline
purpose: Coordinate a 3-role sequential crew that validates prerequisites, executes deployment, and verifies post-deploy health for any CEX release
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "pre_checker -> deployer -> smoke_tester"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Deploy Pipeline Crew Template"
version: "1.0.0"
author: n05_operations
tags: [crew_template, deploy_pipeline, operations, composable, crewai, deployment]
tldr: "3-role sequential crew: pre-deploy check -> execute deploy -> smoke test verification"
domain: "deployment validation orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_pre_checker.md
  - p02_ra_deployer.md
  - p02_ra_smoke_tester.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p12_ct_incident_response.md
  - p12_ct_release_gate.md
  - p12_ct_quality_sweep.md
  - crew-template-builder
  - p11_qg_crew_template
---

## Overview
Instantiate before any CEX release to validate prerequisites, execute the
deployment, and verify post-deploy health. Owner is N05 (operations); consumers
are release engineers, N07 orchestrator, and the incident response crew (if
deploy fails). Each role emits a discrete artifact consumed by the next; no role
begins without reading the upstream output. Handoff is via a2a Task with
artifact path attached. The deployer has an ABORT gate: if pre_checker reports
BLOCKED, the pipeline halts without deploying.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| pre_checker | p02_ra_pre_checker.md | Validates env vars, deps, configs, tool health; emits pre-deploy report |
| deployer | p02_ra_deployer.md | Compiles, commits, pushes, triggers deploy; emits deploy log |
| smoke_tester | p02_ra_smoke_tester.md | Runs post-deploy health checks and smoke tests; emits deploy verdict |

## Process
Topology: `sequential`. Rationale: deployer must NOT deploy without pre_checker's
green light (BLOCKED verdict halts the pipeline). Smoke_tester must NOT run
until deployment is complete (needs the live environment). Parallel would risk
deploying without validation or testing a stale environment.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| pre_checker | shared | per-crew-instance (pre-deploy report consumed by deployer) |
| deployer | shared | per-crew-instance (deploy log consumed by smoke_tester) |
| smoke_tester | shared | persistent (deploy verdict saved for deploy history) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` + `quality_score`. The next role reads prior artifact before
starting its own F1 CONSTRAIN. Signal path: `.cex/runtime/signals/`.

## Abort Protocol
If pre_checker verdict is BLOCKED:
1. Deployer reads pre_deploy_report and finds BLOCKED verdict
2. Deployer emits an abort_report.md (not deploy_log.md) listing all FAIL items
3. Smoke_tester reads abort and emits SKIPPED verdict
4. Pipeline terminates with ABORT status (no deployment occurred)

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] pre_checker report: release_check + setup_validator + sanitize results, per-item PASS/FAIL
- [ ] deployer log: compile results, doctor check, commit SHA, deploy timestamp, changed files
- [ ] smoke_tester verdict: HEALTHY (all endpoints 200, smoke tests pass) or UNHEALTHY with evidence
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No role produced an artifact without reading upstream output
- [ ] If BLOCKED: deployer emits abort, smoke_tester emits SKIPPED (no deployment occurs)

## Instantiation
```bash
python _tools/cex_crew.py run deploy_pipeline \
    --charter N05_operations/P12_orchestration/crews/team_charter_deploy_default.md

python _tools/cex_crew.py run deploy_pipeline \
    --charter N05_operations/P12_orchestration/crews/team_charter_deploy_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_pre_checker.md]] | upstream | 0.48 |
| [[p02_ra_deployer.md]] | upstream | 0.46 |
| [[p02_ra_smoke_tester.md]] | upstream | 0.44 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_collaboration_crew_template]] | related | 0.30 |
| [[p12_ct_incident_response.md]] | sibling | 0.28 |
| [[p12_ct_release_gate.md]] | sibling | 0.26 |
| [[p12_ct_quality_sweep.md]] | sibling | 0.24 |
| [[crew-template-builder]] | related | 0.22 |
| [[p11_qg_crew_template]] | upstream | 0.20 |
