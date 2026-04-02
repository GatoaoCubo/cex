---
id: p10_out_executive_summary
kind: output
pillar: P10
title: "Output: Executive Summary"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 8.7
tags: [output, n01, executive, summary, decision-maker]
tldr: "1-page synthesis for decision-makers: key findings, recommendations, risks, next steps."
density_score: 0.92
---

# Output: Executive Summary

## Usage Guidelines

| Do | Don't | Why |
|---|---|---|
| Lead with TL;DR impact | Start with background | Executives read top-down |
| Quantify findings (%, $, time) | Use vague terms ("significant") | Numbers drive decisions |
| Limit to 3 key findings | List 5+ findings | Cognitive overload kills action |
| Include confidence levels | Present everything as certain | Risk assessment matters |
| Use effort sizing (S/M/L) | Skip implementation reality | Resource allocation critical |

**When to use**: Post-analysis synthesis for C-level, board presentations, funding requests
**Length target**: 1 page (500-800 words max)
**Timing**: After research complete, before stakeholder meetings

## Template
```markdown
# Executive Summary: {{TOPIC}}
**For**: {{AUDIENCE}} | **Date**: {{DATE}} | **Research Depth**: {{L1|L2|L3}}

## TL;DR
{{2-3 sentences with the single most important finding and recommendation}}

## Key Findings
1. {{FINDING}} — confidence: {{HIGH|MED|LOW}}
2. {{FINDING}} — confidence: {{HIGH|MED|LOW}}
3. {{FINDING}} — confidence: {{HIGH|MED|LOW}}

## Recommendations
| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| P1 | {{ACTION}} | {{IMPACT}} | {{S|M|L}} |
| P2 | {{ACTION}} | {{IMPACT}} | {{S|M|L}} |

## Risks
- {{RISK_1}}: mitigation = {{MITIGATION}}
- {{RISK_2}}: mitigation = {{MITIGATION}}

## Next Steps
1. {{IMMEDIATE_ACTION}}
2. {{SHORT_TERM}}
3. {{LONG_TERM}}

## Sources
{{TOP_5_CITATIONS}}
```