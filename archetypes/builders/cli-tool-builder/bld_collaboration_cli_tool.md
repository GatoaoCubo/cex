---
kind: collaboration
id: bld_collaboration_cli_tool
pillar: P12
llm_function: COLLABORATE
purpose: How cli-tool-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
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
