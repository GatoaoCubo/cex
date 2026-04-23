---
kind: quality_gate
id: p10_qg_working_memory
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of working_memory artifacts
quality: 8.8
title: "Gate: working_memory"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, working-memory, P10, short-term]
tldr: "Pass/fail gate for working_memory: task_id, typed slots, capacity_limit, expiry, clear policy."
domain: "working_memory -- short-term context store for a single active task, cleared after completion"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_chunk_strategy
  - p11_qg_constraint_spec
  - p11_qg_memory_scope
  - p11_qg_function_def
  - p11_qg_vision_tool
  - p11_qg_retriever_config
  - p11_qg_entity_memory
  - p11_qg_handoff_protocol
  - bld_examples_validator
  - p11_qg_effort_profile
---

## Quality Gate

# Gate: working_memory

## Definition
| Field | Value |
|---|---|
| metric | working_memory artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: working_memory` |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p10_wm_[a-z][a-z0-9_]+$` | Hyphens, uppercase, or missing prefix |
| H03 | ID equals filename stem | id vs filename mismatch |
| H04 | Kind equals literal `working_memory` | `kind: memory` or any other value |
| H05 | Quality field is null | Any non-null value |
| H06 | task_id declared and non-empty | Missing or empty task_id |
| H07 | context_slots has >= 1 typed slot | Empty map or untyped values |
| H08 | capacity_limit declared with numeric value and unit | Missing or non-numeric |
| H09 | expiry declared and non-empty | Missing expiry |
| H10 | clear_on_complete declared as clear or promote | Missing or invalid enum value |

## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Slot type completeness | 1.5 | All slots have declared types from valid enum |
| Capacity calibration | 1.0 | Capacity appropriate for task complexity |
| Expiry policy | 1.0 | TTL or trigger appropriate for task lifecycle |
| Clear policy quality | 1.0 | Promote declared with targets for research tasks |
| Slot count appropriateness | 0.5 | >= 3 slots for non-trivial tasks |
| Boundary clarity | 1.0 | Not session_state, not entity_memory, not episodic_memory |
| Nucleus binding | 0.5 | nucleus field declared |
| tldr quality | 0.5 | <= 160 chars, includes task and key slots |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Reference working memory spec |
| >= 8.0 | Publish | Ready for task dispatch integration |
| >= 7.0 | Review | Add slot types or expiry |
| < 7.0 | Reject | Return with gate failures |

## Examples

# Examples: working-memory-builder

## Golden Example
INPUT: "Create working memory for N04 knowledge card builder task"
OUTPUT:
```yaml
id: p10_wm_n04_kc_builder
kind: working_memory
pillar: P10
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
task_id: "n04_kc_build_{uuid}"
context_slots:
  current_phase: "string"
  target_kind: "string"
  sections_written: "int"
  accumulated_kc_body: "string"
  gate_checks_passed: "int"
  quality_score: "float"
  is_complete: "bool"
capacity_limit:
  value: 8000
  unit: tokens
expiry: "on_task_complete"
clear_on_complete: promote
promote_targets: [episodic_memory]
nucleus: "n04"
quality: null
tags: [working_memory, n04, knowledge_card_build, P10]
tldr: "Working memory for N04 knowledge card build: tracks phase, sections, quality, promotes episode on complete."
description: "Short-term task state for a single knowledge_card build cycle in N04 nucleus."
```
## Overview
Holds intermediate state for a single knowledge card build task in N04. Tracks current phase, target kind, body accumulation, and gate validation progress.

## Context Slots
| Slot Name | Type | Purpose | Example Value |
|-----------|------|---------|--------------|
| current_phase | string | Which 8F phase is active | "F6_PRODUCE" |
| sections_written | int | How many sections are complete | 3 |
| accumulated_kc_body | string | In-progress body text | "## Overview\n..." |
| quality_score | float | Running quality estimate | 8.5 |
| is_complete | bool | Task completion flag | false |

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p10_wm_` (H02 pass)
- task_id declared (H06 pass)
- context_slots: 7 typed slots (H07 pass)
- capacity_limit declared (H08 pass)
- expiry: on_task_complete (H09 pass)
- clear_on_complete + promote_targets (H10 pass)

## Anti-Example
BAD OUTPUT:
```yaml
id: task-memory
kind: memory
task: "build kc"
slots:
  data: anything
quality: 7.5
```
FAILURES:
1. id: "task-memory" has hyphen, no prefix -> H02 FAIL
2. kind: "memory" not "working_memory" -> H04 FAIL
3. quality: 7.5 (not null) -> H05 FAIL
4. task_id missing (task is not the same field) -> H06 FAIL
5. context_slots: "data: anything" -- no type annotation -> H07 SOFT FAIL
6. capacity_limit missing -> H08 FAIL
7. expiry missing -> H09 FAIL
8. clear_on_complete missing -> H10 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
