---
id: p10_out_executive_summary
kind: output
pillar: P10
title: "Output: Executive Summary"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.1
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

## Example

```markdown
# Executive Summary: AI Customer Service Implementation
**For**: CEO & COO | **Date**: 2026-04-01 | **Research Depth**: L2

## TL;DR
AI chatbot can reduce support costs by 40% ($2M annually) while improving response time by 80%. Recommend 6-month phased rollout starting Q2.

## Key Findings
1. Current support costs $5M/year with 48hr avg response — confidence: HIGH
2. AI handles 70% of tier-1 inquiries with 95% accuracy — confidence: HIGH
3. Customer satisfaction increases 15% with faster resolution — confidence: MED

## Recommendations
| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| P1 | Deploy AI for tier-1 support | $2M cost savings | M |
| P2 | Retrain 40% of support staff | Reduced attrition | L |

## Risks
- Customer pushback on AI: mitigation = hybrid human handoff
- Integration complexity: mitigation = phased rollout with rollback plan

## Next Steps
1. Vendor selection (30 days)
2. Pilot program Q2 (90 days)
3. Full rollout Q3-Q4

## Sources
Salesforce State of Service 2026, Zendesk Benchmark 2025, Internal Support Analytics
```