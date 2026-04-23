---
kind: collaboration
id: bld_collaboration_response_format
pillar: P05
llm_function: COLLABORATE
purpose: How response-format-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Response Format"
version: "1.0.0"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - response-format-builder
  - bld_collaboration_prompt_template
  - bld_collaboration_validation_schema
  - bld_collaboration_action_prompt
  - bld_collaboration_system_prompt
  - bld_collaboration_golden_test
  - bld_collaboration_few_shot_example
  - bld_collaboration_builder
  - bld_collaboration_prompt_version
  - bld_collaboration_parser
---

# Collaboration: response-format-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should the LLM structure its output for this task?"
I design the format the LLM sees during generation. I do not validate output after generation, extract data from it, or transform it between formats.
## Crew Compositions
### Crew: "Structured Output Pipeline"
```
  1. response-format-builder    -> "format spec injected into the prompt (LLM sees this during generation)"
  2. validation-schema-builder  -> "JSON/YAML schema applied post-generation to verify structure"
  3. parser-builder             -> "extractor that pulls fields from the validated output"
```
### Crew: "Agent Prompt Stack"
```
  1. system-prompt-builder      -> "agent identity and fixed instructions"
  2. prompt-template-builder    -> "parameterized template with {{variables}}"
  3. response-format-builder    -> "output structure injected at system_prompt or user_message"
```
### Crew: "Eval-Ready Agent Pack"
```
  1. response-format-builder    -> "canonical output structure the agent must produce"
  2. quality-gate-builder       -> "gates that check the format for completeness and correctness"
  3. golden-test-builder        -> "golden examples of correctly formatted responses"
  4. unit-eval-builder          -> "unit evaluations asserting format compliance"
```
## Handoff Protocol
### I Receive
- seeds: task type, desired format_type (json/yaml/markdown/csv/plaintext), required fields, injection_point
- optional: existing system prompt to inject into, example outputs, validation schema reference
### I Produce
- response_format artifact (YAML frontmatter 19 fields + format body with sections/fields/examples, max 4096 bytes)
- committed to: `cex/P05/examples/p05_rf_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- system-prompt-builder: provides the injection target when injection_point is system_prompt
- prompt-template-builder: provides the template body where the format spec is inserted
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validation-schema-builder | Derives its schema from the fields I specify in the format |
| parser-builder | Knows which fields to extract based on my format definition |
| golden-test-builder | Golden outputs must conform to the format I define |
| formatter-builder | Transforms between formats starting from the structure I establish |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[response-format-builder]] | related | 0.49 |
| [[bld_collaboration_prompt_template]] | sibling | 0.46 |
| [[bld_collaboration_validation_schema]] | sibling | 0.45 |
| [[bld_collaboration_action_prompt]] | sibling | 0.45 |
| [[bld_collaboration_system_prompt]] | sibling | 0.43 |
| [[bld_collaboration_golden_test]] | sibling | 0.43 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.41 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_collaboration_prompt_version]] | sibling | 0.39 |
| [[bld_collaboration_parser]] | sibling | 0.38 |
