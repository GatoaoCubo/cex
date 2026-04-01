---
id: p10_out_trend_report
kind: output
pillar: P10
title: "Output: Trend Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: null
tags: [output, n01, trend, report, momentum]
tldr: "Trend analysis: 3-5 trends with momentum, confidence, evidence, and 'so what?' per finding."
density_score: 0.91
---

# Output: Trend Report

## Template
```markdown
# Trend Report: {{DOMAIN}}
**Period**: {{TIMEFRAME}} | **Sources**: {{COUNT}} | **Date**: {{DATE}}

## Trends Detected

### 1. {{TREND_NAME}} {{MOMENTUM_EMOJI}}
- **Momentum**: {{rising|stable|declining}}
- **Confidence**: {{SCORE}} ({{evidence_count}} data points)
- **Impact**: {{high|medium|low}}
- **Evidence**: {{KEY_EVIDENCE}}
- **So what?**: {{ACTIONABLE_INSIGHT}}

### 2. {{TREND_NAME}} {{MOMENTUM_EMOJI}}
(same structure)

## Trend Matrix

| Trend | Momentum | Confidence | Impact | Action |
|-------|----------|-----------|--------|--------|
| {{NAME}} | 📈/📊/📉 | {{SCORE}} | H/M/L | {{ACTION}} |

## Projections (6-12 months)
- {{PROJECTION_1}}
- {{PROJECTION_2}}

## Sources
{{CITATIONS}}
```
