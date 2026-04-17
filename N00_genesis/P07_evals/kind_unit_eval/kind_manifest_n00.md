---
id: n00_unit_eval_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Unit Eval -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, unit_eval, p07, n00, archetype, template]
density_score: 0.99
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Unit eval defines an agent or prompt unit test that validates a single, isolated capability without running the full pipeline. It specifies a fixed input, expected output pattern, and pass/fail criteria for one component (a builder prompt, an intent resolver, a formatter, or a validator). Unit evals are fast (< 10 seconds), deterministic, and form the foundation of the CEX quality test pyramid.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `unit_eval` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Component name + behavior being tested |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| component_under_test | string | yes | The specific prompt, agent, or tool being unit-tested |
| input_fixture | string | yes | Fixed test input (path or inline) |
| expected_output | object | yes | Assertions on the component output |
| max_duration_seconds | int | yes | Hard timeout (must be < 10) |
| deterministic | bool | yes | Whether output is expected to be exactly reproducible |

## When to use
- Testing a single builder prompt in isolation before integrating into the 8F pipeline
- Validating a new formatter or parser component before deployment
- Building regression coverage for a component that has had previous failures

## Builder
`archetypes/builders/unit_eval-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind unit_eval --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements; all nuclei write unit evals for their components
- `{{SIN_LENS}}` -- Gating Wrath: one component, one behavior, no ambiguity in pass/fail
- `{{TARGET_AUDIENCE}}` -- CI/CD test runner executing on every commit
- `{{DOMAIN_CONTEXT}}` -- component type, expected behavior, determinism requirements

## Example (minimal)
```yaml
---
id: unit_eval_intent_resolver_landing_page
kind: unit_eval
pillar: P07
nucleus: n05
title: "Intent Resolver -- landing_page classification unit eval"
version: 1.0
quality: null
---
component_under_test: "cex_intent_resolver.py"
input_fixture: "make me a landing page"
max_duration_seconds: 5
deterministic: true
expected_output:
  kind: landing_page
  pillar: P05
  nucleus: n02
```

## Related kinds
- `smoke_eval` (P07) -- integration-level sanity check built from passing unit evals
- `e2e_eval` (P07) -- full pipeline test that exercises multiple unit-tested components
- `golden_test` (P07) -- unit eval that has been elevated to golden status
