---
id: p06_schema_competitive_analysis
kind: schema
pillar: P06
title: "Competitive Analysis Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 8.7
tags: [schema, n01, competitive, grid, analysis]
tldr: "Competitor grid schema: N competitors × M dimensions. Required: name, positioning, pricing, strengths, weaknesses, market share estimate."
density_score: 0.92
---

# Competitive Analysis Contract

## Grid Structure
```
Competitors (rows) × Dimensions (columns) = Competitive Grid
```

## Required Dimensions

| Dimension | Type | Description |
|-----------|------|-------------|
| name | string | Company/product name |
| positioning | string | 1-sentence market position |
| pricing_model | enum: free\|freemium\|subscription\|one-time\|enterprise | How they charge |
| price_range | string | Price range in relevant currency |
| strengths | list[string] | Top 3 competitive advantages |
| weaknesses | list[string] | Top 3 vulnerabilities |
| market_share_est | enum: leader\|major\|mid\|niche\|emerging | Estimated position |
| target_audience | string | Primary audience |

## Optional Dimensions
| Dimension | Type |
|-----------|------|
| founded | int (year) |
| funding | string |
| tech_stack | list[string] |
| key_features | list[string] |
| differentiator | string |
| threat_level | enum: high\|medium\|low |
