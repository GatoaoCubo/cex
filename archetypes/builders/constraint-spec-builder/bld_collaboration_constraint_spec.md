---
kind: collaboration
id: bld_collaboration_constraint_spec
pillar: P12
llm_function: COLLABORATE
purpose: How constraint-spec-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: constraint-spec-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this constraint spec?"
I specify constraint spec configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Structured Generation"
```
  1. constraint-spec-builder -> decode constraint
  2. prompt-template-builder -> prompt with constraint
  3. output-validator-builder -> post-gen validation
```
### Crew: "Prompt Engineering"
```
  1. constraint-spec-builder -> output constraint
  2. system-prompt-builder -> agent identity
  3. prompt-version-builder -> version tracking
```

## Handoff Protocol
### I Receive
- seeds: constraint spec purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- constraint_spec artifact (.md + .yaml frontmatter)
- committed to: `cex/P03_prompt/examples/p03_constraint_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| prompt-template-builder | Downstream consumer |
| output-validator-builder | Downstream consumer |
