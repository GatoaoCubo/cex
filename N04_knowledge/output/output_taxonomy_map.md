---
id: p10_out_taxonomy_map
kind: output
pillar: P10
title: "Output: Taxonomy Map"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 8.7
tags: [output, n04, taxonomy, map, classification, visual]
tldr: "Visual taxonomy: kinds × pillars × domains. Coverage heatmap."
density_score: 0.91
---

# Output: Taxonomy Map

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
