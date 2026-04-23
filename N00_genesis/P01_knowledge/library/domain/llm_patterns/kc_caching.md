---
id: p01_kc_caching
kind: knowledge_card
type: domain
pillar: P01
title: "LLM Caching Strategies"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.1
tags: [caching, performance, cost, latency, prompt-cache]
tldr: "Cache LLM responses to reduce cost and latency. Exact match, semantic, prefix caching. Trade-off: freshness vs speed."
when_to_use: "Optimizing cost or latency in production LLM systems"
keywords: [caching, prompt-cache, semantic-cache, memoization, cost-reduction]
density_score: 0.91
updated: "2026-04-07"
related:
  - bld_examples_knowledge_card
  - bld_collaboration_prompt_cache
  - bld_examples_golden_test
  - bld_knowledge_card_prompt_cache
  - p01_kc_prompt_cache
  - ex_knowledge_card_prompt_caching
  - bld_tools_prompt_cache
  - bld_examples_citation
  - prompt-cache-builder
  - p01_kc_universal_llm
---

# LLM Caching Strategies

## Cache Types

| Type | Match | Speed | Use Case |
|------|-------|-------|----------|
| Exact | Hash of full prompt | Fastest | Repeated identical queries |
| Prefix | First N tokens match | Fast | System prompt caching (Claude) |
| Semantic | Embedding similarity >0.95 | Medium | FAQ, common queries |
| Result | Hash of input → stored output | Fast | Deterministic transforms |

## Provider Features

| Provider | Built-in Cache |
|----------|---------------|
| Claude | Prompt caching (prefix, up to 90% cost reduction) |
| GPT | No native cache (use external) |
| Gemini | Context caching (long contexts) |

## CEX Integration
- `compiled/*.yaml` = pre-compiled templates (avoid re-parsing)
- Builder specs loaded once per session, reused across builds
- Brand config cached in memory after first read

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_caching`
- **Tags**: [caching, performance, cost, latency, prompt-cache]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "LLM Caching Strategies"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "LLM Caching Strategies" --top 5
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_knowledge_card]] | downstream | 0.47 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.42 |
| [[bld_examples_golden_test]] | downstream | 0.37 |
| [[bld_knowledge_card_prompt_cache]] | sibling | 0.36 |
| [[p01_kc_prompt_cache]] | sibling | 0.35 |
| [[ex_knowledge_card_prompt_caching]] | sibling | 0.34 |
| [[bld_tools_prompt_cache]] | downstream | 0.34 |
| [[bld_examples_citation]] | downstream | 0.33 |
| [[prompt-cache-builder]] | downstream | 0.32 |
| [[p01_kc_universal_llm]] | sibling | 0.31 |
