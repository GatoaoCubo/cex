---
kind: collaboration
id: bld_collaboration_prompt_template
pillar: P03
llm_function: COLLABORATE
purpose: How prompt-template-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Prompt Template"
version: "1.0.0"
author: n03_builder
tags: [prompt_template, builder, examples]
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
domain: "prompt template construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_response_format
  - bld_collaboration_action_prompt
  - bld_collaboration_prompt_version
  - bld_collaboration_few_shot_example
  - prompt-template-builder
  - bld_collaboration_context_doc
  - bld_collaboration_system_prompt
  - p03_ins_prompt_template
  - bld_collaboration_context_window_config
  - bld_knowledge_card_prompt_template
---

# Collaboration: prompt-template-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the reusable mold that generates this prompt when filled?"
I produce parameterized templates with `{{variables}}` — not fixed prompts, not identities, not instructions without variable slots.
## Crew Compositions
### Crew: "Agent Prompt Stack"
```
  1. system-prompt-builder    -> "fixed identity and persona for the agent"
  2. prompt-template-builder  -> "reusable mold with {{variables}} for dynamic invocations"
  3. response-format-builder  -> "output structure spec injected into the prompt"
```
### Crew: "RAG-Augmented Prompt Pipeline"
```
  1. rag-source-builder       -> "external sources to pull context from at runtime"
  2. context-doc-builder      -> "domain context injected into the template"
  3. prompt-template-builder  -> "template with {{context}} and {{query}} slots"
  4. quality-gate-builder     -> "gates that validate the template before deployment"
```
### Crew: "Few-Shot Template Pack"
```
  1. few-shot-example-builder -> "concrete examples embedded in the template body"
  2. prompt-template-builder  -> "template wrapping examples with {{input}} slot"
  3. validation-schema-builder -> "schema validating filled-template outputs post-generation"
```
## Handoff Protocol
### I Receive
- seeds: task domain, variable names, prompt purpose, target framework (LangChain/DSPy/Mustache/Jinja2)
- optional: few-shot examples, context doc content, system prompt identity, response format spec, type-def schema
### I Produce
- prompt_template artifact (YAML frontmatter + Mustache/bracket body, max 4096 bytes)
- committed to: `cex/P03/examples/p03_pt_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- type-def-builder: provides typed variable schemas that map to `{{variable}}` slots
- few-shot-example-builder: provides examples embedded in the template body
- context-doc-builder: provides domain context injected as a template slot
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| system-prompt-builder | May embed template slots inside system prompts for dynamic identity |
| quality-gate-builder | Gates reference template structure to validate H01-H08 hard gates |
| response-format-builder | Response format is often injected as a variable inside the template |
| agent-package-builder | Packages the template alongside its siblings into a deployable unit |
| knowledge-card-builder | Uses rendered template outputs as prompts for card production |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_response_format]] | sibling | 0.51 |
| [[bld_collaboration_action_prompt]] | sibling | 0.48 |
| [[bld_collaboration_prompt_version]] | sibling | 0.45 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.44 |
| [[prompt-template-builder]] | related | 0.44 |
| [[bld_collaboration_context_doc]] | sibling | 0.41 |
| [[bld_collaboration_system_prompt]] | sibling | 0.39 |
| [[p03_ins_prompt_template]] | related | 0.38 |
| [[bld_collaboration_context_window_config]] | sibling | 0.38 |
| [[bld_knowledge_card_prompt_template]] | upstream | 0.37 |
