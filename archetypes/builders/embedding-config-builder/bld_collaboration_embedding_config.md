---
kind: collaboration
id: bld_collaboration_embedding_config
pillar: P12
llm_function: COLLABORATE
purpose: How embedding-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: embedding-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which embedding model, with what parameters, for this RAG pipeline?"
I do not build search indexes. I do not create knowledge content.
I configure embedding models so vector search systems produce accurate representations.
## Crew Compositions
### Crew: "RAG Pipeline Setup"
```
  1. embedding-config-builder -> "embedding model parameters (dimensions, chunk, distance)"
  2. brain-index-builder -> "search index configuration"
  3. knowledge-card-builder -> "content to embed and index"
```
### Crew: "Vector Infrastructure"
```
  1. embedding-config-builder -> "model config (provider, dimensions, tokenizer)"
  2. brain-index-builder -> "FAISS/BM25 index using embedding config"
  3. benchmark-builder -> "retrieval quality measurement"
```
## Handoff Protocol
### I Receive
- seeds: use case (search, similarity, clustering), content domain
- optional: provider preference, dimension constraints, cost budget, batch size
### I Produce
- embedding_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P01/examples/p01_embedding_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Embedding configs are defined from requirements.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| brain-index-builder | Needs embedding dimensions and distance metric for index config |
| benchmark-builder | Measures retrieval quality using configured embeddings |
