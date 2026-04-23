---
kind: knowledge_card
id: bld_knowledge_card_scoring_rubric
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for scoring_rubric production — atomic searchable facts
sources: scoring-rubric-builder MANIFEST.md + SCHEMA.md, AAC&U VALUE Rubrics, Bloom taxonomy
quality: 9.1
title: "Knowledge Card Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_scoring_rubric
  - p03_sp_scoring_rubric_builder
  - p11_qg_scoring-rubric
  - bld_collaboration_scoring_rubric
  - p03_ins_scoring_rubric_builder
  - scoring-rubric-builder
  - bld_examples_scoring_rubric
  - bld_architecture_scoring_rubric
  - p01_kc_scoring_rubric
  - bld_knowledge_card_quality_gate
---

# Domain Knowledge: scoring_rubric
## Executive Summary
Scoring rubrics are multi-dimensional weighted evaluation frameworks that define how to measure artifact quality across orthogonal dimensions with concrete criteria per level. Each rubric targets specific artifact kinds, assigns weights summing to 100%, and maps scores to action tiers (GOLDEN/PUBLISH/REVIEW/REJECT). They differ from quality gates (which enforce pass/fail barriers), golden tests (which provide reference examples), benchmarks (which measure performance metrics), and unit evals (which test specific behaviors) by defining the complete evaluation methodology with weighted dimensions and calibration.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (evaluation) |
| Kind | `scoring_rubric` (exact literal) |
| ID pattern | `p07_sr_{slug}` |
| Required frontmatter | 15 fields |
| Quality gates | 9 HARD + 9 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Weight invariant | All dimension weights MUST sum to 100% |
| Score tiers | GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0 |
| Min dimensions | 3 orthogonal dimensions |
## Patterns
| Pattern | Application |
|---------|-------------|
| Orthogonal dimensions | Each dimension measures ONE thing; no overlap between dimensions |
| Explicit weights | Sum to exactly 100%; higher weight = more impact on final score |
| Concrete criteria | Specify what counts at each level, not "good" or "apownte" |
| Consistent scales | All dimensions use same scale (0-10) for comparability |
| Golden test calibration | Anchor rubric with known-good examples at 9.5+ |
| Automation status | Declare per dimension: manual, semi-automated, or automated |
| Inter-rater reliability | >= 0.80 agreement indicates reliable rubric |
| Target kind scoping | Rubric applies to specific artifact kinds, not everything |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Weights not summing to 100% | Breaks scoring formula; validator rejects |
| Overlapping dimensions | Double-counting inflates or deflates scores |
| Vague criteria ("good quality") | Not actionable; different raters interpret differently |
| No golden test calibration | Rubric floats without anchoring examples |
| Fewer than 3 dimensions | Insufficient coverage of artifact quality |
| All dimensions equal weight | Usually wrong; some dimensions matter more |
| No automation status declared | Unknown whether scoring is manual or automated |
## Application
1. Identify target artifact kinds this rubric evaluates
2. Define >= 3 orthogonal dimensions, each measuring ONE aspect
3. Assign weights summing to exactly 100%
4. Write concrete criteria per dimension per level (0-10 scale)
5. Map scores to tiers: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0
6. Link golden test examples for calibration
7. Declare automation status per dimension
8. Validate: 9 HARD + 9 SOFT gates, body <= 4096 bytes
## References
- scoring-rubric-builder SCHEMA.md v1.0.0
- AAC&U VALUE Rubrics (16 rubrics for learning outcomes)
- Bloom Taxonomy (Anderson & Krathwohl 2001 revision)
- LLM-as-Judge evaluation framework

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_scoring_rubric]] | downstream | 0.52 |
| [[p03_sp_scoring_rubric_builder]] | downstream | 0.49 |
| [[p11_qg_scoring-rubric]] | downstream | 0.49 |
| [[bld_collaboration_scoring_rubric]] | downstream | 0.48 |
| [[p03_ins_scoring_rubric_builder]] | downstream | 0.44 |
| [[scoring-rubric-builder]] | downstream | 0.42 |
| [[bld_examples_scoring_rubric]] | downstream | 0.39 |
| [[bld_architecture_scoring_rubric]] | downstream | 0.38 |
| [[p01_kc_scoring_rubric]] | sibling | 0.38 |
| [[bld_knowledge_card_quality_gate]] | sibling | 0.38 |
