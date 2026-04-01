---
id: p10_out_source_dossier
kind: output
pillar: P10
title: "Output: Source Dossier"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 8.6
tags: [output, n01, source, dossier, curation]
tldr: "Curated source list with quality scores per source_quality_contract schema."
density_score: 0.91
---

# Output: Source Dossier

## Template
```markdown
# Source Dossier: {{TOPIC}}
**Curated**: {{DATE}} | **Total Sources**: {{COUNT}} | **Avg Reliability**: {{AVG}}/5

## Top Sources

| # | Source | Type | Authority | Freshness | Reliability | URL |
|---|--------|------|-----------|-----------|-------------|-----|
| 1 | {{NAME}} | {{TYPE}} | {{1-5}} | {{DATE}} | {{SCORE}} | {{URL}} |

## Source Distribution
- Web: {{N}} | Academic: {{N}} | Industry: {{N}} | Government: {{N}} | Social: {{N}}

## Reliability Summary
- High (4-5): {{N}} sources
- Medium (3): {{N}} sources
- Low (1-2): {{N}} sources (use with caution)
```
