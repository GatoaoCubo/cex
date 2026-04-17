---
id: bld_scoring_rubric_domain_vocabulary
kind: scoring_rubric
pillar: P07
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [domain_vocabulary, scoring, rubric]
title: "Scoring Rubric: domain_vocabulary"
---
# Scoring Rubric: domain_vocabulary
## 5 Dimensions
| # | Dimension | Weight | Description |
|---|-----------|--------|-------------|
| D1 | Term completeness | 30% | All terms have definition + anti_patterns + industry_standard |
| D2 | Drift prevention | 25% | Anti-patterns prevent semantic drift; deprecated terms tracked |
| D3 | BC scoping | 20% | Vocabulary scoped to single BC; governed_agents explicit |
| D4 | Lifecycle management | 15% | Proposed/active/deprecated states used; replacements documented |
| D5 | Enforceability | 10% | Loading instructions present; F2b SPEAK integration noted |

## Scoring Formula
`score = (D1*0.30 + D2*0.25 + D3*0.20 + D4*0.15 + D5*0.10) * 10`

## Dimension Scoring Guide
### D1 Term completeness (0-10)
- 10: every term has definition + anti_patterns + industry_standard
- 7: all terms defined, some missing anti_patterns
- 4: definitions only, no anti_patterns or references
- 0: terms listed without definitions

### D2 Drift prevention (0-10)
- 10: all terms have anti_patterns + deprecated terms tracked
- 6: most terms have anti_patterns
- 3: some anti_patterns present
- 0: no anti_patterns

### D3 BC scoping (0-10)
- 10: bounded_context + governed_agents both specific
- 6: BC named, governed_agents vague
- 0: BC or governed_agents missing

### D4 Lifecycle management (0-10)
- 10: all 3 states used (proposed/active/deprecated)
- 5: active + deprecated only
- 0: only active state

### D5 Enforceability (0-10)
- 10: F2b SPEAK loading instructions + governed_agents list
- 5: governed_agents listed, no loading instructions
- 0: no enforceability guidance
