---
id: p11_opt_pool_density
kind: optimizer
8f: F8_collaborate
pillar: P11
title: "Optimizer: Pool Density Improvement"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [optimizer, pool, density, quality, feedback]
tldr: "Pool density optimizer: detect low-density artifacts (< 0.8), identify anti-patterns, trigger targeted rewrites to reach >= 0.85"
max_bytes: 1024
density_score: 0.88
source: organization-core/records/framework/docs/LAWS_v3_PRACTICAL.md + CEX 5D rubric
linked_artifacts:
  rubric: p07_sr_5d_scoring
  gate: p11_qg_cex_quality
related:
  - p10_ax_scout_before_create
  - p11_qg_shokunin_pool
  - p10_rs_edison
  - p07_sr_5d_scoring
  - p11_qg_marketing_artifacts
  - bld_tools_naming_rule
  - p01_kc_artifact_quality_evaluation_methods
  - p10_ax_shokunin_quality
  - p01_kc_creation_best_practices
  - p11_qg_orchestration_artifacts
---

# Optimizer: Pool Density Improvement

## Metric

```yaml
density_score:
  target: >= 0.85
  minimum: >= 0.80 (pool eligible)
  golden: >= 0.90
  definition: "information_per_token = unique_facts / total_tokens"
```

## Detection: Low-Density Signals

| Signal | Pattern | Penalty |
|--------|---------|---------|
| Restatement opening | First paragraph = title rephrased | -0.10 D1 |
| Empty sections | H2 with single `_TBD_` or `_See above_` | -0.15 D1 |
| Filler phrases | "As we can see", "It's important to note" | -0.05 per instance |
| Duplicate bullets | Same fact stated 2+ times in different words | -0.10 D1 |
| Over-explaining obvious | "Note: YAML uses indentation" in expert doc | -0.05 D1 |

## Optimization Cycle

```
1. MEASURE:  Grep for anti-patterns → calculate density_score
2. IDENTIFY: Find top 3 density killers in artifact
3. REWRITE:  Apply targeted edits (not full rewrite):
             - Remove restatement opening
             - Compress duplicate bullets into 1
             - Delete filler phrases
             - Replace vague sections with concrete examples
4. VALIDATE: Recalculate density_score → must improve >= 0.05
5. GATE:     If >= 0.85 → pool write. If < 0.80 → repeat cycle.
```

## Anti-Pattern Fixes

```markdown
# BEFORE (density: 0.71)
Scout Before Create is a very important principle in organization.
It means that before you create anything new, you should first
look to see if something similar already exists in the pool.
This is because creating duplicates wastes time.

# AFTER (density: 0.90)
Before any Write: Glob/Grep pool first.
>= 60% similarity → adapt existing. < 60% → build new.
Duplicates cause brain search conflicts and wasted 20-40min builds.
```

## Automation Hook

```python
# Pre-pool-write hook (records/core/python/density_checker.py)
score = calculate_density(artifact_text)
if score < 0.80:
    raise QualityGateError(f"density {score:.2f} < 0.80 — optimize before pooling")
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_ax_scout_before_create]] | upstream | 0.36 |
| [[p11_qg_shokunin_pool]] | related | 0.27 |
| [[p10_rs_edison]] | upstream | 0.24 |
| [[p07_sr_5d_scoring]] | upstream | 0.22 |
| [[p11_qg_marketing_artifacts]] | related | 0.21 |
| [[bld_tools_naming_rule]] | upstream | 0.21 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.20 |
| [[p10_ax_shokunin_quality]] | upstream | 0.20 |
| [[p01_kc_creation_best_practices]] | upstream | 0.20 |
| [[p11_qg_orchestration_artifacts]] | related | 0.19 |
