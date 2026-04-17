---
id: p11_qg_state_machine
kind: quality_gate
pillar: P11
title: "Gate: state_machine"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
domain: "state machine -- formal FSM for entity lifecycle"
quality: null
tags: [quality-gate, state-machine, P12, fsm, entity-lifecycle]
tldr: "Pass/fail gate for state_machine: id pattern, initial/final states, determinism, transitions completeness, all 4 sections."
density_score: 0.90
llm_function: GOVERN
---

# Gate: state_machine

## Definition

| Field | Value |
|---|---|
| metric | state_machine artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: state_machine` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p12_sm_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p12_sm_foo but file is p12_sm_bar.md |
| H04 | Kind equals literal `state_machine` | kind: fsm or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | initial_state is in states list | initial_state refers to undeclared state |
| H07 | All final_states are in states list | final_state refers to undeclared state |
| H08 | states_count matches body count | Declared 7 but listed 5 |
| H09 | transitions_count matches body count | Declared 9 but listed 7 |
| H10 | Body has all 4 required sections | Missing States, Transitions, Guards, or Actions |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| State completeness | 1.0 | All meaningful lifecycle states documented |
| Transition completeness | 1.0 | All valid state changes covered |
| Guard implementability | 1.0 | All guards defined as boolean expressions |
| Action completeness | 1.0 | All side-effects defined with triggers and effects |
| Determinism | 1.0 | No ambiguous transitions without guards |
| Final state coverage | 1.0 | All entity termination paths have final states |
| Event naming | 0.5 | Events in UPPER_SNAKE_CASE |
| Boundary clarity | 1.0 | Explicitly NOT workflow (DAG), NOT process_manager |
| tldr quality | 0.5 | tldr includes entity name, state count, transition count |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
