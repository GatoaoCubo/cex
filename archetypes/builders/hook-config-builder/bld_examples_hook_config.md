---
kind: examples
id: bld_examples_hook_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of hook_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: hook-config-builder
## Golden Example
INPUT: "Create hook config for agent-builder 8F pipeline"
OUTPUT:
```yaml
id: p04_hookconf_agent_builder
kind: hook_config
pillar: P04
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "builder_agent"
name: "Agent Builder Hook Lifecycle"
target_builder: "agent-builder"
phases: [F1_CONSTRAIN, F6_PRODUCE, F7_GOVERN, F8_COLLABORATE]
quality: 8.8
tags: [hook_config, P04, agent-builder]
tldr: "Hook lifecycle for agent-builder — pre-build validation, post-produce compile, quality-fail retry, post-commit signal"
```
## Overview
Hook lifecycle configuration for agent-builder. Declares four hooks across the 8F pipeline:
pre-build schema validation, post-produce compilation, quality-fail retry, and post-commit signaling.

## Hooks
| Phase | Event | Action | Condition |
|-------|-------|--------|-----------|
| F1_CONSTRAIN | pre-build | validate_schema | always |
| F6_PRODUCE | post-produce | compile_yaml | always |
| F7_GOVERN | quality-fail | retry_with_feedback | score < 8.0 |
| F8_COLLABORATE | post-commit | emit_signal | always |

## Lifecycle
Execution order: hooks fire in phase order (F1 -> F8). Within a phase, hooks fire in declaration order.
On error: quality-fail hooks retry up to 2 times. Other hook failures halt the pipeline.
Priority: first-declared wins when multiple hooks bind the same event.

## Integration
- Input: builder pipeline phase transitions from 8F runner
- Output: event triggers consumed by hook implementations
- Pairs with: hook (implementation), quality_gate (scoring), lifecycle_rule (archive/promote)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_hookconf_ pattern (H02 pass)
- kind: hook_config (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Hooks, Lifecycle, Integration (H07 pass)
- Hooks table with phase, event, action, condition (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "hook_config" (S02 pass)
## Anti-Example
INPUT: "Create hook config for validator"
BAD OUTPUT:
```yaml
id: validator-hooks
kind: hook
quality: 8.5
tags: [hooks]
```
FAILURES:
1. id has hyphens and no p04_hookconf_ prefix -> H02 FAIL
2. kind: 'hook' not 'hook_config' -> H04 FAIL
3. Missing fields: target_builder, phases -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. No ## Hooks section in body -> H07 FAIL
6. No hooks declaration table -> S03 FAIL
