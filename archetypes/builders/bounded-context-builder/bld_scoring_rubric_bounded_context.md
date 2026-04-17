---
id: bld_scoring_rubric_bounded_context
kind: scoring_rubric
pillar: P07
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [bounded_context, scoring, rubric]
title: "Scoring Rubric: bounded_context"
---
# Scoring Rubric: bounded_context
## 5 Dimensions
| # | Dimension | Weight | Description |
|---|-----------|--------|-------------|
| D1 | Scope clarity | 30% | Semantic scope_statement; what model applies here and NOT elsewhere |
| D2 | Aggregate completeness | 25% | All key aggregates listed with roles and invariants |
| D3 | Integration architecture | 20% | Neighbors + patterns (ACL/OHS/CF) with rationale |
| D4 | Vocabulary governance | 15% | domain_vocabulary referenced; BC-specific terms noted |
| D5 | Context map position | 10% | Upstream + downstream contexts identified |

## Scoring Formula
`score = (D1*0.30 + D2*0.25 + D3*0.20 + D4*0.15 + D5*0.10) * 10`

## Dimension Scoring Guide
### D1 Scope clarity (0-10)
- 10: scope_statement is semantic (domain model), not technical; what's IN and what's NOT
- 7: semantic but only covers what's in, not what's excluded
- 4: technical boundary description ("service that handles X")
- 0: missing scope_statement

### D2 Aggregate completeness (0-10)
- 10: all major aggregates with roles + at least 1 invariant each
- 7: aggregates listed, some missing invariants
- 4: aggregates listed without roles or invariants
- 0: no aggregates section

### D3 Integration architecture (0-10)
- 10: >= 2 neighbors with pattern + direction + rationale
- 6: neighbors named, patterns without rationale
- 3: some neighbors mentioned
- 0: no integration documentation

### D4 Vocabulary governance (0-10)
- 10: domain_vocabulary reference + key BC-specific terms noted
- 5: vocabulary reference only
- 0: no vocabulary governance

### D5 Context map position (0-10)
- 10: upstream + downstream contexts with integration types
- 5: one direction documented
- 0: no context map position
