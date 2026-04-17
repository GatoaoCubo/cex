---
kind: collaboration
id: bld_collaboration_prompt_compiler
pillar: P02
llm_function: COLLABORATE
purpose: How prompt-compiler-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, collaboration, P03]
tldr: "Collaboration protocol for prompt-compiler-builder: receives kinds registry, produces resolution tables, feeds routers and dispatchers."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
---

# Collaboration: prompt-compiler-builder
## My Role in Crews
I am the FIRST RESOLVER. I answer ONE question: "what does the user want, expressed as {kind, pillar, nucleus, verb}?"
I produce intent resolution tables that every other builder consumes. Without me, builders receive raw user input and must guess the kind. With me, they receive a structured tuple and execute precisely.
## Crew Compositions
### Crew: "Full Intent Pipeline"
```
  1. prompt-compiler-builder  -> "resolve user input to {kind, pillar, nucleus, verb}"
  2. router-builder           -> "route resolved kind to correct provider"
  3. dispatch-rule-builder    -> "dispatch resolved nucleus to agent"
```
### Crew: "Bilingual User Experience"
```
  1. prompt-compiler-builder  -> "bilingual intent resolution (PT-BR + EN)"
  2. glossary-entry-builder   -> "terminology standardization across languages"
  3. prompt-template-builder  -> "localized prompt templates"
```
### Crew: "Knowledge-Augmented Resolution"
```
  1. prompt-compiler-builder  -> "base intent resolution tables"
  2. retriever-builder        -> "semantic similarity for fallback matching"
  3. knowledge-card-builder   -> "domain knowledge enriching resolution context"
```
## Handoff Protocol
### I Receive
- seeds: kinds_meta.json, existing transmutation rules, target languages
- optional: domain-specific patterns, user feedback on misresolutions
### I Produce
- prompt_compiler artifact (YAML frontmatter + kind resolution tables + verb map + fallback, max 16384 bytes)
- committed to: `P03_prompt/p03_pc_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- knowledge-card-builder: provides kind KCs with detailed boundaries
- glossary-entry-builder: provides terminology for bilingual patterns
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| router-builder | Uses resolved kind to determine provider routing |
| dispatch-rule-builder | Uses resolved nucleus to dispatch tasks |
| prompt-template-builder | Uses resolved kind to select correct template |
| system-prompt-builder | Uses resolved domain to configure agent identity |
