---
kind: quality_gate
id: p11_qg_hook_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of hook_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: hook_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, hook-config, P04]
tldr: "Pass/fail gate for hook_config artifacts: required fields, id pattern, body sections, hook declaration completeness."
domain: "hook lifecycle configuration for builder execution"
created: "2026-03-31"
updated: "2026-03-31"
density_score: 0.90
related:
  - bld_examples_hook_config
  - bld_instruction_hook_config
  - p03_sp_hook_config_builder
  - bld_collaboration_hook_config
  - hook-config-builder
  - bld_knowledge_card_hook_config
  - p10_lr_hook_config_builder
  - p01_kc_hook_config
  - bld_architecture_hook_config
  - p11_qg_memory_scope
---

## Quality Gate

# Gate: hook_config
## Definition
| Field | Value |
|---|---|
| metric | hook_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: hook_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_hookconf_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `hook_config` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Hooks or ## Lifecycle or ## Integration |
| H08 | Body <= 4096 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Hook completeness | 1.0 | All hooks have phase, event, action, condition (no placeholders) |
| Condition quality | 1.0 | Each hook condition is specific and testsble |
| Phase coverage | 1.0 | Hooks cover relevant 8F phases for the target builder |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "hook_config", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Hooks and events specific to declared target builder |
| Testability | 0.5 | Hook declarations can be validated with known inputs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
