---
id: p07_sr_5d_scoring
kind: scoring_rubric
8f: F7_govern
pillar: P07
title: "Scoring Rubric: 5D Quality Framework"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.1
tags: [scoring, rubric, 5d, quality, evaluation]
tldr: "5D scoring: Density + Density + Accuracy + Reusability + Actionability — each 0-10, averaged for final score"
max_bytes: 2048
density_score: 0.91
source: organization-core/records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 13 Shokunin)
linked_artifacts:
  gate: p11_qg_cex_quality
  validator: p06_val_quality_score
related:
  - p11_qg_shokunin_pool
  - p01_kc_artifact_quality_evaluation_methods
  - p11_opt_pool_density
  - bld_knowledge_card_scoring_rubric
  - p11_qg_scoring-rubric
  - p08_law_shokunin
  - p07_sr_5_dimension_quality
  - bld_knowledge_card_quality_gate
  - p10_ax_shokunin_quality
  - bld_memory_scoring_rubric
---

# Scoring Rubric: 5D Quality Framework

## Overview

The 5D framework evaluates all organization pool artifacts on 5 dimensions. Final score = weighted average. Used by quality gates before pool writes and during golden promotion.

## Dimensions

| Dim | Name | Weight | Definition |
|-----|------|--------|------------|
| D1 | Density | 0.25 | Information per token ratio. No fluff, every sentence adds value |
| D2 | Accuracy | 0.25 | Factual correctness, verified against source, no hallucinated data |
| D3 | Reusability | 0.20 | Can be used as-is or adapted for similar tasks without modification |
| D4 | Actionability | 0.20 | Reader can act on it immediately — clear steps, not vague guidance |
| D5 | Structure | 0.10 | Well-organized, consistent formatting, navigable |

## Scoring Scale (per dimension)

| Score | Label | Criteria |
|-------|-------|----------|
| 9.5-10 | Masterwork | Exemplary — would use as reference for others |
| 8.0-9.4 | Skilled | Solid, minor improvements possible |
| 7.0-7.9 | Acceptable | Works but has notable gaps |
| 5.0-6.9 | Weak | Significant issues, needs rework |
| < 5.0 | Reject | Discard and rebuild from scratch |

## Calculation

```python
def score_5d(d1, d2, d3, d4, d5):
    weights = [0.25, 0.25, 0.20, 0.20, 0.10]
    dims = [d1, d2, d3, d4, d5]
    return round(sum(w * d for w, d in zip(weights, dims)), 1)

# Example: dense, accurate, highly reusable, actionable, clean structure
score_5d(9.5, 9.0, 9.2, 8.8, 9.0)  # → 9.15 → rounds to 9.2
```

## Anti-Patterns (D1 Density failures)

| Anti-Pattern | Penalty |
|-------------|---------|
| Opening paragraph restates the title | -1.0 D1 |
| "As you can see..." filler phrases | -0.5 D1 |
| Redundant bullet points restating same fact | -1.0 D1 |
| Section with only 1 bullet | -0.5 D5 |

## Application in organization

```
Pool write:   score >= 8.0 (D1 + D2 must be >= 7.5 individually)
Golden:       score >= 9.5 (all dims >= 9.0)
Shokunin cap: score >= 9.5 → "Would I be proud of this?" test
```

## Example Scoring

```yaml
artifact: p04_skill_ml_ads
d1_density: 9.5  # extremely dense, 0 filler
d2_accuracy: 9.0  # verified funnel metrics, real data
d3_reusability: 9.5  # modular, adapts to other ad platforms
d4_actionability: 9.2  # step-by-step execution, quality gates
d5_structure: 9.0  # clean tables, consistent headers
final_score: 9.3   # Skilled → Pool eligible
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_shokunin_pool]] | downstream | 0.29 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.24 |
| [[p11_opt_pool_density]] | downstream | 0.24 |
| [[bld_knowledge_card_scoring_rubric]] | upstream | 0.24 |
| [[p11_qg_scoring-rubric]] | downstream | 0.23 |
| [[p08_law_shokunin]] | downstream | 0.23 |
| [[p07_sr_5_dimension_quality]] | sibling | 0.23 |
| [[bld_knowledge_card_quality_gate]] | downstream | 0.22 |
| [[p10_ax_shokunin_quality]] | downstream | 0.22 |
| [[bld_memory_scoring_rubric]] | downstream | 0.21 |
