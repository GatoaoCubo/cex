---
pillar: P12
llm_function: COLLABORATE
kind: collaboration
domain: naming_rule
version: 1.0.0
---

# Collaboration — Naming Rule Builder

## Role

**naming-rule-builder** is a primary producer. It receives a scope definition and outputs a `naming_rule` artifact. It does not consume other builders' output — naming rules are foundational and independent.

## Crew Compositions

### Composition A: Naming Governance Sprint

```
orchestrator
    |
    +--> naming-rule-builder      [produces naming_rule artifacts]
    |         |
    |         v
    +--> validator-builder (P06)  [consumes naming_rule, produces validator]
              |
              v
         quality-gate check (QUALITY_GATES.md)
```

**Use when**: Establishing naming conventions for a new pillar or domain from scratch.

**Handoff**: naming-rule-builder writes `p05_nr_{scope}.md` to pool → validator-builder reads it to build runtime enforcement.

### Composition B: Full Artifact Lifecycle

```
orchestrator
    |
    +--> naming-rule-builder      [step 1: define naming convention]
    |
    +--> type-def-builder (P06)   [step 2: define abstract type, references naming rule]
    |
    +--> schema-builder           [step 3: define content schema, references naming rule for IDs]
    |
    +--> validator-builder (P06)  [step 4: enforce all three above at runtime]
```

**Use when**: Bootstrapping a new artifact kind end-to-end.

**Note**: naming-rule-builder runs FIRST — type definitions and schemas reference the naming convention, not the other way around.

## Handoff Protocol

**Incoming** (what this builder needs):
- Scope description: one sentence defining what artifact kind is being named
- Pillar assignment: which CEX pillar (p01–p12) governs the scope
- Sibling context: any existing naming rules in the same pillar (for consistency)

**Outgoing** (what this builder produces):
- `p05_nr_{scope_slug}.md` — complete naming_rule artifact in pool
- Populated frontmatter: all SCHEMA.md required fields
- Body: Scope, Pattern Definition (with regex + segments table), Examples (3 valid + 2 invalid), Collision Resolution

**Trigger signal** (when downstream should activate):
- File written to `records/pool/p05/p05_nr_{scope_slug}.md`
- `quality: null` confirms it is a fresh artifact awaiting review

## Dependencies

**None** — naming rules are foundational. This builder does not depend on any other builder's output to function.

| Dependency | Status | Reason |
|------------|--------|--------|
| type-def-builder | NONE | naming rules precede type definitions |
| schema-builder | NONE | naming rules precede schema definitions |
| validator-builder | NONE | naming rules precede validators |
| formatter-builder | NONE | naming rules are independent of output format |

## Dependents

Builders that CONSUME naming_rule artifacts (and therefore cross-reference this builder):

| Builder | How It Uses naming_rule |
|---------|------------------------|
| validator-builder (P06) | Reads `pattern` field to enforce ID format at runtime |
| type-def-builder (P06) | References naming convention when defining type identity fields |
| documentation-builder | Renders naming rule tables in architecture docs |
| code-generator | Uses `pattern`, `prefix`, `separator` to auto-generate compliant names |

## Cross-Reference Reciprocity

Per BUILDER_NORM 12: if builder A references builder B, builder B must reference builder A.

- `validator-builder` MUST reference `naming-rule-builder` in its COLLABORATION.md
- `type-def-builder` MUST reference `naming-rule-builder` in its COLLABORATION.md
