# CEX Crew Runner -- Builder Execution
**Builder**: `unit-eval-builder`
**Function**: GOVERN
**Intent**: reconstroi agent-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.351811

## Intent Context
- **Verb**: reconstroi
- **Object**: agent-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_unit_eval.md
---
id: unit-eval-builder
kind: type_builder
pillar: P07
parent: null
domain: unit_eval
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, unit-eval, P07, specialist, governance]
---

# unit-eval-builder
## Identity
Especialista em construir unit_evals — testes unitarios de agente/prompt individual que verificam corretude isolada.
Conhece padroes de unit testing (assertion, setup/teardown, coverage), e a diferenca entre unit_eval (P07), smoke_eval (P07), e e2e_eval (P07).
## Capabilities
- Produzir unit_eval com input/expected_output/assertion completo
- Definir setup/teardown para isolamento de teste
- Mapear assertions a quality gates do target
- Validar unit_eval contra quality gates (HARD + SOFT)
- Distinguir unit_eval de smoke_eval e e2e_eval
## Routing
keywords: [unit-eval, unit-test, agent-test, prompt-test, assertion, coverage, regression]
triggers: "test this agent", "verify prompt output", "create unit test for"
## Crew Role
In a crew, I handle UNIT TESTING.
I answer: "does this agent/prompt produce correct output for this input?"
I do NOT handle: quick sanity checks (smoke-eval-builder), pipeline tests (e2e-eval-builder), quality calibration (golden-test-builder).

### bld_instruction_unit_eval.md
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
quality: null
tags: [instruction, unit-eval, testing, assertion, P07]
idempotent: true
atomic: true
rollback: "Delete generated unit_eval YAML file"
dependencies: []
logging: true
tldr: "Build a unit_eval YAML that tests one agent or prompt in isolation with a concrete input, expected output, and verifiable assertions."
density_score: 0.90
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
**Action**: Understand what the target does and derive one testable behavior per eval.
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
id: unit_eval_{{test_name}}
kind: unit_eval
pillar: P07
version: 1.0.0
target_id: {{target_id}}
target_kind: {{target_kind}}
test_name: {{test_name}}
edge_case: {{edge_case}}
input: {{input}}
expected_output: {{expected_output}}

### bld_knowledge_card_unit_eval.md
---
kind: knowledge_card
id: bld_knowledge_card_unit_eval
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for unit_eval production — atomic searchable facts
sources: unit-eval-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: unit_eval
## Executive Summary
A `unit_eval` (P07) is a deterministic test for a single agent or prompt in isolation — it answers "does this target produce the correct output for this exact input?" It differs from `smoke_eval` (shallow pass/fail sanity), `e2e_eval` (multi-agent pipeline), and `golden_test` (quality calibration reference) by requiring gate-mapped assertions tied to specific quality gates of the target artifact. Each unit_eval covers ONE target, ONE input scenario.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 |
| Kind | `unit_eval` |
| ID pattern | `^p07_ue_[a-z][a-z0-9_]+$` |
| Naming | `p07_ue_{target_slug}.md` + `.yaml` |
| Max body | 4096 bytes |
| Required frontmatter fields | 18 |
| Recommended fields | 6 |
| `timeout` default | 60 seconds |
| `quality` field | always `null` |
| `assertions` | non-empty list; each item must have `gate_ref` |
## Patterns
| Pattern | Rule |
|---------|------|
| Single responsibility | One unit_eval = one target + one input scenario |
| Concrete assertions | Exact expected values — never "should be good" or vague |
| Gate-mapped checks | Every assertion references a `gate_ref` (e.g. `"H01"`) from the target's quality gates |
| Setup isolation | `setup` section clears external state before test executes |
| Teardown cleanup | `teardown` section prevents pollution of subsequent tests |
| Edge cases separate | Each edge case gets its own unit_eval with `edge_case: true` |
| Timeout explicit | Set `timeout` per expected execution cost; default 60s |
| `score` field | Set expected minimum score when target has numeric quality gate |
**Assertion object structure**:
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `gate_ref` | string | YES | Maps to target's quality gate ID |
| `check` | string | YES | Human-readable description of what is checked |
| `expected` | any | YES | Exact expected value |
| `severity` | enum | YES | `HARD` or `SOFT` |
**Boundary — what unit_eval is NOT**:
| kind | Why NOT unit_eval |
|------|-----------------|
| `smoke_eval` | Shallow pass/fail only, no gate mapping, <30s |
| `e2e_eval` | Tests full pipeline with multiple agents together |
| `golden_test` | 9.5+ reference for calibration, not verification |
| `benchmark` | Measures latency/cost, not output correctness |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague `expected_output` ("looks good") | Assertion is unevaluable; test is meaningless |
| Missing `gate_ref` on assertions | Disconnects test from quality framework; ungated |
| Testing multiple behaviors in one file | Violates single responsibility; failures are ambiguous |
| No `setup` for stateful targets | External state bleeds in; flaky results |
| `quality` set to a score | Never self-score; governance assigns |
| `id` not matching filename stem | Schema constraint violated; indexing breaks |
| Empty `assertions` list | Schema HARD gate: assertions must be non-empty |
## Application
1. Identify `target` (agent/prompt ID) and `target_kind` (artifact kind)
2. Choose ONE input scenario — edge cases get separate files
3. Set `id` = `p07_ue_{target_slug}`, must equal filename stem
4. Write `input` as exact verbatim text to feed the target
5. Write `expected_output` as the correct, concrete expected result
6. Map assertions: for each gate in the target's quality gates, write one assertion object with `gate_ref`, `check`, `expected`, `severity`
7. Write `setup` section: preconditions, state initialization
8. Write `teardown` section: cleanup steps
9. Set `timeout` based on expected execution time; flag `edge_case: true` if applicable
10. Set `quality: null` — do not self-score
## References
- unit-eval-builder MANIFEST.md v1.0.0
- unit-eval-builder SCHEMA.md v1.0.0

