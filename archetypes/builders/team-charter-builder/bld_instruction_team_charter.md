---
kind: instruction
id: bld_instruction_team_charter
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for team_charter
quality: 8.9
title: "Instruction Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, instruction, governance]
tldr: "Step-by-step production process for team_charter"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Read the GDP decision manifest at `.cex/runtime/decisions/decision_manifest.yaml` to extract user's WHAT decisions.
2. Load the referenced `crew_template_ref` to understand the crew's capability profile.
3. Identify all stakeholders from the mission context (user, nuclei, external systems).
4. Survey existing charters in `N06_commercial/` and `P12_*/` for reuse patterns.
5. Extract budget constraints: token budget from context_window_config, time from schedule, cost from commercial targets.
6. Map deliverables to nucleus capabilities (N01-N06 routing table).

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (charter_id, crew_template_ref, mission_statement, deliverables, etc.).
2. Write `mission_statement` as a single sentence: "This crew will [ACTION] [OBJECT] by [DEADLINE] to achieve [OUTCOME]."
3. Define `deliverables` as a numbered list with artifact kinds and pillar paths.
4. Translate GDP decisions into `success_metrics` using OKR format (Objective + 3 Key Results).
5. Set `budget` as three sub-fields: tokens (integer), time_hours (float), cost_usd (float).
6. Set `deadline` as ISO 8601 datetime.
7. List `stakeholders` as RACI table (Responsible, Accountable, Consulted, Informed).
8. Define `quality_gate` referencing the 8F floor (8.0) and target (9.0).
9. Write `escalation_protocol` as IF-THEN rules (e.g., IF score < 8.0 THEN escalate to N07).
10. Write `termination_criteria` as three conditions: success, failure, timeout.

## Phase 3: VALIDATE
- [ ] charter_id present and unique (pattern: `p12_tc_{{mission}}_v{{n}}`).
- [ ] crew_template_ref resolves to an existing template file.
- [ ] mission_statement is one sentence, action-oriented, includes deadline.
- [ ] deliverables list has at least one entry with kind and path.
- [ ] success_metrics follow OKR format (1 Objective + >= 2 Key Results).
- [ ] budget fields all present: tokens, time_hours, cost_usd.
- [ ] deadline is valid ISO 8601 datetime.
- [ ] stakeholders table includes all four RACI roles.
- [ ] quality_gate references 8F thresholds.
- [ ] escalation_protocol has at least one IF-THEN rule.
- [ ] termination_criteria covers success, failure, and timeout.
