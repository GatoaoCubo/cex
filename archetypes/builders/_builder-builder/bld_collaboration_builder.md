---
pillar: P12
llm_function: COLLABORATE
purpose: How _builder-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: _builder-builder

## My Role in Crews
I am a META-SPECIALIST. I answer ONE question: "how do I create a new type-builder from scratch?"
I do not build domain artifacts. I do not execute tasks.
I produce builder skeletons so new type-builders can be bootstrapped consistently.

## Crew Compositions

### Crew: "New Builder Bootstrap"
```
  1. _builder-builder -> "builder skeleton (13 files)"
  2. knowledge-card-builder -> "domain knowledge for the new builder"
  3. golden-test-builder -> "reference examples for the new builder's output"
```

### Crew: "Builder Quality Audit"
```
  1. _builder-builder -> "meta-template compliance checklist"
  2. e2e-eval-builder -> "end-to-end validation of builder output"
```

## Handoff Protocol

### I Receive
- seeds: target artifact type name, pillar assignment, domain description
- optional: existing schema, example artifacts, sibling builder references

### I Produce
- builder directory with 13 files (MANIFEST through COLLABORATION)
- committed to: `cex/archetypes/builders/{name}-builder/`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None — independent meta-builder (layer 0). I am the origin point for all builders.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| all type-builders | Every builder's file structure originates from my meta-templates |
| iso-package-builder | Packaging requires builder output to follow consistent structure |