### bld_quality_gate_unit_eval.md
---
id: p11_qg_unit_eval
kind: quality_gate
pillar: P07
title: "Gate: Unit Eval"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: unit_eval
quality: null
density_score: 0.85
tags:
  - quality-gate
  - unit-eval
  - testing
  - P07
tldr: "Validates unit tests for agents and prompts: input, expected output, target component, and isolation."
---

## Definition
A unit eval tests a single agent, prompt, or component in isolation. It defines an input, an expected output or assertion, the component under test, and setup and teardown steps. Unit evals must be deterministic, fast, and independent of external services. This gate ensures every unit eval is traceable, executable, and covers meaningful behavior rather than trivial cases.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p07_ue_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `unit_eval` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `target`, `target_kind`, `assertions` all defined and non-empty |
| H07 | Input defined | Body or frontmatter contains a concrete, non-empty `input` value |
| H08 | Expected output or assertion | At least one assertion specifies a concrete expected result or a checkable condition |
| H09 | Target component identified | `target` names a specific artifact (not "the system" or "the model") |
| H10 | No pipeline testing | Eval tests one component only; no chained multi-step workflows |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Eval is tight; no filler prose or restatements of the obvious |
| Setup and teardown documented | 0.5 | `setup` and `teardown` steps are present even if empty (explicit null is acceptable) |
| Assertions are deterministic | 1.0 | Each assertion produces the same pass/fail result on every run |
| Coverage mapped to quality gates | 1.0 | Each assertion references at least one gate ID from the target's QUALITY_GATES.md |
| Isolation from external dependencies | 1.0 | No live API calls, file system writes, or database reads in the eval body |
| Tags include unit-eval | 0.5 | `tags` list contains `"unit-eval"` |
| Edge cases included | 0.5 | At least one assertion targets a boundary or failure condition |
| Regression tracking enabled | 0.5 | `regression_id` or equivalent field links this eval to a known past failure |
| Execution time reasonable | 0.5 | Expected runtime is documented and is under 30 seconds |
| Assertions are specific | 1.0 | No vague assertions like "output is correct" or "response is good" |
Sum of weights: 7.5. `soft_score = sum(weight * gate_score) / 7.5 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference unit eval |
| >= 8.0 | PUBLISH — safe to run in CI and quality pipelines |
| >= 7.0 | REVIEW — runnable but coverage or isolation needs improvement |
| < 7.0 | REJECT — do not run; assertions are ambiguous or component not isolated |
## Bypass
| Field | Value |
|-------|-------|
| condition | Target component is under active construction and its interface is not yet stable; eval is written speculatively |
| approver | Engineer who owns the target component |
| audit_log | Entry required in `.claude/bypasses/unit_eval_{date}.md` with the expected stabilization date |
| expiry | Until the target component reaches PUBLISH score; eval must be updated and re-gated at that point |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

### bld_schema_unit_eval.md
---
kind: schema
id: bld_schema_unit_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for unit_eval
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: unit_eval
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_ue_{target_slug}) | YES | — | Namespace compliance |
| kind | literal "unit_eval" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target | string | YES | — | Agent/prompt being tested |
| target_kind | string | YES | — | Artifact kind of the target |
| input | string | YES | — | Exact input to feed the target |
| expected_output | string | YES | — | Correct output for this input |
| assertions | list[object] | YES | — | Gate-mapped checks |
| timeout | integer (seconds) | YES | 60 | Max execution time |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| setup | string | REC | — | Preconditions before test |
| teardown | string | REC | — | Cleanup after test |
| edge_case | boolean | REC | false | Edge case flag |
| coverage_scope | string | REC | — | What this test covers |
| score | float | REC | — | Expected minimum score |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p07_ue_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Assertion Object Schema
```yaml
- gate_ref: "H01"
  check: "YAML parses without error"
  expected: true
  severity: "HARD"
