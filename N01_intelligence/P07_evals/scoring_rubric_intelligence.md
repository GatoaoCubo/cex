---
id: p07_rubric_intelligence
kind: scoring_rubric
pillar: P07
title: "N01 Scoring Rubric — Research Quality"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [scoring_rubric, n01, research, quality]
tldr: "5-dimension scoring for research output: triangulation, freshness, actionability, structure, depth."
density_score: 0.92
---

# N01 Scoring Rubric

| Dimension | Weight | 1-3 (Weak) | 4-6 (Adequate) | 7-9 (Strong) | 10 (Exceptional) |
|-----------|--------|-----------|----------------|--------------|-------------------|
| Triangulation | 25% | Single source, no verification | 2 sources for key claims | 3+ sources with agreement noted | 3+ diverse sources with disagreement analysis |
| Freshness | 20% | Data >1 year old | Data <6 months, some stale | All data <90 days | All data <30 days with trend context |
| Actionability | 25% | Raw data, no interpretation | Some insights | Clear "so what?" per finding | Strategic recommendations with confidence |
| Structure | 15% | Prose paragraphs | Some tables | Grids + tables + sections | Visual hierarchy, scannable, executive summary |
| Depth | 15% | Surface scan only | Key facts covered | Analysis with context | Deep-dive with projections and edge cases |

## Scoring Examples

| Dimension | Score 3 Example | Score 7 Example | Score 10 Example |
|-----------|-----------------|-----------------|-------------------|
| **Triangulation** | "OpenAI revenue is $1B (per TechCrunch)" | "OpenAI revenue $1B (TechCrunch, Reuters, Bloomberg agree)" | "OpenAI revenue $1B (TC/Reuters agree, Anthropic disputes timing)" |
| **Freshness** | "2023 AI market was $50B" | "Q3 2025 AI market hit $120B" | "Jan 2026: AI market $140B, up 15% from Dec" |
| **Actionability** | "Claude usage is growing" | "Claude grew 40% → adoption accelerating" | "Claude 40% growth → invest in competitor analysis, ETA Q2" |
| **Structure** | Wall of text paragraphs | Key findings in bullets + table | Executive summary + visual grid + appendix |
| **Depth** | "AI coding tools popular" | "GitHub Copilot has 1M users, 30% productivity gain" | "Copilot 1M users, 30% gain, but 60% churn in enterprise" |

## Usage Guidelines

**When to use**: Research briefs, competitor analysis, market reports, intelligence summaries
**When NOT to use**: Code documentation, marketing copy, instructional content

**Anti-patterns**:
- Scoring before research is complete
- Conflating data volume with quality depth
- Ignoring source bias in triangulation scoring
- Accepting outdated data without temporal context

## Score Thresholds
- **Publish**: >= 8.0
- **Revise**: 6.0-7.9 (specify which dimensions to improve)
- **Reject**: < 6.0 (re-research needed)