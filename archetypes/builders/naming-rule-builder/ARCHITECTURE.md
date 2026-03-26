---
pillar: P08
llm_function: CONSTRAIN
kind: architecture
domain: naming_rule
version: 1.0.0
---

# Architecture — Naming Rule Builder

## Boundary

A `naming_rule` answers ONE question: **"What string format must the name of this artifact follow?"**

### NAO EH — P05 Siblings (Same Pillar)

| Kind | Answers | Confusion Risk |
|------|---------|---------------|
| response_format | How should the LLM format its reply text? | Medium — both are output specs, but response_format governs LLM reply shape, NOT artifact file names |
| parser | How to extract structured data from LLM output? | Low — parser operates on content, naming_rule operates on name strings |
| formatter | How to render data into a target format (json/md/yaml)? | Low — formatter transforms content, naming_rule constrains name tokens |

### NAO EH — Commonly Confused (P06)

| Kind | Answers | Why NOT a naming_rule |
|------|---------|----------------------|
| validator | Does this artifact's content meet spec? | Validates content correctness, not name format |
| type_def | What abstract category/type does this artifact belong to? | Defines type semantics, not naming strings |

### Decision Question

> **"Does this artifact define what something should be CALLED (name format)?"**
> - YES → naming_rule (this builder)
> - NO, it defines reply shape → response_format
> - NO, it extracts data → parser
> - NO, it renders content → formatter
> - NO, it checks content validity → validator (P06)
> - NO, it defines abstract type → type_def (P06)

## Position in Naming Flow

```
Domain Owner defines scope
        |
        v
naming-rule-builder PRODUCES naming_rule
        |
        v
naming_rule artifact stored in pool (p05_nr_{scope}.md)
        |
        v
validator (P06) CONSUMES naming_rule --> checks artifact IDs at runtime
        |
        v
code generators CONSUME naming_rule --> auto-generate compliant names
        |
        v
documentation builders CONSUME naming_rule --> render naming tables
```

## Dependency Graph

```
domain_owner --> naming-rule-builder
naming-rule-builder --> SCHEMA.md
naming-rule-builder --> OUTPUT_TEMPLATE.md
naming-rule-builder --> KNOWLEDGE.md
naming_rule artifact --> validator_builder (P06)
naming_rule artifact --> code_generator
naming_rule artifact --> documentation_builder
SCHEMA.md --> OUTPUT_TEMPLATE.md
```

## Fractal Position

```
CEX System
  └── P05 (Output Layer)
        ├── response_format-builder   [reply shape]
        ├── parser-builder            [data extraction]
        ├── formatter-builder         [content rendering]
        └── naming-rule-builder       [name convention]  <-- THIS BUILDER
              └── naming_rule artifacts
                    └── consumed by P06 validators, code generators, doc builders
```

## Builder Internal Structure

```
naming-rule-builder/
  MANIFEST.md         P03/BECOME   -- identity + routing
  SYSTEM_PROMPT.md    P03/BECOME   -- persona + ALWAYS/NEVER
  KNOWLEDGE.md        P01/INJECT   -- naming standards, CEX patterns
  INSTRUCTIONS.md     P03/REASON   -- 3-phase execution protocol
  TOOLS.md            P04/CALL     -- brain_query [CONDITIONAL], file tools
  OUTPUT_TEMPLATE.md  P05/PRODUCE  -- artifact structure with {{vars}}
  SCHEMA.md           P06/CONSTRAIN-- field definitions, SOURCE OF TRUTH
  EXAMPLES.md         P07/GOVERN   -- golden + anti-example
  ARCHITECTURE.md     P08/CONSTRAIN-- boundary, flow, dependency graph
  CONFIG.md           P09/CONSTRAIN-- file naming, size limits, enums
  MEMORY.md           P10/INJECT   -- common mistakes, pattern catalog
  QUALITY_GATES.md    P11/GOVERN   -- H01-H08 hard gates, S01-S10 soft gates
  COLLABORATION.md    P12/COLLABORATE-- crew compositions, handoff protocol
```
