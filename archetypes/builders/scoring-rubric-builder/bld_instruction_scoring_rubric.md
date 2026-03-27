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
  - Artifact kind to be evaluated is named (e.g. "skill", "agent", "satellite_spec")
  - At least one quality dimension is identified (e.g. correctness, completeness)
  - Weights must sum to exactly 100
  - Tier thresholds are defined or can be derived (e.g. master >= 9.5, skilled >= 8.0)
validation_method: checklist
domain: scoring_rubric
quality: null
tags: [instruction, scoring-rubric, evaluation, governance, P07]
idempotent: true
atomic: false
rollback: Delete generated scoring_rubric file and restart from Phase 1
dependencies: []
logging: true
tldr: Design a weighted evaluation framework with dimensions, per-tier thresholds, concrete scoring criteria, and calibration guidance.
density_score: 0.88
---

## Context

The scoring-rubric-builder produces `scoring_rubric` artifacts — structured evaluation
frameworks used to measure the quality of a specific artifact kind. A scoring_rubric defines
weighted dimensions, numeric thresholds per quality tier, concrete scoring criteria at each
scale point, and an automation status for each dimension.

**Input contract**:
- `{{artifact_kind}}`: the kind being evaluated (e.g. `skill`, `agent`, `satellite_spec`)
- `{{dimensions_raw}}`: comma-separated quality dimensions to evaluate
- `{{tier_map}}`: tier names with numeric thresholds
  (e.g. `master:9.5, skilled:8.0, learning:7.0, rejected:<7.0`)
- `{{golden_tests_available}}`: boolean — whether reference examples exist for calibration
- `{{automation_target}}`: desired level (`manual`, `semi-automated`, `automated`)

**Output contract**: A single `scoring_rubric` Markdown file with YAML frontmatter,
weighted dimension table, per-dimension scoring scales, tier thresholds, and calibration notes.

**Boundaries**:
- Handles evaluation criteria design only.
- Reference examples for calibration belong in golden_test artifacts.
- Binary pass/fail barriers belong in quality_gate artifacts.
- Performance benchmarks (throughput, latency) belong in benchmark artifacts.

---

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

---

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

---

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
     10: "{{dimension}} is exemplary — exceeds all requirements, zero gaps"
     9:  "{{dimension}} is complete with at most one minor, non-blocking issue"
     7:  "{{dimension}} is present and functional with 1-2 small gaps"
     5:  "{{dimension}} is present but has significant gaps affecting usability"
     3:  "{{dimension}} is partially present, major issues block correct use"
     1:  "{{dimension}} is absent or entirely incorrect"

3. For score points not in anchor set (2, 4, 6, 8):
   Describe as "between [lower anchor] and [upper anchor]" — explicit interpolation.

OUTPUT: scoring_scales{dimension_name: {score: criterion}} for all dimensions
```

Verification: every dimension has anchors at 1, 5, and 10. No criterion uses unqualified
vague terms (good, adequate, decent, reasonable).

---

### Phase 4: Assemble Artifact and Calibration Notes

**Primary action**: Combine all phase outputs into the final scoring_rubric file and
document calibration guidance.

```
INPUT: artifact_profile, weighted_dimensions, tier_thresholds, scoring_scales,
       golden_tests_available

1. Assemble frontmatter:
   id: {{artifact_kind}}-rubric
   kind: scoring_rubric
   pillar: P07
   version: 1.0.0
   target_kind: {{artifact_kind}}
   dimensions_count: len(weighted_dimensions)
   weights_sum: 100
   automation_status: {{automation_target}}
   quality: null

2. Build dimension table (one row per dimension):
   | Dimension | Weight | Automation | Description |

3. Build tier threshold table (one row per tier):
   | Tier | Min Score | Label | Action |

4. Calibration section:
   if golden_tests_available == true:
     "Reference examples are available. Score each golden test through this rubric
     before use. If scores deviate > 1.0 from expected, recalibrate the weights
     for the deviating dimension."
   else:
     "No golden tests available. Apply rubric to 3 sample outputs and check for
     score clustering. If all scores fall within < 2 tiers, redistribute weights."

