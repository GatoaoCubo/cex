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
quality: null
tags: [instruction, validator, pre-commit, pass-fail, P06]
idempotent: true
atomic: true
rollback: "Delete generated validator YAML file"
dependencies: []
logging: true
tldr: "Build a validator YAML that encodes one binary pass/fail rule with structured conditions, severity, auto-fix policy, and bypass audit trail."
density_score: 0.93
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

---

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
  H9: the rule is binary (pass/fail) -- no scoring or partial credit

SOFT gates (log warnings):
  S1: rule_name does not duplicate an existing validator id
  S2: remediation has >= 1 actionable step
  S3: bypass_policy is defined for rules that may legitimately be skipped
  S4: bypass_policy has audit_required: true for error-severity rules
  S5-S7: conditions use specific operators (not generic "equals" for pattern checks)
  S8: auto_fix_action is described when auto_fix is true
  S9: error_message is <= 120 characters (readable in CI output)
  S10: scope matches the artifact lifecycle stage where the violation would occur
```

Verifiable exit: 9/9 HARD gates pass.

---

## Output Contract

```yaml
id: validator_{{rule_name}}
kind: validator
pillar: P06
version: 1.0.0
rule_name: {{rule_name}}
target_kind: {{target_kind}}
scope: {{scope}}
severity: {{severity}}
conditions:
  - field: "{{condition_1_field}}"
    operator: {{condition_1_operator}}
    value: {{condition_1_value}}
    negate: false
auto_fix: {{auto_fix}}
auto_fix_action: {{auto_fix_action}}
error_message: "{{error_message}}"
remediation: "{{remediation}}"
bypass_policy: {{bypass_policy}}
quality: null
created: "{{created}}"
updated: "{{updated}}"
```

---

## Validation

- [ ] H1: rule_name is kebab-case and describes the check
- [ ] H2: target_kind is non-empty
- [ ] H3: scope is one of pre_commit, post_generation, on_demand
- [ ] H4: severity is one of error, warning, info
- [ ] H5: conditions list has >= 1 entry with field and operator
- [ ] H6: error_message names the field and states the expectation
- [ ] H7: auto_fix is false for semantic or structural changes
- [ ] H8: quality is null
- [ ] H9: the rule produces a binary pass/fail result

---

## Metacognition

**Does**:
- Produce a single binary pass/fail validation rule
- Enforce that one validator encodes exactly one check
- Define actionable error messages and remediation steps
- Validate 9 HARD gates before emitting

**Does NOT**:
- Collect multiple rules into a schema (validation_schema handles that)
- Produce quality scores or thresholds (quality_gate handles that)
- Define what inputs are accepted before generation (input_schema handles that)
- Execute the check -- it defines the rule specification only

**Chaining**: validator-builder output is consumed by CI/CD pipelines and generation runners. Build validators after the target artifact schema is stable. Use validation_schema when you need to enforce a full set of field rules together; use validator for individual rules that may need bypass policies or different severities.
