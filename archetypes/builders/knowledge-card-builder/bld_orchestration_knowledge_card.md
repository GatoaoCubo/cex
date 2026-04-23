---
kind: collaboration
id: bld_collaboration_knowledge_card
pillar: P12
llm_function: COLLABORATE
purpose: How knowledge-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_agent
  - bld_collaboration_knowledge_index
  - bld_collaboration_system_prompt
  - bld_collaboration_builder
  - bld_collaboration_context_doc
  - bld_collaboration_boot_config
  - bld_collaboration_rag_source
  - bld_collaboration_instruction
  - bld_collaboration_embedding_config
  - knowledge-card-builder
---

# Collaboration: knowledge-card-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the essential, searchable fact about this topic?"
I do not define agent personas. I do not configure boot parameters.
I distill knowledge into atomic facts so agents and builders have factual context for decisions.
## Crew Compositions
### Crew: "Content Foundation"
```
  1. context-doc-builder -> "domain scope and background"
  2. knowledge-card-builder -> "atomic searchable facts (density > 0.8)"
  3. glossary-entry-builder -> "term definitions"
  4. few-shot-example-builder -> "format examples grounded in knowledge"
```
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge for agent expertise"
  2. agent-builder -> "agent definition shaped by knowledge"
  3. instruction-builder -> "execution steps grounded in facts"
  4. boot-config-builder -> "provider configuration"
  5. agent-package-builder -> "deployable package"
```
### Crew: "RAG Pipeline Setup"
```
  1. knowledge-card-builder -> "content to embed and index"
  2. embedding-config-builder -> "embedding model parameters"
  3. knowledge-index-builder -> "search index configuration"
```
## Handoff Protocol
### I Receive
- seeds: topic name, domain, source material or research brief
- optional: density target, classification (domain_kc or meta_kc), related cards
### I Produce
- knowledge_card artifact (.md + .yaml frontmatter, max 5KB, density > 0.8)
- committed to: `cex/P01/examples/p01_kc_{topic}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Knowledge cards are distilled from source material.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agent expertise is grounded in knowledge cards |
| axiom-builder | Axioms are formalized from distilled facts |
| context-doc-builder | Domain docs reference knowledge card facts |
| knowledge-index-builder | Knowledge cards are primary content for indexing |
| instruction-builder | Recipes reference factual knowledge for accuracy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | sibling | 0.52 |
| [[bld_collaboration_knowledge_index]] | sibling | 0.46 |
| [[bld_collaboration_system_prompt]] | sibling | 0.45 |
| [[bld_collaboration_builder]] | sibling | 0.44 |
| [[bld_collaboration_context_doc]] | sibling | 0.43 |
| [[bld_collaboration_boot_config]] | sibling | 0.42 |
| [[bld_collaboration_rag_source]] | sibling | 0.40 |
| [[bld_collaboration_instruction]] | sibling | 0.40 |
| [[bld_collaboration_embedding_config]] | sibling | 0.39 |
| [[knowledge-card-builder]] | upstream | 0.39 |