5. Run HARD quality gates (all must pass):
   HARD_1: id matches {{artifact_kind}}-rubric pattern
   HARD_2: weights sum exactly to 100
   HARD_3: all dimensions have full scoring scale defined
   HARD_4: tier thresholds have no gaps or overlaps
   HARD_5: every dimension has anchor at score 1 and score 10
   HARD_6: dimensions_count >= 3
   HARD_7: automation_status is valid enum value
   HARD_8: no criterion uses unqualified vague terms
   HARD_9: kind == "scoring_rubric"

OUTPUT: scoring_rubric file, calibration_notes, gate_results{}
```

Verification: all 9 HARD gates pass. `weights_sum` equals exactly 100.

---

## Output Contract

```markdown
---
id: {{artifact_kind}}-rubric
kind: scoring_rubric
pillar: P07
version: 1.0.0
created: {{created_date}}
updated: {{updated_date}}
author: scoring-rubric-builder
target_kind: {{artifact_kind}}
dimensions_count: {{dimensions_count}}
weights_sum: 100
automation_status: {{automation_status}}
tags: [scoring-rubric, {{artifact_kind}}, evaluation]
quality: null
---

# Scoring Rubric: {{artifact_kind}}

## Dimensions and Weights

| Dimension | Weight | Automation | Description |
|-----------|--------|------------|-------------|
| {{dimension_1}} | {{weight_1}} | {{automation_1}} | {{description_1}} |
| {{dimension_N}} | {{weight_N}} | {{automation_N}} | {{description_N}} |
| **Total** | **100** | — | — |

## Tier Thresholds

| Tier | Min Score | Label | Action |
|------|-----------|-------|--------|
| {{tier_1}} | {{min_1}} | {{label_1}} | {{action_1}} |
| {{tier_N}} | {{min_N}} | {{label_N}} | {{action_N}} |

## Scoring Scales

### {{dimension_1}} (weight: {{weight_1}})
{{description_1}}

| Score | Criterion |
|-------|-----------|
| 10 | {{criterion_10}} |
| 9  | {{criterion_9}} |
| 7  | {{criterion_7}} |
| 5  | {{criterion_5}} |
| 3  | {{criterion_3}} |
| 1  | {{criterion_1}} |

[repeat block for each dimension]

## Calibration Notes
{{calibration_notes}}

## Composite Score Formula
weighted_score = sum(dimension_score_i * weight_i / 100 for i in dimensions)
```

---

## Validation

- [ ] HARD: `id` matches pattern `{{artifact_kind}}-rubric`
- [ ] HARD: all dimension weights sum exactly to 100
- [ ] HARD: every dimension has a full scoring scale defined
- [ ] HARD: tier thresholds have no gaps or overlaps between adjacent tiers
- [ ] HARD: every dimension has anchor criteria at score 1 and score 10
- [ ] HARD: `dimensions_count` >= 3
- [ ] HARD: `automation_status` is one of `manual`, `semi-automated`, `automated`
- [ ] HARD: no scoring criterion uses unqualified vague terms
- [ ] HARD: `kind` equals `scoring_rubric`
- [ ] SOFT: correctness dimension has weight >= 25 when objectively measurable
- [ ] SOFT: calibration section documents how to verify weights against examples
- [ ] SOFT: each tier has a documented action (not just a label)
- [ ] SOFT: automation status is documented per individual dimension
- [ ] SOFT: intermediate scores (2, 4, 6, 8) are described or explicitly interpolated
- [ ] SOFT: dimension descriptions are distinct and non-overlapping
- [ ] SOFT: at least one dimension is marked `automated` feasibility
- [ ] SOFT: tier labels are actionable (promote, reject) not purely descriptive
- [ ] SOFT: composite score formula is documented

**Score threshold**: All 9 HARD gates must pass. >= 6 of 9 SOFT gates recommended.

---

## Metacognition

**Does**:
- Design weighted evaluation frameworks for a specific artifact kind
- Assign non-overlapping, measurable quality dimensions
- Define concrete scoring criteria at each scale point
- Ensure weights sum exactly to 100
- Document calibration guidance for human reviewers

**Does NOT**:
- Provide reference examples (those are golden_test artifacts)
- Create binary pass/fail barriers (those are quality_gate artifacts)
- Measure performance throughput or latency (those are benchmark artifacts)
- Score a specific artifact instance — designs the framework, does not apply it

**Chaining**:
- After: golden-test-builder uses rubric tiers to classify reference examples
- After: quality-gate-builder uses the minimum passing threshold to define gate cutoffs
- After: evaluator agents apply this rubric to score produced artifact instances
