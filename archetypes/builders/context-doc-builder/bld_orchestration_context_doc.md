---
kind: collaboration
id: bld_collaboration_context_doc
pillar: P12
llm_function: COLLABORATE
purpose: How context-doc-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_action_prompt
  - context-doc-builder
  - bld_collaboration_knowledge_card
  - bld_collaboration_few_shot_example
  - bld_collaboration_prompt_template
  - bld_collaboration_instruction
  - bld_collaboration_glossary_entry
  - bld_collaboration_prompt_version
  - bld_collaboration_builder
  - bld_knowledge_card_context_doc
---

# Collaboration: context-doc-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what background context does this domain need for prompt hydration?"
I do not distill atomic facts. I do not define terms.
I document domain context so prompt builders can hydrate their prompts with relevant background.
## Crew Compositions
### Crew: "Content Foundation"
```
  1. context-doc-builder -> "domain context (scope, stakeholders, constraints)"
  2. knowledge-card-builder -> "atomic facts from the domain"
  3. glossary-entry-builder -> "term definitions for the domain"
  4. few-shot-example-builder -> "format examples grounded in context"
```
### Crew: "Prompt Hydration"
```
  1. context-doc-builder -> "domain background for injection"
  2. action-prompt-builder -> "task prompt hydrated with context"
  3. chain-builder -> "prompt pipeline with contextual grounding"
```
## Handoff Protocol
### I Receive
- seeds: domain name, scope description, target audience
- optional: stakeholder list, constraints, assumptions, dependencies
### I Produce
- context_doc artifact (.md + .yaml, max 2048 bytes)
- committed to: `cex/P01/examples/p01_context_{domain}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Context docs are authored from domain analysis.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Injects context_doc into task prompts |
| knowledge-card-builder | Uses context scope to bound fact distillation |
| chain-builder | Hydrates chain steps with domain background |
| instruction-builder | Grounds execution recipes in domain context |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_action_prompt]] | sibling | 0.53 |
| [[context-doc-builder]] | upstream | 0.45 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.43 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.41 |
| [[bld_collaboration_prompt_template]] | sibling | 0.40 |
| [[bld_collaboration_instruction]] | sibling | 0.40 |
| [[bld_collaboration_glossary_entry]] | sibling | 0.39 |
| [[bld_collaboration_prompt_version]] | sibling | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.36 |
