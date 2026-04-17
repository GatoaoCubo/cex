---
id: p10_out_market_snapshot
kind: output
pillar: P10
title: "Output: Market Snapshot"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.1
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

## Example Output
```markdown
# Market Snapshot: SaaS Project Management
**Geography**: North America | **Date**: 2026-04-01 | **Sources**: 6

## Market Size
| Metric | Value | Source | Confidence |
|--------|-------|--------|-----------|
| TAM | $47.2B | Gartner 2026 | High |
| SAM | $12.8B | Internal analysis | Medium |
| SOM | $380M | Market model | Medium |
| Growth Rate (CAGR) | 11.2% | IDC Research | High |

## Segments
| Segment | Size | Growth | Our Position |
|---------|------|--------|-------------|
| Enterprise (1000+ employees) | $8.2B | 8% | Not present |
| SMB (10-999 employees) | $3.1B | 15% | Targeting |
| Freelancer/Agency | $1.5B | 22% | Strong fit |

## Key Metrics
- Active players: 180+ vendors
- Avg. ticket: $12/user/month
- Dominant model: Per-seat subscription
- Regulatory: GDPR/SOC2 required

## Sources
1. Gartner Magic Quadrant 2026
2. IDC SaaS Market Report
3. Company annual reports (top 5)
4. G2 pricing data analysis
5. Survey: 2,400 project managers
6. Venture capital deal flow
```