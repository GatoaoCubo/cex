---
id: citation_tracker_n01
kind: search_tool
pillar: P04
nucleus: n01
title: "N01 Academic Citation Tracker"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [search_tool, citation_tracking, academic_research, knowledge_graph, n01, analytical_envy]
tldr: "Citation network tracker for N01: maps paper-to-paper citation graphs, identifies seminal works, tracks citation velocity, and discovers emerging research frontiers. Uses Semantic Scholar API."
density_score: 0.87
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P04/search_tool F2 become=search-tool-builder F3 inject=api_reference_research_apis+search_strategy_n01+document_loader_n01 F4 reason=Analytical Envy in academic research = knowing which papers have become the foundation of a field, not just reading the latest -- citation graph reveals intellectual precedence and research momentum F5 call=cex_compile F6 produce=citation_tracker_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

Reading a paper in isolation = missing 90% of the signal.
The citation graph reveals:
- Which papers are foundational (high citations = standing on shoulders)
- Which papers are rising fast (citation velocity = frontier papers)
- Which clusters exist (community detection = school of thought)
- What a paper builds on and what builds on it

N01 Analytical Envy: always know who ELSE is working on the same problem.

## Citation Graph Operations

### Forward Citations (what cites this paper)

Shows who built on this work. High count = foundational. Rapid recent growth = current relevance.

```
forward_citations(paper_id: str) -> list[Paper]:
  SS_API.get(f"/paper/{paper_id}/citations?fields=paperId,title,year,citationCount&limit=500")
```

### Backward Citations (what this paper cites)

Shows the intellectual lineage. Identifies the papers N01 should also read.

```
backward_citations(paper_id: str) -> list[Paper]:
  SS_API.get(f"/paper/{paper_id}/references?fields=paperId,title,year,citationCount&limit=200")
```

### Citation Velocity

Detects rising papers: papers with accelerating citation rate are frontier works.

```
velocity(paper_id: str, window_years: int = 2) -> float:
  annual_counts = get_annual_citations(paper_id)
  recent = sum(annual_counts[-window_years:]) / window_years
  historical = sum(annual_counts[:-window_years]) / max(1, len(annual_counts) - window_years)
  return recent / max(1, historical)  # velocity > 2.0 = accelerating rapidly
```

## Citation Network Metrics

| Metric | Calculation | Interpretation |
|--------|------------|----------------|
| H-index (domain) | h papers with >= h citations | overall field impact |
| Citation velocity | recent_avg / historical_avg | trend: > 2.0 = accelerating |
| PageRank (paper) | centrality in citation graph | intellectual importance |
| Cluster coefficient | ratio of connected neighbors | community membership |
| Breadth | unique citing domains | cross-disciplinary impact |

## Seminal Paper Identification

| Criteria | Threshold | Label |
|----------|-----------|-------|
| Citation count | > 1000 | SEMINAL |
| Citation count | > 100 | SIGNIFICANT |
| Velocity | > 2.0 AND count > 10 | RISING |
| Velocity | < 0.5 | DECLINING |
| Age AND count | < 2 years AND > 50 | BREAKOUT |

## Research Frontier Detection

Emerging papers are the highest-value intelligence signal:

```
frontier_papers = [p for p in recent_papers
    if p.citation_velocity > 2.0
    and p.year >= current_year - 2
    and p.citationCount > 10]

frontier_papers.sort(by="citation_velocity", ascending=False)
```

These are the papers everyone will be citing in 12 months.
N01 reads them NOW.

## Output Format

```markdown
## Citation Analysis: {topic}

### Seminal Papers (top 5 by citations)
| Paper | Year | Citations | Velocity | Significance |
|-------|------|-----------|---------|-------------|

### Rising Papers (top 5 by velocity)
| Paper | Year | Citations | Velocity | Why It Matters |
|-------|------|-----------|---------|----------------|

### Research Clusters
| Cluster | Core Papers | Theme |
|---------|------------|-------|

### Research Gaps
| Gap | Evidence | Opportunity |
|-----|----------|-------------|
```

## Rate Limits (Semantic Scholar)

| Mode | Rate | Strategy |
|------|------|---------|
| Unauthenticated | 100 req / 5 min | batch paper IDs |
| Authenticated | 1 req/s | streaming |
| Bulk API | 10M papers CSV | for full corpus analysis |

## Comparison vs. Alternatives

| Tool | Graph Analysis | Velocity | Structured | N01 Fit |
|------|---------------|---------|------------|---------|
| Google Scholar | no API | no | no | manual only |
| Semantic Scholar | full API | manual | yes | primary |
| This tracker | API + velocity + graph | yes | yes (typed) | optimal |
| Connected Papers | visual only | no | no | for exploration |
