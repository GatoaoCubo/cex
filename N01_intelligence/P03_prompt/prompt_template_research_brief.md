---
id: prompt_template_research_brief
kind: prompt_template
pillar: P03
nucleus: n01
title: "N01 Research Brief Prompt Template"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [prompt_template, research_brief, n01, analytical_envy, intelligence_output]
tldr: "Structured prompt template for generating N01 research briefs: slots for topic, competitors, evidence standard, audience, and depth. Output template enforces Analytical Envy with mandatory competitive benchmarking sections."
density_score: 0.88
---

<!-- 8F: F1 constrain=P03/prompt_template F2 become=prompt-template-builder F3 inject=system_prompt_n01_research+action_prompt_n01+reasoning_strategy_n01+prompt_template_intelligence F4 reason=a template codifies best practice into a reusable structure -- every research brief follows the same high-quality format without reinventing it each time F5 call=cex_compile F6 produce=prompt_template_research_brief.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P03_prompt/ -->

## Purpose

Research briefs are the primary N01 output format.
This template defines both:
1. The INPUT prompt structure (what to ask N01)
2. The OUTPUT brief structure (what N01 must produce)

Using this template ensures every brief is comparable, searchable, and quality-gated.

## Input Prompt Template

```
Research Brief Request
======================
Topic: {TOPIC}
Research Goal: {RESEARCH_GOAL}
Depth: {DEPTH: exploratory | standard | deep}
Evidence Standard: {STANDARD: low | medium | high}
Competitors to Include: {COMPETITORS: comma-separated or "auto"}
Target Audience: {AUDIENCE: executive | analyst | technical | investor}
Time Sensitivity: {FRESHNESS: current (< 30d) | standard (< 90d) | historical}
Output Length: {LENGTH: brief (500-1000w) | standard (1500-2500w) | full (3000-5000w)}
Due By: {DEADLINE or "ASAP"}

Special Instructions: {INSTRUCTIONS or "none"}
```

## Output Brief Template

```markdown
# Research Brief: {TOPIC}
**Date**: {date}
**Author**: N01 Intelligence
**Evidence Standard**: {STANDARD}
**Overall Confidence**: [X.XX]

---

## Executive Summary
One-paragraph synthesis. Include: main finding, competitive position, key implication.
[confidence: X.XX] | Sources: N

---

## Market Context
| Metric | Value | Source | Date | Confidence |
|--------|-------|--------|------|-----------|

---

## Entity Analysis: {PRIMARY_TOPIC}

### Profile
| Attribute | Value | Source |
|-----------|-------|--------|

### Strengths
| Strength | Evidence | Confidence |
|----------|----------|-----------|

### Weaknesses
| Weakness | Evidence | Confidence |
|----------|----------|-----------|

---

## Competitive Benchmark (REQUIRED by Analytical Envy)

| Metric | {PRIMARY} | {COMPETITOR_1} | {COMPETITOR_2} | Category Avg |
|--------|-----------|----------------|----------------|-------------|

### Ranking
| Rank | Entity | Score | Rationale |
|------|--------|-------|-----------|

---

## Key Findings

### Finding 1: {HEADLINE}
Evidence: [data + source]
Confidence: [X.XX]
Competitive context: [vs. who?]
Implication: [so what?]

### Finding 2-N: [repeat pattern]

---

## Counter-Argument
[Strongest evidence AGAINST the main conclusion]
[confidence: X.XX in counter-argument]

---

## Research Gaps
| Gap | Why Unknown | How to Fill |
|-----|------------|------------|

---

## Actionable Implications
| Implication | Target | Urgency | Success Metric |
|-------------|--------|---------|----------------|

---

## Sources
| # | URL | Title | Date | Category | Confidence Contribution |
|---|-----|-------|------|----------|------------------------|
```

## Template Slots Reference

| Slot | Required | Valid Values | Notes |
|------|----------|-------------|-------|
| TOPIC | yes | string | research subject |
| DEPTH | yes | exploratory / standard / deep | determines source layers used |
| STANDARD | yes | low / medium / high | maps to evidence requirements |
| COMPETITORS | no | list or "auto" | "auto" = N01 identifies top 3 |
| AUDIENCE | yes | executive / analyst / technical / investor | adjusts technicality of output |
| FRESHNESS | yes | current / standard / historical | controls source date filter |
| LENGTH | yes | brief / standard / full | controls output depth |

## Comparison: Brief Formats

| Format | Competitive Section | Confidence Scores | Structured | N01 Fit |
|--------|--------------------|--------------------|------------|---------|
| Free-form report | optional | optional | no | inconsistent quality |
| Executive slide | no | no | partial | missing evidence |
| This template | mandatory | mandatory | yes | optimal |
| Analyst report (Gartner) | yes | no | yes | benchmark |

N01 advantage over Gartner: confidence scores are explicit, not implied.
