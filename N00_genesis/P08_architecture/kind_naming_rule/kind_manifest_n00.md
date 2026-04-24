---
id: n00_naming_rule_manifest
kind: knowledge_card
8f: F3_inject
pillar: P08
nucleus: n00
title: "Naming Rule -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, naming_rule, p08, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_kind
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_action_paradigm
  - bld_schema_roi_calculator
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A naming_rule defines the exact naming convention for a category of artifacts, files, identifiers, or variables in the CEX system. It is loaded at F7 GOVERN to validate that produced artifacts follow established patterns, and at F1 CONSTRAIN to set the naming expectation before production begins. Consistent naming enables automated indexing, retrieval, and refactoring.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `naming_rule` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable rule name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target | string | yes | What is being named (files, ids, variables, functions) |
| pattern | string | yes | Regex or template pattern (e.g. `{kind}_{context}_{nucleus}.md`) |
| case | enum | yes | snake_case \| kebab-case \| PascalCase \| SCREAMING_SNAKE |
| examples | list | yes | Valid name examples |
| anti_examples | list | no | Invalid name examples showing what to avoid |
| scope | list | no | Pillar or nucleus this applies to |

## When to use
- Establishing artifact file naming for a new pillar or kind
- Enforcing identifier conventions across builders before a major refactor
- Documenting the naming contract so auto-indexers (cex_index.py) can rely on it

## Builder
`archetypes/builders/naming_rule-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind naming_rule --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: nr_artifact_ids
kind: naming_rule
pillar: P08
nucleus: n05
title: "Artifact ID Naming Rule"
version: 1.0
quality: null
---
target: artifact frontmatter id field
pattern: "{nucleus}_{kind}_{context}"
case: snake_case
examples: [n03_agent_salesbot, n01_kc_edtech_pricing]
anti_examples: [AgentSalesBot, n03-agent-sales_bot]
scope: [all]
```

## Related kinds
- `invariant` (P08) -- naming rules can be elevated to invariants when non-negotiable
- `decision_record` (P08) -- records why a particular naming convention was chosen
- `schema` (P06) -- schemas that enforce naming patterns via validation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | upstream | 0.46 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_dataset_card]] | upstream | 0.41 |
| [[bld_schema_integration_guide]] | upstream | 0.41 |
| [[bld_schema_search_strategy]] | upstream | 0.40 |
| [[bld_schema_benchmark_suite]] | upstream | 0.40 |
| [[bld_schema_usage_report]] | upstream | 0.40 |
| [[bld_schema_action_paradigm]] | upstream | 0.40 |
| [[bld_schema_roi_calculator]] | upstream | 0.39 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
