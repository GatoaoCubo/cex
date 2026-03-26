---
pillar: P12
llm_function: COLLABORATE
purpose: How embedding-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: embedding-config-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which embedding model, with what parameters, for this RAG pipeline?"
I do not build indexes. I do not index sources.
I CONFIGURE the vectorization model so brain_index and retrievers work correctly.

## Crew Compositions

### Crew: "RAG Pipeline Setup"
```
  1. embedding-config-builder -> "configures the embedding model"
  2. rag-source-builder [PLANNED] -> "registers external sources"
  3. brain-index-builder [PLANNED] -> "configures the search index"
```

### Crew: "Knowledge Infrastructure"
```
  1. embedding-config-builder -> "defines vectorization params"
  2. knowledge-card-builder -> "produces knowledge content"
  3. glossary-entry-builder -> "defines domain terms"
```

## Handoff Protocol

### I Receive
- seeds: model name, provider, use case
- optional: dimension preference, cost constraints, privacy requirements

### I Produce
- embedding_config artifact (YAML)
- committed to: `cex/P01_knowledge/examples/p01_emb_{model_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Embedding configs can be built from a model name alone.

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| brain-index-builder [PLANNED] | Index config needs embedding dimensions and metric |
| knowledge-card-builder | KCs are chunked and embedded using this config |
| rag-source-builder [PLANNED] | Source indexing uses embedding config params |
