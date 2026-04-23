---
kind: schema
id: bld_schema_axiom
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for axiom — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
source: P10_memory/_schema.yaml + SEED_BANK.yaml + TAXONOMY_LAYERS.yaml
quality: 9.1
title: "Schema Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_golden_test
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_knowledge_card
  - bld_schema_handoff_protocol
  - bld_schema_smoke_eval
  - bld_schema_input_schema
  - bld_schema_guardrail
  - bld_schema_unit_eval
---

# Schema: axiom
## Frontmatter Fields (Required — 13)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_ax_{slug}) | YES | — | H02, H03 |
| kind | literal "axiom" | YES | — | H04 |
| pillar | literal "P10" | YES | — | H06 |
| version | semver X.Y.Z | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | H06 |
| updated | date YYYY-MM-DD | YES | — | H06 |
| author | string | YES | — | H06 |
| domain | string | YES | — | Scope domain |
| quality | null | YES | null | H05 — never self-score |
| tags | list[string], len >= 3 | YES | — | H07 |
| tldr | string <= 160ch | YES | — | S01 |
| rule | string | YES | — | The axiom statement (H08) |
| scope | string | YES | — | Where it applies (H09) |
## Frontmatter Fields (Extended — 7)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| rationale | string | REC | Why immutable |
| enforcement | string | REC | How violations detected |
| immutable | literal true | REC | Permanence confirmation |
| priority | integer 1-10 | REC | Relative importance |
| dependencies | list[string] | REC | Other axioms this depends on |
| keywords | list[string] | REC | Brain search terms |
| linked_artifacts | object {primary, related} | REC | Cross-references |
## ID Pattern
Regex: `^p10_ax_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem (H02). Underscores only.
## Linked Artifacts Object
```yaml
linked_artifacts:
  primary: null            # or artifact_id
  related: [p10_ax_xxx]   # list of related ids
```
## Body Structure (required sections)
1. `## Rule Statement` — the axiom in one clear sentence
2. `## Rationale` — 2-3 concrete reasons why immutable
3. `## Scope` — domain, system, layer where it applies
4. `## Enforcement` — how violations are detected
5. `## Examples` — 2+ cases where the axiom holds
6. `## Violations` — 1+ known or hypothetical breaches
7. `## References` — sources, related axioms
## Constraints
- max_bytes: 3072 (body)
- density_min: 0.80
- naming: p10_ax_{slug}.md
- id == filename stem
- rule field: ONE sentence (atomic truth)
- immutable field: true or omitted (never false)
- scope field: must name concrete domain boundary

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.62 |
| [[bld_schema_memory_scope]] | sibling | 0.61 |
| [[bld_schema_output_validator]] | sibling | 0.61 |
| [[bld_schema_knowledge_card]] | sibling | 0.61 |
| [[bld_schema_handoff_protocol]] | sibling | 0.61 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
| [[bld_schema_input_schema]] | sibling | 0.60 |
| [[bld_schema_guardrail]] | sibling | 0.60 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
