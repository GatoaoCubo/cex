---
id: p12_ct_incident_response.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: incident_response
purpose: Coordinate a 4-role sequential crew that detects, contains, analyzes, and documents production incidents end-to-end
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "detector -> responder -> analyst -> reporter"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Incident Response Crew Template"
version: "1.0.0"
author: n05_operations
tags: [crew_template, incident_response, operations, composable, crewai]
tldr: "4-role sequential crew: detect scope -> apply fix -> root cause -> incident report"
domain: "production incident management"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_detector.md
  - p02_ra_responder.md
  - p02_ra_analyst.md
  - p02_ra_reporter.md
  - team_charter_incident_default.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p12_ct_product_launch.md
  - crew-template-builder
  - p11_qg_crew_template
---

## Overview
Instantiate when a production incident requires structured triage, containment,
root-cause analysis, and documentation. Owner is N05 (operations); consumers are
on-call engineers, SRE leads, and the post-incident review process. Each role
emits a discrete artifact consumed by the next; no role begins without reading
the upstream output. Handoff is via a2a Task with artifact path attached.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| detector | p02_ra_detector.md | Scans logs/metrics, triages severity, scopes impact |
| responder | p02_ra_responder.md | Applies fix, validates resolution, documents actions taken |
| analyst | p02_ra_analyst.md | Root cause analysis, identifies systemic patterns, failure modes |
| reporter | p02_ra_reporter.md | Writes incident report, updates runbooks, creates regression checks |

## Process
Topology: `sequential`. Rationale: each role strictly depends on the previous
artifact. Responder needs detector's triage brief; analyst needs responder's
remediation log; reporter needs analyst's RCA. Parallelism introduces
consistency risk (responder must not guess scope; analyst must not fabricate
timeline from scratch).

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| detector | shared | per-crew-instance (triage brief consumed by all downstream) |
| responder | shared | per-crew-instance (remediation log consumed by analyst) |
| analyst | shared | persistent (RCA persists to P01 knowledge base) |
| reporter | shared | persistent (incident report + runbook updates persist cross-session) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` + `quality_score`. The next role reads prior artifact before
starting its own F1 CONSTRAIN. Signal path: `.cex/runtime/signals/`.

## Success Criteria
- [ ] All 4 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] detector triage brief includes severity level (P0/P1/P2/P3) and impact scope
- [ ] responder log documents every action taken with timestamps
- [ ] analyst RCA identifies at least 1 contributing factor and 1 systemic pattern
- [ ] reporter artifact: incident report saved to P08, runbook updated, regression_check created
- [ ] Handoff protocol signals present for 4/4 roles
- [ ] No role produced an artifact without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run incident_response \
    --charter N05_operations/P12_orchestration/crews/team_charter_incident_default.md

python _tools/cex_crew.py run incident_response \
    --charter N05_operations/P12_orchestration/crews/team_charter_incident_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_detector.md]] | upstream | 0.45 |
| [[p02_ra_responder.md]] | upstream | 0.43 |
| [[p02_ra_analyst.md]] | upstream | 0.41 |
| [[p02_ra_reporter.md]] | upstream | 0.40 |
| [[team_charter_incident_default.md]] | downstream | 0.35 |
| [[bld_instruction_crew_template]] | upstream | 0.30 |
| [[bld_collaboration_crew_template]] | related | 0.28 |
| [[p12_ct_product_launch.md]] | sibling | 0.26 |
| [[crew-template-builder]] | related | 0.25 |
| [[p11_qg_crew_template]] | upstream | 0.22 |
