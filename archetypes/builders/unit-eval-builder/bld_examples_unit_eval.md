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
