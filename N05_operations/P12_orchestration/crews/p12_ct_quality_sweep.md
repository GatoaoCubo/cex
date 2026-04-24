---
id: p12_ct_quality_sweep.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: quality_sweep
purpose: Coordinate a 3-role sequential crew that scans, fixes, and validates artifact quality across the entire repository
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "scanner -> fixer -> quality_validator"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Quality Sweep Crew Template"
version: "1.0.0"
author: n05_operations
tags: [crew_template, quality_sweep, operations, composable, crewai, quality]
tldr: "3-role sequential crew: scan quality -> fix artifacts -> validate improvements"
domain: "batch quality improvement"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_scanner.md
  - p02_ra_fixer.md
  - p02_ra_quality_validator.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p12_ct_incident_response.md
  - p12_ct_release_gate.md
  - crew-template-builder
  - p11_qg_crew_template
---

## Overview
Instantiate when repository quality has drifted below target thresholds and batch
remediation is needed. Owner is N05 (operations); consumers are N07 orchestrator
and any nucleus whose artifacts were repaired. Each role emits a discrete artifact
consumed by the next; no role begins without reading the upstream output. Handoff
is via a2a Task with artifact path attached.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| scanner | p02_ra_scanner.md | Scans all artifacts for quality below threshold, categorizes failures, prioritizes fix order |
| fixer | p02_ra_fixer.md | Applies heuristic repairs to triaged artifacts, logs every change with before/after evidence |
| quality_validator | p02_ra_quality_validator.md | Re-scores fixed artifacts, detects regressions, emits final pass/fail verdict |

## Process
Topology: `sequential`. Rationale: fixer cannot repair without scanner's triage
list (needs to know WHAT is broken and WHY). Validator cannot verify without
fixer's change log (needs to know WHAT changed to check for regressions).
Parallel would risk the fixer guessing at failures or the validator missing changes.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| scanner | shared | per-crew-instance (triage list consumed by fixer and validator) |
| fixer | shared | per-crew-instance (fix log consumed by validator) |
| quality_validator | shared | persistent (quality verdict saved for trend tracking) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` + `quality_score`. The next role reads prior artifact before
starting its own F1 CONSTRAIN. Signal path: `.cex/runtime/signals/`.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] scanner triage includes: total scanned, total below threshold, categorized failure list
- [ ] fixer log includes: total attempted, total fixed, per-file before/after evidence
- [ ] validator verdict: PASS (aggregate delta > 0, 0 regressions) or FAIL with specifics
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No role produced an artifact without reading upstream output
- [ ] All fixed artifacts compile successfully via cex_compile.py

## Instantiation
```bash
python _tools/cex_crew.py run quality_sweep \
    --charter N05_operations/P12_orchestration/crews/team_charter_quality_sweep_default.md

python _tools/cex_crew.py run quality_sweep \
    --charter N05_operations/P12_orchestration/crews/team_charter_quality_sweep_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_scanner.md]] | upstream | 0.48 |
| [[p02_ra_fixer.md]] | upstream | 0.46 |
| [[p02_ra_quality_validator.md]] | upstream | 0.44 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_collaboration_crew_template]] | related | 0.30 |
| [[p12_ct_incident_response.md]] | sibling | 0.28 |
| [[p12_ct_release_gate.md]] | sibling | 0.26 |
| [[crew-template-builder]] | related | 0.24 |
| [[p11_qg_crew_template]] | upstream | 0.22 |
