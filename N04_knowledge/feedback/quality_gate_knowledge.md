---
id: p11_qg_knowledge
kind: quality_gate
pillar: P11
title: "N04 Quality Gate — Knowledge Card Validation"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: null
tags: [quality_gate, n04, knowledge, density, freshness, taxonomy]
tldr: "10 checks for KCs: frontmatter complete, density >= 0.85, taxonomy valid, no duplicates, export-ready."
density_score: 0.93
---

# N04 Quality Gate

## Hard Gates

| ID | Check | Rationale |
|----|-------|-----------|
| H01 | All required frontmatter fields present | Incomplete KC breaks indexing |
| H02 | kind exists in kinds_meta.json | Invalid kind = unroutable |
| H03 | density_score >= 0.85 | Low density = wasted tokens |
| H04 | No duplicate KC (same id or >90% content overlap) | Duplicates pollute search |
| H05 | Compiles successfully (cex_compile.py) | Invalid YAML = broken pipeline |

## Soft Scoring

| # | Dimension | Weight | 1 (Poor) | 10 (Excellent) |
|---|-----------|--------|----------|----------------|
| 1 | Density (signal per token) | 1.0 | Filler prose | Every sentence carries info |
| 2 | Taxonomy accuracy | 0.8 | Wrong kind/pillar | Perfect classification |
| 3 | Freshness (<90 days) | 0.8 | >1 year old | <30 days |
| 4 | Export-readiness (JSONL/SQL/YAML) | 0.6 | Only .md | Triple-export ready |
| 5 | Cross-references (linked_artifacts) | 0.4 | No links | 3+ related KCs linked |
