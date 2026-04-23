---
kind: quality_gate
id: p11_qg_unit_eval
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of unit_eval artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Unit Eval'
version: 1.0.0
author: builder
tags:
- eval
- P07
- quality_gate
- examples
tldr: 'Validates unit tests for agents and prompts: input, expected output, target
  component, and isolation.'
domain: unit_eval
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - unit-eval-builder
  - bld_collaboration_unit_eval
  - bld_knowledge_card_unit_eval
  - bld_memory_unit_eval
  - bld_examples_unit_eval
  - bld_output_template_unit_eval
  - bld_collaboration_smoke_eval
  - p11_qg_smoke-eval
  - p03_sp_unit-eval-builder
  - p03_ins_unit_eval
---

## Quality Gate

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

## Examples

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
input: "Destila knowledge about rate limiting for APIs REST"
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
quality: 8.8
tags: [unit-eval, knowledge-card, yaml-parse, HARD-gates]
tldr: "Tests KC builder YAML parse and frontmatter HARD gates H01-H05 + S02"
density_score: 0.91
## Input
Destila knowledge about rate limiting for APIs REST.
Foco: algoritmos (token bucket, sliding window), headers standard, HTTP 429 handling.
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
