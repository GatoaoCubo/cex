---
id: ex_context_session_memory
kind: context
8f: F3_inject
pillar: P01
title: "Example — Session Memory Context"
tags: [context, session, memory, conversation, continuity]
tldr: "Injects the last N conversation turns as context for multi-turn interactions. Manages token budget, summarization triggers, and relevance decay."
references:
  - tpl_context_doc
  - ex_knowledge_card_rag_fundamentals
quality: 9.0
related:
  - p10_cc_rolling_window_50pct
  - p10_rs_conversation
  - p10_memory_summary
  - p01_kc_token_budgeting
  - p01_kc_memory_summary
  - p02_memory_scope
  - bld_examples_memory_summary
  - bld_knowledge_card_memory_summary
  - bld_memory_session_state
  - p01_kc_compression_config
---

# Session Memory Context

## Purpose
Maintains conversational continuity by injecting recent interaction history into the agent's context window. Prevents the "goldfish problem" where each turn starts from zero.

## Configuration
```yaml
id: ctx_session_memory
kind: context
max_turns: 10              # Keep last 10 turns
max_tokens: 4096           # Budget for session memory
summarize_after: 5         # Summarize older turns to save tokens
relevance_decay: 0.9       # Each older turn weighted 10% less
include_tool_calls: false  # Strip tool call details (save tokens)
```

## Injection Format
```markdown
## Session Memory (last 5 turns)
[User] How do I create a knowledge card?
[Agent] Use the 8F pipeline: python cex_8f_runner.py "create knowledge card about X" --execute
[User] What about the frontmatter fields?
[Agent] Required: id, kind, pillar, quality (must be null). Optional: title, tags, tldr.
[User] Can I set quality myself?
[Agent] No — quality: null always. Peer review assigns scores via cex_score.py.
```

## Token Budget Management

| Turns | Strategy | Tokens Used |
|-------|----------|-------------|
| 1-5 | Full verbatim | ~1000 |
| 6-10 | Verbatim recent, summarize old | ~2000 |
| 11-20 | Summary only for turns 1-15 | ~3000 |
| 20+ | Rolling summary + last 5 verbatim | ~4096 (capped) |

## Summarization Trigger
When `turn_count > summarize_after`:
1. Take turns [1..N-5] (oldest)
2. Summarize to ≤500 tokens using LLM
3. Prepend summary, keep last 5 verbatim

## Quality Gate
- [ ] max_tokens ≤ 1/3 of model context window
- [ ] Summarization trigger defined
- [ ] Tool call output excluded (saves 40%+ tokens)
- [ ] Relevance decay prevents stale context dominating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_cc_rolling_window_50pct]] | downstream | 0.41 |
| [[p10_rs_conversation]] | downstream | 0.31 |
| [[p10_memory_summary]] | downstream | 0.30 |
| [[p01_kc_token_budgeting]] | related | 0.28 |
| [[p01_kc_memory_summary]] | downstream | 0.27 |
| [[p02_memory_scope]] | downstream | 0.27 |
| [[bld_examples_memory_summary]] | downstream | 0.26 |
| [[bld_knowledge_card_memory_summary]] | related | 0.25 |
| [[bld_memory_session_state]] | downstream | 0.24 |
| [[p01_kc_compression_config]] | downstream | 0.22 |
