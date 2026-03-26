---
pillar: P12
llm_function: COLLABORATE
purpose: How input-schema-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: input-schema-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what data must be provided to this agent/operation?"
I do not define response formats. I do not check data validity.
I SPECIFY input contracts so agents and callers know what data to provide.

## Crew Compositions

### Crew: "Agent Contract Suite"
```
  1. input-schema-builder -> "defines entry contract (fields, types, defaults)"
  2. interface-builder -> "defines bilateral integration contract"
  3. validator-builder -> "creates validators for contract compliance"
  4. output-template-builder [PLANNED] -> "defines output format"
```

### Crew: "Tool Documentation"
```
  1. input-schema-builder -> "defines tool input contract"
  2. knowledge-card-builder -> "documents tool knowledge"
  3. system-prompt-builder [PLANNED] -> "mentions input requirements in agent prompt"
```

## Handoff Protocol

### I Receive
- seeds: scope (what operation), field names and types
- optional: existing API docs, Pydantic models, JSON Schema

### I Produce
- input_schema artifact (YAML)
- committed to: `cex/P06_schema/examples/p06_is_{scope_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Input schemas are INDEPENDENT — they can be built from requirements alone.

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| interface-builder | Uses input_schemas for method input types |
| validator-builder | Creates compliance checks for the input contract |
| system-prompt-builder [PLANNED] | Documents required inputs in agent prompts |
