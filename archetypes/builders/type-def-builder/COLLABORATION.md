---
id: type-def-builder-collaboration
kind: collaboration
pillar: P12
llm_function: COLLABORATE
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [collaboration, type-def, P12, crew, handoff]
---

## Role in Crews

type-def-builder acts as **Vocabulary Architect** in spec-layer crews. It establishes the shared type language before any input contracts, validators, or grammars are authored. It receives domain context and produces `type_def` YAML that downstream builders reference by id.

## Crew Compositions

### Crew A: Domain Type Modeling

| Step | Builder | Input | Output |
|---|---|---|---|
| 1 | KNOWLEDGE builder | Domain brief | domain KNOWLEDGE.md |
| 2 | **type-def-builder** | KNOWLEDGE.md + type requirements | `p06_td_*.yaml` artifacts |
| 3 | input-schema-builder | `p06_td_*.yaml` references | `p06_is_*.yaml` contracts |
| 4 | validator-builder | `p06_td_*.yaml` + `p06_is_*.yaml` | `p06_val_*.yaml` rules |

### Crew B: Full Spec Layer Bootstrap

| Step | Builder | Input | Output |
|---|---|---|---|
| 1 | artifact-blueprint-builder | System design doc | `p06_ab_*.yaml` blueprints |
| 2 | **type-def-builder** | Blueprint + domain context | `p06_td_*.yaml` type vocabulary |
| 3 | grammar-builder | `p06_td_*.yaml` terminal symbols | `p06_gram_*.yaml` grammars |
| 4 | interface-builder | `p06_td_*.yaml` + agent roster | `p06_iface_*.yaml` contracts |
| 5 | validation-schema-builder | All P06 artifacts | `p06_vs_*.yaml` output contracts |

## Handoff Protocol

### Receive

| From | Artifact | What to Extract |
|---|---|---|
| KNOWLEDGE builder | `p01_kc_*.md` | Domain vocabulary, base type candidates, constraint patterns |
| artifact-blueprint-builder | `p06_ab_*.yaml` | Type names, field lists, structural requirements |
| Human / STELLA | Task description | Type name, domain, constraints, base_type hint |

### Produce

| To | Artifact | What It Contains |
|---|---|---|
| input-schema-builder | `p06_td_*.yaml` | Type vocabulary for field type references |
| validator-builder | `p06_td_*.yaml` | Type assertions for rule authoring |
| grammar-builder | `p06_td_*.yaml` | Terminal symbol types for BNF/EBNF rules |
| interface-builder | `p06_td_*.yaml` | Shared type vocabulary for bilateral contracts |

### Signal

On completion, emit:
```
signal: type_def_produced
artifact_id: p06_td_{type_slug}
domain: {domain}
base_type: {base_type}
quality: null
```

## Dependencies

| Dependency | Kind | Required | Notes |
|---|---|---|---|
| Domain KNOWLEDGE.md | knowledge (P01) | Recommended | Provides vocabulary context |
| `P06_schema/_schema.yaml` | schema | Required | Defines max_bytes, naming, llm_function |
| Brain index | MCP tool | Conditional | Dedup check during DISCOVER phase |

## Dependents

| Builder | How It Uses type_def Output |
|---|---|
| input-schema-builder | References `p06_td_*` ids as field types in entry contracts |
| validator-builder | Uses `p06_td_*` type assertions in pass/fail rules |
| grammar-builder | Uses `p06_td_*` as terminal symbol types in formal grammars |
| interface-builder | Imports shared type vocabulary for agent handshake contracts |
| validation-schema-builder | References `p06_td_*` for post-generation output type checking |

## Cross-Reference Obligations (LAW: COLLABORATION.md norm 12)

type-def-builder references input-schema-builder as a dependent.
input-schema-builder MUST reference type-def-builder as a dependency in its own COLLABORATION.md.

type-def-builder references validator-builder as a dependent.
validator-builder MUST reference type-def-builder as a dependency in its own COLLABORATION.md.

type-def-builder references grammar-builder as a dependent.
grammar-builder MUST reference type-def-builder as a dependency in its own COLLABORATION.md.
