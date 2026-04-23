---
id: p10_memory_summary
kind: memory_summary
pillar: P10
version: 1.0.0
title: "Template — Memory Summary"
tags: [template, memory, summary, compression, context]
tldr: "Compresses long conversation or session history into a concise summary. Preserves key decisions, actions, and outcomes while reducing token count by 80%+."
quality: 9.0
related:
  - p01_kc_memory_summary
  - ex_context_session_memory
  - memory-summary-builder
  - bld_examples_memory_summary
  - p10_cc_rolling_window_50pct
  - p01_kc_session_state
  - bld_collaboration_memory_summary
  - bld_collaboration_session_backend
  - p01_kc_compression_config
  - bld_memory_session_state
---

# Memory Summary: [SESSION_ID]

## Purpose
[WHAT history is being compressed — conversation turns, session actions, build log]

## Summary Schema
```yaml
id: "[SUMMARY_ID]"
session_id: "[SESSION_ID]"
created: "[ISO8601]"
turns_compressed: [N]
tokens_saved: [N]
compression_ratio: [0.1-0.3]  # summary_tokens / original_tokens
```

## Summary Content Template
```markdown
## Session Summary ([DATE])
**Goal**: [What the user/agent was trying to achieve]
**Key Decisions**:
- [DECISION_1 — what was decided and why]
- [DECISION_2]
**Actions Taken**:
- [ACTION_1 — what was done and result]
- [ACTION_2]
**Open Items**:
- [ITEM_1 — what remains to be done]
**Context for Next Session**:
- [KEY_FACT_1 — essential context to carry forward]
```

## Compression Strategy

| Method | Compression | Quality | When |
|--------|-------------|---------|------|
| LLM summary | 80-90% | High | Default for conversations |
| Key extraction | 70-80% | Medium | Fast, for structured logs |
| Last-N truncation | 50% | Low | Fallback when LLM unavailable |

## Trigger Rules
- **Turn count**: Summarize after [10] turns
- **Token count**: Summarize when history exceeds [4096] tokens
- **Session end**: Always summarize at session close
- **Manual**: User requests "summarize this session"

## Preservation Rules (never compress away)
- User preferences and corrections
- Error resolutions (what failed and how it was fixed)
- Explicit decisions with rationale
- Names, IDs, paths mentioned

## Quality Gate
- [ ] Compression ratio ≤ 0.3 (at least 70% reduction)
- [ ] Key decisions preserved (compare against original)
- [ ] Open items carried forward
- [ ] No hallucinated content in summary

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_summary]] | related | 0.39 |
| [[ex_context_session_memory]] | upstream | 0.30 |
| [[memory-summary-builder]] | related | 0.30 |
| [[bld_examples_memory_summary]] | upstream | 0.29 |
| [[p10_cc_rolling_window_50pct]] | related | 0.28 |
| [[p01_kc_session_state]] | related | 0.27 |
| [[bld_collaboration_memory_summary]] | downstream | 0.26 |
| [[bld_collaboration_session_backend]] | downstream | 0.24 |
| [[p01_kc_compression_config]] | related | 0.23 |
| [[bld_memory_session_state]] | related | 0.23 |