```
## Body Structure (required sections)
1. `## Input` — exact input/prompt (verbatim)
2. `## Expected Output` — correct output
3. `## Assertions` — gate-mapped checks with expected values
4. `## Setup` — preconditions
5. `## Teardown` — cleanup
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_ue_{target_slug}.md + .yaml
- id == filename stem
- quality: null always
- assertions must be non-empty list
- each assertion must have gate_ref

### bld_examples_unit_eval.md
---
kind: examples
id: bld_examples_unit_eval
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of unit_eval artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: unit-eval-builder
## Golden Example
INPUT: "Create unit eval for knowledge_card builder testing YAML parse gate"
OUTPUT:
```yaml
id: p07_ue_kc_yaml_parse
kind: unit_eval
pillar: P07
title: "Unit Eval: KC YAML Parse Gate"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target: "knowledge-card-builder"
target_kind: "knowledge_card"
input: "Destila conhecimento sobre rate limiting para APIs REST"
expected_output: "Valid YAML with id, kind, pillar, quality: null, tags >= 3, tldr <= 160ch"
assertions:
  - gate_ref: "H01"
    check: "YAML parses without error"
    expected: true
    severity: "HARD"
  - gate_ref: "H02"
    check: "id starts with p01_kc_"
    expected: true
    severity: "HARD"
  - gate_ref: "H04"
    check: "kind == knowledge_card"
    expected: true
    severity: "HARD"
  - gate_ref: "H05"
    check: "quality == null"
    expected: true
    severity: "HARD"
  - gate_ref: "S02"
    check: "tags list has >= 3 items"
    expected: true
    severity: "SOFT"
timeout: 60
setup: "Load knowledge-card-builder SYSTEM_PROMPT and SCHEMA"
teardown: "Discard generated artifact"
edge_case: false
coverage_scope: "HARD gates H01-H05 + SOFT gate S02"
domain: "knowledge"
quality: null
tags: [unit-eval, knowledge-card, yaml-parse, HARD-gates]
tldr: "Tests KC builder YAML parse and frontmatter HARD gates H01-H05 + S02"
density_score: 0.91
## Input
Destila conhecimento sobre rate limiting para APIs REST.
Foco: algoritmos (token bucket, sliding window), headers padrao, HTTP 429 handling.
## Expected Output
Valid knowledge_card YAML artifact with:
- id matching p01_kc_ prefix
- kind: knowledge_card
- quality: null
- tags with >= 3 items
- tldr <= 160 characters
- Body sections: Conceitos, Quando Usar, Comparativo
## Assertions
- H01: YAML parses without syntax error
- H02: id matches ^p01_kc_[a-z][a-z0-9_]+$
- H04: kind field == "knowledge_card"
- H05: quality field == null (not a number)
- S02: tags is list with length >= 3
## Setup
1. Load knowledge-card-builder SYSTEM_PROMPT
2. Load knowledge-card-builder SCHEMA.md as context
3. Prepare input prompt with domain seeds
## Teardown
1. Discard generated artifact (test-only, not for pool)
2. Clear builder context
```
WHY THIS IS GOLDEN:
- quality: null (never self-scored)
- id matches p07_ue_ pattern
- kind: unit_eval
- 19 frontmatter fields present (all required + recommended)
- assertions list with 5 entries, each with gate_ref + severity
- setup/teardown present and specific
- coverage_scope explicitly stated
- timeout defined (60s)
- Input and Expected Output sections are concrete
- Assertions section maps to specific gates
## Anti-Example
INPUT: "Test the KC builder"
BAD OUTPUT:
```yaml
id: test_kc
kind: unit_test
quality: 7.5
target: KC
## Test
Run the builder and check if it works. Should produce good output.
```
FAILURES:
1. id: no p07_ue_ prefix -> H02 FAIL
2. kind: "unit_test" not "unit_eval" -> H04 FAIL
3. pillar: missing -> H05 FAIL
4. quality: self-scored 7.5 instead of null -> H06 FAIL
5. target: "KC" not valid (should be full builder name) -> H08 FAIL
6. assertions: missing entirely -> H09 FAIL
7. timeout: missing -> H10 FAIL
8. expected_output: vague "good output" not concrete -> S04 FAIL
9. setup/teardown: missing -> S05 FAIL
10. tags: missing -> S02 FAIL
11. tldr: missing -> S01 FAIL
12. coverage_scope: missing -> S06 FAIL

