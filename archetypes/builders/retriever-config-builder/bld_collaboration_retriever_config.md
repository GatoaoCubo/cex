---
kind: collaboration
id: bld_collaboration_retriever_config
pillar: P12
llm_function: COLLABORATE
purpose: How retriever-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: retriever-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this retriever config?"
I specify retriever config configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "RAG Pipeline"
```
  1. chunk-strategy-builder -> chunking
  2. embedding-config-builder -> vectors
  3. retriever-config-builder -> search config
```
### Crew: "Search System"
```
  1. retriever-config-builder -> retrieval params
  2. knowledge-index-builder -> index infra
  3. formatter-builder -> result formatting
```

## Handoff Protocol
### I Receive
- seeds: retriever config purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- retriever_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P01_knowledge/examples/p01_retr_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| chunk-strategy-builder | Upstream dependency |
| embedding-config-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| knowledge-index-builder | Downstream consumer |
