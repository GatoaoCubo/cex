---
id: p12_tc_incident_default.md
kind: team_charter
8f: F8_collaborate
pillar: P12
llm_function: GOVERN
charter_id: incident_default
crew_template_ref: p12_ct_incident_response.md
mission_statement: "Detect, contain, analyze, and document a production incident using the 4-role sequential crew with full knowledge persistence."
quality_gate: 8.5
deadline: "dynamic -- set at instantiation time; P0 default: now + 2h"
deliverables:
  - "Triage brief (triage_brief.md) -- severity P0-P3, affected services, impact estimate"
  - "Remediation log (remediation_log.md) -- action timeline, fix applied, restoration confirmed"
  - "RCA report (rca_report.md) -- root cause, contributing factors, corrective actions"
  - "Incident report (incident_report.md) -- executive summary, timeline, actions; persisted to P08"
  - "Runbook update -- affected service runbook patched with new remediation step"
  - "Regression check (p11_rc_*.md) -- recurrence prevention artifact"
budget:
  tokens: 80000
  wall_clock_seconds: 7200
  usd: 3.00
stakeholders: ["n05_operations", "n07_orchestrator", "on_call_engineer"]
escalation_protocol: "If any role crosses budget ceiling or fails 3 consecutive attempts, emit signal_{role}_escalate.json to .cex/runtime/signals/. n07 reads and either extends budget or pages human SRE."
termination_criteria: "ANY of: (1) reporter signals crew-complete; (2) budget exhausted; (3) deadline passed; (4) 3 consecutive failures on same artifact (stuck loop)."
quality: null
density_score: null
title: "Team Charter -- Incident Response Default"
version: "1.0.0"
tags: [team_charter, incident_response, operations, default]
tldr: "Default mission contract for incident_response crew: 4 deliverables, 8.5 quality gate, 2h wall-clock."
domain: "production incident governance"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p12_ct_incident_response.md
  - p02_ra_detector.md
  - p02_ra_responder.md
  - p02_ra_analyst.md
  - p02_ra_reporter.md
  - bld_examples_team_charter
  - team-charter-builder
  - p01_kc_token_budgeting
  - bld_collaboration_cost_budget
  - p11_qg_crew_template
---

## Mission Statement
Detect, contain, analyze, and document a production incident using the 4-role sequential
crew. Each role produces a discrete artifact; the crew completes when the reporter signals
all 6 deliverables committed and quality >= 8.5.

## Deliverables
1. **Triage brief** -- severity level (P0-P3), affected services, user impact estimate, first-seen timestamp
2. **Remediation log** -- every action taken with timestamps, fix applied, restoration confirmed
3. **RCA report** -- root cause (system property level), >= 2 contributing factors, >= 2 corrective actions
4. **Incident report** -- executive summary, full timeline, impact, RCA summary, action items
5. **Runbook update** -- affected service runbook patched in P08 architecture
6. **Regression check** -- p11_rc_*.md artifact for recurrence prevention

## Success Metrics
- All 6 deliverables exist and committed before termination
- incident_report.md quality >= 8.5 (reporter-attested)
- RCA identifies root cause at system-property level (not "human error")
- Wall-clock within budget for given severity (P0: 2h, P1: 4h, P2: 8h, P3: 48h)
- All 4 a2a-task handoff signals present in `.cex/runtime/signals/`

## Budget
- Tokens: 80000 (hard ceiling; 20k per role)
- Wall-clock: 7200s default (P0 incidents may override to 3600s)
- USD: ~3.00 at Sonnet pricing

## Stakeholders
- `n05_operations` -- nucleus that owns the crew instance
- `n07_orchestrator` -- dispatches, monitors, and consolidates
- `on_call_engineer` -- human escalation target for P0/P1 incidents

## Escalation Protocol
If any role crosses its token ceiling or fails 3 consecutive attempts, emit
`signal_{role}_escalate.json` to `.cex/runtime/signals/`. N07 reads and either
extends the budget (if incident is P0/P1) or pages the on-call engineer.

## Termination Criteria
ANY of:
1. Reporter signals `crew-complete` with all 6 deliverables present
2. Token or wall-clock budget exhausted (emit partial-completion signal)
3. Deadline passed -- save work-in-progress artifacts before exit
4. 3 consecutive failures on the same artifact (stuck loop -- escalate immediately)

## Instantiation Override
Override this charter's fields at instantiation time:
```bash
python _tools/cex_crew.py run incident_response \
    --charter N05_operations/P12_orchestration/crews/team_charter_incident_default.md \
    --override deadline="2026-04-22T14:00:00Z" \
    --override budget.tokens=120000 \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_incident_response.md]] | upstream | 0.50 |
| [[p02_ra_detector.md]] | upstream | 0.35 |
| [[p02_ra_responder.md]] | upstream | 0.33 |
| [[p02_ra_analyst.md]] | upstream | 0.32 |
| [[p02_ra_reporter.md]] | upstream | 0.31 |
| [[bld_examples_team_charter]] | upstream | 0.25 |
| [[team-charter-builder]] | related | 0.22 |
| [[p01_kc_token_budgeting]] | upstream | 0.20 |
| [[bld_collaboration_cost_budget]] | related | 0.18 |
| [[p11_qg_crew_template]] | upstream | 0.15 |
