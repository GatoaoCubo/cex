---
id: p07_sr_commercial
kind: scoring_rubric
pillar: P07
title: "N06 Scoring Rubric — Dual Brand + Monetization"
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n06_commercial
domain: brand-identity-monetization
max_score: 10.0
min_pass: 8.0
golden: 9.0
quality: 8.9
updated: 2026-04-07
tags: [scoring_rubric, commercial, N06, brand, monetization, dual]
tldr: "Dual scoring: BRAND (archetype 0-3, voice 0-2, positioning 0-2, visual 0-2, narrative 0-1) + MONETIZATION (pricing 0-3, funnel 0-2, conversion 0-2, revenue 0-2, market 0-1). Average to 10. Min 8.0, golden 9.0."
density_score: 0.94
axioms:
  - "NEVER self-score — peer nucleus reviews only. quality: null until reviewed."
  - "Min 8.0 to publish, 9.0 is golden. Below 8.0 = rejected, re-work required."
linked_artifacts:
  primary: p07_qg_commercial
  related: [p02_agent_commercial_nucleus, n06_schema_brand_audit, n06_schema_brand_book]
---

# N06 Scoring Rubric — Brand + Monetization

## Scoring Model

N06 produces two categories of artifacts. Score is averaged:
`final_score = (brand_score + monetization_score) / 2`

For pure brand artifacts, use Brand rubric only.
For pure monetization artifacts, use Monetization rubric only.
For mixed artifacts (e.g., branded pricing page), average both.

## BRAND Rubric (10 points)

| Dimension | Points | Criteria |
|-----------|--------|----------|
| **Archetype** | 0-3 | 0=none, 1=named but generic, 2=aligned with tone+visual, 3=deeply integrated with shadow+traits |
| **Voice** | 0-2 | 0=no voice calibration, 1=tone described, 2=full 5D scores + do/don't + calibration phrases |
| **Positioning** | 0-2 | 0=no UVP, 1=generic positioning, 2=specific UVP + differentiator + competitive matrix |
| **Visual** | 0-2 | 0=no colors, 1=palette defined, 2=full palette + fonts + contrast + dark mode + psychology |
| **Narrative** | 0-1 | 0=no story, 1=origin + mission + vision + transformation arc present |

### Brand Score Guide

| Score | Quality |
|-------|---------|
| 9-10 | Exceptional — brand book is publication-ready, all 32 blocks, consistency ≥ 0.95 |
| 8-8.9 | Strong — 18+ blocks, consistency ≥ 0.85, clear archetype alignment |
| 7-7.9 | Adequate — core identity present but gaps in voice or visual |
| 6-6.9 | Weak — archetype named but not integrated, voice inconsistent |
| < 6 | Failing — fundamental identity gaps, re-run Brand Discovery |

## MONETIZATION Rubric (10 points)

| Dimension | Points | Criteria |
|-----------|--------|----------|
| **Pricing** | 0-3 | 0=no price, 1=flat price only, 2=tiered with rationale, 3=tiered + anchor + psychology + projections |
| **Funnel** | 0-2 | 0=no funnel, 1=basic TOFU/MOFU/BOFU, 2=full sequence with copy + conversion benchmarks |
| **Conversion** | 0-2 | 0=no metrics, 1=benchmarks referenced, 2=stage-specific rates + optimization recommendations |
| **Revenue** | 0-2 | 0=no model, 1=basic projection, 2=MRR/LTV scenarios with sensitivity analysis |
| **Market** | 0-1 | 0=generic, 1=market-specific (BR: BRL/PIX/parcelamento, platform named) |

### Monetization Score Guide

| Score | Quality |
|-------|---------|
| 9-10 | Exceptional — implementable pricing + funnel + revenue model with projections |
| 8-8.9 | Strong — tiered pricing, funnel stages defined, conversion benchmarks present |
| 7-7.9 | Adequate — pricing exists but generic, funnel incomplete |
| 6-6.9 | Weak — single price, no funnel, no revenue model |
| < 6 | Failing — no commercial viability analysis |

## Combined Scoring

| Artifact Type | Rubric Used | Example |
|---------------|-------------|---------|
| Brand Book | Brand only | 32-block brand book |
| brand_config.yaml | Brand only | Config file |
| Voice Guide | Brand only | Voice calibration doc |
| Pricing Page | Average(Brand + Monetization) | Branded pricing page |
| Course Outline | Average(Brand + Monetization) | On-brand course structure |
| Funnel Sequence | Average(Brand + Monetization) | Brand-voice funnel copy |
| Revenue Model | Monetization only | MRR/LTV projection |

## Thresholds

| Level | Score | Action |
|-------|-------|--------|
| Gold | 9.0+ | Publish, archive as exemplar |
| Pass | 8.0-8.9 | Publish, note improvements |
| Review | 7.0-7.9 | Revise weak dimensions |
| Fail | < 7.0 | Reject, re-build |

## Boundary

Criterio de avaliacao com framework. NAO eh benchmark (nao mede) nem quality_gate (P11, nao bloqueia).


## 8F Pipeline Function

Primary function: **GOVERN**
