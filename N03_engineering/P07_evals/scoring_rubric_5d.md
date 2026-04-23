---
id: p07_sr_5_dimension_quality
kind: scoring_rubric
pillar: P07
title: 5-Dimension Quality Scoring (5D)
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [scoring-rubric, 5d, quality, dimensions, measurement]
tldr: Every artifact is scored on 5 orthogonal dimensions. Final score = weighted average. Thresholds enforce build/no-build decisions.
density_score: 0.93
related:
  - p07_qg_12_point_validation
  - bld_collaboration_golden_test
  - p03_sp_n03_creation_nucleus
  - bld_collaboration_kind
  - p11_qg_creation_artifacts
  - bld_collaboration_workflow
  - p10_lr_kind_builder
  - p01_kc_artifact_quality_evaluation_methods
  - bld_collaboration_validation_schema
  - skill
---

# 5-Dimension Quality Scoring (5D)

## The 5 Dimensions

| # | Dimension | Weight | What It Measures | 10/10 Looks Like |
|---|-----------|--------|------------------|-------------------|
| D1 | **Structural Integrity** | 25% | Frontmatter, schema compliance, naming, pillar alignment | Perfect 12LP pass, zero structural issues |
| D2 | **Content Density** | 20% | Signal-to-noise ratio, tables over prose, decision trees | density_score >= 0.90, every line carries meaning |
| D3 | **Actionability** | 25% | Can a builder USE this artifact without additional context? | Self-contained, copy-paste usable, no tribal knowledge |
| D4 | **Boundary Discipline** | 15% | Single kind, single responsibility, no scope creep | Artifact does ONE thing, references others for the rest |
| D5 | **Composability** | 15% | Can this artifact combine with others in a crew/pipeline? | Clean inputs/outputs, follows interface contracts |

## Scoring Scale

Each dimension: 1-10 integer.

| Score | Meaning |
|-------|---------|
| 10 | Exemplary. Reference-quality. |
| 9 | Excellent. Minor polish possible. |
| 8 | Good. Publishable without changes. |
| 7 | Acceptable. Needs iteration. |
| 6 | Weak. Specific flaws identified. |
| 5 | Below standard. Major rework. |
| 1-4 | Reject. Rebuild from scratch. |

## Final Score Calculation

```
final = (D1 * 0.25) + (D2 * 0.20) + (D3 * 0.25) + (D4 * 0.15) + (D5 * 0.15)
```

Example: D1=9, D2=8, D3=9, D4=8, D5=9
  = (9*0.25) + (8*0.20) + (9*0.25) + (8*0.15) + (9*0.15)
  = 2.25 + 1.60 + 2.25 + 1.20 + 1.35
  = 8.65

## Threshold Actions

| Final Score | Tier | Action | Signal |
|-------------|------|--------|--------|
| >= 9.5 | GOLDEN | Promote to reference examples | signal(golden) |
| 8.0 - 9.4 | PUBLISH | Commit to repository | signal(complete) |
| 7.0 - 7.9 | ITERATE | Retry F6-F7 (max 2) | no signal yet |
| < 7.0 | REJECT | Delete draft, restart from F4 | signal(failed) |

## Builder-Specific Floors

| Context | Minimum Score | Rationale |
|---------|--------------|-----------|
| N03 (meta-construction) | 8.5 | Builders build builders. Higher standard. |
| N07 (orchestration) | 8.0 | Dispatch artifacts need reliability. |
| N01-N06 (domain) | 8.0 | Standard publication quality. |
| Grid batch (headless) | 8.0 | Same quality as interactive. No degradation. |

## Dimension Deep Dive

### D1: Structural Integrity (25%)

Automated checks:
- Frontmatter: all required fields present and typed correctly
- Schema: sections match pillar schema
- Naming: follows kinds_meta.json convention
- Pillar: file in correct P-directory
- Size: within max_bytes for the kind

### D2: Content Density (20%)

Heuristics:
- Table lines / total lines >= 0.30
- Code block lines / total lines >= 0.15
- Average line length: 40-100 chars (not too sparse, not walls of text)
- No filler phrases ("it is important to note that...")

### D3: Actionability (25%)

The "stranger test": give this artifact to a builder who has never seen
the system. Can they USE it within 2 minutes? If not, D3 < 7.

### D4: Boundary Discipline (15%)

One artifact = one kind = one pillar. If you are writing a knowledge_card
and it starts explaining a workflow, STOP. Create a separate workflow artifact.

### D5: Composability (15%)

Can this artifact be referenced by other artifacts? Does it have clear
inputs and outputs? Can it participate in a builder crew composition?

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_qg_12_point_validation]] | related | 0.27 |
| [[bld_collaboration_golden_test]] | downstream | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.26 |
| [[bld_collaboration_kind]] | downstream | 0.26 |
| [[p11_qg_creation_artifacts]] | downstream | 0.25 |
| [[bld_collaboration_workflow]] | downstream | 0.25 |
| [[p10_lr_kind_builder]] | downstream | 0.24 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.24 |
| [[bld_collaboration_validation_schema]] | upstream | 0.24 |
| [[skill]] | downstream | 0.24 |
