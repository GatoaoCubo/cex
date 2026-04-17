---
kind: instruction
id: bld_instruction_state_machine
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for state_machine
pattern: 3-phase pipeline (define -> compose -> validate)
quality: null
title: "Instruction State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, instruction]
tldr: "3-phase: enumerate states and events, define transitions with guards/actions, validate determinism and completeness."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce a state_machine

## Phase 1: DEFINE

1. Identify the entity whose lifecycle this machine governs
2. Enumerate all states the entity can be in (initial, intermediate, final)
3. Identify the initial state (only one)
4. Identify all final states (terminal states with no outgoing transitions)
5. For each state pair: what events can trigger a transition between them?
6. For each transition: are there conditions (guards) that must be true?
7. For each transition: are there side-effects (actions) to execute?
8. For each state: are there entry or exit actions?
9. Verify determinism: no two transitions have the same (from_state, event) pair without guards
10. Count states and transitions for frontmatter fields

## Phase 2: COMPOSE

1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p12_sm_{entity_slug}` -- verify pattern `^p12_sm_[a-z][a-z0-9_]+$`
4. Set entity, initial_state, final_states, states_count, transitions_count
5. Write States section: table with state name, type (initial/intermediate/final), description
6. Write Transitions section: full table with from, event, to, guard, action
7. Write Guards section: define each guard condition as a boolean expression
8. Write Actions section: define each action with its trigger and effect
9. Verify body <= 4096 bytes

## Phase 3: VALIDATE

1. Confirm id matches `^p12_sm_[a-z][a-z0-9_]+$`
2. Confirm kind == state_machine
3. Confirm initial_state is in states list
4. Confirm all final_states are in states list
5. Confirm states_count matches states table row count
6. Confirm transitions_count matches transitions table row count
7. Check determinism: no (from_state, event) appears twice without guards
8. Confirm all 4 sections present: States, Transitions, Guards, Actions
9. Cross-check: not workflow (no DAG), not process_manager (no event orchestration)
10. Confirm quality: null
11. Revise if score < 8.0
