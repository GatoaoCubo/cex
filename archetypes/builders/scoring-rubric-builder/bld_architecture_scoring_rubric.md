---
kind: architecture
id: bld_architecture_scoring_rubric
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of scoring_rubric — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_scoring_rubric_builder
  - scoring-rubric-builder
  - bld_knowledge_card_scoring_rubric
  - bld_memory_scoring_rubric
  - p01_kc_scoring_rubric
  - bld_architecture_quality_gate
  - p03_ins_scoring_rubric_builder
  - bld_examples_scoring_rubric
  - bld_collaboration_scoring_rubric
  - bld_architecture_golden_test
---

# Architecture: scoring_rubric in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_kind, dimensions_count, etc.) | scoring-rubric-builder | active |
| dimensions | Named evaluation axes with descriptions and rationale | author | active |
| weights | Percentage weight per dimension (must sum to 100%) | author | active |
| scale_definitions | Per-dimension scoring scale with concrete criteria at each level | author | active |
| tier_thresholds | Score ranges mapped to quality tiers (master, skilled, learning, rejected) | author | active |
| calibration_refs | Golden test references used to anchor consistent scoring | author | active |
| automation_status | Which dimensions are automated, semi-automated, or manual | author | active |
## Dependency Graph
```
domain_knowledge  --produces-->  scoring_rubric  --consumed_by-->  quality_gate
golden_test       --calibrates-> scoring_rubric  --consumed_by-->  evaluator
scoring_rubric    --signals-->   calibration_drift
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | scoring_rubric | data_flow | domain expertise informing dimension selection |
| golden_test (P07) | scoring_rubric | data_flow | reference examples for scoring calibration |
| scoring_rubric | quality_gate (P11) | consumes | gate uses rubric criteria for scoring decisions |
| scoring_rubric | evaluator | consumes | human or automated evaluator applies the rubric |
| scoring_rubric | calibration_drift (P12) | signals | emitted when inter-rater agreement drops |
| benchmark (P07) | scoring_rubric | dependency | benchmarks may inform threshold selection |
## Boundary Table
| scoring_rubric IS | scoring_rubric IS NOT |
|-------------------|----------------------|
| An evaluation framework with weighted dimensions and tiers | A reference example of ideal output (golden_test P07) |
| Defines how quality is measured with concrete criteria | A pass/fail quality barrier (quality_gate P11) |
| Dimensions sum to 100% weight for balanced scoring | A technical validation rule (validator P06) |
| Calibrated against golden tests for consistency | A performance measurement (benchmark P07) |
| Scoped to one artifact kind with kind-specific criteria | A universal evaluation applicable to all kinds |
| Supports manual, semi-automated, and automated evaluation | An exclusively automated check without human option |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Domain | knowledge_card, benchmark | Supply domain expertise and performance baselines |
| Framework | frontmatter, dimensions, weights | Define evaluation axes and their relative importance |
| Criteria | scale_definitions, tier_thresholds | Specify concrete scoring levels and quality tiers |
| Calibration | calibration_refs, golden_test | Anchor consistent scoring with reference examples |
| Application | quality_gate, evaluator, automation_status | Apply the rubric in automated or manual evaluation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_scoring_rubric_builder]] | upstream | 0.46 |
| [[scoring-rubric-builder]] | upstream | 0.44 |
| [[bld_knowledge_card_scoring_rubric]] | upstream | 0.42 |
| [[bld_memory_scoring_rubric]] | downstream | 0.41 |
| [[p01_kc_scoring_rubric]] | upstream | 0.40 |
| [[bld_architecture_quality_gate]] | sibling | 0.39 |
| [[p03_ins_scoring_rubric_builder]] | upstream | 0.36 |
| [[bld_examples_scoring_rubric]] | upstream | 0.34 |
| [[bld_collaboration_scoring_rubric]] | upstream | 0.34 |
| [[bld_architecture_golden_test]] | sibling | 0.33 |
