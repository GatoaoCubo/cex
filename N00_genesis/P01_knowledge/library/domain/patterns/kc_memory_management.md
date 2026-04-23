---
id: p01_kc_memory_management
kind: knowledge_card
type: domain
pillar: P01
title: "Memory Management"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, memory, tiers, persistence, forgetting, hot-warm-cold]
tldr: "Not everything worth remembering. Tier memory as hot (session), warm (handoff), cold (KC). Filter by impact. Decay stale memories. Never persist debug output."
when_to_use: "At session boundaries, when context fills up, and when deciding what to persist for future sessions."
keywords: [memory, tiers, persistence, forgetting, hot-warm-cold, decay, learning]
density_score: 0.95
related:
  - p01_kc_context_overflow
  - p01_kc_memory_scope
  - bld_system_prompt_memory_type
  - p01_kc_memory_type
  - p01_kc_memory_consolidation
  - p01_kc_session_state
  - bld_knowledge_card_memory_type
  - p01_kc_memory_persistence
  - SPEC_04_memory_system
  - bld_memory_session_state
---

# Memory Management

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Tier information by persistence need; aggressively forget low-value signals |
| Trigger | Session end, context overflow, handoff, learning event |
| Benefit | Future sessions start smarter; context stays lean |
| Risk if skipped | Bloated context, stale data, repeated mistakes |

## Memory Tiers

| Tier | Scope | Persistence | TTL | Example |
|------|-------|-------------|-----|---------|
| Hot | Current session only | RAM (context window) | Session | Debug output, intermediate drafts |
| Warm | Cross-session, short-term | Files (handoffs/) | 1–5 sessions | Task progress, current decisions |
| Cold | Permanent knowledge | Artifacts (KC, learning records) | Indefinite | Patterns, corrections, conventions |
| Frozen | Archived, rarely accessed | Git history | Forever | Old mission plans, deprecated configs |

## Persistence Decision Matrix

| Signal Type | Persist? | Where | Rationale |
|-------------|----------|-------|-----------|
| Error + fix pair | **Yes** | learning_record | Prevents repeat mistakes |
| Discovered pattern | **Yes** | knowledge_card | Reusable across sessions |
| User preference | **Yes** | decision_manifest | GDP compliance |
| Brand decision | **Yes** | brand_config.yaml | Identity consistency |
| Debug/trace output | **No** | ephemeral | High volume, low reuse value |
| Intermediate draft | **No** | ephemeral | Superseded by final version |
| Task completion signal | **Warm** | handoffs/ | Needed for session continuity only |
| Quality score delta | **Yes** | experiments.tsv | Calibration data for evolution |

## Memory Types (CEX taxonomy)

| Type | Definition | Example |
|------|-----------|---------|
| Correction | Error caught + fix applied | "Always use UTF-8 encoding in file opens" |
| Preference | User-stated choice | "Prefer tables over prose" |
| Convention | Team/project standard | "Frontmatter quality never self-scored" |
| Context | Situational fact | "Project uses Python 3.12, Windows" |

## Decay Strategy

| Age | Confidence Modifier | Action |
|-----|---------------------|--------|
| < 30 days | 1.0 (full trust) | Use directly |
| 30–90 days | 0.8 | Use with caveat |
| 90–180 days | 0.6 | Verify before applying |
| 180–365 days | 0.4 | Re-validate or archive |
| > 365 days | 0.2 | Archive unless explicitly reconfirmed |

## Pruning Protocol

| Step | Action | Tool |
|------|--------|------|
| 1 | Scan all warm/cold memories | `cex_memory_age.py` |
| 2 | Score each by impact × recency | `cex_memory_select.py` |
| 3 | Archive memories below threshold | `cex_memory_update.py` |
| 4 | Verify no active references broken | Cross-reference scan |
| 5 | Log pruning event | `.cex/learning_records/` |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Remember everything | Context bloat, stale data dominates |
| Forget everything | Repeats mistakes, loses user preferences |
| No decay | Year-old memories treated as fresh facts |
| Persist debug logs | 90% of volume, 0% of reuse value |
| Manual-only pruning | Never happens at scale |

## Linked Artifacts

- `p01_kc_context_overflow` — when to trigger memory offload
- `p01_kc_token_budgeting` — how memory competes for context budget
- `p01_kc_knowledge_distillation` — compress warm memories into cold KCs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_context_overflow]] | sibling | 0.32 |
| [[p01_kc_memory_scope]] | sibling | 0.31 |
| [[bld_system_prompt_memory_type]] | downstream | 0.29 |
| [[p01_kc_memory_type]] | sibling | 0.28 |
| [[p01_kc_memory_consolidation]] | sibling | 0.26 |
| [[p01_kc_session_state]] | sibling | 0.26 |
| [[bld_knowledge_card_memory_type]] | sibling | 0.24 |
| [[p01_kc_memory_persistence]] | sibling | 0.24 |
| [[SPEC_04_memory_system]] | related | 0.24 |
| [[bld_memory_session_state]] | downstream | 0.24 |