### bld_config_unit_eval.md
---
kind: config
id: bld_config_unit_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for unit_eval production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: unit_eval Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_ue_{target_slug}.md | p07_ue_kc_yaml_parse.md |
| Compiled | p07_ue_{target_slug}.yaml | p07_ue_kc_yaml_parse.yaml |
| Builder dir | kebab-case | unit-eval-builder/ |
| Fields | snake_case | target_kind, expected_output |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/p07_ue_{target_slug}.md
- Compiled: cex/P07_evals/compiled/p07_ue_{target_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Timeout: default 60s, max 300s for unit scope
## Assertion Policy
- Minimum 1 assertion per unit_eval
- Each assertion MUST reference a gate_ref from target builder
- Severity must be HARD or SOFT (no custom levels)

### bld_output_template_unit_eval.md
---
kind: output_template
id: bld_output_template_unit_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for unit_eval production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: unit_eval
```yaml
id: p07_ue_{{target_slug}}
kind: unit_eval
pillar: P07
title: "{{eval_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target: "{{agent_or_prompt_name}}"
target_kind: "{{artifact_kind_of_target}}"
input: "{{exact_input_prompt}}"
expected_output: "{{correct_output_description}}"
assertions:
  - gate_ref: "{{gate_id}}"
    check: "{{what_to_verify}}"
    expected: {{true_or_value}}
    severity: "{{HARD_or_SOFT}}"
timeout: {{seconds}}
setup: "{{preconditions}}"
teardown: "{{cleanup}}"
edge_case: {{true_or_false}}
coverage_scope: "{{what_gates_this_covers}}"
domain: "{{domain_value}}"
quality: null
tags: [unit-eval, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
## Input
{{verbatim_input_prompt}}
## Expected Output
{{concrete_expected_output}}
## Assertions
{{gate_mapped_checks_with_expected_values}}
## Setup
{{preconditions_and_state_init}}
## Teardown
{{cleanup_after_execution}}
```

### bld_architecture_unit_eval.md
---
kind: architecture
id: bld_architecture_unit_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of unit_eval — inventory, dependencies, and architectural position
---

# Architecture: unit_eval in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target, assertion_count, etc.) | unit-eval-builder | active |
| test_input | Concrete input provided to the target agent or prompt | author | active |
| expected_output | The correct output that the target should produce | author | active |
| assertions | Specific conditions that must hold true for the test to pass | author | active |
| setup_teardown | Pre-test initialization and post-test cleanup procedures | author | active |
| coverage_mapping | Which capabilities or code paths this test exercises | author | active |
## Dependency Graph
```
target_agent    --tested_by-->   unit_eval  --produces-->    test_result
golden_test     --calibrates-->  unit_eval  --signals-->     eval_event
unit_eval       --depends-->     quality_gate
```
| From | To | Type | Data |
|------|----|------|------|
| target_agent/prompt | unit_eval | data_flow | target under test provides actual output |
| unit_eval | test_result | produces | pass/fail per assertion with details |
| golden_test (P07) | unit_eval | dependency | golden tests provide reference for expected output |
| unit_eval | eval_event (P12) | signals | emitted on test pass or fail |
| quality_gate (P11) | unit_eval | dependency | gate may require unit eval pass before promotion |
| scoring_rubric (P07) | unit_eval | dependency | rubric criteria may inform assertion design |
## Boundary Table
| unit_eval IS | unit_eval IS NOT |
|--------------|-----------------|
| A test of one agent or prompt in isolation with concrete I/O | A fast sanity check (< 30s) for basic health (smoke_eval P07) |
| Has explicit input, expected output, and assertions | A full pipeline test across multiple agents (e2e_eval P07) |
| Includes setup/teardown for test isolation | A reference example of ideal output (golden_test P07) |
| Maps coverage to specific capabilities or code paths | A performance measurement (benchmark P07) |
| Produces per-assertion pass/fail results | A weighted score across dimensions (scoring_rubric P07) |
| Regression-focused: catches breakage in existing behavior | A calibration tool for scoring consistency |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Setup | setup_teardown, golden_test | Initialize test environment and load reference data |
| Input | frontmatter, test_input | Define test identity and concrete input |
| Execution | target_agent/prompt | Run the target with test input |
| Verification | expected_output, assertions, coverage_mapping | Compare actual vs expected and check assertions |
| Output | test_result, eval_event | Report results and signal downstream |

### bld_collaboration_unit_eval.md
---
kind: collaboration
id: bld_collaboration_unit_eval
pillar: P07
llm_function: COLLABORATE
purpose: How unit-eval-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: unit-eval-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "does this agent or prompt produce correct output for this specific input?"
I write isolated unit tests with input, expected_output, and assertions mapped to quality gates. I do NOT handle pipeline-level tests (e2e-eval-builder), quick sanity checks (smoke-eval-builder), or quality calibration against golden examples (golden-test-builder).
## Crew Compositions
### Crew: "Agent Build + Test"
```
  1. system-prompt-builder -> "builds the agent identity and rules being tested"
  2. unit-eval-builder -> "writes unit evals: input/expected_output/assertions per capability"
  3. validator-builder -> "adds pre-commit checks that unit eval artifacts are structurally valid"
```
### Crew: "Test Suite"
```
  1. unit-eval-builder -> "verifies individual agent/prompt correctness with assertions"
  2. smoke-eval-builder -> "runs quick sanity checks on the same targets"
  3. e2e-eval-builder -> "tests the full pipeline composed of agents unit-eval verified"
```
## Handoff Protocol
### I Receive
- seeds: target agent or prompt artifact id, capability list to cover, quality gates to assert against
- optional: golden_test reference for expected_output, setup/teardown requirements, edge case inputs
### I Produce
- unit_eval artifact (YAML, input + expected_output + assertions, max 80 lines per eval)
- committed to: `cex/P07_evals/examples/p07_ue_{target_slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- scoring-rubric-builder: provides evaluation criteria dimensions for assertion mapping
- golden-test-builder: provides reference outputs to use as expected_output in assertions
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| golden-test-builder | uses unit_evals to validate golden candidate quality before promotion |
| e2e-eval-builder | composes unit_evals into pipeline-level integration tests |
| smoke-eval-builder | derives quick sanity checks from unit_eval assertion sets |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `unit-eval-builder` for pipeline function `GOVERN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
