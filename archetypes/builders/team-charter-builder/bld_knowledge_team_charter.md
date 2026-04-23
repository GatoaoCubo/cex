---
kind: knowledge_card
id: bld_knowledge_card_team_charter
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for team_charter production
quality: 9.2
title: "Knowledge Card Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, knowledge_card, governance, OKR, PMI, SLA]
tldr: "Domain knowledge for team_charter production"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - team-charter-builder
  - p03_sp_team_charter_builder
  - bld_collaboration_team_charter
  - bld_tools_team_charter
  - bld_schema_team_charter
  - kc_team_charter
  - p12_qg_team_charter
  - bld_examples_team_charter
  - bld_instruction_team_charter
  - p10_lr_team_charter_builder
---

## Domain Overview
A team_charter is the governance contract that authorizes an AI crew instance to execute a mission autonomously. It fuses three industry frameworks: the PMI Project Charter (scope, budget, stakeholders, authorization), the OKR framework (Objectives and Key Results for measurable outcomes), and the SLA contract (service-level commitments with escalation and termination clauses). In the CEX system, the charter specifically bridges GDP (Guided Decision Protocol) -- where the user decides WHAT -- to autonomous nucleus execution -- where the LLM decides HOW.

Every charter is instantiated from a `crew_template_ref`, which defines the crew's capability profile. The charter layer adds mission-specific values: the deliverables this crew will produce, the budget this mission is authorized to consume, and the conditions under which the mission terminates (success, failure, or timeout).

## Key Concepts
| Concept | Definition | Source |
|---------|------------|--------|
| Team Charter | Mission contract authorizing a crew instance to execute autonomously | PMI PMBOK 7th Ed |
| OKR | Objective + Key Results: qualitative goal + quantitative success signals | Google OKR Framework |
| SLA | Service Level Agreement: committed delivery standards + breach remediation | ITIL 4 Practice Guide |
| GDP | Guided Decision Protocol: user decides WHAT before LLM executes HOW | CEX guided-decisions.md |
| crew_template_ref | Pointer to the reusable crew definition this charter instantiates | CEX P12 taxonomy |
| RACI | Responsible/Accountable/Consulted/Informed matrix for stakeholder roles | PMI Responsibility Matrix |
| Termination Criteria | Explicit conditions that end the mission: SUCCESS, FAILURE, or TIMEOUT | SLA contract law |
| Escalation Protocol | IF-THEN rules that trigger human or N07 intervention | ITIL Incident Management |
| Budget (3-field) | tokens (LLM cost), time_hours (wall-clock), cost_usd (dollar spend) | CEX token_budget.py |
| quality_gate | Score thresholds enforced by the 8F F7 GOVERN step (floor 8.0, target 9.0) | CEX 8F pipeline |

## Industry Standards
- PMI PMBOK 7th Edition (project charter, RACI, scope management)
- Google OKR Framework (Objective + Key Results with numeric thresholds)
- ITIL 4 (SLA design, escalation management, incident response)
- ISO 31000:2018 (risk management -- escalation protocol design)
- OpenAPI SLA extension (machine-readable SLA format)
- A2A Protocol (agent-to-agent communication contracts, Google 2025)

## Common Patterns
1. Write `mission_statement` as: "This crew will [ACTION] [OBJECT] by [DEADLINE] to achieve [OUTCOME]."
2. Use three Key Results minimum: one quality score, one business metric, one process metric.
3. Set `budget.cost_usd` ceiling at 1.5x expected cost to allow retry headroom.
4. RACI: N07 is always Accountable; the user is always Informed and final Approver.
5. Escalation Protocol: always include a GDP conflict rule (IF manifest contradicts charter THEN halt + re-run GDP).
6. Termination TIMEOUT should be <= 90% of the deadline to allow consolidation time.

## Pitfalls
- Chartering a crew without a `crew_template_ref` -- the charter becomes a free-floating contract with no capability validation.
- Mission statements that describe HOW (implementation) instead of WHAT (outcome) -- conflates charter with handoff.
- OKRs without numeric thresholds -- N07 cannot algorithmically evaluate success.
- Missing timeout termination criteria -- crews run indefinitely on failures, burning budget.
- RACI without an Accountable role -- no one owns the mission outcome.
- Setting `deadline` in the past at charter creation time -- immediately triggers EXPIRED state.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[team-charter-builder]] | downstream | 0.58 |
| [[p03_sp_team_charter_builder]] | downstream | 0.51 |
| [[bld_collaboration_team_charter]] | downstream | 0.44 |
| [[bld_tools_team_charter]] | downstream | 0.43 |
| [[bld_schema_team_charter]] | downstream | 0.42 |
| [[kc_team_charter]] | sibling | 0.40 |
| [[p12_qg_team_charter]] | downstream | 0.40 |
| [[bld_examples_team_charter]] | downstream | 0.38 |
| [[bld_instruction_team_charter]] | downstream | 0.37 |
| [[p10_lr_team_charter_builder]] | downstream | 0.36 |
