---
quality: 8.4
quality: 8.0
kind: config
id: bld_config_state_machine
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
title: "Config State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, config]
tldr: "Naming: p12_sm_{entity}.md. States in UPPER_SNAKE_CASE. Events in UPPER_SNAKE_CASE. Guards as boolean expressions."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_memory_runtime_state
  - bld_schema_lifecycle_rule
  - bld_schema_runtime_state
  - p03_ins_lifecycle_rule
  - p03_sp_lifecycle_rule_builder
  - bld_memory_action_paradigm
  - runtime-state-builder
  - p11_qg_runtime_state
  - bld_memory_lifecycle_rule
  - p11_qg_lifecycle_rule
---

# Config: state_machine Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p12_sm_{entity_slug}.md` | `p12_sm_order_lifecycle.md` |
| Builder directory | kebab-case | `state-machine-builder/` |
| State names | UPPER_SNAKE_CASE | `DRAFT`, `SUBMITTED`, `FULFILLING` |
| Event names | UPPER_SNAKE_CASE | `SUBMIT`, `PAYMENT_CONFIRMED`, `CANCEL` |
| Guard names | camelCase() with parens | `hasItems()`, `allItemsPacked()` |
| Action names | camelCase() with parens | `reserveInventory()`, `sendConfirmation()` |
| Entity slug | snake_case, lowercase | `order_lifecycle`, `agent_session` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths

- Output: `N0X_{domain}/P12_orchestration/p12_sm_{entity_slug}.md`
- Compiled: `N0X_{domain}/P12_orchestration/compiled/p12_sm_{entity_slug}.yaml`

## Size Limits

- Body: max 4096 bytes
- Density: >= 0.80 (tables > prose)

## Determinism Rule

| Situation | Requirement |
|-----------|-------------|
| Two transitions from same state on same event | HARD FAIL -- ambiguous |
| Two transitions from same state on same event with different guards | ALLOWED if guards are mutually exclusive |
| Transition without guard | Executes whenever event occurs in from_state |
| Missing final state | WARN -- entity lifecycle never terminates |

## State Count Guidelines

| Entity Complexity | Typical States | Max Recommended |
|------------------|---------------|-----------------|
| Simple (toggle) | 2-3 | 5 |
| Standard (lifecycle) | 5-8 | 10 |
| Complex (multi-phase) | 8-15 | 20 |
| > 20 states | Refactor into sub-machines | -- |

## Guard Expression Formats

| Format | Example | Use When |
|--------|---------|----------|
| Method call | `hasItems()` | Business logic in entity |
| Field check | `order.status == 'paid'` | Simple field comparison |
| Compound | `isAdmin() AND hasItems()` | Multiple conditions |
| Negation | `!isSuspended()` | Exclude condition |

## Action Classification

| Action Type | Trigger | Example |
|-------------|---------|---------|
| Entry action | On state entry | sendWelcomeEmail() on ACTIVE entry |
| Exit action | On state exit | stopTimer() on ACTIVE exit |
| Transition action | On specific transition | refundPayment() on PAID -> CANCELLED |
| Guard-conditional | Only when guard passes | reserveInventory() if hasStock() |

## State Table Required Columns

| Column | Format | Required |
|--------|--------|----------|
| state | UPPER_SNAKE_CASE | YES |
| type | initial / normal / final | YES |
| description | one-line business meaning | YES |

## Common Config Mistakes

| Mistake | Consequence | Correct Behavior |
|---------|-------------|-----------------|
| No final states | Infinite lifecycle loops | Always declare TERMINATED or COMPLETED |
| Guards as prose strings | Unimplementable spec | Define as boolean expressions |
| Non-deterministic (state, event) | Random runtime behavior | Add mutually exclusive guards |
| > 20 states | Unmaintainable spec | Refactor into sub-machines |
| state as workflow steps | Using FSM for sequences | Use workflow (DAG) for sequential steps |
| missing guards | Unguarded same-event | Add boolean guards for disambiguation |
| no outgoing transitions from final | Final states have zero exits? | Yes |
| events list | All events declared in frontmatter? | Yes |
| initial_state in states | Initial state is valid state? | Yes |
| final_states in states | All final states are valid states? | Yes |
| guard_exclusivity | Mutually exclusive guards verified? | Yes |
| action_type | Entry/exit/transition typed? | Yes |
| entity domain documented | Entity name + domain in frontmatter? | Yes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_runtime_state]] | downstream | 0.36 |
| [[bld_schema_lifecycle_rule]] | upstream | 0.32 |
| [[bld_schema_runtime_state]] | upstream | 0.32 |
| [[p03_ins_lifecycle_rule]] | upstream | 0.29 |
| [[p03_sp_lifecycle_rule_builder]] | upstream | 0.28 |
| [[bld_memory_action_paradigm]] | downstream | 0.28 |
| [[runtime-state-builder]] | downstream | 0.26 |
| [[p11_qg_runtime_state]] | downstream | 0.26 |
| [[bld_memory_lifecycle_rule]] | downstream | 0.26 |
| [[p11_qg_lifecycle_rule]] | downstream | 0.25 |
