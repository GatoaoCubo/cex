---
quality: 8.4
quality: 7.9
id: bld_kc_curation_nudge
kind: knowledge_card
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for curation_nudge builder (F3 INJECT)
title: "Knowledge Card: Curation Nudge Builder"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [curation_nudge, builder, knowledge_card, hermes, memory, proactive]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "Domain knowledge for curation_nudge builder (F3 INJECT)"
density_score: 0.89
related:
  - p01_kc_memory_scope
  - bld_memory_session_state
  - bld_knowledge_card_memory_scope
  - p01_kc_memory_consolidation
  - p01_kc_memory_persistence
  - p01_kc_session_backend
  - p01_kc_session_state
  - bld_collaboration_memory_type
  - bld_collaboration_memory_scope
  - atom_22_memory_taxonomy
---

## Domain Knowledge

### HERMES Agent-Curated Memory Pattern

Source: NousResearch/hermes-agent
Core principle: "Agents should proactively manage their own memory, nudging themselves to
persist high-value observations before they fall out of the active context window."

The nudge is not a command. It is a self-directed question: "Should I save this?"
The agent evaluates: novelty, utility, durability, and destination fit.

### Trigger Types -- When to Fire

| Trigger | Semantics | Session Profile |
|---------|-----------|----------------|
| `turn_count` | N turns elapsed | Universal; works in all session types |
| `density_threshold` | N new facts observed | Research, analysis, knowledge-heavy sessions |
| `tool_call_count` | N tool calls completed | Agentic, coding, file-intensive sessions |
| `user_correction` | User contradicts prior output | Preference learning; highest signal per fire |

### Destination Semantics

| Destination | Structure | Best For |
|-------------|-----------|---------|
| `MEMORY.md` | Flat markdown entries | General preferences, conventions, project facts |
| `entity_memory` | Structured entity records | People, systems, organizations, products |
| `knowledge_card` | Rich KC document | Complex domain knowledge worthy of full artifact |

### Honcho User Model Integration

The HERMES Honcho pattern uses curation_nudge as the ingestion mechanism for the user_model:
```
in-session observation
  -> curation_nudge fires
  -> agent asks for confirmation
  -> confirmed: write to MEMORY.md entry
  -> at session end: user_model builder reads MEMORY.md
  -> updates long-term user_model artifact
```
This is how CEX implements cross-session learning without continuous fine-tuning.

### Anti-Patterns (learned from HERMES deployments)

| Anti-Pattern | Why It Fails | Correct Pattern |
|-------------|-------------|----------------|
| Threshold < 5 | Spam; agent spends more time on nudges than task | Minimum 5 |
| max_per_session > 5 | Context saturation; user loses trust | Maximum 5 per session |
| Missing observation placeholder | Generic prompt; unactionable (H05 fails) | Always include observation var |
| Nudge as blocking mechanism | Breaks user flow; use guardrail | Nudge ASKS only |
| All sessions use same nudge | Different sessions need different triggers | Match trigger to session profile |

### CEX Memory Architecture (nudge fit)

```
Short-term (in-session):
  Working context window -> curation_nudge monitors -> fires at threshold

Medium-term (cross-session):
  MEMORY.md -> auto-loaded at session start -> provides continuity

Long-term (persistent):
  entity_memory + knowledge_card -> curated, structured, versioned
  user_model (Honcho) -> aggregates nudge output into preference model
```

### Builder Constraints (enforce at F7 GOVERN)

- `trigger.threshold` MUST be >= 5 (below 5 degrades session quality via nudge spam)
- `max_per_session` MUST be <= 5 (above 5 saturates user attention budget)
- `prompt_template` MUST reference `{{observation}}` (generic prompt fails H05)
- `target_memory.destination` MUST be one of the three canonical sinks
- Naming pattern: `p11_cn_{{trigger_type}}.yaml` enforced by H02
- `cadence.min_interval_turns` prevents double-firing within a single burst
- Tag `hermes_origin` required on all curation_nudge artifacts for provenance tracking
- `auto_write_if_confirmed: true` is the recommended default; false requires explicit user gesture
- When `trigger.type = user_correction`, threshold MUST be 1 (fire immediately on correction signal)
- `MEMORY.md` destination requires no frontmatter; entity_memory and knowledge_card do
- Cadence field `min_interval_turns` default is 5; setting to 0 allows immediate re-fire (not recommended)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_scope]] | sibling | 0.33 |
| [[bld_memory_session_state]] | downstream | 0.31 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.31 |
| [[p01_kc_memory_consolidation]] | sibling | 0.30 |
| [[p01_kc_memory_persistence]] | sibling | 0.30 |
| [[p01_kc_session_backend]] | sibling | 0.29 |
| [[p01_kc_session_state]] | sibling | 0.29 |
| [[bld_collaboration_memory_type]] | downstream | 0.28 |
| [[bld_collaboration_memory_scope]] | downstream | 0.27 |
| [[atom_22_memory_taxonomy]] | sibling | 0.27 |
