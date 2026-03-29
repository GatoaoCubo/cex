---
kind: collaboration
id: bld_collaboration_chunk_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How chunk-strategy-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: chunk-strategy-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this chunk strategy?"
I specify chunk strategy configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "RAG Pipeline"
```
  1. chunk-strategy-builder -> chunking config
  2. embedding-config-builder -> vector model config
  3. retriever-config-builder -> search config
```
### Crew: "Document Processing"
```
  1. chunk-strategy-builder -> split strategy
  2. document-loader-builder -> ingestion
  3. parser-builder -> extraction
```

## Handoff Protocol
### I Receive
- seeds: chunk strategy purpose, target system, constraints
- optional: specific parameter values, upstream artifact references
### I Produce
- chunk_strategy artifact (.md + .yaml frontmatter)
- committed to: `cex/P01_knowledge/examples/p01_chunk_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| embedding-config-builder | Downstream consumer |
| retriever-config-builder | Downstream consumer |
| brain-index-builder | Downstream consumer |
