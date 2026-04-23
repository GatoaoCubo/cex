---
quality: 8.4
quality: 7.9
id: p11_ins_curation_nudge
kind: instruction
pillar: P11
llm_function: REASON
purpose: Step-by-step build instructions for curation_nudge
title: "Instructions: Curation Nudge Builder"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [instruction, curation_nudge, builder, memory, hermes, proactive]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
idempotent: true
atomic: false
rollback: "Delete produced nudge file. No downstream effects until embedded in an agent session config."
related:
  - bld_collaboration_memory_type
  - bld_collaboration_memory_scope
  - bld_manifest_memory_type
  - p03_ins_quality_gate
  - p01_kc_memory_scope
  - p03_ins_prompt_template
  - p03_ins_prompt_compiler
  - memory-summary-builder
  - bld_config_memory_type
  - bld_knowledge_card_memory_scope
---

## Context
A `curation_nudge` configures when an AI agent should prompt itself to persist observed
knowledge to durable memory. It answers: "after how many turns (or fact observations, or
tool calls) should I ask myself: should I save this to MEMORY.md?"

**Inputs**

| Field | Type | Description |
|-------|------|-------------|
| `trigger_type` | enum | turn_count \| density_threshold \| tool_call_count \| user_correction |
| `threshold` | int | Count at which nudge fires (default: 10, minimum: 5) |
| `destination` | enum | MEMORY.md \| entity_memory \| knowledge_card |
| `max_per_session` | int | Hard session cap on nudge frequency (default: 3) |
| `min_interval_turns` | int | Anti-spam minimum gap between nudges (default: 5) |

**Output**
A single `.md` file (compiled to `.yaml`) with YAML frontmatter + body containing:
trigger table, prompt template, target memory config, boundary rules, and usage block.

**Boundary rules**
- curation_nudge = proactive in-session ASKING prompt to persist knowledge (this builder)
- guardrail = BLOCKS an action before it happens (different builder, different semantics)
- quality_gate = single pass/fail check on an artifact score (different builder)
- notifier = external broadcast to Slack/email/webhook (different builder, different pillar P04)
- memory_summary = compresses accumulated context (different builder, P10)

## Phase 1: Classify -- Boundary Check
```
IF caller wants to BLOCK an agent action:
  RETURN "Route to guardrail-builder -- handles safety restrictions."
IF caller wants a pass/fail quality check:
  RETURN "Route to quality-gate-builder -- handles single-check quality barriers."
IF caller wants to broadcast to external channels:
  RETURN "Route to notifier-builder -- handles external system notifications."
IF caller wants to compress accumulated memory:
  RETURN "Route to memory-summary-builder -- handles context compression."
IF caller wants proactive in-session memory persistence prompts:
  PROCEED as curation_nudge
```
Deliverable: confirmed `kind: curation_nudge` with one-line justification.

## Phase 2: Research -- Parameter Resolution
```
RESOLVE trigger_type:
  IF user mentions "turns" or "every N turns": use turn_count
  IF user mentions "information", "facts", "density": use density_threshold
  IF user mentions "tool calls", "file reads": use tool_call_count
  IF user mentions "corrections", "contradictions", "user changed mind": use user_correction
  DEFAULT: turn_count (most universal)

RESOLVE threshold:
  IF unspecified: default to 10
  ENFORCE minimum: 5 (below 5 causes excessive nudge spam)
  IF user_correction trigger: threshold = 1 (fire on every correction)

RESOLVE destination:
  IF user mentions "MEMORY.md": use MEMORY.md
  IF user mentions "entity", "person", "object": use entity_memory
  IF user mentions "knowledge card", "document": use knowledge_card
  DEFAULT: MEMORY.md (most common CEX sink)

RESOLVE cadence:
  min_interval_turns: default 5 (anti-spam)
  max_per_session: default 3 (prevents context saturation)
```
Deliverable: resolved parameter set ready for frontmatter.

## Phase 3: Compose -- Build the Nudge
```
ID generation:
  id = "cn_" + trigger_type_slug
  filename = "p11_cn_" + trigger_type_slug + ".yaml"

Frontmatter (required fields):
  id, kind (= curation_nudge), pillar (= P11), title,
  trigger.type, trigger.threshold,
  cadence.min_interval_turns, cadence.max_per_session,
  prompt_template (must contain {{observation}}),
  target_memory.destination, target_memory.auto_write_if_confirmed,
  version (= 1.0.0), quality (= null), tags

prompt_template MUST contain:
  {{observation}} -- runtime-substituted observation text

Body structure:
  ## Nudge: {{trigger}}
  ### Trigger Configuration (table: parameter | value | notes)
  ### Prompt Template (code block with template text)
  ### Target Memory (table: field | value | description)
  ### Boundaries (NOT table -- 4 items minimum)
  ### Usage in agent session (code block)
```
Deliverable: complete `.md` file with frontmatter + 5 body sections.

## Phase 4: Validate -- Gate the Nudge
```
HARD gates (block if any fail):
  H01: kind == "curation_nudge"
  H02: trigger.threshold >= 5 (positive integer)
  H03: trigger.type in {turn_count, density_threshold, tool_call_count, user_correction}
  H04: target_memory.destination in {MEMORY.md, entity_memory, knowledge_card}
  H05: prompt_template contains "{{observation}}"
  H06: quality == null

SOFT gates (score contribution):
  S01: Boundaries section present with all 4 NOT-items (0.25)
  S02: cadence.min_interval_turns >= 5 AND cadence.max_per_session <= 5 (0.25)
  S03: Usage in agent session code block present (0.25)
  S04: tags include hermes_origin (0.25)
```
Deliverable: PASS/FAIL on all HARD gates. Score on SOFT gates.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_type]] | downstream | 0.31 |
| [[bld_collaboration_memory_scope]] | downstream | 0.29 |
| [[bld_manifest_memory_type]] | upstream | 0.28 |
| [[p03_ins_quality_gate]] | sibling | 0.26 |
| [[p01_kc_memory_scope]] | upstream | 0.25 |
| [[p03_ins_prompt_template]] | sibling | 0.24 |
| [[p03_ins_prompt_compiler]] | sibling | 0.23 |
| [[memory-summary-builder]] | upstream | 0.23 |
| [[bld_config_memory_type]] | upstream | 0.23 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.23 |
