---
id: p10_out_taxonomy_map
kind: output
8f: F6_produce
pillar: P10
title: "Output: Taxonomy Map"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [output, n04, taxonomy, map, classification, visual]
tldr: "Visual taxonomy: kinds × pillars × domains. Coverage heatmap."
density_score: 0.91
related:
  - p10_out_gap_report
  - output_kc_quality_audit_20260408
  - p10_out_sql_migration
  - spec_mission_100pct_coverage
  - self_review_2026-04-02
  - p10_out_knowledge_graph
  - p06_schema_taxonomy
  - p04_tool_taxonomy_builder
  - leverage_map_v2_n05_verify
  - self_audit_newpc
---

# Output: Taxonomy Map

## Usage Guidelines

| When to Use | When NOT to Use |
|-------------|-----------------|
| Knowledge audit across pillars | Single pillar analysis |
| Gap identification for new KCs | Quality assessment of existing KCs |
| Strategic KC roadmapping | Tactical KC fixes |
| Cross-domain coverage planning | Domain-specific deep dives |

## Template
```markdown
# Taxonomy Map
**Date**: {{DATE}} | **Total Kinds**: {{COUNT}} | **Total KCs**: {{COUNT}}

## Coverage Heatmap (kinds × pillars)

| Kind | P01 | P02 | P03 | P04 | P06 | P07 | P08 | P11 | P12 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| agent | ✅ | ✅ | ✅ | | | | | | |
| workflow | ✅ | | | | | | | | ✅ |
| knowledge_card | ✅ | | | | | | | | |
| schema | | | | | ✅ | | | | |

## Domain Distribution
| Domain | KC Count | Coverage |
|--------|----------|----------|
| {{DOMAIN}} | {{N}} | {{%}} |

## Gaps (empty cells above)
- {{KIND}} × {{PILLAR}}: no KC exists
```

## Interpretation Guide

| Coverage Pattern | Action Required |
|------------------|-----------------|
| 0-25% coverage | Create foundational KCs |
| 25-75% coverage | Fill critical gaps |
| 75%+ coverage | Quality improvement focus |
| Scattered coverage | Consolidate related KCs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_gap_report]] | sibling | 0.31 |
| [[output_kc_quality_audit_20260408]] | upstream | 0.31 |
| [[p10_out_sql_migration]] | sibling | 0.29 |
| [[spec_mission_100pct_coverage]] | upstream | 0.28 |
| [[self_review_2026-04-02]] | upstream | 0.25 |
| [[p10_out_knowledge_graph]] | sibling | 0.24 |
| [[p06_schema_taxonomy]] | upstream | 0.23 |
| [[p04_tool_taxonomy_builder]] | upstream | 0.23 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.22 |
| [[self_audit_newpc]] | upstream | 0.22 |
