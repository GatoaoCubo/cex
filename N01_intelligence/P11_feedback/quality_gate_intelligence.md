---
id: p11_qg_intelligence
kind: quality_gate
8f: F7_govern
pillar: P11
title: "N01 Quality Gate — Research Output Validation"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [quality_gate, n01, research, triangulation, freshness]
tldr: "10 checks for research output: source count, triangulation, freshness, citation format, confidence scoring, brand alignment."
density_score: 0.93
related:
  - p03_sp_intelligence_nucleus
  - p01_kc_confidence_scoring
  - n01_qg_intelligence
  - p10_out_source_dossier
  - p07_rubric_intelligence
  - p01_kc_source_triangulation
  - p10_lr_research_sessions
  - p12_wf_intelligence
  - p01_kc_intelligence_best_practices
  - bld_examples_runtime_state
---

# N01 Quality Gate

## Hard Gates (fail = reject)

| ID | Check | Rationale |
|----|-------|-----------|
| H01 | Minimum 3 sources cited per major claim | Triangulation is mandatory |
| H02 | Every source has URL + access date | Unverifiable sources are worthless |
| H03 | Confidence score on every key finding | Reader must know certainty level |
| H04 | No data older than 90 days without ⚠️ warning | Stale data misleads |
| H05 | Output follows assigned template | Consistency across deliverables |

## Soft Scoring

| # | Dimension | Weight | 1 (Poor) | 10 (Excellent) |
|---|-----------|--------|----------|----------------|
| 1 | Source diversity (web + academic + industry) | 1.0 | All from 1 type | 3+ source types |
| 2 | Actionable insights (not just data) | 1.0 | Raw data dump | Every finding has "so what?" |
| 3 | Competitive grid completeness | 0.8 | Missing competitors | All major players + dimensions |
| 4 | Visual structure (tables, grids) | 0.6 | Wall of text | Structured with tables |
| 5 | Brand context alignment | 0.6 | Generic research | Through lens of user's market |

## Application Guide

| Stage | Action | Example |
|-------|--------|---------|
| **Pre-research** | Define confidence thresholds | "High confidence" = 3+ sources agree |
| **During research** | Track source types in real-time | Academic: 2, Industry: 1, Web: 3 |
| **Post-research** | Validate each claim against H01-H05 | "Market size $50B" → 3 sources + confidence score |
| **Before delivery** | Run final gate check | All hard gates PASS, soft score ≥7.0 |

## Anti-patterns

- **Single source syndrome**: One great source ≠ validated claim
- **Stale data masquerading**: 2023 data presented as current without warning
- **Confidence inflation**: "High confidence" without multi-source backing

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_intelligence_nucleus]] | upstream | 0.30 |
| [[p01_kc_confidence_scoring]] | upstream | 0.26 |
| [[n01_qg_intelligence]] | sibling | 0.26 |
| [[p10_out_source_dossier]] | upstream | 0.25 |
| [[p07_rubric_intelligence]] | upstream | 0.25 |
| [[p01_kc_source_triangulation]] | upstream | 0.25 |
| [[p10_lr_research_sessions]] | upstream | 0.24 |
| [[p12_wf_intelligence]] | downstream | 0.24 |
| [[p01_kc_intelligence_best_practices]] | upstream | 0.22 |
| [[bld_examples_runtime_state]] | upstream | 0.21 |
