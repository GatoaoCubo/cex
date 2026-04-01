---
id: p10_out_market_snapshot
kind: output
pillar: P10
title: "Output: Market Snapshot"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: null
tags: [output, n01, market, tam, sam, som, snapshot]
tldr: "TAM/SAM/SOM estimate + key market metrics + growth rate + segments."
density_score: 0.92
---

# Output: Market Snapshot

## Template
```markdown
# Market Snapshot: {{CATEGORY}}
**Geography**: {{GEO}} | **Date**: {{DATE}} | **Sources**: {{COUNT}}

## Market Size
| Metric | Value | Source | Confidence |
|--------|-------|--------|-----------|
| TAM | {{VALUE}} | {{SOURCE}} | {{SCORE}} |
| SAM | {{VALUE}} | {{SOURCE}} | {{SCORE}} |
| SOM | {{VALUE}} | {{SOURCE}} | {{SCORE}} |
| Growth Rate (CAGR) | {{PERCENT}}% | {{SOURCE}} | {{SCORE}} |

## Segments
| Segment | Size | Growth | Our Position |
|---------|------|--------|-------------|
| {{SEG1}} | {{VALUE}} | {{RATE}} | {{POSITION}} |

## Key Metrics
- Active players: {{COUNT}}
- Avg. ticket: {{VALUE}}
- Dominant model: {{BUSINESS_MODEL}}
- Regulatory: {{STATUS}}

## Sources
{{CITATIONS}}
```
