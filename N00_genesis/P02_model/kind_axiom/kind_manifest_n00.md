---
id: n00_axiom_manifest
kind: knowledge_card
8f: F3_inject
pillar: P02
nucleus: n00
title: "Axiom -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, axiom, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_axiom
  - p01_kc_axiom
  - tpl_axiom
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_architecture_axiom
  - bld_collaboration_axiom
  - bld_schema_dataset_card
  - bld_schema_nucleus_def
  - bld_schema_integration_guide
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Axiom defines a fundamental immutable principle that forms part of a nucleus or agent's identity. Axioms are non-negotiable behavioral rules that cannot be overridden by user instructions or runtime context. They represent the philosophical bedrock of a nucleus -- the BECOME function in 8F injects axioms to ensure consistent identity even under adversarial prompting.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `axiom` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Axiom statement (imperative) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Owning nucleus or agent |
| statement | string | yes | The axiom in precise, imperative language |
| rationale | string | yes | Why this principle is non-negotiable |
| override_conditions | list | no | Conditions (if any) that may suspend the axiom |
| priority | int | yes | Conflict resolution order (1 = highest) |

## When to use
- When formalizing non-negotiable behavioral rules for a nucleus
- When encoding identity constraints that survive prompt injection attacks
- When establishing the cultural DNA of a new agent

## Builder
`archetypes/builders/axiom-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind axiom --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA this axiom enforces
- `{{TARGET_AUDIENCE}}` -- the agent this axiom constrains
- `{{DOMAIN_CONTEXT}}` -- operational context where axiom applies

## Example (minimal)
```yaml
---
id: axiom_n07_never_build
kind: axiom
pillar: P02
nucleus: n07
title: "N07 Never Builds Directly"
version: 1.0
quality: null
---
nucleus: n07
statement: "N07 orchestrates. N07 never produces artifacts directly. All builds route to N03."
rationale: "Separation of concerns. Orchestrator that builds loses the ability to govern quality objectively."
override_conditions: []
priority: 1
```

## Related kinds
- `nucleus_def` (P02) -- formal nucleus definition that includes axioms
- `agent_profile` (P02) -- persona that is constrained by axioms
- `lens` (P02) -- specialized perspective that axioms shape
- `mental_model` (P02) -- reasoning framework built on axioms

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_axiom]] | downstream | 0.45 |
| [[p01_kc_axiom]] | sibling | 0.42 |
| [[tpl_axiom]] | related | 0.39 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
| [[bld_architecture_axiom]] | downstream | 0.38 |
| [[bld_collaboration_axiom]] | downstream | 0.38 |
| [[bld_schema_dataset_card]] | downstream | 0.38 |
| [[bld_schema_nucleus_def]] | downstream | 0.38 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
