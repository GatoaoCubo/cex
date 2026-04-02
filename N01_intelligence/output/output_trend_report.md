---
id: p10_out_trend_report
kind: output
pillar: P10
title: "Output: Trend Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
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

### 1. {{TREND_NAME}} {{📈|📊|📉}}
- **Momentum**: {{rising|stable|declining}} ({{%_change}} over {{period}})
- **Confidence**: {{0.1-1.0}} ({{evidence_count}} data points, {{source_diversity}} sources)
- **Impact**: {{high|medium|low}} (affects {{audience_size}} {{audience_type}})
- **Evidence**: {{quantified_metrics}} + {{qualitative_signals}}
- **So what?**: {{specific_action}} by {{timeframe}} or {{risk/opportunity}}

### 2. {{TREND_NAME}} {{📈|📊|📉}}
- **Momentum**: {{rising|stable|declining}} ({{%_change}} over {{period}})
- **Confidence**: {{0.1-1.0}} ({{evidence_count}} data points, {{source_diversity}} sources)
- **Impact**: {{high|medium|low}} (affects {{audience_size}} {{audience_type}})
- **Evidence**: {{quantified_metrics}} + {{qualitative_signals}}
- **So what?**: {{specific_action}} by {{timeframe}} or {{risk/opportunity}}

## Trend Matrix

| Trend | Momentum | Confidence | Impact | Action Required |
|-------|----------|-----------|--------|-----------------|
| {{NAME}} | 📈/📊/📉 {{%}} | {{0.1-1.0}} | H/M/L | {{verb}} {{target}} by {{date}} |
| {{NAME}} | 📈/📊/📉 {{%}} | {{0.1-1.0}} | H/M/L | {{verb}} {{target}} by {{date}} |

## Projections (6-12 months)
- **{{trend_1}}**: {{current_state}} → {{projected_state}} ({{probability}}%)
- **{{trend_2}}**: {{current_state}} → {{projected_state}} ({{probability}}%)
- **Wildcards**: {{low_probability_high_impact_scenarios}}

## Sources
{{CITATION_FORMAT}}: [Title](URL) - {{data_type}}, {{sample_size}}, {{date}}
```