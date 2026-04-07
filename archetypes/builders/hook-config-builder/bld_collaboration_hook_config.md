---
kind: collaboration
id: bld_collaboration_hook_config
pillar: P12
llm_function: COLLABORATE
purpose: How hook-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: hook-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which hooks fire at each build phase and under what conditions?"
I declare hook lifecycle configurations so builders and pipelines can bind events.
## Crew Compositions
### Crew: "Builder Pipeline"
```
  1. hook-config-builder -> hook lifecycle ofclaration
  2. quality-gate-builder -> quality scoring rules
  3. lifecycle-rule-builder -> archive/promote policy
```
### Crew: "Execution Framework"
```
  1. hook-config-builder -> event bindings
  2. plugin-builder -> extension modules
  3. agent-builder -> agent execution config
```

## Handoff Protocol
### I Receive
- seeds: target builder, pipeline phases, hook requirements
- optional: specific event bindings, upstream artifact references
### I Produce
- hook_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P04_execution/examples/p04_hookconf_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| hook-builder | Implements hooks declared by this config |
| quality-gate-builder | May bind quality-fail hooks |
| lifecycle-rule-builder | May bind archive/promote hooks |
