---
id: p03_ins_scoring_rubric_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Scoring Rubric Builder Instructions
target: scoring-rubric-builder agent
phases_count: 4
prerequisites:
  - Artifact kind to be evaluated is named (e.g. "skill", "agent", "agent_card")
  - At least one quality dimension is identified (e.g. correctness, completeness)
  - Weights must sum to exactly 100
  - Tier thresholds are defined or can be derived (e.g. master >= 9.5, skilled >= 8.0)
validation_method: checklist
domain: scoring_rubric
quality: 9.0
tags: [instruction, scoring-rubric, evaluation, governance, P07]
idempotent: true
atomic: false
rollback: Delete generated scoring_rubric file and restart from Phase 1
dependencies: []
logging: true
tldr: Design a weighted evaluation framework with dimensions, per-tier thresholds, concrete scoring criteria, and calibration guidance.
density_score: 0.88
llm_function: REASON
---
## Context
The scoring-rubric-builder produces `scoring_rubric` artifacts — structured evaluation
frameworks used to measure the quality of a specific artifact kind. A scoring_rubric defines
weighted dimensions, numeric thresholds per quality tier, concrete scoring criteria at each
scale point, and an automation status for each dimension.
**Input contract**:
- `{{artifact_kind}}`: the kind being evaluated (e.g. `skill`, `agent`, `agent_card`)
- `{{dimensions_raw}}`: comma-separated quality dimensions to evaluate
- `{{tier_map}}`: tier names with numeric thresholds
  (e.g. `master:9.5, skilled:8.0, learning:7.0, rejected:<7.0`)
- `{{golden_tests_available}}`: boolean — whether reference examples exist for calibration
- `{{automation_target}}`: desired level (`manual`, `semi-automated`, `automated`)
**Output contract**: A single `scoring_rubric` Markdown file with YAML frontmatter,
weighted dimension table, per-dimension scoring scales, tier thresholds, and calibration notes.
**Boundaries**:
- Handles evaluation criteria ofsign only.
- Reference examples for calibration belong in golden_test artifacts.
- Binary pass/fail barriers belong in quality_gate artifacts.
- Performance benchmarks (throughput, latency) belong in benchmark artifacts.
## Phases
### Phase 1: Analyze Artifact Kind and Dimensions
**Primary action**: Understand what quality means for `{{artifact_kind}}` and decompose
it into measurable, non-overlapping dimensions.
```
INPUT: artifact_kind, dimensions_raw
1. Characterize the artifact kind:
   artifact_profile = {
     kind: {{artifact_kind}},
     primary_consumer: "human" | "machine" | "both",
     output_type: "text" | "code" | "data" | "config",
     correctness_verifiable: true | false
   }
2. Parse and expand dimensions_raw into dimension_list:
   for each dimension in dimensions_raw.split(","):
     dimension_entry = {
       name: dimension.strip(),
       description: one-sentence definition,
       measurability: "objective" | "subjective" | "semi-objective",
       automation_feasibility: "high" | "medium" | "low"
     }
3. Validate non-overlap:
   for each pair (d1, d2) in dimension_list:
     if d1 and d2 measure the same thing: merge or rename
4. Enforce coverage floor:
   required = ["correctness", "completeness", "clarity"]
   for each missing in required - dimension_list.names:
     add with default one-sentence definition
OUTPUT: artifact_profile{}, dimension_list[] (>= 3 dimensions, non-overlapping)
```
Verification: `dimension_list` has >= 3 entries. No two dimensions share identical
descriptions.
### Phase 2: Assign Weights and Define Tiers
**Primary action**: Distribute the 100-point weight budget across dimensions and define
numeric thresholds for each quality tier.
```
INPUT: dimension_list[], tier_map, artifact_profile
1. Weight allocation:
   if artifact_profile.correctness_verifiable == true:
     correctness_weight >= 30
   Distribute remaining weight by measurability:
     "objective" dimensions receive higher weight
     "subjective" dimensions receive lower weight
   ASSERT sum(all weights) == 100  # hard requirement
2. Tier threshold definition from tier_map:
   tiers = []
   for each (tier_name, min_score) in tier_map:
     tiers.append({
       name: tier_name,
       min_score: min_score,
       label: descriptive label,
       action: what happens at this tier (e.g. "promote", "reject with feedback")
     })
   Sort tiers by min_score descending.
   Verify no gaps or overlaps between adjacent tier ranges.
3. Per-dimension automation status:
   for each dimension in dimension_list:
     if automation_feasibility == "high":   status = "automated"
     elif automation_feasibility == "medium": status = "semi-automated"
     else:                                    status = "manual"
   Document any gap between dimension status and {{automation_target}}.
OUTPUT: weighted_dimensions[] (sum == 100), tier_thresholds[], automation_map{}
```
Verification: weights sum exactly to 100. Each tier has a distinct, non-overlapping range.
### Phase 3: Define Scoring Scales
**Primary action**: For each dimension, write concrete, discriminating criteria at each
key score point on the chosen scale.
```
INPUT: weighted_dimensions[], artifact_profile
1. Choose scale type (consistent across all dimensions):
   default: 1-10 integer scale
   alternative: 1-5 integer scale (only if tier_map max is <= 5)
2. For each dimension, write score anchors at points [1, 3, 5, 7, 9, 10]:
   Criterion rules:
     - Must be observable (not "good" or "acceptable" without qualifier)
     - Must discriminate from adjacent score point
     - Must reference the artifact's actual content, not meta-quality
   Standard anchor pattern:
     10: "`{{dimension}}` is exemplary — exceeds all requirements, zero gaps"
     9:  "`{{dimension}}` is complete with at most one minor, non-blocking issue"
     7:  "`{{dimension}}` is present and functional with 1-2 small gaps"
     5:  "`{{dimension}}` is present but has significant gaps affecting usability"
     3:  "`{{dimension}}` is partially present, major issues block correct use"
