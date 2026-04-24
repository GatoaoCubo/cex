---
id: p12_ct_release_gate.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: release_gate
purpose: Coordinate a 3-role sequential crew that validates a release through automated testing, security scanning, and final pass/fail verdict before any public push
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "test_runner -> security_scanner -> gate_keeper"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Release Gate Crew Template"
version: "1.0.0"
author: n05_operations
tags: [crew_template, release_gate, operations, composable, crewai, quality]
tldr: "3-role sequential crew: test suite -> security scan -> pass/fail verdict"
domain: "release validation orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_test_runner.md
  - p02_ra_security_scanner.md
  - p02_ra_gate_keeper.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p12_ct_incident_response.md
  - crew-template-builder
  - p11_qg_crew_template
  - p12_ct_product_launch.md
---

## Overview
Instantiate before any public release push to validate quality, security, and
compliance thresholds. Owner is N05 (operations); consumers are release engineers
and N07 orchestrator. Each role emits a discrete report consumed by the next.
Handoff is via a2a Task with artifact path attached.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| test_runner | p02_ra_test_runner.md | Runs doctor, flywheel audit, system tests; emits test results report |
| security_scanner | p02_ra_security_scanner.md | Checks secrets, dependencies, license compliance, OWASP; emits scan report |
| gate_keeper | p02_ra_gate_keeper.md | Aggregates upstream reports into final pass/fail release verdict |

## Process
Topology: `sequential`. Rationale: gate_keeper cannot issue a verdict without
both upstream reports. Sequential ordering gives a simpler signal contract;
gate_keeper never starts until both test_results.md and scan_report.md exist.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| test_runner | shared | per-crew-instance (test results consumed by gate_keeper) |
| security_scanner | shared | per-crew-instance (scan report consumed by gate_keeper) |
| gate_keeper | shared | persistent (release verdict saved to P08 decision record) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` + `quality_score`. The next role reads prior artifact before
starting its own F1 CONSTRAIN. Signal path: `.cex/runtime/signals/`.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] test_runner report: cex_doctor.py pass rate, flywheel audit score, system test count
- [ ] security_scanner report: 0 hardcoded secrets, 0 known-vulnerable deps, license matrix complete
- [ ] gate_keeper verdict: PASS or FAIL with explicit threshold citations from both reports
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No role produced an artifact without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run release_gate \
    --charter N05_operations/P12_orchestration/crews/team_charter_release_default.md

python _tools/cex_crew.py run release_gate \
    --charter N05_operations/P12_orchestration/crews/team_charter_release_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_test_runner.md]] | upstream | 0.48 |
| [[p02_ra_security_scanner.md]] | upstream | 0.46 |
| [[p02_ra_gate_keeper.md]] | upstream | 0.44 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_collaboration_crew_template]] | related | 0.30 |
| [[p12_ct_incident_response.md]] | sibling | 0.28 |
| [[crew-template-builder]] | related | 0.26 |
| [[p11_qg_crew_template]] | upstream | 0.24 |
| [[p12_ct_product_launch.md]] | sibling | 0.22 |
