---
id: p03_ins_unit_eval
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Unit Eval Builder Instructions
target: "unit-eval-builder agent"
phases_count: 4
prerequisites:
  - "Target agent or prompt artifact is identified by name"
  - "At least one specific input/output pair is known"
  - "Expected behavior specification or quality gates for the target exist"
  - "Test scope is bounded to a single agent or prompt (not a pipeline)"
validation_method: checklist
domain: unit_eval
quality: 9.0
tags: [instruction, unit-eval, testing, assertion, P07]
idempotent: true
atomic: true
rollback: "Delete generated unit_eval YAML file"
dependencies: []
logging: true
tldr: "Build a unit_eval YAML that tests one agent or prompt in isolation with a concrete input, expected output, and verifiable assertions."
density_score: 0.90
llm_function: REASON
---
## Context
The unit-eval-builder produces a `unit_eval` artifact -- a structured YAML that defines an isolated test for a single agent or prompt. Each unit_eval specifies the exact input, the expected output, the assertions that must hold, and the setup/teardown state needed to run the test independently.
**Critical distinction**: `unit_eval` tests one component in isolation with a known expected output. It is NOT a quick sanity check (smoke_eval), a full pipeline test (e2e_eval), or a quality calibration benchmark (golden_test). Mixing these types produces tests that fail for the wrong reasons.
**Input contract**:
- `target_id`: string -- the id of the agent or prompt artifact being tested
- `target_kind`: enum -- `system_prompt` | `action_prompt` | `prompt_template` | `instruction`
- `test_name`: string -- kebab-case test identifier (e.g. `rejects-empty-input`, `formats-output-as-json`)
- `input`: string or object -- the exact value fed to the target
- `expected_output`: string or object -- the correct output for this input
- `assertions`: list -- each assertion maps a property to an expected value or condition
- `setup`: object or null -- preconditions and state to initialize before the test
- `teardown`: object or null -- cleanup steps after the test runs
- `timeout_s`: integer -- maximum seconds allowed (default 60)
- `edge_case`: boolean -- whether this test covers a boundary or failure condition
**Output contract**: a single `unit_eval` YAML with all required fields, stored at `records/evals/unit/{test_name}.yaml`.
**Variables**:
- `{{test_name}}` -- kebab-case test identifier
- `{{target_id}}` -- id of the artifact under test
- `{{input}}` -- exact test input
- `{{expected_output}}` -- expected result
- `{{assertion_N}}` -- Nth assertion object
## Phases
### Phase 1: Analyze Target and Define Test Scope
**Action**: Understand what the target does and derive one testsble behavior per eval.
```
FOR the given target_id:
    1. Identify the target's primary output contract
    2. Select ONE specific behavior to test (not multiple)
    3. Determine if input requires setup state or can run standalone
IF edge_case:
    input = boundary value or invalid input
    expected_output = error, rejection, or fallback response
ELSE:
    input = representative valid input
    expected_output = correct nominal output
ASSERT: test_name describes the behavior being tested, not the target name
  good: "rejects-null-agent-name"
  bad:  "system-prompt-builder-test-1"
```
Verifiable exit: one behavior selected; test_name describes that behavior; input and expected_output are defined.
### Phase 2: Define Assertions
**Action**: Translate expected_output into a list of verifiable assertion objects.
Assertion object schema:
```
{
  property: string -- what to check (e.g. "output.kind", "output.length", "exit_code"),
  operator: enum [equals, contains, matches, greater_than, less_than, is_null, is_not_null],
  expected: the value to compare against,
  gate_ref: string or null -- reference to a quality gate this assertion enforces
}
```
Assertion rules:
- Every assertion must have a concrete expected value -- no vague checks ("should be good")
- At least one assertion must check the primary output field
- For structured outputs: add one assertion per required field
- For string outputs: add assertions for presence of key terms and absence of forbidden terms
```
ASSERT len(assertions) >= 1
FOR each assertion:
    ASSERT assertion.expected is not null
    ASSERT assertion.operator is a valid enum value
```
Verifiable exit: assertions list is non-empty; all assertions have concrete expected values.
### Phase 3: Define Setup and Teardown
**Action**: Specify state isolation requirements.
```
IF target requires external state (file, db record, env var):
    setup = { state_type: description, initial_values: {...} }
    teardown = { cleanup: description }
ELSE:
    setup = null
    teardown = null
timeout_s = 60  # default for unit scope
IF target is known to be slow (>60s expected):
    timeout_s = explicit override, max 300
```
Verifiable exit: setup is null or has state_type and initial_values; teardown matches setup (both null or both defined).
### Phase 4: Validate Against Quality Gates
**Action**: Run 7 HARD gates before emitting; log 3 SOFT gates as warnings.
```
HARD gates (all must pass):
  H1: target_id is non-empty and references a known artifact
  H2: target_kind is one of the 4 valid enum values
  H3: test_name is kebab-case and describes the behavior (not the target)
  H4: input is defined and non-empty
  H5: expected_output is defined and non-empty
  H6: assertions list has >= 1 item, each with property, operator, and expected
  H7: timeout_s is a positive integer <= 300
SOFT gates (log warnings):
  S1: edge_case is true for boundary/failure tests (not defaulted false)
  S2: teardown is defined when setup is defined
  S3: at least one assertion references a gate_ref
```
Verifiable exit: 7/7 HARD gates pass.
## Output Contract
```yaml
id: unit_eval_`{{test_name}}`
kind: unit_eval
pillar: P07
version: 1.0.0
target_id: `{{target_id}}`
target_kind: `{{target_kind}}`
test_name: `{{test_name}}`
edge_case: `{{edge_case}}`
input: `{{input}}`
expected_output: `{{expected_output}}`
