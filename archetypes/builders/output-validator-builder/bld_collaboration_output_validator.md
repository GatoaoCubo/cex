---
kind: collaboration
id: bld_collaboration_output_validator
pillar: P12
llm_function: COLLABORATE
purpose: How output-validator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: output-validator-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this output validator?"
I specify output validator configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Validation Pipeline"
```
  1. constraint-spec-builder -> decode constraint
  2. output-validator-builder -> post-gen validation
  3. quality-gate-builder -> scoring
```
### Crew: "Output Quality"
```
  1. output-validator-builder -> structural validation
  2. formatter-builder -> output formatting
  3. parser-builder -> output extraction
```

## Handoff Protocol
### I Receive
- seeds: output validator purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- output_validator artifact (.md + .yaml frontmatter)
- committed to: `cex/P05_output/examples/p05_oval_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| constraint-spec-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | Downstream consumer |
| formatter-builder | Downstream consumer |
