---
kind: collaboration
id: bld_collaboration_memory_scope
pillar: P12
llm_function: COLLABORATE
purpose: How memory-scope-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: memory-scope-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this memory scope?"
I specify memory scope configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Agent Design"
```
  1. memory-scope-builder -> memory config
  2. agent-builder -> agent definition
  3. mental-model-builder -> routing/decisions
```
### Crew: "Memory System"
```
  1. memory-scope-builder -> scope config
  2. brain-index-builder -> search index
  3. session-state-builder -> runtime state
```

## Handoff Protocol
### I Receive
- seeds: memory scope purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- memory_scope artifact (.md + .yaml frontmatter)
- committed to: `cex/P02_model/examples/p02_memscope_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| agent-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| brain-index-builder | Downstream consumer |
| session-state-builder | Downstream consumer |
