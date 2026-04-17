---
id: p10_out_source_dossier
kind: output
pillar: P10
title: "Output: Source Dossier"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.1
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

## Example Output
```markdown
# Source Dossier: AI Safety Research
**Curated**: 2026-03-31 | **Total Sources**: 8 | **Avg Reliability**: 4.1/5

## Top Sources

| # | Source | Type | Authority | Freshness | Reliability | URL |
|---|--------|------|-----------|-----------|-------------|-----|
| 1 | OpenAI Research | Industry | 5 | 2026-03-15 | 4.8 | research.openai.com |
| 2 | Nature AI Ethics | Academic | 5 | 2026-02-28 | 4.9 | nature.com/ai-ethics |
| 3 | AI Now Institute | Industry | 4 | 2026-03-10 | 4.2 | ainowinstitute.org |

## Source Distribution
- Web: 2 | Academic: 3 | Industry: 2 | Government: 1 | Social: 0

## Reliability Summary
- High (4-5): 6 sources
- Medium (3): 2 sources
- Low (1-2): 0 sources
```

## Validation Checklist

| Check | Criteria | Pass/Fail |
|-------|----------|-----------|
| **Authority Verification** | Each source has documented authority level (1-5) | ☐ |
| **Freshness Dating** | All sources include publication/update dates | ☐ |
| **URL Validation** | All links are live and accessible | ☐ |
| **Distribution Balance** | No single source type exceeds 70% of total | ☐ |
| **Quality Threshold** | Average reliability ≥ 3.0/5 across all sources | ☐ |
| **Scope Focus** | All sources relate to single research topic | ☐ |

## Usage Guidelines

### When to Use
- Competitive intelligence gathering (curate industry sources)
- Academic research prep (rank papers and journals)
- Due diligence investigations (score source credibility)
- Content strategy research (evaluate topic authorities)

### Quality Criteria
- **Authority 5**: Government agencies, peer-reviewed journals
- **Authority 4**: Industry leaders, established news outlets
- **Authority 3**: Professional blogs, trade publications
- **Authority 2**: General websites, unverified sources
- **Authority 1**: Social media, anonymous posts

### Anti-Patterns
- Including sources without reliability scores
- Mixing different research topics in one dossier
- Over-weighting quantity vs quality (prefer 10 great sources over 50 mediocre)