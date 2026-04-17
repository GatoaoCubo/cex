---
kind: examples
id: bld_examples_working_memory
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of working_memory artifacts
quality: 8.2
title: "Examples Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, examples]
tldr: "Golden and anti-examples for working_memory construction."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

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
