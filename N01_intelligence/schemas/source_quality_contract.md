---
id: p06_schema_source_quality
kind: schema
pillar: P06
title: "Source Quality Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 8.6
tags: [schema, n01, source, quality, scoring, citation]
tldr: "Source scoring: authority (1-5), freshness, bias assessment, accessibility. Every cited source gets a quality card."
density_score: 0.93
---

# Source Quality Contract

## Source Quality Card

| Field | Type | Description |
|-------|------|-------------|
| url | string | Full URL |
| title | string | Page/document title |
| type | enum: web\|academic\|industry\|government\|social\|internal | Source type |
| authority | int 1-5 | 1=blog, 2=news, 3=industry report, 4=academic, 5=primary/government |
| freshness | date | Publication or last update date |
| bias | enum: low\|medium\|high | Potential bias assessment |
| accessibility | enum: free\|paywall\|registration | Access level |
| accessed_at | date | When we read it |
| reliability | float 0-1 | Computed: (authority/5 × 0.4) + (freshness_score × 0.3) + (bias_inv × 0.3) |

## Freshness Scoring
| Age | Score |
|-----|-------|
| <30 days | 1.0 |
| 30-90 days | 0.8 |
| 90-180 days | 0.5 |
| 180-365 days | 0.3 |
| >1 year | 0.1 ⚠️ |
