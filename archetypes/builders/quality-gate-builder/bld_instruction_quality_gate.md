---
id: p03_ins_quality_gate
kind: instruction
pillar: P11
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Quality Gate Builder Instructions
target: "quality-gate-builder agent"
phases_count: 4
prerequisites:
  - "Caller has identified the artifact kind being gated (e.g. prompt_template, router, response_format)"
  - "At least one quality dimension is named (e.g. completeness, correctness, structural validity)"
  - "Delivery threshold is known or can be inferred (numeric score 0.0-1.0)"
validation_method: checklist
domain: quality_gate
quality: 9.1
tags: [instruction, quality-gate, P11, governance, scoring, threshold]
idempotent: true
atomic: false
rollback: "Delete produced gate file. No downstream effects until the gate is wired to a delivery pipeline."
dependencies: []
logging: true
tldr: "Define HARD block gates and SOFT scoring gates with numeric thresholds for a target artifact kind, then validate the gate spec internally."
density_score: 0.91
llm_function: REASON
---
## Context
A **quality_gate** is a pass/fail or scored checkpoint applied to an artifact before it is accepted downstream. HARD gates are binary blockers — a single failure prevents delivery. SOFT gates contribute to a weighted aggregate score; if the score falls below the delivery threshold, the artifact is rejected. This builder produces gate *specifications*, not executable validator code.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `artifact_kind` | string | The kind being gated (e.g. `prompt_template`, `router`, `response_format`) |
| `dimensions` | list | Quality dimensions to evaluate (e.g. `completeness`, `correctness`, `safety`) |
| `delivery_threshold` | float | Minimum acceptable soft-gate aggregate score (0.0–1.0) |
| `bypass_policy` | string | Who may override a gate failure: `none`, `owner`, or `admin` |
**Output**
A single `.md` file with YAML frontmatter + body containing: HARD gate table, SOFT gate table with weights, aggregate scoring formula, and bypass policy. Weights across all SOFT gates must sum to 1.0.
**Boundary rules**
- quality_gate = pass/fail specification for artifact acceptance (this builder)
- validation_schema = executable code that validates artifact structure post-generation (different builder)
- rubric = criteria for human scoring panels (different builder)
- lifecycle_rule = when to promote, retire, or deprecate an artifact (different builder)
## Phases
### Phase 1: Research — Dimension Mapping
Map each quality dimension to concrete, objectively verifiable checks.
```
FOR each dimension in dimensions:
  identify 1-3 concrete checks that are objectively verifiable
  classify each check:
    HARD if: binary outcome only (present/absent, valid/invalid, correct/incorrect)
             AND failure would make the artifact non-functional or misleading
    SOFT if: gradable (partial credit exists)
             OR contributes to overall quality without blocking basic utility
  assign weight to each SOFT gate
  NOTE: all SOFT gate weights must sum to exactly 1.0
IF no dimensions provided, infer from artifact_kind using standard set:
  structural:   schema validity, required fields present
  semantic:     content correctness, boundary adherence
  operational:  usability, completeness of examples, actionability
Research existing gates for similar artifact kinds to calibrate thresholds.
Identify industry-standard thresholds for the domain where applicable.
```
Deliverable: classified list of HARD checks and SOFT checks with weights.
### Phase 2: Classify — Boundary Check
Confirm this artifact belongs to `quality_gate` and not a sibling kind.
```
IF caller wants executable code that validates artifact structure:
  RETURN "Route to validation-schema-builder — produces code, not a gate spec."
IF caller wants criteria for human scoring panels or review committees:
  RETURN "Route to rubric-builder — rubrics serve human reviewers."
IF caller wants lifecycle rules (when to retire, promote, deprecate):
  RETURN "Route to lifecycle-rule-builder."
IF caller wants runtime behavior limits (timeout, retry, rate limit):
  RETURN "Route to runtime-rule-builder."
IF caller wants HARD+SOFT gate spec with numeric delivery threshold:
  PROCEED as quality_gate
```
Deliverable: confirmed `kind: quality_gate` with one-line justification.
### Phase 3: Compose — Build the Gate Specification
Assemble frontmatter and body following SCHEMA.md and OUTPUT_TEMPLATE.md.
```
ID generation:
  id = "p11_qg_" + artifact_kind_slug
  pattern must match valid quality_gate id format
Frontmatter (required fields):
  id, kind (= quality_gate), pillar (= P11), title, version,
  created, updated, author, target_kind, delivery_threshold,
  bypass_policy, dimensions, quality (= null), tags
Body structure:
  ## Definition
  Table: metric | threshold | operator | scope
  One row per top-level quality dimension.
  ## HARD Gates
  Table: ID | Criterion | Failure Action
  Rows: H01, H02, ... (sequential, no gaps)
  Each criterion: objectively verifiable, no subjective adjectives alone.
  Failure action: always "block" for HARD gates.
  Minimum: 2 HARD gates required.
  ## SOFT Gates
  Table: ID | Criterion | Weight | Scoring Method
  Rows: S01, S02, ... (sequential, no gaps)
  Scoring method: "binary" (0 or weight) or "graduated" (partial credit)
  Weights: must sum to exactly 1.0
  Minimum: 3 SOFT gates required.
  ## Scoring Formula
  aggregate_score = SUM(gate_score * weight for each SOFT gate)
  PASS condition: all HARD gates pass AND aggregate_score >= {delivery_threshold}
  State formula explicitly — do not leave it implicit.
  ## Actions
  Table: outcome | consequence
  PASS: artifact proceeds to delivery/pool
  FAIL: artifact returned with gate failure details
  ## Bypass Policy
  Who may override: {none | owner | admin}
  Conditions for bypass: explicit criteria (not vague)
  Audit requirement: what must be logged when bypass is used
```
Deliverable: complete `.md` file with frontmatter + 5 body sections.
### Phase 4: Validate — Gate the Gate Spec
Apply meta-checks to the gate spec itself before delivering.
```
