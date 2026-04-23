---
kind: collaboration
id: bld_collaboration_input_schema
pillar: P12
llm_function: COLLABORATE
purpose: How input-schema-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Input Schema"
version: "1.0.0"
author: n03_builder
tags: [input_schema, builder, examples]
tldr: "Golden and anti-examples for input schema construction, demonstrating ideal structure and common pitfalls."
domain: "input schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_action_prompt
  - bld_collaboration_few_shot_example
  - bld_collaboration_validation_schema
  - input-schema-builder
  - bld_collaboration_interface
  - bld_collaboration_golden_test
  - bld_collaboration_formatter
  - bld_collaboration_response_format
  - bld_collaboration_prompt_version
  - bld_collaboration_chain
---

# Collaboration: input-schema-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what data must be provided to this agent/operation?"
I do not define bilateral contracts. I do not validate output.
I specify unilateral input contracts so producers know exactly what data consumers require.
## Crew Compositions
### Crew: "Contract Stack"
```
  1. input-schema-builder -> "unilateral input contract (fields, types, defaults)"
  2. interface-builder -> "bilateral integration contract"
  3. formatter-builder -> "output format specification"
```
### Crew: "Prompt Engineering"
```
  1. input-schema-builder -> "input contract for the prompt"
  2. action-prompt-builder -> "task prompt respecting input schema"
  3. few-shot-example-builder -> "examples conforming to schema"
```
## Handoff Protocol
### I Receive
- seeds: consumer name, required fields with types
- optional: defaults, coercion rules, validation patterns, error messages
### I Produce
- input_schema artifact (.md + .yaml frontmatter)
- committed to: `cex/P06/examples/p06_input_{consumer}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Input schemas are defined from consumer requirements.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Prompts must respect input contract |
| chain-builder | Chain steps pass data conforming to input schemas |
| few-shot-example-builder | Examples must match input format |
| formatter-builder | Formatters transform data described by input schemas |
| interface-builder | Bilateral contracts compose from input schemas |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_action_prompt]] | sibling | 0.53 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.50 |
| [[bld_collaboration_validation_schema]] | sibling | 0.42 |
| [[input-schema-builder]] | upstream | 0.40 |
| [[bld_collaboration_interface]] | sibling | 0.40 |
| [[bld_collaboration_golden_test]] | sibling | 0.38 |
| [[bld_collaboration_formatter]] | sibling | 0.37 |
| [[bld_collaboration_response_format]] | sibling | 0.37 |
| [[bld_collaboration_prompt_version]] | sibling | 0.37 |
| [[bld_collaboration_chain]] | sibling | 0.36 |
