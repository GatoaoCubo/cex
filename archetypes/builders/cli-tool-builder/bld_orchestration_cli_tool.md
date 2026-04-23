---
kind: collaboration
id: bld_collaboration_cli_tool
pillar: P12
llm_function: COLLABORATE
purpose: How cli-tool-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Cli Tool"
version: "1.0.0"
author: n03_builder
tags: [cli_tool, builder, examples]
tldr: "Golden and anti-examples for cli tool construction, demonstrating ideal structure and common pitfalls."
domain: "cli tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - cli-tool-builder
  - bld_collaboration_hook
  - bld_collaboration_formatter
  - bld_collaboration_builder
  - bld_collaboration_code_executor
  - bld_collaboration_daemon
  - bld_collaboration_vision_tool
  - bld_collaboration_hook_config
  - bld_knowledge_card_cli_tool
  - bld_collaboration_golden_test
---

# Collaboration: cli-tool-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what commands does this tool expose, and what are its flags and exit codes?"
I do not build background processes. I do not define API clients.
I specify one-shot command-line tools so users and agents can invoke operations from terminal.
## Crew Compositions
### Crew: "Developer Tooling"
```
  1. cli-tool-builder -> "CLI tool specification (commands, flags, exit codes)"
  2. input-schema-builder -> "input validation for CLI arguments"
  3. formatter-builder -> "output formatting (text/json/table)"
```
### Crew: "Tool Ecosystem"
```
  1. cli-tool-builder -> "one-shot CLI tool"
  2. daemon-builder -> "persistent background service"
  3. hook-builder -> "event hooks that invoke CLI tools"
```
## Handoff Protocol
### I Receive
- seeds: tool purpose, command names, expected input/output
- optional: config file spec, env var overrides, exit code mapping
### I Produce
- cli_tool artifact (.md + .yaml frontmatter)
- committed to: `cex/P04/examples/p04_cli_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). CLI tools can be defined standalone.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| hook-builder | Hooks may invoke CLI tools as their execution script |
| daemon-builder | Daemons may wrap CLI tools in persistent loops |
| instruction-builder | Recipes reference CLI tools as execution steps |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[cli-tool-builder]] | upstream | 0.51 |
| [[bld_collaboration_hook]] | sibling | 0.41 |
| [[bld_collaboration_formatter]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[bld_collaboration_code_executor]] | sibling | 0.35 |
| [[bld_collaboration_daemon]] | sibling | 0.33 |
| [[bld_collaboration_vision_tool]] | sibling | 0.32 |
| [[bld_collaboration_hook_config]] | sibling | 0.32 |
| [[bld_knowledge_card_cli_tool]] | upstream | 0.32 |
| [[bld_collaboration_golden_test]] | sibling | 0.32 |
