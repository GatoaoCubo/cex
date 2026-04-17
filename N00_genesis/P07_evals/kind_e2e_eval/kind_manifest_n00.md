---
id: n00_e2e_eval_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "E2e Eval -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, e2e_eval, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
E2e eval defines an end-to-end pipeline test that validates a complete workflow from user input to final artifact output, exercising every stage of the 8F pipeline in sequence. Unlike unit_eval (single component) or smoke_eval (quick sanity), e2e eval tests the full integration: input transmutation, nucleus dispatch, builder execution, compilation, and signal emission. It is the highest-confidence validation artifact in CEX.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `e2e_eval` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Pipeline name + "E2E Eval" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| pipeline_under_test | string | yes | Full pipeline path being tested |
| input_fixture | string | yes | Path to test input fixture |
| expected_output | object | yes | Assertions on final output (structure, quality, paths) |
| timeout_seconds | int | yes | Max allowed time for full pipeline run |
| stages_validated | list | yes | 8F stages explicitly checked (F1-F8) |

## When to use
- Validating that a full 8F pipeline run produces a correct, compilable artifact
- Running pre-release integration tests across all nuclei
- Catching regressions that unit tests cannot detect because they test components in isolation

## Builder
`archetypes/builders/e2e_eval-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind e2e_eval --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements; all nuclei are tested
- `{{SIN_LENS}}` -- Gating Wrath: zero regressions reach production
- `{{TARGET_AUDIENCE}}` -- CI/CD pipeline and release gate automation
- `{{DOMAIN_CONTEXT}}` -- pipeline type, nucleus combination, artifact kind under test

## Example (minimal)
```yaml
---
id: e2e_eval_n03_knowledge_card
kind: e2e_eval
pillar: P07
nucleus: n05
title: "N03 Knowledge Card Build -- E2E Eval"
version: 1.0
quality: null
---
pipeline_under_test: "N03 8F pipeline -> knowledge_card"
input_fixture: "tests/fixtures/intent_build_kc.yaml"
timeout_seconds: 300
stages_validated: [F1, F2, F3, F6, F7, F8]
expected_output: {file_exists: true, quality_score_not_null: false, compiled: true}
```

## Related kinds
- `smoke_eval` (P07) -- quick subset of e2e_eval; run more frequently
- `unit_eval` (P07) -- tests individual components that e2e_eval exercises together
- `golden_test` (P07) -- reference e2e result used as the comparison baseline
