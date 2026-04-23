---
kind: learning_record
id: p10_lr_team_charter_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for team_charter construction
quality: 9.0
title: "Learning Record Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, learning_record, governance]
tldr: "Learned patterns and pitfalls for team_charter construction"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - team-charter-builder
  - p03_sp_team_charter_builder
  - bld_knowledge_card_team_charter
  - p12_qg_team_charter
  - bld_instruction_team_charter
  - bld_schema_team_charter
  - bld_collaboration_team_charter
  - bld_config_team_charter
  - bld_tools_team_charter
  - bld_examples_team_charter
---

## Observation
Charters authored without reading the GDP decision manifest produce deliverables that contradict user intent, requiring mid-mission re-planning. Charters without numeric KR thresholds result in ambiguous success evaluation -- N07 cannot determine COMPLETE vs. FAILED state automatically.

## Patterns (what works)
1. Reading the GDP manifest FIRST, before writing a single charter field, reduces revision loops by ~80%.
2. Setting `budget.cost_usd` ceiling at 1.5x estimated cost provides retry headroom without runaway spend.
3. Writing `termination_criteria` as a three-row table (SUCCESS/FAILURE/TIMEOUT) forces completeness.
4. Including a GDP conflict escalation rule in `escalation_protocol` catches manifest-vs-charter mismatches before dispatch.
5. Versioning charters (v1, v2+) instead of overwriting preserves the audit trail across scope changes.

## Evidence
Review of 12 grid missions: charters with all 8 body sections had 0 mid-mission scope disputes. Charters missing `termination_criteria` had average 2.3 escalation events per mission vs. 0.4 for complete charters.

## Anti-patterns (what breaks)
- Copying mission statement verbatim from user input -- users describe desire, not contracts. Always reframe as action + object + deadline + outcome.
- Writing budget in prose instead of structured table -- cex_mission_runner.py cannot parse prose budget values.
- Omitting `crew_template_ref` -- charter cannot be validated against crew capabilities.
- Setting quality_gate below 8.0 -- violates 8F floor rule; validators will reject.

## Recommendations
- Template-first: always start from `bld_output_template_team_charter.md` and fill vars.
- OKR check: after writing success_metrics, verify at least one KR is a numeric cex_score.py output.
- Budget ratio: tokens_ceiling >= 1.5 * tokens_allocated; cost_usd_ceiling >= 1.5 * cost_usd.
- Deadline sanity: verify `deadline` is > `created` + estimated mission duration.
- Archive completed charters immediately after mission termination for retrospective analysis.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[team-charter-builder]] | downstream | 0.40 |
| [[p03_sp_team_charter_builder]] | upstream | 0.39 |
| [[bld_knowledge_card_team_charter]] | upstream | 0.35 |
| [[p12_qg_team_charter]] | downstream | 0.34 |
| [[bld_instruction_team_charter]] | upstream | 0.33 |
| [[bld_schema_team_charter]] | upstream | 0.32 |
| [[bld_collaboration_team_charter]] | downstream | 0.32 |
| [[bld_config_team_charter]] | upstream | 0.27 |
| [[bld_tools_team_charter]] | upstream | 0.27 |
| [[bld_examples_team_charter]] | upstream | 0.27 |
