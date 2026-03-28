---
kind: collaboration
id: bld_collaboration_validator
pillar: P06
llm_function: COLLABORATE
purpose: How validator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
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
