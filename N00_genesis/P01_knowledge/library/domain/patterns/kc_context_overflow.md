---
id: p01_kc_context_overflow
kind: knowledge_card
type: domain
pillar: P01
title: "Context Overflow Management"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, context-overflow, window-limit, compression, handoff]
tldr: "Detect early, compress at 50%, offload at 70%, handoff at 80%. All state persists in files. Never lose work to a context limit."
when_to_use: "In any long-running task, multi-step pipeline, or session approaching model context limits."
keywords: [context-overflow, window-limit, compression, handoff, token-budget, session]
density_score: 0.95
related:
  - p12_wf_auto_handoff
  - bld_collaboration_session_state
  - bld_collaboration_handoff
  - handoff-builder
  - p01_kc_anti_full_context
  - p01_kc_handoff
  - handoff-protocol-builder
  - p12_ho_builder_nucleus
  - bld_memory_session_state
  - p01_kc_memory_management
---

# Context Overflow Management

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Monitor context usage, compress/offload/handoff at thresholds |
| Trigger | Context usage crosses 50%, 70%, or 80% of model window |
| Benefit | Zero work lost to context limits; seamless continuity |
| Risk if skipped | Truncated context → lost instructions, broken outputs, repeated work |

## Threshold Strategy

| Context Used | Strategy | Action | State Impact |
|-------------|----------|--------|-------------|
| < 50% | Normal | Full context available | None |
| 50% | Summarize | Compress conversation history to key decisions + outcomes | ~40% reduction |
| 70% | Offload | Write all state to files (handoff docs, progress, decisions) | ~60% reduction |
| 80% | Handoff | Full session handoff — new session reads files | 100% fresh context |
| 90%+ | Emergency | Abort current task, dump state, signal incomplete | Partial loss risk |

## Compression Techniques

| Technique | Tokens Saved | When to Use |
|-----------|-------------|-------------|
| Drop debug output | 20-40% | Always first — debug logs are ephemeral |
| Summarize conversation | 30-50% | After decisions are made and logged |
| Reference files instead of inline | 40-60% | Large code blocks, data tables |
| Prune completed tasks | 20-30% | Multi-step pipelines past checkpoint |
| Replace examples with pointers | 10-20% | After pattern is established |

## Handoff Protocol

| Step | Action | File |
|------|--------|------|
| 1 | Write current task state | `.cex/runtime/handoffs/n{XX}_task.md` |
| 2 | Write decisions made | `.cex/runtime/decisions/decision_manifest.yaml` |
| 3 | Write progress checkpoint | `.cex/runtime/handoffs/progress.md` |
| 4 | Signal handoff needed | `signal_writer.py` → `handoff` signal |
| 5 | New session reads handoff files | First action in new context |

## Detection Methods

| Method | Accuracy | Cost |
|--------|----------|------|
| Token counting (cex_token_budget.py) | High | 1 API call |
| Message count heuristic (>40 turns) | Medium | Free |
| Output degradation detection | High | Requires comparison |
| Model-reported context usage | Varies | Model-dependent |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Ignoring limits until crash | Abrupt truncation loses recent context silently |
| Compressing too early | Loses detail needed for current task |
| Handoff without state files | New session starts blind, repeats work |
| Keeping full conversation "just in case" | Burns context on resolved history |
| No progress checkpoints | Handoff without knowing what's done vs pending |

## CEX Integration

| Concept | CEX artifact / tool |
|---------|-------------------|
| Token counting | `cex_token_budget.py` |
| State persistence | `.cex/runtime/handoffs/` |
| Decision preservation | `decision_manifest.yaml` |
| Handoff signals | `signal_writer.py` |
| Memory tiering | `cex_memory_types.py` (hot/warm/cold) |

## Linked Artifacts

- `p01_kc_token_budgeting` — allocation strategy within the window
- `p01_kc_memory_management` — what to persist vs discard
- `p01_kc_self_healing_skill` — recover from overflow-induced errors

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_handoff]] | downstream | 0.41 |
| [[bld_collaboration_session_state]] | downstream | 0.35 |
| [[bld_collaboration_handoff]] | downstream | 0.32 |
| [[handoff-builder]] | downstream | 0.30 |
| [[p01_kc_anti_full_context]] | sibling | 0.30 |
| [[p01_kc_handoff]] | sibling | 0.29 |
| [[handoff-protocol-builder]] | downstream | 0.29 |
| [[p12_ho_builder_nucleus]] | downstream | 0.28 |
| [[bld_memory_session_state]] | downstream | 0.27 |
| [[p01_kc_memory_management]] | sibling | 0.27 |
