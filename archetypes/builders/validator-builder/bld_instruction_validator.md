---
id: p03_ins_validator
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Validator Builder Instructions
target: "validator-builder agent"
phases_count: 4
prerequisites:
  - "Target artifact kind is identified"
  - "The specific field or property to check is named"
  - "Severity level is determined: error, warning, or info"
  - "The check is binary pass/fail (not a score or range)"
validation_method: checklist
domain: validator
quality: 9.0
tags: [instruction, validator, pre-commit, pass-fail, P06]
idempotent: true
atomic: true
rollback: "Delete generated validator YAML file"
dependencies: []
logging: true
tldr: "Build a validator YAML that encodes one binary pass/fail rule with structured conditions, severity, auto-fix policy, and bypass audit trail."
density_score: 0.93
llm_function: REASON
---
## Context
The validator-builder produces a `validator` artifact -- a structured YAML that encodes a single binary pass/fail technical check. Validators run at defined pipeline checkpoints (pre-commit, post-generation, or on-demand) and either block, warn, or inform based on severity.
**Critical distinction**: a `validator` is a single binary rule. It is NOT a collection of field rules in a schema (`validation_schema` -- system applies multiple rules together), NOT a quality score with thresholds (`quality_gate` -- P11, produces a score), and NOT an input contract (`input_schema` -- governs what inputs are accepted). Confusing these produces checks at the wrong granularity.
**Input contract**:
- `rule_name`: string -- kebab-case rule identifier (e.g. `require-quality-null`, `id-matches-pattern`)
- `target_kind`: string -- the artifact kind this rule applies to
- `scope`: enum -- `pre_commit` | `post_generation` | `on_demand`
- `severity`: enum -- `error` | `warning` | `info`
- `conditions`: list of condition objects (see Phase 2)
- `auto_fix`: boolean -- whether the system can automatically correct violations
- `auto_fix_action`: string or null -- description of the correction applied if auto_fix is true
- `bypass_policy`: object or null -- conditions under which the rule can be bypassed
- `error_message`: string -- actionable message shown when the rule fails
- `remediation`: string -- steps the author can take to fix the violation
**Output contract**: a single `validator` YAML with all required fields, stored at `records/validators/{rule_name}.yaml`.
**Variables**:
- `{{rule_name}}` -- kebab-case rule identifier
- `{{target_kind}}` -- artifact kind the rule targets
- `{{condition_N}}` -- Nth condition object
- `{{error_message}}` -- violation message
- `{{remediation}}` -- fix instructions
## Phases
### Phase 1: Define the Rule and Determine Severity
**Action**: Translate the check requirement into a single focused rule with a severity assignment.
```
A valid validator encodes EXACTLY ONE check. If you have two checks, build two validators.
rule_name must describe the check, not the target:
  good: "require-quality-null"
  bad:  "system-prompt-validator"
severity assignment:
  error   -> failure blocks the pipeline; artifact is rejected
  warning -> failure logged; pipeline continues; author notified
  info    -> failure logged silently; no author notification
auto_fix eligibility:
  YES: string casing, whitespace, enum normalization, date format
  NO:  missing required fields, logic errors, structural violations,
       any change that alters semantic meaning
```
Verifiable exit: rule_name describes the check; severity is assigned; auto_fix eligibility is determined.
### Phase 2: Define Conditions
**Action**: Encode the check logic as a list of structured condition objects.
Condition object schema:
```
{
  field: string -- dot-notation path to the field being checked (e.g. "frontmatter.quality")
  operator: enum [equals, not_equals, exists, not_exists, matches, not_matches,
                  greater_than, less_than, contains, not_contains, in, not_in]
  value: the expected value or pattern
  negate: boolean -- if true, the condition passes when the check fails (logical NOT)
}
```
Composition rules:
- Multiple conditions default to AND (all must pass for the rule to pass)
- To express OR: use separate validators and a dispatch rule
- `matches` / `not_matches` require a valid regex in `value`
- `in` / `not_in` require a list in `value`
```
ASSERT len(conditions) >= 1
FOR each condition:
    ASSERT condition.field is a dot-notation path
    ASSERT condition.operator is a valid enum value
    ASSERT condition.value is defined (unless operator is exists/not_exists)
```
Verifiable exit: conditions list is non-empty; each condition has field, operator, and value where required.
### Phase 3: Define Error Handling and Bypass Policy
**Action**: Write the user-facing error message and optional bypass rules.
```
error_message format:
  "[field] [violation description]. Expected: [expected]. Got: [actual]."
  example: "frontmatter.quality must be null. Expected: null. Got: 8.5."
remediation format:
  Numbered steps the author takes to fix the violation.
  Max 3 steps. First step is always the most direct fix.
bypass_policy (optional):
  {
    allowed: boolean
    conditions: string -- when bypass is permitted
    approver: string -- who can approve a bypass
    audit_required: boolean -- whether bypass must be logged
  }
IF bypass_policy is null:
    the rule has no bypass -- all violations must be fixed
```
Verifiable exit: error_message names the field and states the expectation; remediation has >= 1 step.
### Phase 4: Validate Against Quality Gates
**Action**: Run 9 HARD gates before emitting; log 10 SOFT gates as warnings.
```
HARD gates (all must pass):
  H1: rule_name is kebab-case and describes the check (not the target)
  H2: target_kind is non-empty
  H3: scope is one of pre_commit, post_generation, on_demand
  H4: severity is one of error, warning, info
  H5: conditions list has >= 1 entry, each with field and operator
  H6: error_message names the field and states the expectation
  H7: auto_fix is false for any semantic/structural change
  H8: quality is null
