---
kind: collaboration
id: bld_collaboration_validator
pillar: P06
llm_function: COLLABORATE
purpose: How validator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_validation_schema
  - bld_collaboration_quality_gate
  - validator-builder
  - bld_collaboration_output_validator
  - bld_collaboration_type_def
  - bld_collaboration_builder
  - bld_collaboration_scoring_rubric
  - bld_collaboration_enum_def
  - bld_collaboration_golden_test
  - quality-gate-builder
---

# Collaboration: validator-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what technical check must pass before this artifact is accepted?"
I define individual pass/fail rules with structured conditions (field/operator/value), severity levels (error/warning/info), and auto-fix policies. I do NOT produce quality gates with scoring (quality-gate-builder), scoring rubric criteria (scoring-rubric-builder), or input schema contracts (input-schema-builder).
## Crew Compositions
### Crew: "Artifact Governance Pipeline"
```
  1. type-def-builder -> "establishes field types and constraints that validators reference"
  2. validation-schema-builder -> "defines the structural output contract at schema level"
  3. validator-builder -> "adds individual pre-commit rules: field checks, regex, severity, bypass"
```
### Crew: "Pre-Commit Quality Gate"
```
  1. validator-builder -> "defines pass/fail rules that run before the artifact is accepted"
  2. quality-gate-builder -> "applies weighted scoring after all validators pass"
  3. unit-eval-builder -> "verifies the artifact passes both validators and functional tests"
```
## Handoff Protocol
### I Receive
- seeds: artifact kind to validate, field list with constraints, severity requirements
- optional: regex patterns, enum constraints, auto_fix candidates, bypass policy, audit trail requirements
### I Produce
- validator artifact (YAML, frontmatter 22 fields, structured conditions, max 100 lines)
- committed to: `cex/P06_schema/examples/p06_val_{rule_slug}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- type-def-builder: field type definitions inform the operator and value choices in rule conditions
- validation-schema-builder: schema-level contracts reveal which fields need individual validator coverage
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | uses validators as the HARD gate checklist source before scoring |
| workflow-builder | workflow steps run validators as acceptance gates before advancing |
| unit-eval-builder | test assertions may verify that validators correctly catch invalid inputs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validation_schema]] | sibling | 0.55 |
| [[bld_collaboration_quality_gate]] | sibling | 0.50 |
| [[validator-builder]] | related | 0.46 |
| [[bld_collaboration_output_validator]] | sibling | 0.40 |
| [[bld_collaboration_type_def]] | sibling | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.38 |
| [[bld_collaboration_scoring_rubric]] | sibling | 0.38 |
| [[bld_collaboration_enum_def]] | sibling | 0.36 |
| [[bld_collaboration_golden_test]] | sibling | 0.34 |
| [[quality-gate-builder]] | downstream | 0.34 |
