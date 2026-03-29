---
kind: collaboration
id: bld_collaboration_prompt_version
pillar: P12
llm_function: COLLABORATE
purpose: How prompt-version-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: prompt-version-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this prompt version?"
I specify prompt version configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Prompt Lifecycle"
```
  1. prompt-template-builder -> mutable template
  2. prompt-version-builder -> immutable snapshot
  3. few-shot-example-builder -> examples
```
### Crew: "Prompt Optimization"
```
  1. prompt-version-builder -> version tracking
  2. constraint-spec-builder -> output constraints
  3. e2e-eval-builder -> version evaluation
```

## Handoff Protocol
### I Receive
- seeds: prompt version purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- prompt_version artifact (.md + .yaml frontmatter)
- committed to: `cex/P03_prompt/examples/p03_pv_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| prompt-template-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Downstream consumer |
| smoke-eval-builder | Downstream consumer |
