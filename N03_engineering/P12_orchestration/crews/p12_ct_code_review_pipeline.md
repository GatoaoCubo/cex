---
id: p12_ct_code_review_pipeline.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: code_review_pipeline
purpose: "3-role sequential crew that performs comprehensive code and artifact review -- regression scan, security audit, and LLM-as-judge quality assessment"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "scanner -> security_auditor -> quality_judge"
handoff_protocol_id: a2a-task-sequential
quality: null
title: "Code Review Pipeline Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, code_review, engineering, security, quality_gate, composable, crewai]
tldr: "3-role sequential crew: regression scan -> security audit -> LLM-as-judge final score"
domain: "engineering code review"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_scanner.md
  - p02_ra_security_auditor.md
  - p02_ra_quality_judge.md
  - p12_ct_artifact_factory.md
  - bld_instruction_crew_template
  - p11_qg_crew_template
  - crew-template-builder
---

## Overview
Instantiate when a code change, PR diff, or artifact set requires a structured
3-phase review before merge or publication. Owner: N03 (engineering). Consumers:
N07 (consolidation gate) + N05 (CI/CD pipeline). Typical trigger: PR with
>3 files changed, schema-affecting artifact, or any change to P06/P09 configs.
Each role produces a structured report that the next role grounds on. Handoff
via a2a Task with `report_path` + `risk_level` + `quality_score`.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| scanner | p02_ra_scanner.md | Detect regressions, breaking changes, schema violations before deeper review |
| security_auditor | p02_ra_security_auditor.md | Assess vulnerabilities, injection risks, credential exposure on clean-scan input |
| quality_judge | p02_ra_quality_judge.md | LLM-as-judge final score and publish/reject decision grounded on both prior reports |

## Process
Topology: `sequential`. Rationale: strict dependency chain -- security_auditor
needs the regression report to scope its threat surface; quality_judge needs
both reports to produce a calibrated score. Running in parallel would force
each role to re-derive upstream context independently, tripling token spend
with no quality gain.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| scanner | shared | per-crew-instance (regression_check archive appended) |
| security_auditor | shared | per-crew-instance (threat model saved to P07) |
| quality_judge | shared | persistent (LLM-judge scores logged to P11 feedback) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal to
`.cex/runtime/signals/` with `report_path` + `risk_level` + `quality_score`
+ `role_name`. security_auditor reads scanner report before starting;
quality_judge reads both reports before issuing final verdict.

## Success Criteria
- [ ] scanner regression report exists with risk_level in {low, medium, high, critical}
- [ ] security_auditor threat report exists with vuln_count >= 0 and credential_exposure: false
- [ ] quality_judge score >= 8.0 (publish gate) or rejection with gate-specific fix list
- [ ] 3/3 a2a-task handoff signals present in `.cex/runtime/signals/`
- [ ] No role produced a report without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run code_review_pipeline \
    --charter N03_engineering/P12_orchestration/crews/team_charter_review.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_scanner.md]] | upstream | 0.60 |
| [[p02_ra_security_auditor.md]] | upstream | 0.58 |
| [[p02_ra_quality_judge.md]] | upstream | 0.55 |
| [[p12_ct_artifact_factory.md]] | sibling | 0.42 |
| [[bld_instruction_crew_template]] | upstream | 0.35 |
| [[p11_qg_crew_template]] | downstream | 0.30 |
| [[crew-template-builder]] | related | 0.27 |
