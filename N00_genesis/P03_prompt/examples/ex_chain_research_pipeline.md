---
id: ex_chain_research_pipeline
kind: chain
pillar: P03
title: "Research Pipeline Chain"
tags: [chain, research, multi-step, search, synthesis]
tldr: "4-step research chain: SEARCH→FILTER→SYNTHESIZE→CITE. Each step has a prompt template, input/output schema, and quality gate. Implements STORM/CRAG patterns."
references:
  - tpl_chain
  - ex_skill_web_scraper
  - ex_dispatch_rule_research
quality: 9.0
domain: "prompt engineering"
density_score: 0.83
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
version: "1.0.0"
---

# Research Pipeline Chain

## Chain Overview
```
SEARCH → FILTER → SYNTHESIZE → CITE
  (N01)    (N01)     (N01)      (N01)
```

## Step 1: SEARCH
**Prompt**: "Given the query `{query}`, generate 5 search queries that cover different angles."
**Input**: `{query: string, domain: string, max_sources: int}`
**Output**: `{queries: string[], sources: {url, title, snippet}[]}`
**Tool**: Web search API (Google/Bing/SearXNG)
**Gate**: ≥ 3 unique sources found

## Step 2: FILTER
**Prompt**: "Rate each source 1-5 on relevance, authority, freshness. Keep only ≥3."
**Input**: `{sources: Source[], criteria: FilterCriteria}`
**Output**: `{filtered_sources: Source[], rejected: {url, reason}[]}`
**Gate**: ≥ 2 sources pass filter (otherwise expand search)

| Criterion | Weight | Threshold |
|-----------|--------|-----------|
| Relevance | 0.4 | ≥ 3/5 |
| Authority | 0.3 | ≥ 3/5 |
| Freshness | 0.2 | ≥ 2/5 |
| Bias check | 0.1 | ≥ 2/5 |

## Step 3: SYNTHESIZE
**Prompt**: "Synthesize findings from {N} sources into a coherent analysis. Structure: Overview → Key Findings → Contradictions → Gaps."
**Input**: `{filtered_sources: Source[], query: string}`
**Output**: `{synthesis: string, key_findings: string[], confidence: float}`
**Gate**: synthesis ≥ 200 words, confidence ≥ 0.7

## Step 4: CITE
**Prompt**: "Add inline citations [1], [2] to the synthesis. Generate bibliography."
**Input**: `{synthesis: string, sources: Source[]}`
**Output**: `{cited_text: string, bibliography: Citation[]}`
**Gate**: Every claim has ≥ 1 citation, no hallucinated sources

## Error Recovery

| Failure | Recovery |
|---------|----------|
| SEARCH returns 0 | Rephrase query, retry once |
| FILTER too aggressive | Lower threshold by 1 point |
| SYNTHESIZE incoherent | Re-run with "be more structured" |
| CITE misses claims | Highlight uncited sentences, re-run |

## Quality Gate
- [ ] All 4 steps have prompt + input + output + gate
- [ ] Error recovery defined per step
- [ ] Citation integrity (no made-up sources)
- [ ] Total chain timeout ≤ 120s
