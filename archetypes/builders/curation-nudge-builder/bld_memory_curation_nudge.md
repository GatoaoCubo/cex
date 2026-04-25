---
id: p11_mem_curation_nudge
kind: procedural_memory
pillar: P10
llm_function: INJECT
purpose: Learned patterns and anti-patterns for curation_nudge builder
quality: 8.7
title: "Memory: Curation Nudge Builder"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [memory, curation_nudge, builder, p10, hermes, anti_patterns]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "Learned patterns and anti-patterns for curation_nudge builder"
density_score: 0.88
related:
  - bld_collaboration_memory_type
  - p01_kc_memory_scope
  - bld_knowledge_card_memory_scope
  - bld_collaboration_memory_scope
  - p01_kc_session_state
  - skill_memory_update
  - bld_memory_session_state
  - bld_examples_memory_scope
  - p01_kc_session_backend
  - p01_kc_memory_persistence
---

## Learned Patterns

### Pattern 1: Trigger-Destination Affinity
```
turn_count -> MEMORY.md (general preferences, conventions)
density_threshold -> entity_memory (structured entities accumulate under research)
tool_call_count -> MEMORY.md (agentic conventions, tool preferences)
user_correction -> MEMORY.md (preference corrections are flat-text entries)
```
**Why:** Each trigger type reflects a different observation modality. Matching destination
to trigger prevents over-engineering (e.g., don't create a knowledge_card for a simple preference).

### Pattern 2: Session Profile Tuning
```
Long research session: density_threshold=5, max_per_session=2 (few high-signal nudges)
Short coding session: tool_call_count=15, max_per_session=1 (one end-of-session nudge)
Preference learning: user_correction=1, min_interval_turns=3 (every correction, not spam)
General conversation: turn_count=10, max_per_session=3 (HERMES default)
```
**Why:** One-size nudge degrades all session types. Session profile awareness maximizes nudge value.

### Pattern 3: Prompt Template Localization
```
PT-BR sessions: "Notei [observation]. Devo persistir em MEMORY.md?"
EN sessions: "I noticed [observation]. Should I persist this to MEMORY.md?"
Mixed: Use PT-BR (CEX default); agents understand both
```
**Why:** Native-language prompts reduce agent processing overhead. CEX defaults to PT-BR.

## Anti-Patterns (do NOT repeat)

| Anti-Pattern | Root Cause | Fix |
|-------------|-----------|-----|
| Threshold below 5 | Misunderstanding of minimum | Enforce H02: threshold >= 5 |
| Missing observation placeholder | Template copy-paste without observation var | Enforce H05: must contain placeholder |
| destination=slack_channel | Confusion with notifier pattern | Enforce H04: only 3 valid destinations |
| Nudge that blocks | Trying to use nudge as guardrail | Route to guardrail-builder |
| max_per_session=0 | Attempting to disable nudging via nudge | Use lifecycle_rule or env var CN_MAX_PER_SESSION=0 |

## Calibration Data (from HERMES deployments)

| Parameter | Too Low | Optimal | Too High |
|-----------|---------|---------|---------|
| threshold (turn_count) | <5: spam | 8-12: good | >20: misses knowledge |
| min_interval_turns | <3: chained spam | 5-7: good | >15: gaps persist |
| max_per_session | 0: disabled | 2-4: good | >6: context saturation |

## Collaboration Lessons

1. **N04 owns destinations** -- always coordinate with N04 when creating new memory sinks
2. **MEMORY.md is the default** -- unless caller explicitly needs structured data, use flat text
3. **user_correction is highest signal** -- even one correction warrants immediate nudge
4. **End-of-session is the best nudge slot** -- F8 COLLABORATE should always fire a nudge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_type]] | downstream | 0.27 |
| [[p01_kc_memory_scope]] | upstream | 0.27 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.25 |
| [[bld_collaboration_memory_scope]] | downstream | 0.25 |
| [[p01_kc_session_state]] | related | 0.25 |
| [[skill_memory_update]] | related | 0.24 |
| [[bld_memory_session_state]] | related | 0.24 |
| [[bld_examples_memory_scope]] | upstream | 0.23 |
| [[p01_kc_session_backend]] | related | 0.22 |
| [[p01_kc_memory_persistence]] | upstream | 0.22 |
