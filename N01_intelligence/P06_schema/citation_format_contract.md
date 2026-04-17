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
---

# Citation Format Contract

## Format
```
[N] Author/Org. "Title." Source, Date. URL. Accessed: DATE. Reliability: N/5.
```

## Example
```
[1] McKinsey & Co. "State of AI 2025." McKinsey.com, 2025-03-15.
    https://mckinsey.com/state-of-ai-2025. Accessed: 2026-03-31. Reliability: 4/5.
[2] @johndoe. "AI agents are replacing..." Twitter/X, 2026-03-28.
    https://x.com/johndoe/status/123. Accessed: 2026-03-31. Reliability: 2/5.
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
| 4/5 | Reputable media, analysts | McKinsey, TechCrunch, Bloomberg |
| 3/5 | Industry blogs, newsletters | a16z blog, Stratechery |
| 2/5 | Social media, forums | Twitter, Reddit, LinkedIn |
| 1/5 | Unverified, anonymous | Medium randos, comment sections |