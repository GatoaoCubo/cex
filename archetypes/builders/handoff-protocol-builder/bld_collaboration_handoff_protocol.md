---
kind: collaboration
id: bld_collaboration_handoff_protocol
pillar: P12
llm_function: COLLABORATE
purpose: How handoff-protocol-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: handoff-protocol-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this handoff protocol?"
I specify handoff protocol configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Multi-Agent System"
```
  1. handoff-protocol-builder -> inter-agent protocol
  2. agent-builder -> agent definitions
  3. router-builder -> task routing
```
### Crew: "Orchestration"
```
  1. handoff-protocol-builder -> handoff contracts
  2. dispatch-rule-builder -> keyword routing
  3. workflow-builder -> multi-step flows
```

## Handoff Protocol
### I Receive
- seeds: handoff protocol purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- handoff_protocol artifact (.md + .yaml frontmatter)
- committed to: `cex/P02_model/examples/p02_handoff_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| agent-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder | Downstream consumer |
| dispatch-rule-builder | Downstream consumer |
