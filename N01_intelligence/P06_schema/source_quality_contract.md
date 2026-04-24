---
id: p06_schema_source_quality
kind: schema
8f: F1_constrain
pillar: P06
title: "Source Quality Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [schema, n01, source, quality, scoring, citation]
tldr: "Source scoring: authority (1-5), freshness, bias assessment, accessibility. Every cited source gets a quality card."
density_score: 0.93
related:
  - p10_out_source_dossier
  - p04_tool_search_config
  - p01_kc_source_credibility_scoring_frameworks
  - p10_out_kc_audit_report
  - p01_kc_intelligence_best_practices
  - p06_schema_citation_format
  - p11_qg_intelligence
  - p01_kc_citation
  - p01_kc_source_triangulation
  - bld_config_rag_source
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

## Implementation Guidelines

| When to Use | When NOT to Use | Anti-patterns |
|-------------|-----------------|---------------|
| Research briefs | Internal memos | Scoring opinion as fact |
| Competitive analysis | Quick status updates | Ignoring publication date |
| Market reports | Brainstorm sessions | Missing bias assessment |
| Citation validation | Creative writing | Over-weighting blog posts |

**Workflow**: Score during research → filter <0.4 reliability → flag bias conflicts → archive with metadata

## Usage Examples

| Source | Authority | Freshness | Bias | Reliability | Notes |
|--------|-----------|-----------|------|-------------|-------|
| Federal Reserve paper | 5 | 0.8 (60 days) | low | 0.86 | Primary government source |
| TechCrunch article | 2 | 1.0 (15 days) | medium | 0.50 | News with commercial bias |
| Personal blog | 1 | 0.3 (200 days) | high | 0.22 | Low authority + stale |
| MIT research paper | 4 | 0.5 (120 days) | low | 0.74 | Academic authority |
| Company press release | 3 | 1.0 (5 days) | high | 0.52 | Fresh but high bias |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_source_dossier]] | downstream | 0.35 |
| [[p04_tool_search_config]] | upstream | 0.25 |
| [[p01_kc_source_credibility_scoring_frameworks]] | upstream | 0.24 |
| [[p10_out_kc_audit_report]] | downstream | 0.23 |
| [[p01_kc_intelligence_best_practices]] | upstream | 0.22 |
| [[p06_schema_citation_format]] | sibling | 0.22 |
| [[p11_qg_intelligence]] | downstream | 0.21 |
| [[p01_kc_citation]] | upstream | 0.20 |
| [[p01_kc_source_triangulation]] | upstream | 0.20 |
| [[bld_config_rag_source]] | downstream | 0.19 |
