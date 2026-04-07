---
kind: examples
id: bld_examples_citation
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of citation artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: citation-builder
## Golden Example
INPUT: "Create citation for Anthropic prompt caching documentation"
OUTPUT:
```yaml
---
id: p01_cit_anthropic_prompt_caching
kind: citation
pillar: P01
title: "Anthropic Prompt Caching Documentation"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "citation-builder"
source_type: web
reliability_tier: tier_2
url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
date_accessed: "2026-04-07"
excerpt: "Prompt caching allows you to cache frequently used context between API calls, reducing latency by up to 85% and costs by up to 90% for long prompts."
relevance_scope: [llm_engineering, prompt_cache, cost_optimization]
domain: llm_engineering
quality: null
tags: [citation, anthropic, prompt-caching, cost-optimization]
tldr: "Official Anthropic docs on prompt caching — 90% cost reduction, 85% latency reduction via prefix reuse with 5min TTL"
---

# Anthropic Prompt Caching Documentation

## Source
- **Author**: Anthropic
- **Title**: Prompt Caching (Build with Claude)
- **Publisher/Venue**: docs.anthropic.com
- **Date**: 2025 (continuously updated)
- **Type**: web (tier_2 — official documentation)

## Excerpt
> Prompt caching allows you to cache frequently used context between API calls, reducing latency by up to 85% and costs by up to 90% for long prompts. Minimum cacheable prefix is 1024 tokens. Cache TTL is 5 minutes.

## Relevance
- Supports: p01_kc_prompt_caching, prompt_cache configuration decisions
- Scope: llm_engineering, cost optimization, API integration

## Verification
- URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Accessed: 2026-04-07
- Freshness policy: 90 days (API docs evolve)
- DOI/ISBN: N/A
```
WHY THIS IS GOLDEN:
- quality: null
- id matches p01_cit_ pattern
- source_type and reliability_tier are valid enums
- excerpt is concrete (numbers: 85%, 90%, 1024 tokens, 5min)
- date_accessed present
- relevance_scope mapped
- Under 2048 bytes

## Anti-Example
INPUT: "Cite prompt caching"
BAD OUTPUT:
```yaml
id: caching_ref
kind: citation
url: https://docs.anthropic.com
quality: 8.5
```
FAILURES:
1. id: no p01_cit_ prefix
2. quality: not null — self-scored
3. No source_type, reliability_tier, excerpt, date_accessed
4. URL too generic (no specific page)
5. No body sections
