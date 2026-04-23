---
id: p06_schema_citation_format
kind: schema
pillar: P06
title: "Citation Format Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [schema, n01, citation, reference, format]
tldr: "APA-lite citation format for N01 research output. URL, title, author, date, accessed, reliability."
density_score: 0.91
related:
  - bld_schema_citation
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_rl_algorithm
  - bld_schema_thinking_config
  - bld_schema_voice_pipeline
  - bld_schema_reranker_config
  - bld_schema_dataset_card
---

# Citation Format Contract

## Format
```
[N] Author/Org. "Title." Source, Date. URL. Accessed: DATE. Reliability: N/5.
```

## Example
```
[1] Example Research Group. "State of AI 2025." example-research.com, 2025-03-15.
    https://example-research.com/state-of-ai-2025. Accessed: 2026-03-31. Reliability: 4/5.
[2] @sampleuser. "AI agents are replacing..." Twitter/X, 2026-03-28.
    https://x.com/sampleuser/status/123. Accessed: 2026-03-31. Reliability: 2/5.
```

## Fields
| Field | Required | Description |
|-------|----------|-------------|
| number | Yes | Sequential reference number |
| author | Yes | Person or organization |
| title | Yes | Document/page title |
| source | Yes | Platform or publication |
| date | Yes | Publication date |
| url | Yes | Full URL |
| accessed | Yes | When we accessed it |
| reliability | Yes | 1-5 scale (from source_quality_contract) |

## Usage Guidelines

| Use When | Don't Use When |
|----------|----------------|
| N01 research briefs | Academic papers (use APA) |
| Competitive analysis | Internal docs (use file paths) |
| Market research | Code repos (use commit refs) |
| Trend reports | Books (use ISBN format) |

## Reliability Scale
| Score | Source Type | Examples |
|-------|-------------|----------|
| 5/5 | Peer-reviewed, official | Nature, .gov sites, company 10-Ks |
| 4/5 | Reputable media, analysts | Major consultancies, tech news outlets |
| 3/5 | Industry blogs, newsletters | VC firm blogs, independent analysts |
| 2/5 | Social media, forums | Twitter, Reddit, LinkedIn |
| 1/5 | Unverified, anonymous | Medium randos, comment sections |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_citation]] | sibling | 0.36 |
| [[bld_schema_search_strategy]] | sibling | 0.36 |
| [[bld_schema_quickstart_guide]] | sibling | 0.35 |
| [[bld_schema_usage_report]] | sibling | 0.34 |
| [[bld_schema_integration_guide]] | sibling | 0.34 |
| [[bld_schema_rl_algorithm]] | sibling | 0.33 |
| [[bld_schema_thinking_config]] | sibling | 0.33 |
| [[bld_schema_voice_pipeline]] | sibling | 0.33 |
| [[bld_schema_reranker_config]] | sibling | 0.32 |
| [[bld_schema_dataset_card]] | sibling | 0.32 |
