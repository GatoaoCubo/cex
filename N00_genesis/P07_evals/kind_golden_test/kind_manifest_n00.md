---
id: n00_golden_test_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Golden Test -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, golden_test, p07, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Golden test defines a reference test case at quality 9.5+ that serves as the canonical correct answer for a given input. Golden tests are the highest-confidence artifacts in the eval system: they have been human-verified, peer-scored, and approved as the authoritative baseline for regression detection. Any regression that moves output away from the golden test result triggers a blocking alert.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `golden_test` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Capability name + "Golden Test" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed; must be 9.5+ to publish) |
| input_fixture | string | yes | Path to the canonical test input |
| expected_output | object | yes | Exact or near-exact expected result assertions |
| tolerance | object | no | Acceptable deviation thresholds per dimension |
| human_verified_by | string | yes | Name of reviewer who certified this golden test |
| verification_date | date | yes | Date of human verification |

## When to use
- Establishing the reference answer for a core capability before deploying
- Creating the regression baseline for a critical pipeline path
- Building the "gold" standard that LLM judges are calibrated against

## Builder
`archetypes/builders/golden_test-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind golden_test --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence creates; human expert verifies
- `{{SIN_LENS}}` -- Analytical Envy: only the highest-quality examples earn golden status
- `{{TARGET_AUDIENCE}}` -- regression checks and LLM judges using this as calibration baseline
- `{{DOMAIN_CONTEXT}}` -- capability being anchored, tolerance for near-match acceptance

## Example (minimal)
```yaml
---
id: golden_test_8f_intent_resolution
kind: golden_test
pillar: P07
nucleus: n01
title: "8F Intent Resolution -- Golden Test"
version: 1.0
quality: null
---
input_fixture: "tests/golden/intent_build_landing_page.yaml"
human_verified_by: "Gato3"
verification_date: "2026-04-17"
expected_output:
  kind: landing_page
  pillar: P05
  nucleus: n02
```

## Related kinds
- `regression_check` (P07) -- compares production output against this golden test
- `llm_judge` (P07) -- calibrated using golden tests as reference answers
- `eval_dataset` (P07) -- golden tests are the highest-quality subset of the eval dataset
