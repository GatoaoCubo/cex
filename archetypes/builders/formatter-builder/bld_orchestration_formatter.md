---
kind: collaboration
id: bld_collaboration_formatter
pillar: P12
llm_function: COLLABORATE
purpose: How formatter-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Formatter"
version: "1.0.0"
author: n03_builder
tags: [formatter, builder, examples]
tldr: "Golden and anti-examples for formatter construction, demonstrating ideal structure and common pitfalls."
domain: "formatter construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - formatter-builder
  - bld_collaboration_input_schema
  - bld_collaboration_response_format
  - bld_collaboration_few_shot_example
  - bld_collaboration_parser
  - bld_collaboration_output_validator
  - bld_collaboration_cli_tool
  - bld_architecture_formatter
  - bld_collaboration_builder
  - bld_collaboration_action_prompt
---

# Collaboration: formatter-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should structured data be presented in this format?"
I do not extract data. I do not validate content.
I design output transformations so data is presented in readable, consumable formats.
## Crew Compositions
### Crew: "Output Pipeline"
```
  1. input-schema-builder -> "input data contract"
  2. formatter-builder -> "output transformation rules (JSON/YAML/Markdown/table)"
  3. cli-tool-builder -> "CLI tool that applies the formatter"
```
### Crew: "Report Generation"
```
  1. knowledge-card-builder -> "source facts"
  2. formatter-builder -> "presentation format (table, markdown, HTML)"
  3. diagram-builder -> "visual elements in the report"
```
## Handoff Protocol
### I Receive
- seeds: input data type, target output format (JSON, YAML, Markdown, HTML, table)
- optional: template engine, escaping rules, locale, truncation policy
### I Produce
- formatter artifact (.md + .yaml frontmatter)
- committed to: `cex/P05/examples/p05_formatter_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- input-schema-builder: provides data structure that the formatter transforms
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| cli-tool-builder | CLI tools use formatters for output display |
| few-shot-example-builder | Examples must match formatter output shape |
| action-prompt-builder | Prompts may specify output via formatter rules |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[formatter-builder]] | upstream | 0.46 |
| [[bld_collaboration_input_schema]] | sibling | 0.44 |
| [[bld_collaboration_response_format]] | sibling | 0.43 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.43 |
| [[bld_collaboration_parser]] | sibling | 0.42 |
| [[bld_collaboration_output_validator]] | sibling | 0.41 |
| [[bld_collaboration_cli_tool]] | sibling | 0.40 |
| [[bld_architecture_formatter]] | upstream | 0.40 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_collaboration_action_prompt]] | sibling | 0.38 |
