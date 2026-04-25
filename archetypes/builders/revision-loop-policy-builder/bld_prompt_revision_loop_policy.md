---
quality: 8.4
quality: 7.9
id: p11_ins_revision_loop_policy
kind: instruction
pillar: P11
llm_function: REASON
purpose: Step-by-step build instructions for revision_loop_policy
title: "Instructions: Revision Loop Policy Builder"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [instruction, revision_loop_policy, builder, governance, hermes, escalation]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "Step-by-step build instructions for revision_loop_policy"
density_score: 0.91
idempotent: true
atomic: false
rollback: "Delete produced policy file. No downstream effects until referenced in a pipeline_template."
related:
  - p03_ins_quality_gate
  - bld_collaboration_quality_gate
  - p03_ins_response_format
  - p03_ins_prompt_compiler
  - bld_instruction_kind
  - bld_architecture_kind
  - bld_output_template_kind
  - p03_ins_prompt_template
  - p03_sp_quality_gate_builder
  - bld_collaboration_regression_check
---

## Context
A `revision_loop_policy` governs iterative content-quality improvement cycles in AI agent pipelines.
It answers: "how many times can this artifact be revised before we escalate to a human?"

**Inputs**

| Field | Type | Description |
|-------|------|-------------|
| `policy_name` | string | Slug for the policy (used in id and filename) |
| `scenario` | string | Target context (standard, security_critical, documentation, custom) |
| `max_iterations` | int | Max revision cycles (default: 3 per HERMES) |
| `escalation_target` | enum | user \| senior_nucleus \| freeze |
| `overrides` | map | Per-scenario iteration budget overrides |

**Output**
A single `.md` file (compiled to `.yaml`) with YAML frontmatter + body containing:
policy table, scenario overrides, escalation protocol, boundary rules, and pipeline_template usage.

**Boundary rules**
- revision_loop_policy = iterative content-quality improvement loop (this builder)
- quality_gate = single pass/fail check at one pipeline point (different builder)
- retry_policy = transient-failure retries (network, timeout, rate-limit) (different builder)
- regression_check = diff vs known baseline (different builder)
- bugloop = auto-detect > fix > verify for code bugs (different builder)

## Phase 1: Classify -- Boundary Check
```
IF caller wants retry on network/timeout/rate-limit failure:
  RETURN "Route to retry-policy-builder -- handles transient infrastructure failures."
IF caller wants a single pass/fail quality check:
  RETURN "Route to quality-gate-builder -- handles single-check quality barriers."
IF caller wants code bug auto-correction:
  RETURN "Route to bugloop-builder -- handles detect>fix>verify code cycles."
IF caller wants diff against known baseline:
  RETURN "Route to regression-check-builder -- handles baseline comparison."
IF caller wants N iterative content-quality improvement cycles:
  PROCEED as revision_loop_policy
```
Deliverable: confirmed `kind: revision_loop_policy` with one-line justification.

## Phase 2: Research -- Parameter Resolution
```
RESOLVE max_iterations:
  IF scenario == "security_critical": use 5 (HERMES override)
  IF scenario == "documentation": use 2
  ELSE: use 3 (HERMES standard default)

RESOLVE escalation_target:
  IF unspecified: default to "user"
  IF fully automated pipeline: consider "senior_nucleus"
  IF pipeline must never block: consider "freeze" (accept despite failures)

RESOLVE priority_order:
  Always: [security, quality, implementation]
  This is the canonical OpenCode-Hermes order -- never reorder unless explicitly requested.

RESOLVE per_scenario_overrides:
  Include standard set: {security_critical: 5, documentation: 2}
  Add any caller-requested custom scenarios.
```
Deliverable: resolved parameter set ready for frontmatter.

## Phase 3: Compose -- Build the Policy
```
ID generation:
  id = "rlp_" + policy_name_slug
  filename = "p11_rlp_" + policy_name_slug + ".yaml"

Frontmatter (required fields):
  id, kind (= revision_loop_policy), pillar (= P11), title,
  max_iterations, iteration_on_quality_floor (default: 8.5),
  priority_order, escalation_target, escalation_message_template,
  per_scenario_overrides, version (= 1.0.0), quality (= null), tags

escalation_message_template MUST contain:
  {{max_iterations}} -- actual count
  {{failing_gates}} -- list of gates that failed

Body structure:
  ## Policy: {{name}}
  ### Revision Loop Behavior (table: parameter | value | notes)
  ### Scenario Overrides (table: scenario | max_iterations | rationale)
  ### Escalation Protocol (numbered steps)
  ### Boundaries (NOT table)
  ### Usage in pipeline_template (code block)
```
Deliverable: complete `.md` file with frontmatter + 5 body sections.

## Phase 4: Validate -- Gate the Policy
```
HARD gates (block if any fail):
  H01: kind == "revision_loop_policy"
  H02: max_iterations is a positive integer
  H03: priority_order contains exactly [security, quality, implementation]
  H04: escalation_target in {user, senior_nucleus, freeze}
  H05: escalation_message_template contains "{{max_iterations}}" AND "{{failing_gates}}"
  H06: quality == null

SOFT gates (score contribution):
  S01: Boundary section present with all 4 NOT-items (0.25)
  S02: per_scenario_overrides includes security_critical and documentation (0.25)
  S03: Usage in pipeline_template code block present (0.25)
  S04: tags include hermes_origin (0.25)
```
Deliverable: PASS/FAIL on all HARD gates. Score on SOFT gates.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_quality_gate]] | sibling | 0.33 |
| [[bld_collaboration_quality_gate]] | related | 0.25 |
| [[p03_ins_response_format]] | sibling | 0.24 |
| [[p03_ins_prompt_compiler]] | sibling | 0.23 |
| [[bld_instruction_kind]] | sibling | 0.23 |
| [[bld_architecture_kind]] | upstream | 0.21 |
| [[bld_output_template_kind]] | upstream | 0.21 |
| [[p03_ins_prompt_template]] | sibling | 0.21 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.21 |
| [[bld_collaboration_regression_check]] | downstream | 0.20 |
