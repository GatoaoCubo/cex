---
kind: collaboration
id: bld_collaboration_input_schema
pillar: P12
llm_function: COLLABORATE
purpose: How input-schema-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: input-schema-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what data must be provided to this agent/operation?"
I do not define bilateral contracts. I do not validate output.
I specify unilateral input contracts so producers know exactly what data consumers require.

## Crew Compositions

### Crew: "Contract Stack"
```
  1. input-schema-builder -> "unilateral input contract (fields, types, defaults)"
  2. interface-builder -> "bilateral integration contract"
  3. formatter-builder -> "output format specification"
```

### Crew: "Prompt Engineering"
```
  1. input-schema-builder -> "input contract for the prompt"
  2. action-prompt-builder -> "task prompt respecting input schema"
  3. few-shot-example-builder -> "examples conforming to schema"
```

## Handoff Protocol

### I Receive
- seeds: consumer name, required fields with types
- optional: defaults, coercion rules, validation patterns, error messages

### I Produce
- input_schema artifact (.md + .yaml frontmatter)
- committed to: `cex/P06/examples/p06_input_{consumer}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None — independent builder (layer 0). Input schemas are defined from consumer requirements.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| action-prompt-builder | Prompts must respect input contract |
| chain-builder | Chain steps pass data conforming to input schemas |
| few-shot-example-builder | Examples must match input format |
| formatter-builder | Formatters transform data described by input schemas |
| interface-builder | Bilateral contracts compose from input schemas |
