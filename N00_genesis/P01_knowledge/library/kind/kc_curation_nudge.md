---
quality: 8.0
quality: 7.6
id: kc_curation_nudge
kind: knowledge_card
pillar: P01
nucleus: n00
title: "KC: Curation Nudge"
version: 1.0
tags: [curation_nudge, p11, knowledge_card, hermes, memory, proactive]
density_score: 0.92
related:
  - bld_collaboration_agent
  - p01_kc_memory_scope
  - bld_knowledge_card_memory_scope
  - p01_kc_memory_persistence
  - p10_rs_conversation
  - bld_collaboration_memory_scope
  - agent_card_n04
  - bld_collaboration_memory_summary
  - ex_context_session_memory
  - bld_collaboration_memory_type
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder F4=plan F5=scan F6=produce F7=gate F8=save -->

## What is a curation_nudge?

A `curation_nudge` is a declarative configuration for proactive in-session memory-persistence
reminders. It tells an agent: "when you have observed X things (by turn count, density, or
tool-call count), ask yourself whether this observation should be persisted to durable memory."

**HERMES origin:** "Agent-curated memory with periodic nudges. Agent-curated facts written to
MEMORY.md with periodic nudges to persist durable knowledge." (NousResearch/hermes-agent)

## Why it exists

LLM agents lose knowledge at context boundaries. Without proactive nudging:
- A user preference observed in turn 5 is forgotten by turn 200
- Corrections given mid-session never reach MEMORY.md
- Cross-session learning degrades -- each session starts from zero

The nudge pattern solves this by inserting lightweight confirmatory prompts BEFORE
knowledge falls out of the active window.

## Trigger types

| Type | Fires When | Best For |
|------|-----------|---------|
| `turn_count` | Every N conversation turns | General sessions |
| `density_threshold` | Information density exceeds N new facts | Research-heavy sessions |
| `tool_call_count` | Every N tool calls | Coding / agentic sessions |
| `user_correction` | User contradicts agent's prior statement | Preference learning |

## Boundary table

| Kind | Pillar | What it does | How it differs from nudge |
|------|--------|--------------|--------------------------|
| `guardrail` | P11 | BLOCKS an action | Nudge ASKS; never blocks |
| `quality_gate` | P11 | PASS/FAIL check on an artifact | Nudge is informational |
| `notifier` | P04 | External broadcast (Slack, email) | Nudge is in-session only |
| `memory_summary` | P10 | Compresses accumulated knowledge | Nudge triggers the decision to persist |
| `entity_memory` | P10 | Stores discrete entities | Nudge feeds entity_memory as destination |
| `user_model` | P10 | Long-term user preference model (Honcho) | Nudge is the ingestion mechanism |

## Key fields explained

| Field | Type | Notes |
|-------|------|-------|
| `trigger.type` | enum | turn_count \| density_threshold \| tool_call_count \| user_correction |
| `trigger.threshold` | int | When to fire (default: 10) |
| `cadence.min_interval_turns` | int | Anti-spam: min turns between nudges |
| `cadence.max_per_session` | int | Hard session cap (default: 3) |
| `prompt_template` | string | Must contain `{{observation}}` placeholder |
| `target_memory.destination` | enum | MEMORY.md \| entity_memory \| knowledge_card |
| `target_memory.auto_write_if_confirmed` | bool | Persist immediately on agent confirmation |

## Naming convention
```
p11_cn_{{trigger}}.yaml
```
Examples: `p11_cn_turn_count.yaml`, `p11_cn_user_correction.yaml`

## Integration: where nudges fire in 8F

```
F3 INJECT (context assembly):
  Agent notes new facts while loading context

F4 REASON (planning):
  IF turn_count >= threshold: evaluate nudge
  ASK: "Notei {{observation}}. Persistir?"
  IF confirmed: write to target_memory.destination

F8 COLLABORATE (post-build):
  Nudge fires after artifact delivery
  Agent self-prompts: what from this session survives?
```

## Anti-patterns

- Using `curation_nudge` to BLOCK an action -- use `guardrail` instead
- Setting `max_per_session: 0` -- disables nudging entirely; use lifecycle_rule to suppress
- Using `trigger.threshold: 1` -- fires every turn; spams the agent; set min 5
- Omitting `{{observation}}` from prompt_template -- breaks runtime substitution (HARD gate H05)

## Builder
`archetypes/builders/curation-nudge-builder/`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | downstream | 0.27 |
| [[p01_kc_memory_scope]] | sibling | 0.26 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.25 |
| [[p01_kc_memory_persistence]] | sibling | 0.25 |
| [[p10_rs_conversation]] | downstream | 0.25 |
| [[bld_collaboration_memory_scope]] | downstream | 0.25 |
| [[agent_card_n04]] | related | 0.24 |
| [[bld_collaboration_memory_summary]] | downstream | 0.24 |
| [[ex_context_session_memory]] | related | 0.23 |
| [[bld_collaboration_memory_type]] | downstream | 0.23 |
