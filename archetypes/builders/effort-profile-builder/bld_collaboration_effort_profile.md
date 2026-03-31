---
kind: collaboration
id: bld_collaboration_effort_profile
pillar: P12
llm_function: COLLABORATE
purpose: How effort-profile-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: effort-profile-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which model and thinking level should this builder use?"
I specify effort profiles so dispatchers and runtime systems can allocate the right resources.
## Crew Compositions
### Crew: "Builder Configuration"
```
  1. effort-profile-builder -> model + thinking config
  2. runtime-rule-builder -> execution rules
  3. env-config-builder -> environment variables
```
### Crew: "Dispatch Pipeline"
```
  1. effort-profile-builder -> effort allocation
  2. agent-builder -> agent definition
  3. system-prompt-builder -> agent persona
```

## Handoff Protocol
### I Receive
- seeds: target builder, complexity requirements, budget constraints
- optional: specific model preferences, upstream artifact references
### I Produce
- effort_profile artifact (.md + .yaml frontmatter)
- committed to: `cex/P09_config/examples/p09_effort_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| runtime-rule-builder | Uses effort profile for execution planning |
| agent-builder | References model/thinking in agent config |
| system-prompt-builder | Adapts prompt complexity to thinking level |
